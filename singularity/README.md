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

###Resume page###

Most of the fields are self-explanatory, such as the title of your resume, your personal information, your photo, and personal statement. There are various sections such as "Experience", "Education", "Publications", whose headings and subheading can be set. 

**Experiences**

Work experiences, include the name of the place in which you worked ("Institution"), your title whilst there, the date range you worked there and some statements about working there (e.g. a bullet list of your responsibilities and achievements). You can easily add more experiences by clicking `Add another`.

**Qualifications**

These go under the section titled "Education" in the demo. Each has fields for the institute at which you studied, qualification title, date range, and some statements about your qualification (e.g. grade, advisor, courses taken...). Again you can easily add another by clicking the button.

**Publications**

Here you can add any publicationsmay have. Including the journal and arXiv preprints.

**Skills**

The `content` field is used to provide the rich text field for the skills section.

###About us###

Add your company values and history and employee profiles (picture, title, blurb).

###Portfolio page (don't confuse with the Portfolio link to section on index)###

Use `content` to set the text appearing above the portfolio (e.g. "selection of my freelance work"), and use `Columns` to select if this Portfolio is to be 2-column, 3-column or 4-column.

### Portfolio item ###

If `Featured` is checked, then if this items parent porfolio is selected as the featured portfolio on the homepage (see above) then this item will be amongst those items featured on the homepage from the portfolio. PortfolioItems also have categories that will appear in the right-hand side of the page, a featured image (the image displayed when the item is viewed in the parent portfolio) and a selection of extra images to appear in the item's slider. Short description appears in the right-hand panel and as the sub-text when viewing item in parent portfolio.

