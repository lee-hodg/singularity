# Theme development guide #

## Tools ##

Make a static copy of the entire site:

    httrack http://127.0.0.1:8000 -O /home/lee/Desktop/Singularity_static/ +*127.0.0.1/* -v -s0

(needs local django dev server to be running).

Make a zip of relevant parts of theme:
    
    zip -r /home/lee/Desktop/Singularity.zip . -x static/\* \*.git\* logicon/local_settings.py \*.pyc logicon/MYNOTES.md venv/\*

## Form templates ##

The `fields_for` templatag is a nice way to standardize the layout of various forms appearing on your site (and associated field errors), for example contact forms (although in this theme I don't actually use it on contact form), blog post comments and replies to comments. You can edit the template that this tag renders to by copying the file `mezzanine.core.templates.includes.form_fields.html` to your `theme.templates.includes` dir, and editing the HTML as you like.

## Editing comments (for blog or otherwise)

Copy the file `mezzanine.generic.templates.generic.includes.comment.html`
and `comments.html` (similar for `rating.html` or style `disqus.html` too), then edit as you like. See my blog post series on Mezzanine comment and how they work recursively for more.

## Easiest way to get content from the server to local

Just copy the `/srv/databases/` logicon db to the local folder on laptop as `dev.db`, also
grab the media uploads from `/srv/www/logicon/media/uploads` as a tar ball, and put them in the local media dir.

Remember that `DEBUG=True` is needed for the local runserver to serve static content too.
The static content itself should be in the git repo, and we just need a `collectstatic` to be ran.

## urls 

By default Mezzanine ships with the static `index.html` as the root (`^$`) homepage. To make
a homepage that is a `Page` object whose model you can customise and edit in the page tree, like another other Mezzanine page, you must create your model, run south and then add the page in the admin to the tree, before you specify its URL (in the Meta Data section) as `/`. Now uncomment the line

    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

in the urls file. Finally, add any other custom urls under "MEZZANINE'S URLS" but before the catchall

    ("^", include("mezzanine.urls")),

line. 

For example I have my custom AJAX view for comments here(this view enables AJAX pagination of my comments):

    ("^ajax_comments/(?P<pk>\d+)/$", 'theme.views.ajax_comments')



# defaults.py

In this file you can register settings to be editable in the admin easily. See the docs
[here](http://mezzanine.jupo.org/docs/configuration.html#registering-settings) for example.
This also makes the setting available in a view with

    from mezzanine.conf import settings
    settings.SOCIAL_LINK_FACEBOOK

for example.

Note that if multiple settings are prepended with the same name before the underscore,
they will be displayed within the same section in the admin, e.g. we have the SOCIAL and
PERSONAL sections. NB you **DON'T** also set the setting in `settings.py`.

The `COMMENTS_...` block already exists for example, so comments related settings should be added to it by the appropriate prepend. See [here](http://mezzanine.jupo.org/docs/configuration.html) for more settings available by default.

To make these settings accessible in templates they need to be appended to the existing setting
`TEMPLATE_ACCESSIBLE_SETTINGS`.

# admin.py

For editing child models of the parent (i.e.) inlines (for example slides on homepage), it's best to see the Django docs, or just try them out. Mezzanine difference it that it usually just adds `Dynamic`, which just adds some js to  add another one easily, e.g. instead of `DynamicInlineAdmin` we have `TabularDynamicInlineAdmin`. 

# page_processors.py

Page processors are a little like views, but whereas a URL points to a given view as specified in `urls.py`, page processors will always operate for a given page type.

Note that the `published()` filter obviously returns only pages published, and `published(for_user=request.user)` returns only
the pages that are published and *accessible* to the current `request.user`, e.g. admin, staff, anonymous etc..

# views.py

My only custom view was an AJAX view to handle AJAX paginating comments.

# index.html

## Musings on better way to add contact form to HomePage

Could there be a better way to put a form on the homepage?
Starting out with the Form type page model and extending it would seem like a good idea.
This way we could do all the nice things in the admin that one can do usually for the Form page such
as managing fields, making fields required or not, submit button text recipient emails etc. We'd of course need to extend this Form model to make our HomePage model, and the multitude of fields that go with that, model, headings, subheadings, and so on.

Simply subclassing of Form instead of Page doesn't seem to play well. 
It seems you can't overwrite the Form, you can only inherit from Page in Mezzanine. Field injection
on the Form model is an option. Simply copy and pasting the Form model, customising, and then using that, would be another
(i.e. just copy and paste these fields into the HomePage model.)

It probably is even easier just to add any desired fields like `contact_recipients` to the HomePage model.

## Thumbnail templatetag and jpegs

For the `thumbnail` template tag to work with jpegs, you will need 
to install the necessary lib for `pillow` to do conv: 

    sudo apt-get install libjpeg-dev

and reinstall pillow: 
    pip install -I pillow

Otherwise you will just get the original image url returned, not a scaled version. 
You can use the shell to investigate this with 

    from mezzanine.core.templatetags.mezzanine_tags import thumbnail.

Note when using `thumbnail` something like `0 100` means height fixed at `100`, but that width will scale proportionally to aspect ratio. There are also options like `top=0 left=0` to choose how image is cropped (default `0.5 0.5`, which will crop vertically and horizontally in center). Finally there is the quality option. See Mezzanine docs for more.

## Mixitup panel

The mixitup panel has a finite delay in filling the
`#Container` div upon page load. This delay is both due to image loading
(if images not already in browser cache) and the animation itself.

This means upon page load initially
the div is smaller, and `#link-contact` redirects (either on form error, or external (non-index) page loads) are messed up. The offset from top is actually changing as Mixitup fills the `#Container` div.

Setting `min-height` of the section div does not help, since the user controls content, we don't know
what that `min-height` should be all the time, so if they add more and more PortfolioItems until the section height is beyond `min-height`, we will be back to square one when the animation expands the section beyond `min-height`..

The jQuery `$(window).load()` can help with image loading. Regarding the animations: I used the `mixItEnd` callback of the mixitup script and a counter to fire this function whenever the
count is zero (fire only on page loads, not every time that the user does the sort animation).
I also use a recursive check to make sure the height of the last image is non-zero to test
whether images are truly loaded.

1)If the contact-form has errors this function just redirects to contact form. 2) If not, but the user 
loaded the index page from an external page(e.g. nav on resume page), and wanted to get to a given sec using the hash it redirects the user there, now the animation is done and offsets from top can be correctly calculated.

## The method `blog_post.description_from_content()`

N.B. to see the way `description_from_content()` works see 
`mezzanine.core.models.py`. If there is a paragraph sep by `<br/><br/>` with
`</p>` at end of the whole block, this function can end up taking the whole block 
. The reason is it looks for `</p>` first using the list 

    ends = ("</p>", "<br />", "<br/>", "<br>", "</ul>", "\n", ". ", "! ", "? ") 
    for end in ends: pos = description.lower().find(end)

It thus finds the `</p>` exists, sets it to be the end point for truncation,
and then stops (even though `<br/>`  came before). I suppose it guards against hanging `<p>` this way....

This is not the behaviour I want, so I just add `truncatewords_html:100`
too to ensure this doesn't get too long no matter what user enters.

## Contact form fields

Could have used the `fields_for` tag just like for blog comment replies. With the `includes/form_fields.html` setting the styling universally for fields, but I thought I'd do it a different way here.

## Page menus 

**Recursive building.**

 See the [Page Menus docs](http://mezzanine.jupo.org/docs/content-architecture.html)
 Notice if e.g. in zeroth branch we recursively make a call to `page_menu`
 , which is the function we called from base.html, the second time round we will
 be in a sub-branch, so the branch_level not zero, and flow jumps to `else` clause. Here again
 a recursive call to `page_menu` is made if any children present, and so on.

**dropdown.html**

 With our one-page design and the need for links to **sections** of the home page in this dropdown,
 rather than simply absolute links to independent pages, adding these section hash links to sections
 initially posed a problem. 

 The best solution I ultimately found was to add 'Link' type objects
 to the page hierarchy in the admin (this is the Mezzanine way).
 You can choose the link URL to be # to make it a dud,
 or to something like `#link-features` to link to a section on the index page itself.
 Now you can simply drag and drop your other pages under these links if needed.
 (yes you can drag-and-drop under existing pages too, just pull to the right).

 Other options where explored (and seem silly now), but each had problems. Slugifying the title with `page.title|slugify`, and using this like `#link-{{page.title|slugify}}` in the href for all parent pages, fails since not all parent links should be section links, and secondly if the user changes the page title so that it no longer matches the section anchor on index the whole idea breaks down.

 Using field injection on the Mezzanine Page model (remember we can't subclass so this is
 how we must add new custom fields) to add a `sectionLink` field was another idea.
 This would give the user option in the admin for every Page. If filled in we'd use a section link
 rather than absolute link. For example if `page.portfolio` then `page.sectionLink` could be set as `#link-portoilio`. This still relies on identifying the page as the portfolio, which may not be reliable if user changes names or has multiple portfolios. The remnants of field injection can be seen in `settings.py` anyway, and may be useful for something else in future.

However, I still used `page.html_id` to identify the blog page, and to specify a section link for it rather the absolute URL for the blog page itself.  This seems to be robust to user changing things like blog title(Remember blog is both section on homepage and independent page).

N.B. The jsddm we are currently using for the dropdown menu is limited to single level(even if extra `<ul>` are inserted in the HTML). See mlddm for more(not free!).

**Filtering pages in which menus**

For filtering based on `page.in_menu`, make sure you change `PAGE_MENU_TEMPLATES` of `settings.py`
, so that the menus offered in admin for page includes correctly match your menu templates. You can also
set the default menus a page should appear in in `settings.py` too with `PAGE_MENU_TEMPLATES_DEFAULT`. Now the user can easily select which menus a given page should appear in from the admin.

# comments

## comment.html

### Pagination notes (see my blog for more)

Use a custom `paginated_comment_thread` inclusion tag to build the parent
(zeroth level in tree) comments. The template it calls `comment_with_pagination.html`,
is an extension of `comment.html`, only it overrides the pagination_foot block, with
some code that actually calls `pagination_for` on the comment paginator that the `paginated_comment_thread`
tag provides it with (`comment_for_thread_paginator`).

In the tag the paginate function works by simply taking the `comment_for_thread` list (which
in our case in the list of zeroth level comments for a BlogPost) and then ripping the page
number parameter from the GETstr. It takes `COMMENTS_PER_PAGE` custom setting, and behaves how you'd
expect. When `.object_list` is called on it, it yields up the list of comments for that page, which
can then just be displayed as normal.

By passing the actual paginator itself back, we can easily render the pagination footer
(arrows and "Page 1 of 2" etc) by calling the pagination_for mezzanine tag (c.f. blog_post_list).

You may think about doing this with only one tag and one template, which might have been possible, but
the problem is the recursive calls modify the context as they are called one by one, and by the time you
get to the bottom of the html in the outer `comment.html` template the context is different to at the top, and
to what you might have been expecting, thus it's very difficult to render pagination footers for just the parents.

The approach used with the extension of `comment.html` by comment_with_pagination.html is fairly DRY anyway, so we
should be good.

## comments.html

Some old and redundant ajax post script

    //NB post is just an ajax conveinience method
    //jQuery.post( url [, data ] [, success ] [, dataType ] )
    //it doesn't offer error handler. But this is ajax req errors
    //not django form errors, don't confuse the two!
    //$.post(form.attr('action'), form.serialize(), function(data) {
    //ajax success
    //            if (data.location) {
    //                // I think this is for the case when login needed to comment
    //                // to redirect to designated login url
    //                console.log('AJAX performing a redirect')
    //                location = data.location;
    //            }else if(data.errors){
    //                console.log('There were some form errors');
    //                if(data.errors.hasOwnProperty('name')){
    //                    //build up ul error list
    //                    var items = [];
    //                    var name_field = $(form).find('.input_id_name');
    //                    items.push('<ul class="errorlist">');
    //                    $.each(data.errors.name, function(i, item) {
    //                        items.push('<li>' + item + '</li><i class="tag-tip"><i></i></i>');
    //                    });
    //                    items.push('</ul>');
    //                    $(name_field).prepend(items.join(''));
    //                }
    //                if(data.errors.hasOwnProperty('email')){
    //                    //build up ul error list
    //                    var items = [];
    //                    var email_field = $(form).find('.input_id_email');
    //                    items.push('<ul class="errorlist">');
    //                    $.each(data.errors.email, function(i, item) {
    //                        items.push('<li>' + item + '</li><i class="tag-tip"><i></i></i>');
    //                    });
    //                    items.push('</ul>');
    //                    $(email_field).prepend(items.join(''));  
    //                }
    //                if(data.errors.hasOwnProperty('comment')){
    //                    //build up ul error list
    //                    var items = [];
    //                    var comment_field = $(form).find('.input_id_comment');
    //                    items.push('<ul class="errorlist">');
    //                    $.each(data.errors.comment, function(i, item) {
    //                        items.push('<li>' + item + '</li><i class="tag-tip"><i></i></i>');
    //                    });
    //                    items.push('</ul>');
    //                    $(comment_field).prepend(items.join(''));
    //                }
    //            }else{console.log('What happened?');}
    //        }, 'json');  
    //
    //        //event.preventDefault();
    //        return false;
    //    });
    //});

# Blog posts

## Post I

[Mezzanine][1] is a CMS based on the Django framework. Like any CMS such as Wordpress, it gives the user an interface for managing blog posts, form data, pages and many other types of content. It also has an active community, which takes the form of an IRC channel and a google group. In fact I created this site itself with the Mezzanine CMS. I'd recommend anyone who wants to get started with Mezzanine to check out the [tutorial][2] by Josh Cartmell and [the one][3] by Ross Laird, they really helped me when I was starting out.

Whilst, I doubt I'll be able to write something as clear and useful as the above two mentioned authors (which I definitely recommend you start with if you are completely new to Mezzanine, as here I won't be discussing the basics, since those two sites already do a great job of that), lately I began creating a new Mezzanine theme, and I thought I'd share a few things that weren't immediately obvious (at least to me) when trying to accomplish some tasks in Mezzanine, as well as some general notes about Mezzanine.

This first post will form part one of a series of three, and here I will prime with a background discussion/walk-through of the comment source code in Mezzanine.
In the later posts of the series, I will show you how to paginate comments, AJAXify comments and introduce stackexchange style popularity rank/time-decay sorting by ranking of your comments.

#Understanding comments in Mezzanine

What CMS based site is complete without a blog? and every blog of course needs a system for comments. Mezzanine does most of the hard work for you by default, but you may want to add a few extra features such as comment pagination and AJAX calls.

The way a blog post is rendered is controlled by the `blog/blog_post_detail.html` template, and in this template you will see near the bottom `{% comments_for blog_post %}`  This is a Django [inclusion tag][4] for rendering the comments of a given blog post. Take a look at the source code for this tag at `mezzanine/generic/templatetags/comment_tags.py ` (remember comments are generic items, not necessarily associated with a blog post):

    #!python
    @register.inclusion_tag("generic/includes/comments.html", takes_context=True)    
    def comments_for(context, obj):                                                  
        """                                                                          
       Provides a generic context variable name for the object that                 
       comments are being rendered for.                                             
       """                                                                          
       form = ThreadedCommentForm(context["request"], obj)                          
       try:                                                                         
            context["posted_comment_form"]                                              
       except KeyError:                                                             
           context["posted_comment_form"] = form                                    
       context["unposted_comment_form"] = form                                      
       context["comment_url"] = reverse("comment")                                  
       context["object_for_comments"] = obj                                         
       return context

What is going on here? Well, not a lot; the `obj` in our case is the `BlogPost` associated with the detail page, a suitable form for posting a new comment is instantiated from the request, and the context is updated with some generically named variables (the url, `comment_url`,  where a comment form should be sent upon submission so that the correct view can deal with it, and the blog object itself, which the comments are to be fetched for). After the context has been suitably updated we send the context back to the template to be included, `generic/includes/comments.html`.  I suggest you open that template next and take a look at the source as I take a walk through it in what follows.

In this template we find the key inclusion tag, `{% comment_thread object_for_comments %}` (remember that the `object_for_comments` variable in the context was set to be the BlogPost object in our case). The `comment_thread` tag (again you can view the code in `generic/templatetags/comment_tags.py`) first grabs the comments queryset for the given blog post (depending on whether the user is staff or not), e.g.

    ::python     
         comments_queryset = parent.comments.all()      

and then does roughly
 
    ::python
    for comment in comments_queryset:               
        comments[comment.replied_to_id].append(comment)              

This means the comments dictionary ends up being built in a hierarchy. The zeroth level parent comments, replied to no other comments, and their `replied_to_id` attribute is `None`. Thus the `None` key of the dict points to a list of all the zeroth-level comments in the tree. If on the other hand, a comment with id of 3 has a number of direct replies, the key `3` of the dict will point to a list containing that comment's children. In other words, each key of the dictionary is either None (representing the BlogPost itself of which all zeroth-level comments are children) or is the id of a comment which has children, and each of these keys points to a list containing all of the relevant parent object's child comments. 

*In case you are wondering why the comments dictionary doesn't trigger a KeyError when you at first try to append a comment to a given key (that doesn't yet exist in the dictionary) it is actually a `defaultdict(list) ` object.  This object is like a regular dictionary, except that if you try to get a value for a non-existent key, it doesn't throw an error but rather returns an empty list. Handy eh?*

