# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import postviews

urlpatterns = [
    url('^$', postviews.index),
]
