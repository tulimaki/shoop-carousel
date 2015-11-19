# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from shoop.admin.base import AdminModule, MenuEntry
from shoop.admin.utils.urls import derive_model_url, admin_url, get_edit_and_list_urls

from shoop_carousel.models import Carousel


class CarouselModule(AdminModule):
    name = _("Carousels")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="shoop_admin:carousel.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^carousels",
            view_template="shoop_carousel.admin.views.Carousel%sView",
            name_template="carousel.%s"
        ) + [
            admin_url(
                "^carousel/(?P<pk>\d+)/delete/$",
                "shoop_carousel.admin.views.CarouselDeleteView",
                name="carousel.delete"
            ),
        ]

    def get_menu_category_icons(self):
        return {self.name: "fa fa-image"}

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-image",
                url="shoop_admin:carousel.list",
                category=self.name
            )
        ]

    def get_model_url(self, object, kind):
        return derive_model_url(Carousel, "shoop_admin:carousel", object, kind)