The other smart thing to notice about this tag is that it only builds up the dictionary of comments once. If the `all_comments` var already exists in the context, the line `if "all_comments" not in context:` ensures we don't bother to build it again. This is important, since as we will see this tag must be called recursively, and it would be a performance hit to regenerate the dictionary each time.

All that's left to do now is grab the parent's id and return just the direct descendants to start with. 

    ::python
    parent_id = parent.id if isinstance(parent, ThreadedComment) else None

(i.e. for the BlogPost itself or other non-comment object for which comments are being generated, the `parent.id` is going to read `None` otherwise it will read as the id of the comment that the tag was called on)

Armed with this id we can return the direct descendants only, first of all, with

    ::python
    "comments_for_thread": context["all_comments"].get(parent_id, []),

So the first time the `comment thread` inclusion tag is called (in `comments.html`), it is being fed the blog post itself as parent, the id is going to read as `None` (no ancestors) and all the direct descendant comments (level zero comments) are going to be sent back in a list `comments_for_thread`.

## Let the recursion begin

Now browse to `templates/generic/includes/comment.html`, this is the template that the `comment_thread` tag we just discussed is going to feed with the context that it built up for us.

The `comments_for_thread` context variable (which contains the zeroth-level blog post comment list) is looped over:

    ::python
     {% for comment in comments_for_thread %}
         .
         .
         # display the comment and its associated reply form...

         # recursively call the comment_thread tag
         {% comment_thread comment %}
    {% endfor %}

