from django.conf import settings

# Max container width. Use 0 for full width.
RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH = \
    getattr(settings, 'RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH', 1060)

RESPONSIVE_ADMIN_FIXED_SUBMIT_LINE = \
    getattr(settings, 'RESPONSIVE_ADMIN_FIXED_SUBMIT_LINE', True)
