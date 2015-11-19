# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import enumfields.fields
import shoop_carousel.models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('shoop', '0012_add_configurations'),
        ('shoop_simple_cms', '0002_fk_on_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name is only used to configure carousels.', max_length=50, verbose_name='name')),
                ('animation', enumfields.fields.EnumIntegerField(default=0, help_text='Animation type for cycling slides.', enum=shoop_carousel.models.CarouselMode, verbose_name='animation')),
                ('interval', models.IntegerField(default=5, help_text='Slide interval in seconds.', verbose_name='interval')),
                ('pause_on_hover', models.BooleanField(default=True, help_text='Pauses the cycling of the carousel on mouse over.')),
                ('is_arrows_visible', models.BooleanField(default=True, verbose_name='show navigation arrows')),
                ('use_dot_navigation', models.BooleanField(default=True, verbose_name='show navigation dots')),
                ('image_width', models.IntegerField(default=1200, help_text='Slide images will be cropped to this width.', verbose_name='image width')),
                ('image_height', models.IntegerField(default=600, help_text='Slide images will be cropped to this height.', verbose_name='image height')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name is only used to configure slides.', max_length=50, null=True, verbose_name='name', blank=True)),
                ('ordering', models.IntegerField(default=0, null=True, verbose_name='ordering', blank=True)),
                ('carousel', models.ForeignKey(related_name='slides', to='shoop_carousel.Carousel')),
                ('category_link', models.ForeignKey(verbose_name='category link', blank=True, to='shoop.Category', null=True)),
                ('cms_page_link', models.ForeignKey(verbose_name='cms page link', blank=True, to='shoop_simple_cms.Page', null=True)),
                ('product_link', models.ForeignKey(verbose_name='product link', blank=True, to='shoop.Product', null=True)),
            ],
            options={
                'ordering': ['ordering'],
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
        migrations.CreateModel(
            name='SlideTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('caption', models.CharField(max_length=80, null=True, verbose_name='caption', blank=True)),
                ('external_link', models.CharField(max_length=160, null=True, verbose_name='external link', blank=True)),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', blank=True, to='filer.Image', null=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='shoop_carousel.Slide', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'shoop_carousel_slide_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Slide Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='slidetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
