# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('history', models.TextField(help_text=b"Enter your company's history.")),
                ('values', models.TextField(help_text=b"Enter your company's values.")),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'About page',
                'verbose_name_plural': 'About pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='AboutProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('blurb', models.TextField()),
                ('aboutpage', models.ForeignKey(related_name='profiles', to='theme.AboutPage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='ExperienceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('institute', models.CharField(help_text=b'Name of institute.', max_length=500)),
                ('position_title', models.CharField(help_text=b'Title you held.', max_length=500)),
                ('startdate', models.DateField(help_text=b'Your start date.', verbose_name=b'Start date')),
                ('enddate', models.DateField(help_text=b'Your end date.', verbose_name=b'End date')),
                ('statements_text', mezzanine.core.fields.RichTextField(help_text=b'Your responsibilities, duties and skills you developed.', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('features_heading', models.CharField(default=b'Features', help_text=b'The features heading.', max_length=200)),
                ('features_text', mezzanine.core.fields.RichTextField(default=b'With Singularity you get a tonne of features out of the box', help_text=b'The features text.', max_length=200)),
                ('parallax_image', mezzanine.core.fields.FileField(help_text=b'The parallax section image.', max_length=255, null=True, verbose_name='Parallax Image', blank=True)),
                ('parallax_heading', models.CharField(default=b'Parallax scrolling at its finest.', help_text=b'The parallax section heading.', max_length=200)),
                ('parallax_subheading', models.CharField(default=b'Display your photos in a new way.', help_text=b'The parallax section subheading', max_length=200)),
                ('portfolio_sec_heading', models.CharField(default=b'Portfolio', max_length=200)),
                ('testimonials_heading', models.CharField(default=b'About us!', max_length=200)),
                ('testimonials_subheading', models.CharField(default=b'What other people say about us...', max_length=200)),
                ('testimonials_image', mezzanine.core.fields.FileField(help_text=b'The parallax testimonals section image.', max_length=255, null=True, verbose_name='Testimonials Image', blank=True)),
                ('contact_recipients', models.CharField(help_text=b'Provide a comma separated list of email addresses to be notified upon form submission. If blank, notifications disabled.', max_length=500)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='IconBlurb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('fa_icon', models.CharField(default=b'none', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.CharField(help_text=b'Optional, if provided clicking the blurb will go here.', max_length=2000, blank=True)),
                ('homepage', models.ForeignKey(related_name='blurbs', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(blank=True)),
                ('columns', models.CharField(default=b'3', max_length=1, choices=[(b'2', b'Two columns'), (b'3', b'Three columns'), (b'4', b'Four Columns')])),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('featured', models.BooleanField(help_text=b'Show image of home page when this portfolio is selected.')),
                ('featured_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Featured Image', blank=True)),
                ('short_description', mezzanine.core.fields.RichTextField(blank=True)),
                ('href', models.CharField(help_text=b'A link to the finished project (optional)', max_length=2000, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Portfolio item',
                'verbose_name_plural': 'Portfolio items',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='PortfolioItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Portfolio Item Category',
                'verbose_name_plural': 'Portfolio Item Categories',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItemImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name='File')),
                ('portfolioitem', models.ForeignKey(related_name='images', to='theme.PortfolioItem')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='PublicationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(help_text=b'Publication title.', max_length=500)),
                ('authors', models.CharField(help_text=b'Comma sep authors.', max_length=500)),
                ('journal', models.CharField(help_text=b'Journal name,e.g. Phys. Rev. D.(opt)', max_length=500, blank=True)),
                ('volume', models.CharField(help_text=b'Journal vol,e.g. D89(opt)', max_length=20, blank=True)),
                ('pages', models.CharField(help_text=b'Journal page,e.g. 104002(opt)', max_length=500, blank=True)),
                ('arxivident', models.CharField(help_text=b'Arxiv ident, e.g. 1401.2667 (opt)', max_length=100, blank=True)),
                ('primaryClass', models.CharField(help_text=b'ArXiv class e.g. gr-qc', max_length=10)),
                ('year', models.IntegerField(help_text=b'Year of publication.')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('institute', models.CharField(help_text=b'Name of institute.', max_length=500)),
                ('qualification_title', models.CharField(help_text=b'Title of qualification.', max_length=500)),
                ('startdate', models.DateField(help_text=b'Your start date.', verbose_name=b'Start date')),
                ('enddate', models.DateField(help_text=b'Your end date.', verbose_name=b'End date')),
                ('statements_text', mezzanine.core.fields.RichTextField(help_text=b' The skills you learnt, grade, thesis title and advisor etc.', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Qualification',
                'verbose_name_plural': 'Qualifications',
            },
        ),
        migrations.CreateModel(
            name='ResumePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('heading', models.CharField(help_text=b'The heading of the resume, e.g. Resume', max_length=200)),
                ('telephone', models.CharField(help_text=b'Your telephone no.', max_length=200)),
                ('email', models.CharField(help_text=b'Your email address.', max_length=200)),
                ('location', models.CharField(help_text=b'Your location.', max_length=200)),
                ('nationality', models.CharField(help_text=b'Your nationality.', max_length=200)),
                ('dob', models.CharField(help_text=b'Your date of birth on CV.', max_length=200)),
                ('statement', models.TextField(help_text=b'Personal statement on CV')),
                ('resume_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Resume Image', blank=True)),
                ('experience_sec_heading', models.CharField(default=b'Experience', help_text=b'The heading of the experience sec.', max_length=200)),
                ('education_sec_heading', models.CharField(default=b'Education', help_text=b'The heading of the education sec.', max_length=200)),
                ('skills_sec_heading', models.CharField(default=b'Skills', help_text=b'The heading of the skills sec.', max_length=200)),
                ('skills_subsec_heading', models.CharField(default=b'Things I can do.', help_text=b'The subheading of the skills sec.', max_length=200)),
                ('publications_sec_heading', models.CharField(default=b'Publications', help_text=b'The heading of the publications sec.', max_length=200)),
                ('publications_subsec_heading', models.CharField(default=b'My work', help_text=b'The subheading of the  publications sec.', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Resume page',
                'verbose_name_plural': 'Resume pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('cap_header', models.CharField(max_length=200)),
                ('cap_sub', models.CharField(max_length=200)),
                ('cap_image1', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='cap image 1', blank=True)),
                ('cap_image2', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='cap image 2', blank=True)),
                ('homepage', models.ForeignKey(related_name='slides', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('homepage', models.ForeignKey(related_name='testimonials', to='theme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.AddField(
            model_name='qualification',
            name='resumepage',
            field=models.ForeignKey(related_name='qualifications', to='theme.ResumePage'),
        ),
        migrations.AddField(
            model_name='publicationitem',
            name='resumepage',
            field=models.ForeignKey(related_name='publications', to='theme.ResumePage'),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='categories',
            field=models.ManyToManyField(related_name='portfolioitems', verbose_name='Categories', to='theme.PortfolioItemCategory', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featured_portfolio',
            field=models.ForeignKey(blank=True, to='theme.Portfolio', help_text=b'If selected, items from this portfolio will be featured  on the home page.', null=True),
        ),
        migrations.AddField(
            model_name='experienceitem',
            name='resumepage',
            field=models.ForeignKey(related_name='experiences', to='theme.ResumePage'),
        ),
    ]
