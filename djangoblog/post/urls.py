# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import postviews

urlpatterns = [
    url('^$', postviews.IndexView.as_view(), name='index'),
]
