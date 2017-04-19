# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from home_application.models import Record


def zsgc(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/zsgc.html')


