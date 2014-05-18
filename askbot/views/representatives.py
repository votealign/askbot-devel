"""
:synopsis: representative-related views

This module contains views relating to representatives.
"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators import csrf

from askbot import const, models
from askbot.utils import functions

def show_representatives(request):
    """View of a list of representatives."""

    REPRESENTATIVES_PAGE_SIZE = const.USERS_PAGE_SIZE

    representatives = models.Representative.objects.all()

    # TODO: make sorting work

    order_by_parameter = sortby = 'name'

    objects_list = Paginator(
        representatives.order_by(order_by_parameter),
        REPRESENTATIVES_PAGE_SIZE,
    )

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    representatives_page = objects_list.page(page)

    paginator_data = {
        'is_paginated' : True,
        'pages': objects_list.num_pages,
        'current_page_number': page,
        'page_object': representatives_page,
        'base_url' : request.path + '?sort=%s&amp;' % sortby,
    }
    paginator_context = functions.setup_paginator(paginator_data)

    # TODO: which of these variables are necessary?

    data = {
        #'active_tab': 'representatives',
        #'page_class': 'representatives-page',
        'representatives': representatives_page,
        #'group': group,
        #'search_query': search_query,
        #'tab_id': sortby,
        'paginator_context': paginator_context,
        #'group_email_moderation_enabled': group_email_moderation_enabled,
        #'user_acceptance_level': user_acceptance_level,
        #'user_membership_level': user_membership_level,
        #'user_groups': user_groups,
        #'group_openness_choices': group_openness_choices,
    }

    return render(request, 'representatives.html', data)

@login_required
@csrf.csrf_protect
def representative_edit(request, id):
    # TODO: stub
    pass

def representative(request, id, slug=None, tab_name=None):
    # TODO: stub
    pass