So in the above the comment is displayed in whatever way you like, along with an associated "reply-to-comment" form for replying directly to this comment, and finally a recursive call is made to the `comment_thread` tag, but this time with the comment itself as the object to be acted upon (recall the first time around it was the blog post object). This happens for every comment in the list of zeroth level comments, and these Django inclusion tags means html is being pushed into the template at the appropriate places as the loop marches onward. 

Let's go through one more level of iteration just for absolute clarity. Note the context is persistent through each call to the tag, and this time when the `if "all_comments" not in context:` check runs, it finds that indeed `all_comments` is in the context and there is no need to go through all the work of rebuilding this dictionary. Thus, the next step is to grab the id of the level one comment that did the calling, and then reset the `comments_for_thread` variable to point to a list of all the direct descendants of this comment itself:

    ::python
    "comments_for_thread": context["all_comments"].get(parent_id, [])

With the context modified, it is fed back to `generic/includes/comment.html`, the descendants are looped over, each one of which is displayed, and which then calls the tag again...ad infinitum...

## Summary

Hopefully, you have now seen how comments for an object are built up and displayed in Mezzanine by default. In part II of this series, I will explain how to use this understanding to do some funky things: pagination of comments, ordering of comments by popularity decay algorithms, and AJAXifying comments.

  [1]: http://mezzanine.jupo.org/
  [2]: http://bitofpixels.com/blog/mezzatheming-creating-mezzanine-themes-part-1-basehtml/
  [3]: http://www.rosslaird.com/blog/first-steps-with-mezzanine/
  [4]: https://docs.djangoproject.com/en/dev/howto/custom-template-tags/#inclusion-tags

