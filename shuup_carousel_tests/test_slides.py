# -*- coding: utf-8 -*-
# This file is part of Shuup Carousel.
#
# Copyright (c) 2012-2015, Shuup Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
from datetime import datetime, timedelta

import pytest
from django.utils import translation
from filer.models import Image

from shuup.testing.factories import get_default_category, get_default_product
from shuup_carousel.models import Carousel, LinkTargetType, Slide
from shuup_tests.simple_cms.utils import create_page


@pytest.mark.django_db
def test_image_translations():
    test_carousel = Carousel.objects.create(name="test")
    test_image_1 = Image.objects.create(original_filename="slide1.jpg")
    test_image_2 = Image.objects.create(original_filename="slide2.jpg")

    with translation.override("en"):
        test_slide = Slide.objects.create(carousel=test_carousel, name="test", image=test_image_1)
        assert len(test_carousel.slides.all()) == 1
        assert test_slide.get_translated_field("image").original_filename == "slide1.jpg"

    test_slide.set_current_language("fi")
    assert test_slide.get_translated_field("image").original_filename == "slide1.jpg"
    test_slide.image = test_image_2
    test_slide.save()
    assert test_slide.get_translated_field("image").original_filename == "slide2.jpg"

    test_slide.set_current_language("en")
    assert test_slide.get_translated_field("image").original_filename == "slide1.jpg"

    test_slide.set_current_language("jp")
    assert test_slide.get_translated_field("image").original_filename == "slide1.jpg"


@pytest.mark.django_db
def test_slide_links():
    test_carousel = Carousel.objects.create(name="test")
    test_image_1 = Image.objects.create(original_filename="slide1.jpg")
    with translation.override("en"):
        test_slide = Slide.objects.create(carousel=test_carousel, name="test", image=test_image_1)

    # Test external link
    assert len(test_carousel.slides.all()) == 1
    test_link = "http://example.com"
    test_slide.external_link = test_link
    test_slide.save()
    assert test_slide.get_translated_field("external_link") == test_link
    assert test_slide.get_link_url() == test_link

    # Test Product url and link priorities
    test_product = get_default_product()
    test_slide.product_link = test_product
    test_slide.save()
    assert test_slide.get_link_url() == test_link
    test_slide.external_link = None
    test_slide.save()
    assert test_slide.get_link_url().startswith("/p/")  # Close enough...

    # Test Category url and link priorities
    test_category = get_default_category()
    test_slide.category_link = test_category
    test_slide.save()
    assert test_slide.get_link_url().startswith("/p/")  # Close enough...
    test_slide.product_link = None
    test_slide.save()
    assert test_slide.get_link_url().startswith("/c/")  # Close enough...

    # Test CMS page url and link priorities
    attrs = {"url": "test"}
    test_page = create_page(**attrs)
    test_slide.cms_page_link = test_page
    test_slide.save()
    assert test_slide.get_link_url().startswith("/c/")  # Close enough...
    test_slide.category_link = None
    test_slide.save()
    assert test_slide.get_link_url().startswith("/test/")

    # Check that external link overrides everything
    test_slide.external_link = test_link
    test_slide.save()
    assert test_slide.get_link_url() == test_link


@pytest.mark.django_db
def test_visible_manager():
    test_dt = datetime(2016, 3, 18, 20, 34, 1, 922791)
    test_carousel = Carousel.objects.create(name="test")
    test_image = Image.objects.create(original_filename="slide.jpg")

    test_slide = Slide.objects.create(carousel=test_carousel, name="test", image=test_image)
    assert not list(test_carousel.slides.visible(dt=test_dt))

    # Available since last week
    test_slide.available_from = test_dt - timedelta(days=7)
    test_slide.save()
    assert len(test_carousel.slides.visible(dt=test_dt)) == 1

    # Available until tomorrow
    test_slide.available_to = test_dt + timedelta(days=1)
    test_slide.save()
    assert len(test_carousel.slides.visible(dt=test_dt)) == 1

    # Expired yesterday
    test_slide.available_to = test_dt - timedelta(days=1)
    test_slide.save()
    assert not list(test_carousel.slides.visible(dt=test_dt))

    # Not available until next week
    test_slide.available_from = test_dt + timedelta(days=7)
    test_slide.available_to = test_dt + timedelta(days=8)
    test_slide.save()
    assert not list(test_carousel.slides.visible(dt=test_dt))


@pytest.mark.django_db
def test_is_visible():
    test_dt = datetime(2016, 3, 18, 20, 34, 1, 922791)
    test_carousel = Carousel.objects.create(name="test")
    test_image = Image.objects.create(original_filename="slide.jpg")
    test_slide = Slide.objects.create(carousel=test_carousel, name="test", image=test_image)
    assert not test_slide.is_visible(dt=test_dt)

    # Available since last week
    test_slide.available_from = test_dt - timedelta(days=7)
    test_slide.save()
    assert test_slide.is_visible(dt=test_dt)

    # Available until tomorrow
    test_slide.available_to = test_dt + timedelta(days=1)
    test_slide.save()
    assert test_slide.is_visible(dt=test_dt)

    # Expired yesterday
    test_slide.available_to = test_dt - timedelta(days=1)
    test_slide.save()
    assert not test_slide.is_visible(dt=test_dt)

    # Not available until next week
    test_slide.available_from = test_dt + timedelta(days=7)
    test_slide.available_to = test_dt + timedelta(days=8)
    test_slide.save()
    assert not test_slide.is_visible(dt=test_dt)


@pytest.mark.django_db
@pytest.mark.parametrize("target_type,expected_target", [
    (LinkTargetType.CURRENT, "_self"),
    (LinkTargetType.NEW, "_blank"),
])
def test_get_link_target(target_type, expected_target):
    test_carousel = Carousel.objects.create(name="test")
    test_image = Image.objects.create(original_filename="slide.jpg")
    test_slide = Slide.objects.create(carousel=test_carousel, name="test", image=test_image, target=target_type)
    assert test_slide.get_link_target() == expected_target
