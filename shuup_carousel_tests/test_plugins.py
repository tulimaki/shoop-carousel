# -*- coding: utf-8 -*-
# This file is part of Shuup Carousel.
#
# Copyright (c) 2012-2015, Shuup Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
import pytest

from shuup_carousel.models import Carousel
from shuup_carousel.plugins import BannerBoxPlugin, CarouselPlugin
from shuup_tests.front.fixtures import get_jinja_context


@pytest.mark.django_db
def test_carousel_plugin_form():
    test_carousel = Carousel.objects.create(name="test")
    plugin = CarouselPlugin(config={})
    form_class = plugin.get_editor_form_class()
    form = form_class(data={"carousel": test_carousel.pk}, plugin=plugin)
    assert form.is_valid()
    assert form.get_config() == {"carousel": test_carousel.pk}


@pytest.mark.django_db
def test_carousel_plugin_form_get_context():
    context = get_jinja_context()
    test_carousel = Carousel.objects.create(name="test")
    plugin = CarouselPlugin(config={"carousel": test_carousel.pk})
    assert plugin.get_context_data(context).get("carousel") == test_carousel


@pytest.mark.django_db
def test_banner_box_plugin():
    context = get_jinja_context()
    test_carousel = Carousel.objects.create(name="test")
    plugin = BannerBoxPlugin(config={"carousel": test_carousel.pk, "title": "Test"})
    data = plugin.get_context_data(context)
    assert data.get("carousel") == test_carousel
    assert data.get("title") == "Test"
