# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
import pytest

from django.utils import translation
from filer.models import Image
from shoop.testing.factories import get_default_product, get_default_category
from shoop_tests.simple_cms.utils import create_page

from shoop_carousel.models import Carousel, Slide


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
