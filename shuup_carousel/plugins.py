# -*- coding: utf-8 -*-
# This file is part of Shuup Carousel.
#
# Copyright (c) 2012-2015, Shuup Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from shuup.xtheme.plugins.forms import TranslatableField
from shuup.xtheme.resources import add_resource
from shuup_carousel.models import Carousel

from .forms import BannerBoxConfigForm, CarouselConfigForm

try:
    from shuup.xtheme import TemplatedPlugin
except ImportError:  # before Shuup 3.0
    from shuup.xtheme.plugins import TemplatedPlugin




class CarouselPlugin(TemplatedPlugin):
    identifier = "shuup_carousel.product_highlight"
    name = _("Carousel Plugin")
    template_name = "shuup_carousel/carousel.jinja"
    fields = ["carousel"]
    editor_form_class = CarouselConfigForm

    def render(self, context):
        """
        Custom render for to add css resource for carousel

        :param context: current context
        :return: html content for the plugin
        """
        add_resource(context, "head_end", "%sshuup_carousel/css/style.css" % settings.STATIC_URL)
        add_resource(context, "body_end", "%sshuup_carousel/js/vendor/owl.carousel.min.js" % settings.STATIC_URL)
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


class BannerBoxPlugin(CarouselPlugin):
    identifier = "shuup_carousel.banner_box"
    name = _("Banner Box")
    template_name = "shuup_carousel/banner_box.jinja"
    editor_form_class = BannerBoxConfigForm

    fields = [
        ("title", TranslatableField(label=_("Title"), required=False, initial="")),
    ]

    def render(self, context):
        """
        Custom render for to add js resource for banner box

        :param context: current context
        :return: html content for the plugin
        """
        add_resource(context, "body_end", "%sshuup_carousel/js/script.js" % settings.STATIC_URL)
        return super(BannerBoxPlugin, self).render(context)

    def get_context_data(self, context):
        """
        Add title from config to context data

        :param context: Current context
        :return: updated Plugin context
        :rtype: dict
        """
        data = super(BannerBoxPlugin, self).get_context_data(context)
        data["title"] = self.get_translated_value("title")
        return data
