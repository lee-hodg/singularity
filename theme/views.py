# from django.shortcuts import render
# from mezzanine.generic.templatetags.comment_tags import comments_for
from django.template.loader import render_to_string
from mezzanine.blog.models import BlogPost
from django.template import RequestContext
from django.http import HttpResponse
import json
from mezzanine.generic.forms import ThreadedCommentForm
from django.core.urlresolvers import reverse


def ajax_comments(request, pk):
    '''
    Render to string the comments for a given BlogPost or
    whatever.
    '''
    # Either object matching or None
    obj = BlogPost.objects.filter(pk=pk).first()
    response_data = {}
    if not obj:
        response_data['success'] = 'false'
    else:
        # replicate context building of comments_for
        # I should try and understand the posted/unposted distinction better
        context = {}
        context["request"] = request
        context["object_for_comments"] = obj
        context["comment_url"] = reverse("comment")
        form = ThreadedCommentForm(context["request"], obj)
        try:
            context["posted_comment_form"]
        except KeyError:
            context["posted_comment_form"] = form
        context["unposted_comment_form"] = form

        # Now pretend we are comments_for tag, and get the string resp it would.
        comments_str = render_to_string("generic/includes/comments.html",
                                        RequestContext(request, context))
        response_data = {}
        response_data['comments'] = comments_str
        response_data['success'] = 'true'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
