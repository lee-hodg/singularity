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


