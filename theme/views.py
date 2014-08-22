from django.shortcuts import render
from mezzanine.generic.templatetags.comment_tags import comments_for
from django.template.loader import render_to_string


def ajax_comments(request, pk):
    '''
    Render to string the comments for a given BlogPost or
    whatever.
    '''
    context["request"] = request
    obj = BlogPost.objects.filter(pk=pk)
    context = comments_for(context, obj)
    comments_str = render_to_string("generic/includes/comments.html",
                                    RequestContext(request, context))
    response_data = {}
    response_data['comments'] = comments_str
    return HttpResponse(json.dumps(response_data), content_type="application/json")
