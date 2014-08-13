# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ResumePage.resume_image'
        db.add_column(u'theme_resumepage', 'resume_image',
                      self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ResumePage.resume_image'
        db.delete_column(u'theme_resumepage', 'resume_image')


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
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'theme.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_heading': ('django.db.models.fields.CharField', [], {'default': "'About us!'", 'max_length': '200'}),
            'featured_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['theme.Portfolio']", 'null': 'True', 'blank': 'True'}),
            'featured_works_heading': ('django.db.models.fields.CharField', [], {'default': "'Featured Works'", 'max_length': '200'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latest_posts_heading': ('django.db.models.fields.CharField', [], {'default': "'Latest Posts'", 'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.iconblurb': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'IconBlurb'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'fa_icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
        u'theme.resumepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'ResumePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'resume_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'theme.slide': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['theme.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['theme']