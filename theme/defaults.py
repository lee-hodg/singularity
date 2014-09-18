from mezzanine.conf import register_setting
from django.utils.translation import gettext as _  # import as '_', used for trans

# Register settings so that they are available in the admin for editing.

# Social settings

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
                  "footer and contact sections."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
                  "footer and contact sections."),
    editable=True,
    default="https://twitter.com/MEZZaTHEME",
)

register_setting(
    name="SOCIAL_LINK_VIMEO",
    label=_("Vimeo link"),
    description=_("If present a vimeo icon linking here will be in the "
                  "footer and contact sections."),  # the _(...) is the ugettext function imported as _
    editable=True,
    default="https://vimeo.com/test",
)

register_setting(
    name="SOCIAL_LINK_DELICIOUS",
    label=_("Delicious link"),
    description=_("If present a delicious icon linking here will be in the "
                  "footer and contact sections."),  # the _(...) is the ugettext function imported as _
    editable=True,
    default="https://delicious.com/test",
)

register_setting(
    name="SOCIAL_LINK_TUMBLR",
    label=_("Tumblr link"),
    description=_("If present a tumblr icon linking here will be in the "
                  "footer and contact sections."),  # the _(...) is the ugettext function imported as _
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

# Personal settings.

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

# Misc settings

COLORS = (('scheme-orange', 'Orange'),
         ('scheme-blue', 'Blue')
         )
register_setting(
    name="COLORSCHEME",
    label=_("Color scheme"),
    description=_("Color scheme of the theme."),
    editable=True,
    choices=COLORS,
    default='scheme-orange',
)

# ( the COMMENTS_ prefix puts this setting
# into existing comments grouping)
register_setting(
    name="COMMENTS_ORDERBYSCORE",
    label=_("Score order comments"),
    description=_("Order comments by rating but decay by age"),
    editable=True,
    choices=((True, 'True'), (False, 'False')),
    default=True,
)

register_setting(
    name="COMMENTS_PER_PAGE",
    label=_("Comments per page"),
    description=_("Number of comments per page"),
    editable=True,
    default=10,
)

register_setting(
    name="COMMENTS_USE_RATINGS",
    label=_("Comments ratable"),
    description=_("Allow rating for comments"),
    editable=True,
    choices=((True, 'True'), (False, 'False')),
    default=True,
)

# Make settings available from within templates by appending
# to existing `TEMPLATE ACCESSIBLE SETTINGS` setting.

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
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
             "COMMENTS_ORDERBYSCORE",
             "COMMENTS_PER_PAGE",
             "COMMENTS_USE_RATINGS",
             "COLORSCHEME",
             ),
)
