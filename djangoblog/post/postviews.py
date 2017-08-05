import logging
from django.shortcuts import render

from django.http.response import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index View")
    return HttpResponse("Index View")
