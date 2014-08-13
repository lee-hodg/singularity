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
