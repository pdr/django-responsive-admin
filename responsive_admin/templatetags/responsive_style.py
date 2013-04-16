from django import template
from responsive_admin.conf import settings

register = template.Library()


def max_width():
    if settings.RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH != 0:
        style = '%ipx' % settings.RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH
        return style
    else:
        return 'none'


@register.inclusion_tag('templatetags/fixed_submit_line.html')
def fixed_submit_line():
    return {'FIXED_SUBMIT_LINE': settings.RESPONSIVE_ADMIN_FIXED_SUBMIT_LINE}


register.simple_tag(max_width)