## Post II

In my previous post on Mezzanine comments, I tried to give a walk-through of how comments for an object work in Mezzanine. In this post, armed with that knowledge, I will show you how you can get paginated comments for your Mezzanine blog (or indeed any other object you want to generate comments for).

We saw in the previous post that it was the `comment_thread` inclusion tag that was doing most of the grunt work generating comments recursively. In order to have pagination, I'm going to define a new tag based on this, called `paginated_comment_thread`, and a new template `comment_with_pagination.html`.  

In the `comments.html` template we will now call `{% paginated_comment_thread object_for_comments %}` instead of plane old `{% comment_thread object_for_comments %}` (remember in `comments.html` it is the blog post itself that is the `object_for_comments`).

How does this new tag look?

    ::python
    from mezzanine.utils.views import paginate 
    @register.inclusion_tag("generic/includes/comment_with_pagination.html", takes_context=True)
    

    .
    .
     # same code as original building up the all_comments dict and updating the context
    .
    # Pagination for zeroth level comments                                       
    comments_for_thread = context["all_comments"].get(parent_id, [])             
    context.update({"comments_for_thread": comments_for_thread})                 
    if parent_id is None:                                                        
        # Zeroth-level comment                                                   
        comments_for_thread_paginator = paginate(comments_for_thread,            
                                                 context["request"].GET.get("page", 1), 
                                                 settings.COMMENTS_PER_PAGE,        
                                                 settings.MAX_PAGING_LINKS)     
                             
        context.update({"comments_for_thread":                                   
                        comments_for_thread_paginator.object_list})              
        context.update({"comments_for_thread_paginator":                         
                        comments_for_thread_paginator}) 
                         
    context.update({                                                             
        "no_comments": parent_id is None and not context["all_comments"],        
        "replied_to": replied_to,                                                
    })                                                                           
    return context 

