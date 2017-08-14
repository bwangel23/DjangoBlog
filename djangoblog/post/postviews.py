import logging
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

logger = logging.getLogger(__name__)


class IndexView(ListView):
    model = Post
    template_name = 'post/index.html'
    content_object_name = 'post_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []

        left_has_more = False
        right_has_more = False

        first = False
        last = False

        page_number = page.number

        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 3]

            if right[-1] < total_pages - 2:
                right_has_more = True

            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[
                   total_pages-2 if total_pages-2 > 0 else 0:total_pages]

            if left[0] > 3:
                left_has_more = True

            if left[0] > 1:
                first = True
        else:
            left = page_range[
                   page_number - 2 if page_number - 2 > 0 else 0:page_number]
            right = page_range[page_number:page_number+3]

            if right[-1] < total_pages - 2:
                right_has_more = True

            if right[-1] < total_pages:
                last = True

            if left[0] > 3:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'left_has_more': left_has_more,
            'first': first,
            'right': right,
            'right_has_more': right_has_more,
            'last': last,
        }

        return data
