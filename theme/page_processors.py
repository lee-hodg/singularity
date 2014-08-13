from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
# from django import forms
from .models import HomePage
from .models import Portfolio, PortfolioItem, PortfolioItemCategory
from mezzanine.blog.models import BlogPost
from .forms import ContactForm
from smtplib import SMTPRecipientsRefused
# from django import forms
from django.contrib import messages


@processor_for(Portfolio)
def portfolio_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    # get the Portfolio's items, prefetching categories for performance
    items = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related('categories')
    items = items.filter(parent=page)
    # filter out only cateogries that are user in the Portfolio's items
    categories = PortfolioItemCategory.objects.filter(
        portfolioitems__in=items).distinct()

    return {'items': items, 'categories': categories}


@processor_for(PortfolioItem)
def portfolioitem_processor(request, page):
    '''
    Adds a portfolio's portfolio items to the context
    '''
    portfolioitem = PortfolioItem.objects.published(
        for_user=request.user).prefetch_related(
        'categories', 'images').get(id=page.portfolioitem.id)
    return {'portfolioitem': portfolioitem}


@processor_for(HomePage)
def home_processor(request, page):
    '''
    Grab featured portfolio items from featured portfolio
    '''
    featured_portfolio_id = page.homepage.featured_portfolio_id
    # first() returns first db obj or None
    featured_portfolio = Portfolio.objects.filter(pk=featured_portfolio_id).first()
    items = []
    categories = []
    if featured_portfolio:
        # prob that these are pages not models
        items = featured_portfolio.children.published(  # PortfolioItem.objects.published(
            for_user=request.user) #.prefetch_related('categories')
        # get models themselves
        items = [item.get_content_model() for item in items]
        items = [item for item in items if item.featured]
        # items = items.filter(featured=True)  # only keep featured ones.
        # filter out only cateogries that are user in the Portfolio's items
        categories = PortfolioItemCategory.objects.filter(
            portfolioitems__in=items).distinct()

    blog_posts = BlogPost.objects.all()[:10]  # get ten most recent

    # process contact form
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            name = form.cleaned_data['name']
            recipients = ['lee@localhost']

            from django.core.mail import send_mail
            try:
                send_mail(subject, name+message, sender, recipients)
            except SMTPRecipientsRefused:
                messages.error(request, "That email is invalid.")

            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)  # Redirect after POST

    return {'items': items, 'categories': categories, 'blog_posts': blog_posts,
            'contact_form': form}
