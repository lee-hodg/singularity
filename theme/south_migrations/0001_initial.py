# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutPage'
        db.create_table(u'theme_aboutpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('history', self.gf('django.db.models.fields.TextField')()),
            ('values', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'theme', ['AboutPage'])

        # Adding model 'AboutProfile'
        db.create_table(u'theme_aboutprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('aboutpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profiles', to=orm['theme.AboutPage'])),
            ('icon', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('blurb', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'theme', ['AboutProfile'])

        # Adding model 'HomePage'
        db.create_table(u'theme_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('features_heading', self.gf('django.db.models.fields.CharField')(default='Features', max_length=200)),
            ('features_text', self.gf('mezzanine.core.fields.RichTextField')(default='With Singularity you get a tonne of features out of the box', max_length=200)),
            ('parallax_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('parallax_heading', self.gf('django.db.models.fields.CharField')(default='Parallax scrolling at its finest.', max_length=200)),
            ('parallax_subheading', self.gf('django.db.models.fields.CharField')(default='Display your photos in a new way.', max_length=200)),
            ('portfolio_sec_heading', self.gf('django.db.models.fields.CharField')(default='Portfolio', max_length=200)),
            ('featured_portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.Portfolio'], null=True, blank=True)),
            ('testimonials_heading', self.gf('django.db.models.fields.CharField')(default='About us!', max_length=200)),
            ('testimonials_subheading', self.gf('django.db.models.fields.CharField')(default='What other people say about us...', max_length=200)),
            ('testimonials_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('contact_recipients', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'theme', ['HomePage'])

        # Adding model 'Slide'
        db.create_table(u'theme_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['theme.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('cap_header', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cap_sub', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cap_image1', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('cap_image2', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['Slide'])

        # Adding model 'IconBlurb'
        db.create_table(u'theme_iconblurb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='blurbs', to=orm['theme.HomePage'])),
            ('icon', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('fa_icon', self.gf('django.db.models.fields.CharField')(default='none', max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'theme', ['IconBlurb'])

        # Adding model 'Testimonial'
        db.create_table(u'theme_testimonial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='testimonials', to=orm['theme.HomePage'])),
            ('icon', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'theme', ['Testimonial'])

        # Adding model 'Portfolio'
        db.create_table(u'theme_portfolio', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
            ('columns', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal(u'theme', ['Portfolio'])

        # Adding model 'PortfolioItem'
        db.create_table(u'theme_portfolioitem', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('short_description', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItem'])

        # Adding M2M table for field categories on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'theme_portfolioitem_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'theme.portfolioitem'], null=False)),
            ('portfolioitemcategory', models.ForeignKey(orm[u'theme.portfolioitemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfolioitemcategory_id'])

        # Adding model 'PortfolioItemImage'
        db.create_table(u'theme_portfolioitemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('portfolioitem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['theme.PortfolioItem'])),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemImage'])

        # Adding model 'PortfolioItemCategory'
        db.create_table(u'theme_portfolioitemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'theme', ['PortfolioItemCategory'])

        # Adding model 'ResumePage'
        db.create_table(u'theme_resumepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dob', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('statement', self.gf('django.db.models.fields.TextField')()),
            ('resume_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('experience_sec_heading', self.gf('django.db.models.fields.CharField')(default='Experience', max_length=200)),
            ('education_sec_heading', self.gf('django.db.models.fields.CharField')(default='Education', max_length=200)),
            ('skills_sec_heading', self.gf('django.db.models.fields.CharField')(default='Skills', max_length=200)),
            ('skills_subsec_heading', self.gf('django.db.models.fields.CharField')(default='Things I can do.', max_length=200)),
            ('publications_sec_heading', self.gf('django.db.models.fields.CharField')(default='Publications', max_length=200)),
            ('publications_subsec_heading', self.gf('django.db.models.fields.CharField')(default='My work', max_length=200)),
        ))
        db.send_create_signal(u'theme', ['ResumePage'])

        # Adding model 'ExperienceItem'
        db.create_table(u'theme_experienceitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('resumepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='experiences', to=orm['theme.ResumePage'])),
            ('institute', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('position_title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('startdate', self.gf('django.db.models.fields.DateField')()),
            ('enddate', self.gf('django.db.models.fields.DateField')()),
            ('statements_text', self.gf('mezzanine.core.fields.RichTextField')(max_length=200)),
        ))
        db.send_create_signal(u'theme', ['ExperienceItem'])

        # Adding model 'Qualification'
        db.create_table(u'theme_qualification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('resumepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='qualifications', to=orm['theme.ResumePage'])),
            ('institute', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('qualification_title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('startdate', self.gf('django.db.models.fields.DateField')()),
            ('enddate', self.gf('django.db.models.fields.DateField')()),
            ('statements_text', self.gf('mezzanine.core.fields.RichTextField')(max_length=200)),
        ))
        db.send_create_signal(u'theme', ['Qualification'])

        # Adding model 'PublicationItem'
        db.create_table(u'theme_publicationitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('resumepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publications', to=orm['theme.ResumePage'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('arxivident', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('primaryClass', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'theme', ['PublicationItem'])


    def backwards(self, orm):
        # Deleting model 'AboutPage'
        db.delete_table(u'theme_aboutpage')

        # Deleting model 'AboutProfile'
        db.delete_table(u'theme_aboutprofile')

        # Deleting model 'HomePage'
        db.delete_table(u'theme_homepage')

        # Deleting model 'Slide'
        db.delete_table(u'theme_slide')

        # Deleting model 'IconBlurb'
        db.delete_table(u'theme_iconblurb')

        # Deleting model 'Testimonial'
        db.delete_table(u'theme_testimonial')

        # Deleting model 'Portfolio'
        db.delete_table(u'theme_portfolio')

        # Deleting model 'PortfolioItem'
        db.delete_table(u'theme_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'theme_portfolioitem_categories'))

        # Deleting model 'PortfolioItemImage'
        db.delete_table(u'theme_portfolioitemimage')

        # Deleting model 'PortfolioItemCategory'
        db.delete_table(u'theme_portfolioitemcategory')

        # Deleting model 'ResumePage'
        db.delete_table(u'theme_resumepage')

        # Deleting model 'ExperienceItem'
        db.delete_table(u'theme_experienceitem')

        # Deleting model 'Qualification'
        db.delete_table(u'theme_qualification')

        # Deleting model 'PublicationItem'
        db.delete_table(u'theme_publicationitem')


    models = {
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'theme.aboutpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'AboutPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'history': ('django.db.models.fields.TextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'values': ('django.db.models.fields.TextField', [], {})
        },
        u'theme.aboutprofile': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'AboutProfile'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'aboutpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profiles'", 'to': u"orm['theme.AboutPage']"}),
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'icon': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.experienceitem': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ExperienceItem'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'position_title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'resumepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'experiences'", 'to': u"orm['theme.ResumePage']"}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'statements_text': ('mezzanine.core.fields.RichTextField', [], {'max_length': '200'})
        },
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'contact_recipients': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['theme.Portfolio']", 'null': 'True', 'blank': 'True'}),
            'features_heading': ('django.db.models.fields.CharField', [], {'default': "'Features'", 'max_length': '200'}),
            'features_text': ('mezzanine.core.fields.RichTextField', [], {'default': "'With Singularity you get a tonne of features out of the box'", 'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'parallax_heading': ('django.db.models.fields.CharField', [], {'default': "'Parallax scrolling at its finest.'", 'max_length': '200'}),
            'parallax_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parallax_subheading': ('django.db.models.fields.CharField', [], {'default': "'Display your photos in a new way.'", 'max_length': '200'}),
            'portfolio_sec_heading': ('django.db.models.fields.CharField', [], {'default': "'Portfolio'", 'max_length': '200'}),
            'testimonials_heading': ('django.db.models.fields.CharField', [], {'default': "'About us!'", 'max_length': '200'}),
            'testimonials_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'testimonials_subheading': ('django.db.models.fields.CharField', [], {'default': "'What other people say about us...'", 'max_length': '200'})
        },
        u'theme.iconblurb': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'IconBlurb'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'fa_icon': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '50'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'blurbs'", 'to': u"orm['theme.HomePage']"}),
            'icon': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.portfolio': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Portfolio', '_ormbases': [u'pages.Page']},
            'columns': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'theme.portfolioitem': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItem', '_ormbases': [u'pages.Page']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portfolioitems'", 'blank': 'True', 'to': u"orm['theme.PortfolioItemCategory']"}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'short_description': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'})
        },
        u'theme.portfolioitemcategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'PortfolioItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'theme.portfolioitemimage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PortfolioItemImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolioitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['theme.PortfolioItem']"})
        },
        u'theme.publicationitem': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'PublicationItem'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'arxivident': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'primaryClass': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'resumepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publications'", 'to': u"orm['theme.ResumePage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'theme.qualification': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Qualification'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'qualification_title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'resumepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qualifications'", 'to': u"orm['theme.ResumePage']"}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'statements_text': ('mezzanine.core.fields.RichTextField', [], {'max_length': '200'})
        },
        u'theme.resumepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ResumePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'education_sec_heading': ('django.db.models.fields.CharField', [], {'default': "'Education'", 'max_length': '200'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'experience_sec_heading': ('django.db.models.fields.CharField', [], {'default': "'Experience'", 'max_length': '200'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'publications_sec_heading': ('django.db.models.fields.CharField', [], {'default': "'Publications'", 'max_length': '200'}),
            'publications_subsec_heading': ('django.db.models.fields.CharField', [], {'default': "'My work'", 'max_length': '200'}),
            'resume_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'skills_sec_heading': ('django.db.models.fields.CharField', [], {'default': "'Skills'", 'max_length': '200'}),
            'skills_subsec_heading': ('django.db.models.fields.CharField', [], {'default': "'Things I can do.'", 'max_length': '200'}),
            'statement': ('django.db.models.fields.TextField', [], {}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'cap_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cap_image1': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cap_image2': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cap_sub': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'theme.testimonial': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Testimonial'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'testimonials'", 'to': u"orm['theme.HomePage']"}),
            'icon': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['theme']