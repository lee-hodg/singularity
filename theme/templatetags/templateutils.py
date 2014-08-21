from __future__ import division
from django.template import Library
# from math import ceil
from collections import defaultdict
from mezzanine.utils.views import paginate
from mezzanine.conf import settings
from mezzanine.generic.models import ThreadedComment


def ceildiv(a, b):
    return -(-a // b)

register = Library()


@register.filter(name='linebreaksbr')
def linebreaksbr(line):
    '''
    Take a comma seperated line of text,
    for example an address, and replace
    the commas with linebreaks
    '''
    try:
        line = line.replace(',', ',<br />')
    except:
        # on failure, e.g. not a str
        # just return orig
        pass

    return line


@register.filter(name='splitcolor')
def splitcolor(word, args):
    '''
    Take a word find the midpoint
    , color first half red, second black.
    '''
    try:
        if args is None:
            return word
        colors = [arg.strip() for arg in args.split(',')]
        if len(colors) != 2:
            return word
        mid = ceildiv(len(word), 2)  # Rem python div takes floor
        newword = '<span style="color:'+colors[0]+'">'+word[:mid]+'</span>'
        newword += '<span style="color:'+colors[1]+'">'+word[mid:]+'</span>'
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
    simply with {{mydict.keys}}.  However because of the
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
    Ovverride Mezzanine's comment_thread inclusion_tag.
    The aim is to paginate all parent comments, but otherwise
    the behaviour is the same. N.B. context persists between the
    recursive calls to this tag. Remember this gets call with BlogPost
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
        # For ease tell the context we are at zeroth level in tree too
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
