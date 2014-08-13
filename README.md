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
