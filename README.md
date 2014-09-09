# Setting the homepage.

You need to first create a new `homepage` type of page in the admin,
and set the URL to `/` in the meta data. Now edit `urls.py` by commenting
out the entry for static homepage, and uncommenting

    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home")

line.

# Editing the template used by fields_for tag (e.g. in form for blog comment)

Copy the file mezzanine.core.templates.includes.form_fields.html to your
theme.templates.includes dir.

Now edit it as you would like.

# Editing blog comments themselves

Copy the file mezzanine.generic.templates.generic.includes.comment.html
or comments.html (similar for rating or style disqus.html too)

Proceed to edit.

# South migrations for theme

Weirdly theme ended up with two initial migrations  `0001_initial` and `0007_initial`, we need to fake the latter. This can be achieved by manual migrations upto and including six, e.g.

    python manage.py migrate theme 0001
    python manage.py migrate theme 0002
    .
    .
    .

then faking seven:
    
    python manage.py migrate theme 0007 --fake

followed by the rest:

    python manage.py migrate theme
# Easiest way to get content from the server to local

Just copy the `/srv/databases/` logicon db to the local folder on laptop as `dev.db`, also
grab the media uploads from `/srv/www/logicon/media/uploads` as a tar ball, and put them in the local media dir.

Remember `DEBUG=True` needed for the local runserver to serve static content too.
The static content itself should be in the git repo, and we just need a `collectstatic` to be ran.


# urls 

By default Mezzanine ships with the static index.html as the ^$ homepage. To make
a homepage that is a `Page` object whose model you can customise and edit in the page tree
you must create your model, run south and then add the page in the admin to the tree, before
you specify its URL (in the Meta Data section) as "/". Now uncomment the line

    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

in the urls file. Finally, add any other custom urls under "MEZZANINE'S URLS" but before the catchall

    ("^", include("mezzanine.urls")),

line. For example I have my ajax view for comments here:

    ("^ajax_comments/(?P<pk>\d+)/$", 'theme.views.ajax_comments')

# settings

Need to decide whether to use rating for comments with the `COMMENTS_USE_RATINGS` bool setting,
if not they will be ordered by date. Need to add the site domains to `ALLOWED_HOSTS`, also set
`DEBUG=False`. Need to set the database correctly plus `STATIC_ROOT` and `MEDIA_ROOT`. The urls
file should be set in `ROOT_URLCONF` too. `SECRET_KEY` should be set, probably from env.

# defaults.py

In this file you can register settings to be editable in the admin easily. See the docs
[here](http://mezzanine.jupo.org/docs/configuration.html#registering-settings) for example.
This also makes the setting available in a view with

    from mezzanine.conf import settings
    settings.SOCIAL_LINK_FACEBOOK

for example.

Note that if multiple settings are prepended with the same name before the underscore,
they will be displayed within the same section in the admin, e.g. we have the SOCIAL and
PERSONAL sections. NB you DON'T also set the setting in `settings.py`. 

To make these settings accessible in templates they need to be appended to the existing setting
`TEMPLATE_ACCESSIBLE_SETTINGS`.
See [here](http://mezzanine.jupo.org/docs/configuration.html) for more settings available by default.

# admin.py

For editing child models of the parent (i.e.) inlines, it's best to see the Django docs, or just
try them out. Mezzanine usually just adds `Dynamic`, which just adds some js to  add another easily.

# models.py

# page_processors.py

Note that the `published()` filter obviously returns only pages published, and `published(for_user=request.user)` returns only
the pages that are published and accessible to the current request.user, e.g. admin, staff, anonymous etc..

# views.py

# base.html

# index.html

## Thoughts on better way to add contact form to HomePage

Could there be a better way to put a form on the homepage?
Starting out with the Form type page model and extending it would seem like a good idea.
This way we could do all the nice things in the admin that one can do usually for the Form page such
as managing fields, making fields required or not, submit btn text recipient emails etc. We'd of course need to extend this Form model
to make our HomePage model and all the fields that go with that model, headings, subheadings, and so on.
Simply subclass of Form instead of Page doesn't seem to play well. 
It seems you can't overwrite the Form, you can only inherit from Page. Field injection
on the Form model is an option. Simply copy and pasting the Form model, customising, and then using that, would be another
(i.e. just copy and paste these fields into the HomePage model.

## Thumbnail templatetag and jpegs

For the thumbnail templatetag to work with jpegs, you will need 
to install the necessary lib for pillow to do conv: `sudo apt-get install libjpeg-dev`
and reinstall pillow: pip install -I pillow, otherwise you will just get the original 
image url returned. You can use the shell to work this out with 
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

See the source, this stops at first para or br (etc) unless user unchecked generate in admin and entered their own.
The problem is it searches para first and if there is a para right at the end but a break before it, it will still take
the latter para as the truncation point (I guess to avoid leaving trailing html tags?). Instead I just add truncatewords_html:100
too to ensure this doesn't get too long no matter what.

### thumbnail

Note something like 0 100 means height fixed at 100, but width will scale proportionaly to aspect ratio. There
are also options like `top=0 left=0` to choose how image is cropped (default 0.5 0.5, which will crop vertically and horizontally
in center). Finally there is the quality option.

### Contact form fields

Could have used the `fields_for` tag just like for blog comment replies. With the `includes/form_fields.html` setting the styling
universally for fields, but I thought I'd do it a different way here.

# Page menus 
