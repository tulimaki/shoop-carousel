# -*- coding: utf-8 -*-
# This file is part of Shuup Carousel.
#
# Copyright (c) 2012-2015, Shuup Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from shuup.admin.base import AdminModule, MenuEntry
from shuup.admin.utils.urls import derive_model_url, admin_url, get_edit_and_list_urls

from shuup_carousel.models import Carousel


class CarouselModule(AdminModule):
    name = _("Carousels")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="shuup_admin:carousel.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^carousels",
            view_template="shuup_carousel.admin.views.Carousel%sView",
            name_template="carousel.%s"
        ) + [
            admin_url(
                "^carousel/(?P<pk>\d+)/delete/$",
                "shuup_carousel.admin.views.CarouselDeleteView",
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
                url="shuup_admin:carousel.list",
                category=self.name
            )
        ]

    def get_model_url(self, object, kind):
        return derive_model_url(Carousel, "shuup_admin:carousel", object, kind)
