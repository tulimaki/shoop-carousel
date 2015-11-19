# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
from .delete import CarouselDeleteView
from .edit import CarouselEditView
from .list import CarouselListView

__all__ = [
    "CarouselDeleteView",
    "CarouselEditView",
    "CarouselListView"
]
