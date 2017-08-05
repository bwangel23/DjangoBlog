# -*- coding: utf-8 -*-

import logging

from ..middleware.middlewareutil import REQUEST_THREAD_LOCAL


class RequestInfoFilter(logging.Filter):
    def filter(self, record):
        record.request_id = REQUEST_THREAD_LOCAL.request_id
        return True
