# from django.shortcuts import render
# from mezzanine.generic.templatetags.comment_tags import comments_for
from django.template.loader import render_to_string
from mezzanine.blog.models import BlogPost
from django.template import RequestContext
from django.http import HttpResponse
import json
from mezzanine.generic.forms import ThreadedCommentForm
from django.core.urlresolvers import reverse
from theme.templatetags.templateutils import order_comments_by_score_for
from mezzanine.conf import settings


def ajax_comments(request, pk):
    '''
    Render to string the comments for a given BlogPost (or
    other object with comments).
    '''
    # Returns either object matching pk or None
    obj = BlogPost.objects.filter(pk=pk).first()
    response_data = {}
    if not obj:
        response_data['success'] = 'false'
    else:
        context = {}
        context["request"] = request
        # First if `COMMENTS_ORDERBYSCORE` setting, we
        # need to call `order_comments_by_score_for` first.
        # This simulates how in a template we'd call
        # the `order_comments_by_score_for` tag before the
        # `comments_for` tag, setting the `all_comments` var
        # in the context in advance, so `comments_thread` tag doesn't
        # need to touch it.
        if settings.COMMENTS_ORDERBYSCORE:
            # Context passed by ref
            order_comments_by_score_for(context, obj)

        # Replicate context building of `comments_for`
        # (I should try and understand the posted/unposted distinction better.)
        context["object_for_comments"] = obj
        context["comment_url"] = reverse("comment")
        form = ThreadedCommentForm(context["request"], obj)
        try:
            context["posted_comment_form"]
        except KeyError:
            context["posted_comment_form"] = form
        context["unposted_comment_form"] = form

        # Now pretend we are `comments_for` tag, and get the string resp it would.
        comments_str = render_to_string("generic/includes/comments.html",
                                        RequestContext(request, context))
        response_data = {}
        response_data['comments'] = comments_str
        response_data['success'] = 'true'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
