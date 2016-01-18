# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
try:
    from shoop.xtheme import TemplatedPlugin
except ImportError:  # before Shoop 3.0
    from shoop.xtheme.plugins import TemplatedPlugin
from shoop.xtheme.resources import add_resource

from shoop_carousel.models import Carousel
from shoop.xtheme.plugins.forms import GenericPluginForm


class CarouselConfigForm(GenericPluginForm):
    def __init__(self, **kwargs):
        super(CarouselConfigForm, self).__init__(**kwargs)

    def populate(self):
        self.fields["carousel"] = forms.ModelChoiceField(
            label=_("Carousel"),
            queryset=Carousel.objects.all(),
            required=False,
            initial=self.plugin.config.get("carousel") if self.plugin else None
        )

    def clean(self):
        cleaned_data = super(CarouselConfigForm, self).clean()
        carousel = cleaned_data.get("carousel")
        cleaned_data["carousel"] = carousel.pk if hasattr(carousel, "pk") else None
        return cleaned_data


class CarouselPlugin(TemplatedPlugin):
    identifier = "shoop_carousel.product_highlight"
    name = _("Carousel plugin")
    template_name = "shoop_carousel/carousel.jinja"
    fields = ["carousel"]
    editor_form_class = CarouselConfigForm

    def render(self, context):
        """
        Custom render for to add css resource for carousel

        :param context: current context
        :return: html content for the plugin
        """
        add_resource(context, "head_end", "%sshoop_carousel/css/style.css" % settings.STATIC_URL)
        return super(CarouselPlugin, self).render(context)

    def get_context_data(self, context):
        """
        Use only slides that has translated image in current language

        :param context: current context
        :return: updated plugin context
        :rtype: dict
        """
        carousel_id = self.config.get("carousel")
        return {
            "request": context["request"],
            "carousel": Carousel.objects.filter(id=carousel_id).first() if carousel_id else None,
        }
