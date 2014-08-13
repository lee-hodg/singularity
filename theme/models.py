# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
# from mezzanine.forms.models import Form
from mezzanine.utils.models import upload_to


class AboutPage(Page, RichText):
    '''
    An about us type page, which with the
    associated About Profiles gives a space
    to put employer profiles and some text
    about the company, e.g. values or history.
    These can be put in the Page model's content field.
    '''

    history = models.TextField(help_text="Enter your company's history.")
    values = models.TextField(help_text="Enter your company's values.")

    class Meta:
        verbose_name = _('About page')
        verbose_name_plural = _('About pages')


class AboutProfile(Orderable):
    '''
    A profile of personnel on a About page.
    Consisting of image, name of staff, their role and their
    blurb text.
    '''
    aboutpage = models.ForeignKey(AboutPage, related_name='profiles')
    icon = FileField(verbose_name=_('Image'),
                     upload_to=upload_to('theme.AboutProfile.icon',
                                         'icons'),
                     format='Image', max_length=255,
                     blank=True, null=True)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    blurb = models.TextField()


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
                               help_text='The heading under the icon'
                                         'blurbs')
    subheading = models.CharField(max_length=200,
                                  help_text='The subheading just below'
                                            'the heading')
    featured_works_heading = models.CharField(max_length=200,
                                              default='Featured Works')

    parallax_image = FileField(verbose_name=_('Image'),
                               upload_to=upload_to('theme.Parallax.image',
                                                   'parallaxIMG'),
                               format='Image',
                               max_length=255, null=True, blank=True)
    parallax_heading = models.CharField(max_length=200,
                                        help_text='The parallax sec'
                                                  'heading.',
                                        default='Parallax scrolling at'
                                                'its finest.')
    parallax_subheading = models.CharField(max_length=200,
                                           help_text='The parallax sec'
                                                     'subheading',
                                           default='Display your photos'
                                                   'in a new way.')
    featured_portfolio = models.ForeignKey('Portfolio',
                                           blank=True, null=True,
                                           help_text='If selected items'
                                                     'from this portfolio will'
                                                     'be featured '
                                                     'on the home page.')
    content_heading = models.CharField(max_length=200,
                                       default='About us!')
    latest_posts_heading = models.CharField(max_length=200,
                                            default='Latest Posts')

    class Meta:
        verbose_name = _('Home page')
        verbose_name_plural = _('Home pages')


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name='slides')
    image = FileField(verbose_name=_('Image'),
                      upload_to=upload_to('theme.Slide.image', 'slider'),
                      format='Image',
                      max_length=255, null=True, blank=True)

    # Caption
    cap_header = models.CharField(max_length=200)
    cap_sub = models.CharField(max_length=200)
    cap_image1 = FileField(verbose_name=_('cap image 1'),
                           upload_to=upload_to('theme.slide.cap_image1',
                                               'slider'),
                           format='Image',
                           max_length=255,
                           null=True, blank=True)
    cap_image2 = FileField(verbose_name=_('cap image 2'),
                           upload_to=upload_to('theme.slide.cap_image2',
                                               'slider'),
                           format='Image', max_length=255,
                           null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name='blurbs')
    icon = FileField(verbose_name=_('Image'),
                     upload_to=upload_to('theme.IconBlurb.icon', 'icons'),
                     format='Image', max_length=255, blank=True, null=True)
    fa_icon = models.CharField(max_length=50)  # font-awesome classes
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
                            help_text='Optional, if provided clicking the blurb'
                            'will go here.')


class Testimonial(Orderable):
    '''
    An testimonial on a HomePage
    Consisting of image, name of reviewer and their
    testimonial text.
    '''
    homepage = models.ForeignKey(HomePage, related_name='testimonials')
    icon = FileField(verbose_name=_('Image'),
                     upload_to=upload_to('theme.Testimonial.icon', 'icons'),
                     format='Image', max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200)
    content = models.TextField()