This is largely the same tag as the default, except that instead of just adding the `comments_for_thread` to the context straight away, if the parent is `None` i.e. as we learnt in the last tutorial, if the comment is a zeroth-level (direct descendent of a BlogPost object) comment, it paginates the list first. In other words it uses the setting `COMMENTS_PER_PAGE` to divide up the list up into pages each containing a fixed number of comments, and sets the active page to that which it grabs the page variable from the GET string of the request (by default page 1). Note that this setting must be added to your `settings.py` file, and also if you want to use it in a template,  you must register it in your `defaults.py` file.

To get the actual list of objects for this active page we can call the `.object_list` method of the paginator, and update the `comments_for_thread` context variable with just the parent comments on the active page. This is returned in the context along with the paginator object itself as `comments_for_thread_paginator` to my new template `generic/includes/comment_with_pagination.html`.

As for this new template, it is very simple:

    #!python
    {% extends "generic/includes/comment.html" %}

    {% load i18n mezzanine_tags %}

    {% block pagination_foot %}
        {% pagination_for comments_for_thread_paginator %}
    {% endblock %}

All we do to extend the regular `comment.html` template is to add the pagination footer (the thing with "previous" and "next" links and "page 1 of 2" for example) to the bottom of the template. The `pagination_for` tag is a built in Mezzanine tag that takes a paginator object, and generates the required html from it to form this "footer". Remember the paginator knows what page is active, it knows how many pages in total, and thus it has all the info needed to build up the usual paging "footer".


