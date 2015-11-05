# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
import pytest

from shoop_tests.front.fixtures import get_jinja_context

from shoop_carousel.models import Carousel
from shoop_carousel.plugins import CarouselPlugin


@pytest.mark.django_db
def test_plugin_form():
    test_carousel = Carousel.objects.create(name="test")
    plugin = CarouselPlugin(config={})
    form_class = plugin.get_editor_form_class()
    form = form_class(data={"carousel": test_carousel.pk}, plugin=plugin)
    assert form.is_valid()
    assert form.get_config() == {"carousel": test_carousel.pk}


@pytest.mark.django_db
def test_plugin_form():
    context = get_jinja_context()
    test_carousel = Carousel.objects.create(name="test")
    plugin = CarouselPlugin(config={"carousel": test_carousel.pk})
    assert plugin.get_context_data(context).get("carousel") == test_carousel
