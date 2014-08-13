# Register your models here.
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin,StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import AboutPage, AboutProfile, HomePage, Slide, IconBlurb, Testimonial


#TabularDynamicInlineAdmin for the Slide and IconBlurb
#NB the dynamic just gives some js to "add another" easily.
class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb

class TestimonialInline(TabularDynamicInlineAdmin):
    model = Testimonial

class AboutProfileInline(TabularDynamicInlineAdmin):
    model = AboutProfile

# HomePage admin custom class.
class HomePageAdmin(PageAdmin):
    inlines = [IconBlurbInline, SlideInline, TestimonialInline]


# AboutPage admin custom class.
class AboutPageAdmin(PageAdmin):
    inlines = [AboutProfileInline]

#register HomePage with its custom admin model
admin.site.register(HomePage, HomePageAdmin)
#admin.site.register(HomeFormPage, PageAdmin)

#register AboutPage with its custom admin model
admin.site.register(AboutPage, AboutPageAdmin)

from .models import Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory

#register Portfolio with default PageAdmin
admin.site.register(Portfolio,PageAdmin)

class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage

class PortfolioItemAdmin(PageAdmin):
      inlines = (PortfolioItemImageInline,)

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)

#################ResumePage and PublicationItems################
from .models import ResumePage, PublicationItem

#class PublicationAuthorInline(TabularDynamicInlineAdmin):
#    model = Author

class PublicationItemInline(StackedDynamicInlineAdmin): #TabularDynamicInlineAdmin):
    model = PublicationItem
#    inlines = [PublicationAuthorInline]

# ResumePage admin custom class.
class ResumePageAdmin(PageAdmin):
     inlines = [PublicationItemInline]

#register HomePage with its custom admin model
admin.site.register(ResumePage, ResumePageAdmin)
#admin.site.register(PublicationAuthor)



