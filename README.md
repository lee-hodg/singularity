# Theme user guide #

## Setting the homepage. ##

One of the first tasks you will have after installing the theme is to first create a new `HomePage` type of page in the admin area. After doing so, set the URL to `/` in the meta data. Now edit the `urls.py` by commenting out the entry for static homepage, and uncommenting the

    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home")

line.

## settings.py ##

Set your Django `SECRET_KEY` and `NEVERCACHE_KEY` (consider setting them in `local_settings.py` file or from the environment).  Add your site's domain to `ALLOWED_HOSTS`, and also remember to set `DEBUG=False` when you make the site live. You will also need to ensure that `STATIC_ROOT` and `MEDIA_ROOT` point to the correct location on your server, and finally make sure the database is setup correctly for your server.

## Admin settings ##

### Blog ###

This theme comes with the built-in threaded blog comments, which can be ranked (similarly to reddit or stackexchange, comments raise to the top with rank but also decay with time) are are paginated. However, if you would like instead to use `Disqus` to manage your comments, simply fill in the `Disqus` public and private keys and your `Disqus` shortname in the comments section of the admin settings area. 

If you choose to use the theme's built-in comments(by not setting Disqus information), then you can decide whether you would like your comments ordered by the ranking algorithm or simply by datetime. You can modify the `Score order comments` setting to achieve this. You can modify the number of comments per page, and whether to make comments ratable at all, also in the comments section of the admin settings page.

You can also choose the number of blog posts to be displayed per page with the `Blog posts per page` setting from the Miscellaneous section, and the gradation of colors in the blog's tag-cloud with `Tag Cloud Sizes` setting, also in the Miscellaneous section.

### Personal information and social icons ###

You can add in information like your name, address, email, telephone etc in the Personal section. This information is used to populate the  `CONTACT INFO` section near the contact form. If your Skype address is entered a link to begin a call to you will be added in the footer, and if you add your email a link to email you will be added in the footer. If you add the various social media available, links to these appear in the contact section and footer also.

### Misc ###

There are plenty of other features here that should be intuitive. You can your google analytics id to set up tracking, use the `Akismet` spam comment filtering service, change the number of search results appearing per page, and so on.
 
## Page tree structure 

You will notice in the demo site that `Features`, `Portfolios`, `Testimonials`, `Contact-us` and `Pages` are simply `Link` objects, which should be added to the page tree and whose URLs should be set respectively to `#link-features`, `#link-portfolio`, `#link-testimonials` `#link-contact`  and `#`. These are included in the menus `Index top nav bar` and `Non-index top nav bar` but not the `Footer` menu in the demo (the `Non-index top nav bar` is just the top navigation bar but when the user is not on the index page). These links allow navigation to various sections of the one-page index page. 

One can then add Portfolio pages under the Portfolio link, and in turn Portfolio Item type pages under the Portfolio pages. One can also add Resume pages and About-us pages under the Pages link.

Mezzanine allows you to drag and drop the order and hierarchy of your pages, so reorganization is easy, and with Mezzanine you can choose which pages appear in which navigation menus by selecting/deselecting the check-boxes for the corresponding menus.

## Pages ##

### Home Page ####

**Features**
Most of the admin for the home page should be intuitive after seeing the demo, but some notable features: You can use either font-awesome icon classes or regular images to set the icon in the features section. So for example not adding an image but changing the "Fa icon" field to `fa-cog` will give you a cog icon in the features section. Alternatively keeping the "Fa icon" field as `none` but adding an image will use your image as the feature icon. Otherwise these feature icons should be self-explanatory; you add the title, a paragraph of text describing the feature and an optional link.

**Portfolio**

The home page includes a drop down of your available portfolios, if you select one of these to be "featured", then any items from it that are marked as featured will be included in the panel on the home page.

**Contact**

Add the e-mail address you wish contact form messages to be sent to in the contact recipients field (if multiple provide a comma separated list).

**Misc**

Other things are pretty standard, you can change section heading and subheading, add slides with captions and subimages for the responsive slider, change the parallax section images, and add testimonials from your clients.



# Theme development guide #

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

## Mixitup panel

The mixitup panel has a finite delay in filling the
`#Container` div upon page load. This delay is both due to image loading
(if images not already in browser cache) and the animation itself.

This means upon page load initially
the div is smaller, and `#link-contact` redirects (either on form error, or ext page loads)
are messed up. The offset from top is actually changing as mixitup fills the `#Container` div.