We just need to change `comment.html` itself a little bit to add the new block:
`{% block pagination_foot %}{% endblock %}` (you can place this wherever you want the pagination footer HTML to appear, I usually place it near the bottom, just before `{% if no_comments %}`). 


Otherwise the original `comment.html` template is unchanged. When the iteration over `comments_for_thread` occurs for all the zeroth-level comments(**FOR COMMENTS ON THAT PAGE OF PAGINATION ONLY THIS TIME**), it will be the regular `{% comment_thread comment %}` line that gets called, and thus the child comments will not be paginated and will render their context to the regular `comment.html` template. From that stage onward, it is the same old story as we met in the first part of the tutorial.

## Summary

Here I tried to show one method of paginating your comments in Mezzanine. I'm sure there are others. Next I will consider AJAXification.     

## Post III

In the previous two posts of this series, I tried to give a base understanding of the Mezzanine comments system and to show you how to paginate your Mezzanine comments (e.g. for a blog post). In this part of the series, I will show you how to use AJAX in your Mezzanine blog.

# How to AJAXify your shiny new paginated comments

The easiest way I found to do this was to create a new view function specifically for handling ajax requests for comment pages. First, in `urls.py`  add

    ::python
    #make sure this is above the mezzanine catchall!
    ("^ajax_comments/(?P<pk>\d+)/$", 'theme.views.ajax_comments'),

