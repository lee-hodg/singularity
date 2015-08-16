from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
# from django import forms
from .models import HomePage
from .models import Portfolio, PortfolioItem, PortfolioItemCategory
from mezzanine.blog.models import BlogPost
from .forms import ContactForm
from smtplib import SMTPRecipientsRefused
from django.contrib import messages
from django.contrib.sites.models import Site


@processor_for(Portfolio)
def portfolio_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    # Get the Portfolio's items, prefetching categories for performance.
    items = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related('categories')
    items = items.filter(parent=page)
    # Filter out only categories that are used in the Portfolio's items
    categories = PortfolioItemCategory.objects.filter(
        portfolioitems__in=items).distinct()

    return {'items': items, 'categories': categories}


@processor_for(PortfolioItem)
def portfolioitem_processor(request, page):
    '''
    Adds the PortfolioItem to the context.
    '''
    portfolioitem = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related(
        'categories', 'images').get(id=page.portfolioitem.id)
    return {'portfolioitem': portfolioitem}


@processor_for(HomePage)
def home_processor(request, page):
    '''
    Page processor for the HomePage page.
    '''

    # **********PORTFOLIO*******************
    # Remember we select a portfolio to be featured on the home page
    # but within a portfolio we also select items to be featured too.
    # Featured portfolio id.
    featured_portfolio_id = page.homepage.featured_portfolio_id
    # `first()` returns first db obj or None.
    featured_portfolio = Portfolio.objects.filter(pk=featured_portfolio_id).first()
    items = []
    categories = []
    if featured_portfolio:
        # Grab child pages (PortfolioItem pages) for the Portfolio
        # (N.B. children are page objs not models)
        items = featured_portfolio.children.published(
            for_user=request.user)
        # Get models themselves (could use .portfolioitem too).
        items = [item.get_content_model() for item in items]
        # Keep only featured ones.
        items = [item for item in items if item.featured]
        # Get categories for these featured PortfolioItems in
        # the featured Portfolio.
        categories = PortfolioItemCategory.objects.filter(
            portfolioitems__in=items).distinct()

    # ***************BLOG***********************
    # Up to three most recent posts to be displayed on HomePage.
    blog_posts = BlogPost.objects.order_by('-publish_date')[:3]

    # ***************CONTACT FORM***************
    # Process contact form.
    submitted = 'false'
    form = ContactForm()
    # get current site domain
    current_site = Site.objects.get_current()
    if current_site.domain:
        SITE_DOM = current_site.domain
    else:
        SITE_DOM = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # All validation rules pass
            subject = SITE_DOM + ' :' + form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            name = form.cleaned_data['name']
            recipients = []
            for rec in page.homepage.contact_recipients.split(','):
                recipients.append(rec.strip())
            # Send e-mail.
            if recipients:
                from django.core.mail import send_mail
                try:
                    send_mail(subject, message+'\n\n'+name, sender, recipients)
                except SMTPRecipientsRefused:
                    messages.error(request, "Recipient e-mail is invalid. Please contact admin.")

            # Redirect after POST
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    elif request.method == 'GET':
        # If submitted form, display thanks msg instead of form.
        submitted = request.GET.get('submitted', 'false')

    return {'items': items, 'categories': categories, 'blog_posts': blog_posts,
            'contact_form': form, 'submitted': submitted}