Setting min-height of the section div does not help, since the user controls content, we don't know
what that min-height should be all the time, so if they add more and more PortfolioItems until the section
height is beyond min-height, we will be back to square one when the animation expands the section beyond min-height..

jQuery `$(window).load()` can help with img loading. 

Regarding the animations: I used the `mixItEnd` callback of the mixitup script 
and a counter to fire this function, whenever the
count is zero (fire only on page loads, not everytime user does the sort animation).

I also use a recursive check to make sure the height of the last img is non-zero to test
whether images are truly loaded.
1)If the contact-form has errors this func just redirects to contact form. 2) If not, but the user 
loaded the index page from an external page(e.g. nav on resume), and wanted to get to a given sec using the hash
it redirects the user there, now the animation is done.

### blog_post.description_from_content

NB to see the way `description_from_content()` works see 
`mezzanine.core.models.py`. If there is a para sep by `<br/><br/>` with
`</p>` at end of the whole block, this function can end up taking the whole block 
. The reason is it looks for `</p>` first using the list 

    ends = ("</p>", "<br />", "<br/>", "<br>", "</ul>", "\n", ". ", "! ", "? ") 
    for end in ends: pos = description.lower().find(end)

it thus finds the `</p>` exists sets it to be the end point for truncation,
and then breaks (even though `<br/>` etc came before) 
I suppose it guards against hanging `<p>` this way....

I just add truncatewords_html:100
too to ensure this doesn't get too long no matter what.

### thumbnail

Note something like 0 100 means height fixed at 100, but width will scale proportionaly to aspect ratio. There
are also options like `top=0 left=0` to choose how image is cropped (default 0.5 0.5, which will crop vertically and horizontally
in center). Finally there is the quality option.

### Contact form fields

Could have used the `fields_for` tag just like for blog comment replies. With the `includes/form_fields.html` setting the styling
universally for fields, but I thought I'd do it a different way here.

# Page menus 

 ## Recursive building.
 See the [Page Menus docs](http://mezzanine.jupo.org/docs/content-architecture.html)
 Notice if e.g. in zeroth branch we recursively make a call to `page_menu`
 , which is the function we called from base.html, the second time round we will
 be in a subbranch, so the branch_level not 0, and flow jumps to `else`. Here again
 a recursive call to `page_menu` is made if any children present, and so on.

 ## dropdown.html

 With our one-page design and the need for links to *sections* of the home page in this dropdown,
 rather than simply absolute links to independent pages, adding these section # links to sections
 initially posed a problem. 

 The best solution I ultimately found was to add 'Link' type objects
 to the page heirarchy in the admin. You can choose the link URL to be # to make it a dud,
 or to something like #link-features to link to a section on the index page itself.
 Now you can simply drag and drop your other pages under these links if needed.
 (yes you can drag-and-drop under existing pages too, just pull to right).

 Other options where explored, but each had problems. Slugifying the page.title|slugify
 and using this like #link-{{page.title|slugify}} in the href for all parent pages, fails
 since not all parent links should be section links, secondly if the user changes the page title
 so that it no longer matches the section anchor on index the whole idea breaks down.
 Using field injection on the Mezzanine Page model (remember we can't subclass so this is
 how we must add new custom fields) to add a BooleanField 'sectionLink' checkbox was another idea.
 This would give the user a checkbox in the admin for every Page, and if checked we'd use a sectionLink
 rather than absolute URL. For example if page.portfolio and page.sectionLink: href="#link-portoilio".
 This still relies on identifiying page as portfolio, which may not be reliable if user changes names
 or has multiple portfolios. The remnants of field injection can be seen in settings.py anyway,
 and may be useful for something else in future.

 I used `page.html_id` to identify the blog page and specify section link for it rather the blog page itself. 
 This seems to be robust to user changing things like blog title(Remember blog is both section on homepage and
 independent page)

 N.B. The jsddm we are currently using for the dropdown menu is limited to single level even if extra <ul> are inserted.
 See mlddm for more(costs).

 ## Filtering pages in which menus

    For filtering based on `page.in_menu`, make sure you change `PAGE_MENU_TEMPLATES` of `settings.py`
 so that the menus offered in admin for page includes correctly match your menu templates. You can also
set the default menus a page should appear in in `settings.py` too. Now the user can easily select which menus
a given page should appear in.

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

Some old ajax post script

        //NB post is just an ajax conveinience method
        //jQuery.post( url [, data ] [, success ] [, dataType ] )
        //it doesn't offer error handler. But this is ajax req errors
        //not django form errors, don't confuse the two!
//        $.post(form.attr('action'), form.serialize(), function(data) {
//            //ajax success
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