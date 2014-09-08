# Register your models here.
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import AboutPage, AboutProfile, HomePage, Slide, IconBlurb, Testimonial
from .models import Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory
from .models import ResumePage, PublicationItem

# ******** HOME PAGE**********************


# TabularDynamicInlineAdmin for the Slide and IconBlurb
# N.B. the `Dynamic` just gives some js to "add another" easily.
class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb


class TestimonialInline(TabularDynamicInlineAdmin):
    model = Testimonial


# HomePage admin custom class.
class HomePageAdmin(PageAdmin):
    inlines = [IconBlurbInline, SlideInline, TestimonialInline]


# Register HomePage with its custom admin model.
admin.site.register(HomePage, HomePageAdmin)
# admin.site.register(HomeFormPage, PageAdmin)

# ******** ABOUT PAGE*******************


class AboutProfileInline(TabularDynamicInlineAdmin):
    model = AboutProfile


# AboutPage admin custom class.
class AboutPageAdmin(PageAdmin):
    inlines = [AboutProfileInline]


# Register AboutPage with its custom admin model
admin.site.register(AboutPage, AboutPageAdmin)

# *************PORTFOLIO****************

# Register Portfolio with default PageAdmin
admin.site.register(Portfolio, PageAdmin)

# ************PORTFOLIO ITEM************


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage


class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)

admin.site.register(PortfolioItem, PortfolioItemAdmin)

# *************PORTFOLIO CATEGORY*******
admin.site.register(PortfolioItemCategory)

# *************RESUME*******************


class PublicationItemInline(StackedDynamicInlineAdmin):
    model = PublicationItem


# ResumePage admin custom class.
class ResumePageAdmin(PageAdmin):
    inlines = [PublicationItemInline]

# Register ResumePage with its custom admin model.
admin.site.register(ResumePage, ResumePageAdmin)
