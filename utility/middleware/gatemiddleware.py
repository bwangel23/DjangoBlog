# -*- coding: utf-8 -*-"

import logging
import uuid
import traceback
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from .middlewareutil import REQUEST_THREAD_LOCAL


logger = logging.getLogger(__name__)


class APIGateMiddleware(MiddlewareMixin):
    """GateMiddleware

    网关中间件,所有API访问的进出口.
    该middleware应该放在middlewares的第一位

    该middleware做了以下事情:
    为每个request编号
    拦截所有request, 把request_id和ip,device,data等信息打印到log
    拦截所有response, 把request_id和此次访问所耗时间打印到log
    """

    def process_request(self, request):
        """记录request进入的时间, 为request编号"""
        REQUEST_THREAD_LOCAL.request_id = uuid.uuid4()
        REQUEST_THREAD_LOCAL.incoming_time = datetime.now()
        request.ip = get_client_ip(request)
        logger.info(
            "REQUEST IN[{id}], IP: {ip}".format(
                id=REQUEST_THREAD_LOCAL.request_id, ip=request.ip)
        )


    def process_response(self, request, response):
        """拦截所有request出去, 把request_id和此次访问所耗时间打印到log"""
        duration = int(
            (datetime.now() - REQUEST_THREAD_LOCAL.incoming_time)
            .total_seconds() * 1000
        )
        logger.info("REQUEST OUT[{id}], Duration:{duration}".format(
            id=REQUEST_THREAD_LOCAL.request_id, duration=duration))
        return response


def get_client_ip(request):
    x_forward_for = request.META.get("HTTP_X_FORWARD_FOR")
    if x_forward_for:
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
