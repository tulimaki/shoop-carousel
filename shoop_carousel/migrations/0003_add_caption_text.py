# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoop_carousel', '0002_protect_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidetranslation',
            name='caption_text',
            field=models.TextField(null=True, verbose_name='caption text', blank=True),
        ),
    ]
