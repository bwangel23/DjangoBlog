# -*- coding: utf-8 -*-

import threading


# 线程本地变量，贯穿整个请求，用来保存该上下文中需要追踪的数据
REQUEST_THREAD_LOCAL = threading.local()
