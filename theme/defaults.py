from mezzanine.conf import register_setting
from django.utils.translation import gettext as _  # import as '_', used for trans

# These register setting to editable in the admin easily.
# http://mezzanine.jupo.org/docs/configuration.html#registering-settings

# Register our new settings, so we can change their vals in admin.
# this also makes them available in a view say as
# from mezzanine.conf import settings
# settings.SOCIAL_LINK_FACEBOOK.
# But if we want avail in template see further down.
register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
                  "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
                  "header."),
    editable=True,
    default="https://twitter.com/lee84bc",
)

register_setting(
    name="SOCIAL_LINK_VIMEO",
    label=_("Vimeo link"),
    description=_("If present a vimeo icon linking here will be in the "
                  "header."),  # the _(...) is the ugettext function imported as _
    editable=True,
    default="https://vimeo.com/test",
)

register_setting(
    name="SOCIAL_LINK_DELICIOUS",
    label=_("Delicious link"),
    description=_("If present a delicious icon linking here will be in the "
                  "header."),  # the _(...) is the ugettext function imported as _
    editable=True,
    default="https://delicious.com/test",
)

register_setting(
    name="SOCIAL_LINK_TUMBLR",
    label=_("Tumblr link"),
    description=_("If present a tumblr icon linking here will be in the "
                  "header."),  # the _(...) is the ugettext function imported as _
    editable=True,
    default="https://tumblr.com/test",
)

# register_setting(
#     name="FLICKR_ID",
#     label=_("Flickr ID"),
#     description=_("ID for flickr account bottom right. "),
#     editable=True,
#     default="55925941",
# )

# register_setting(
#     name="GMAP_LOC",
#     label=_("Google map location"),
#     description=_("Address for google maps. "),
#     editable=True,
#     default="Bellecour, Lyon, France",
# )


# Contact and personal details
# NB If multiple settings prepended with the same
# , before the underscore, they will get there own
# section of this name in the admin.

register_setting(
    name="PERSONAL_NAME",
    label=_("Name"),
    description=_("Your name."),
    editable=True,
    default="Joey Bloggs",
)

register_setting(
    name="PERSONAL_EMAIL",
    label=_("E-mail"),
    description=_("Your e-mail address."),
    editable=True,
    default="me@somewhere.com",
)

register_setting(
    name="PERSONAL_PHONE",
    label=_("Telephone"),
    description=_("Your phone number."),
    editable=True,
    default="555-555-665",
)

register_setting(
    name="PERSONAL_ADDRESS",
    label=_("Address"),
    description=_("Your address."),
    editable=True,
    default="742 Evergreen Terrace, Springfield, US",
)

register_setting(
    name="PERSONAL_SKYPE",
    label=_("Skype"),
    description=_("Your Skype handle."),
    editable=True,
    default="joeyblogs84",
)

register_setting(
    name="COMMENTS_ORDER_BY_SCORE",
    label=_("Score order comments"),
    description=_("Ord comments by rating but decay by age"),
    editable=True,
    default=False,
)

# TEMPLATE_ACCESSIBLE_SETTINGS is one of the existing settings
# specifying all setting names available within templates, thus
# we want to append our new settings to it so we can use them in templates
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,                           # Because we append these to
    default=("SOCIAL_LINK_FACEBOOK",       # exiisting templatate accessible settings.
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_VIMEO",
             "SOCIAL_LINK_TUMBLR",
             "SOCIAL_LINK_DELICIOUS",
             # "GMAP_LOC",
             # "FLICKR_ID",
             "PERSONAL_NAME",
             "PERSONAL_EMAIL",
             "PERSONAL_PHONE",
             "PERSONAL_ADDRESS",
             "PERSONAL_SKYPE",
             "COMMENTS_ORDER_BY_SCORE",
             ),
)
