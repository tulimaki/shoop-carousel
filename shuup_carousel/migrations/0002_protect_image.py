# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidetranslation',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='image', blank=True, to='filer.Image', null=True),
        ),
    ]
