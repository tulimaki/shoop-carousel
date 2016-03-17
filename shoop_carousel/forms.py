# -*- coding: utf-8 -*-
# This file is part of Shoop Carousel.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.utils.translation import ugettext_lazy as _

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


class BannerBoxConfigForm(GenericPluginForm):
    def __init__(self, **kwargs):
        super(BannerBoxConfigForm, self).__init__(**kwargs)

    def populate(self):
        super(BannerBoxConfigForm, self).populate()
        self.fields["carousel"] = forms.ModelChoiceField(
            label=_("Carousel"),
            queryset=Carousel.objects.all(),
            required=False,
            initial=self.plugin.config.get("carousel") if self.plugin else None
        )

    def clean(self):
        cleaned_data = super(BannerBoxConfigForm, self).clean()
        carousel = cleaned_data.get("carousel")
        cleaned_data["carousel"] = carousel.pk if hasattr(carousel, "pk") else None
        return cleaned_data