COLUMNS_CHOICES = (
    ('2', 'Two columns'),  # two columns use span6
    ('3', 'Three columns'),  # three columns use span4
    ('4', 'Four Columns'),  # four columns use span3
)


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    We nest the PortfolioItems under this page (i.e. in the admin
    add a portfolio page, then 'under it' add portfolio item pages)
    '''
    content = RichTextField(blank=True)
    columns = models.CharField(max_length=1, choices=COLUMNS_CHOICES,
                               default='3')

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')


class PortfolioItem(Page, RichText):
    '''
    An individual portfolio item, should be nested under a Portfolio
    '''
    # This is the featured image, but also we use PortfolioItemImage
    # to add more images that can be scrolled through (c.f. choices
    # associated with a Poll obj in django tut via Foreign key)

    # NB the related names are what you will need when grabbing these
    # objects in either view or template after dotting.
    featured = models.BooleanField()  # to be featured on homepage or not.

    featured_image = FileField(verbose_name=_('Featured Image'),
                               upload_to=upload_to('theme.PortfolioItem.featured_image',
                                                   'portfolio'),
                               format='Image', max_length=255,
                               null=True, blank=True)
    short_description = RichTextField(blank=True)
    categories = models.ManyToManyField('PortfolioItemCategory',
                                        verbose_name=_('Categories'),
                                        blank=True,
                                        related_name='portfolioitems')
    href = models.CharField(max_length=2000, blank=True,
                            help_text='A link to the finished project (optional)')

    class Meta:
        verbose_name = _('Portfolio item')
        verbose_name_plural = _('Portfolio items')


class PortfolioItemImage(Orderable):
    '''
    An image for a PortfolioItem
    '''
    portfolioitem = models.ForeignKey(PortfolioItem, related_name='images')
    file = FileField(_('File'), max_length=200, format='Image',
                     upload_to=upload_to('theme.PortfolioItemImage.file',
                                         'portfolio items'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class PortfolioItemCategory(Slugged):
    '''
    A category for grouping portfolio items into a series.
    '''

    class Meta:
        verbose_name = _('Portfolio Item Category')
        verbose_name_plural = _('Portfolio Item Categories')
        ordering = ('title',)


# # Resume page? Maybe it doesn't change often enough to bother?
# # But could follow the portfolio example above creating a resume model,
# # this would consist of things like PublicationItems, SkillItems and so on...
class ResumePage(Page, RichText):
    '''
    A page representing the format of the resume page
    '''
    heading = models.CharField(max_length=200,
                               help_text='The heading of the resume, e.g. Resume')
    telephone = models.CharField(max_length=200,
                                 help_text='Your telephone no.')
    email = models.CharField(max_length=200,
                             help_text='Your email address.')
    location = models.CharField(max_length=200,
                                help_text='Your location.')
    nationality = models.CharField(max_length=200,
                                   help_text='Your nationality.')
    dob = models.CharField(max_length=200,
                           help_text='Your date of birth on CV.')
    statement = models.TextField(help_text='Personal statement on CV')
    resume_image = FileField(verbose_name=_('Resume Image'),
                             upload_to=upload_to('theme.ResumePage.resume_image',
                                                 'resumepage'),
                             format='Image', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Resume page')
        verbose_name_plural = _('Resume pages')


class PublicationItem(Orderable):
    '''
    An academic publication for resume.
    See inspire bibtex syntax.
    '''
    resumepage = models.ForeignKey(ResumePage, related_name='publications')

    title = models.CharField(max_length=500, help_text='Publication title.')

    # This would have been nice
    # Many2Many field with some kind
    # of inline in the admin, but since
    # pubs is also an inline, authors would
    # need to be a nested inline, which I don't
    # believe is possible?
    authors = models.CharField(max_length=500, help_text='Comma sep authors.')

    journal = models.CharField(max_length=500, blank=True,
                               help_text='Journal name,e.g. Phys. Rev. D.(opt)')
    volume = models.CharField(max_length=20, blank=True, help_text='Journal vol,e.g. D89(opt)')
    pages = models.CharField(max_length=500, blank=True, help_text='Journal page,e.g. 104002(opt)')
    arxivident = models.CharField(max_length=100, blank=True,
                                  help_text='Arxiv ident, e.g. 1401.2667 (opt)')
    primaryClass = models.CharField(max_length=10, help_text='ArXiv class e.g. gr-qc')
    year = models.IntegerField(help_text='Year of publication.')

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
