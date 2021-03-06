from __future__ import division
from django.template import Library
from collections import defaultdict
from mezzanine.utils.views import paginate
from mezzanine.conf import settings
from mezzanine.generic.models import ThreadedComment


def ceildiv(a, b):
    '''
    Instead of floor division take ceiling, e.g.
    ceildiv(5,2)=3, ceildiv(-5,2)=-2.
    '''
    return -(-a // b)

register = Library()

from django.utils.timezone import now


def order_by_score(queryset, date_field):
    """
    Take some queryset(e.g. comments) and order them by score,
    which is basically "rating_sum/age_in_seconds^scale", where scale
    is a const that can be used to control how fast scores reduce over time.
    To perform this in the db it needs to support POW func, which postgres and
    mysql do. For db that don't like sqlite, we perform scoring/sorting in memory
    which will suffice for developement. We also have a date_field arg for controlling
    which field on the model represents its creation time
    Pilfered from:
    http://blog.jupo.org/2013/04/30/building-social-apps-with-mezzanine-drum/
    """

    scale = getattr(settings, "SCORE_SCALE_FACTOR", 2)

    # Timestamp SQL function snippets mapped to DB back-ends.
    # Defining these assumes the SQL functions POW() and NOW()
    # are available for the DB back-end.

    timestamp_sqls = {
        "mysql": "UNIX_TIMESTAMP(%s)",
        "postgresql_psycopg2": "EXTRACT(EPOCH FROM %s)",
    }
    # e.g quersey.db is 'default'
    db_engine = settings.DATABASES[queryset.db]["ENGINE"].rsplit(".", 1)[1]
    timestamp_sql = timestamp_sqls.get(db_engine)

    # This just produces the db query needed to implement the score func
    # e.g. for mysql, and if data_field='created_at', scale=2:
    # score_sql = "rating_sum / POW(UNIX_TIMESTAMP(NOW())
    #                               -UNIX_TIMESTAMP(created_at), 2)"
    if timestamp_sql:
        score_sql = "rating_sum / POW(%s - %s, %s)" % (
            timestamp_sql % "NOW()",
            timestamp_sql % date_field,
            scale,
        )
        # see django extra and select docs
        return queryset.extra(select={"score": score_sql}).order_by("-score")
    else:
        # We're using sqlite and have to do it in memory
        # but what about neg comments? For 2 comments with same neg rank
        # the older comment will get less neg score and will be pushed up.
        # (N.B. Since up+down=count and up-down=sum....so up=(count+sum)/2
        # down=(count-sum)/2)
        for obj in queryset:
            age = (now() - getattr(obj, date_field)).total_seconds()
            setattr(obj, "score", obj.rating_sum / pow(age, scale))
        return sorted(queryset, key=lambda obj: obj.score, reverse=True)


@register.filter(name='linebreaksbr')
def linebreaksbr(line):
    '''
    Take a comma seperated line of text,
    for example an address, and replace
    the commas with linebreaks.
    '''
    try:
        line = line.replace(',', ',<br />')
    except:
        # On failure, e.g. not a str
        # just return orig
        pass

    return line


@register.filter(name='splitcolor')
def splitcolor(word):
    '''
    Take a word, find the midpoint
    , color first half one color, second half another.
    '''
    try:
        # if args is None:
        #     return word
        # colors = [arg.strip() for arg in args.split(',')]
        # if len(colors) != 2:
        #     return word
        mid = ceildiv(len(word), 2)  # Rem python div takes floor
        newword = '<span class="split1">'+word[:mid]+'</span>'
        if word[mid:]:
            newword += '<span class="split2">'+word[mid:]+'</span>'
        word = newword
    except:
        # on failure, e.g. not a str
        # just return orig
        pass

    return word


@register.filter(name='defaultdict_keys')
def defaultdict_keys(ddict):
    '''
    Normally in the template given a dictionary
    called mydict in the context, keys() can be called
    simply with {{mydict.keys}}.  However, because of the
    way Django does look ups, namely first trying to
    see if a key called 'keys' exists and only trying keys()
    method if not, and because of the nature of the defaultdict(list)
    , namely returning [] even if the key lookup failed and creating
    a key called 'keys', {{mydict.keys}} will just result in []
    not the actual keys of the defaultdict.

    This filter grabs the existings keys of a defaultdict.
    '''
    return ddict.keys()


@register.filter(name='comment_level')
def comment_level(comment):
    '''
    Takes a comment and returns its level in the tree heirarchy.
    Parent comments are not replies to anything and have level 0.
    '''
    level = 0
    while True:
        if not comment.replied_to:
            # comment is not a reply, but a level 0 parent.
            break
        else:
            # comment is a reply, inc level +1
            level += 1
            # move to comment above
            comment = comment.replied_to
        # at end of recursion rtn level
    return level


@register.inclusion_tag("generic/includes/comment_with_pagination.html", takes_context=True)
def paginated_comment_thread(context, parent):
    """
    Override Mezzanine's comment_thread inclusion_tag.
    The aim is to paginate all parent comments, but otherwise
    the behaviour is the same. N.B. context persists between the
    recursive calls to this tag. Remember this gets called with BlogPost
    as parent first.

    Return a list of child comments for the given parent, storing all
    comments in a dict in the context when first called, using parents
    as keys for retrieval on subsequent recursive calls from the
    comments template.
    """
    if "all_comments" not in context:
        comments = defaultdict(list)
        if "request" in context and context["request"].user.is_staff:
            comments_queryset = parent.comments.all()
        else:
            comments_queryset = parent.comments.visible()
        for comment in comments_queryset.select_related("user"):
            comments[comment.replied_to_id].append(comment)
        context["all_comments"] = comments
    parent_id = parent.id if isinstance(parent, ThreadedComment) else None
    try:
        replied_to = int(context["request"].POST["replied_to"])
    except KeyError:
        replied_to = 0

    # Pagination for zeroth level comments
    comments_for_thread = context["all_comments"].get(parent_id, [])
    context.update({"comments_for_thread": comments_for_thread})
    if parent_id is None:
        # Zeroth level comment
        comments_for_thread_paginator = paginate(comments_for_thread,
                                                 context["request"].GET.get("page", 1),
                                                 settings.COMMENTS_PER_PAGE,
                                                 settings.MAX_PAGING_LINKS)
        # For ease, tell the context we are at zeroth level in tree too
        # context.update({"zeroth_level": True})
        context.update({"comments_for_thread":
                        comments_for_thread_paginator.object_list})
        context.update({"comments_for_thread_paginator":
                        comments_for_thread_paginator})

    # If any comment id in all_comments keys, it means that it has children
    # comment_ids = [comment.id for comment in comments_for_thread]
    # more_children = any(map(lambda x: x in context["all_comments"].keys(),
    #                        comment_ids))

    context.update({
        "no_comments": parent_id is None and not context["all_comments"],
        "replied_to": replied_to,
    })
    return context


@register.simple_tag(takes_context=True)
def order_comments_by_score_for(context, parent):
    '''
     This essentially mimics the initial part of comment_thread,
     retrieving and building the comment tree, and storing it in the
     template context, prior to comments_for even being called.
     By using the correct variable name (all_comments), the first call
     to the comments_thread tag will entirely bypass retrieving comments
     from the database, when it sees theye already in the template context.
     Thus this tag should be called before comments_for
     (in for example blog_post_detail.html).The difference now is that comments
     have been ordered by score, where score is as defined above, proportional
     to comment rating, but also decaying with comment age.
    '''
    if "all_comments" not in context:
        comments = defaultdict(list)
        if "request" in context and context["request"].user.is_staff:
            comments_queryset = parent.comments.all()
        else:
            comments_queryset = parent.comments.visible()
        for comment in order_by_score(comments_queryset, "submit_date"):
            comments[comment.replied_to_id].append(comment)
        context["all_comments"] = comments
    return ""
