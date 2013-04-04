from django import template
from responsive_admin.conf import settings

register = template.Library()

def max_width():
    if settings.RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH != 0:
        style = '%ipx' % settings.RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH
        return style
    else:
        return 'none'

register.simple_tag(max_width)