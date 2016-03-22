# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import enumfields.fields
import shoop_carousel.models


class Migration(migrations.Migration):

    dependencies = [
        ('shoop_carousel', '0003_add_caption_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='available_from',
            field=models.DateTimeField(null=True, verbose_name='available from', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='available_to',
            field=models.DateTimeField(null=True, verbose_name='available to', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='target',
            field=enumfields.fields.EnumIntegerField(default=0, enum=shoop_carousel.models.LinkTargetType, verbose_name='link target'),
        ),
        migrations.AlterField(
            model_name='slidetranslation',
            name='caption_text',
            field=models.TextField(help_text='When displayed in banner box mode, caption text is shown as a tooltip', null=True, verbose_name='caption text', blank=True),
        ),
    ]