which takes the `pk` parameter of the object we want to get comments for. Then define the view function itself by

    ::python
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
            context = {}                                                             
            context["request"] = request                 
                                                                      
            # replicate context building of comments_for  tag                           
            context["object_for_comments"] = obj                                     
            context["comment_url"] = reverse("comment")                              
            form = ThreadedCommentForm(context["request"], obj)                      
            try:                                                                     
                context["posted_comment_form"]                                       
            except KeyError:                                                         
                context["posted_comment_form"] = form
            context["unposted_comment_form"] = form                                                                                         
            # Now pretend we are comments_for tag, 
            # and get the string resp it would. 
            comments_str = render_to_string("generic/includes/comments.html", RequestContext(request, context))           
            response_data = {}                                                          
            response_data['comments'] = comments_str                                    
            response_data['success'] = 'true'                                           
        return HttpResponse(json.dumps(response_data), content_type="application/json")


What this view is doing is essentially just replicating what the `comments_for` tag would normally do when encountered on the `blog_page_detail.html` page.  It builds a context from the blog post object and the request in exactly the same way. 

The tricky part comes in what to do with this context; normally an inclusion tag would pass it to a given template to be included, and the whole recursion chain would load. Luckily with the `render_to_string` function, we can simulate exactly that and get the HTML that would be built by the cascade that follows the call of the `comments_for` tag. Now with this string we can easily return a JSON dump of the data.

Finally for the frotend AJAX:

    ::javascript
    //ajax comment paging arrows
    $(function() {
        $('pagination-nav>li').click(function(event) {

        var link = $(this).find('a');
        // what page do does the link go to
        if ($(link).attr('href')){
            page_no = link.attr('href').match(/\?page=(\d+)/)[1]; 
        } else {
            // must be a disabled nav
            event.preventDefault();
            return false;
        }
        // with the pageno, make the ajax req
        $.ajax({
            url: '/ajax_comments/'+{{ object_for_comments.pk}},
            type: 'GET',
            data: {'page': page_no},
            dataType: 'json',
         })
        .done(function (data) {
            //ajax success
            if(data.success){
                //this means no server side errors
                //push data.comments into appropriate place
            }else{
                console.log("Oops, server side problem.");
            }
        })
       .error(function (request, error) {
            console.log('AJAX request error.');
         })

        //stop default behavior of links and numbers in paginated footer
        event.preventDefault();
        return false;
        });
    });

# Some other notes on Mezzanine comments and AJAX while we're here

The view for the submission of the comment forms handles some AJAX already in the out-of-the-box Mezzanine install, so if you want to use AJAX to process your comment form errors, you should be more or less good to go. You for example use

    ::javascript
    $(function() {
        $('form#blog-comment, .comment-reply-form').submit(function(event) {
        $.ajax({
            url: form.attr('action'),
            type: 'POST',
            data: form.serialize(),
            dataType: 'json',
         })
        .done(function (data) {
            //ajax success
            if (data.location) {
                // This is for redirection when login needed to post comment
                location = data.location;
            }else if(data.errors){
                // deal with form validation errors
            }
       .error(function (request, error) {
            alert('THANKS FOR THE COMMENT');
            location.reload();
         })
         return false
        });
    });

One thing I couldn't see in the out-of-the-box Mezzanine view to handle this form 
(`generic/views.py` comment) was how the view is supposed to handle case when *there are no validation errors*. It doesn't pass a JSON dump of the new data like I initially might have expected, it simply reloads the entire page/template, so as far as AJAX is concerned it looks like an error since it need no receive back the required JSON response. It's necessary thus, to simply thank the user for the comment before hand and then reload the page. Maybe I'm missing something?

Similarly the view for ratings also handles AJAX without any extra work sending you back the JSON of various useful variables, such as the updated rating's count(number of votes), average and sum (net score). So it's pretty easy to ajaxify the ratings forms in a similar manner to comment replies.

Finally if you are looking to order your comments by rating (perhaps with highest rating comments floating to the top, but their popularity decaying also with their age to stop all time greats lingering at the top forever), I suggest checking out [this](http://blog.jupo.org/2013/04/30/building-social-apps-with-mezzanine-drum/) post to see how easy it is in Mezzanine to implement a Reddit style popularity algorithm with a custom `order_comments_by_score_for` tag that gets called just before `comments_for` to update the `all_comments` context variable in exactly the same way as we have discussed only now with comments scored by your algorithm (with this in the context `comments_for` just skips building `all_comments` as it sees it is already there, and everything else runs just as normal for therein).

