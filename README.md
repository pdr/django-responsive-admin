django-responsive-admin
=======================

A responsive skin for the Django Admin built using the Kube CSS Framework. The objective is to provide a more modern look and feel to the django admin, while keeping the changes at the template level as much as possible.

Installation
------------

To install it, simply:

    pip install django-responsive-admin

Then add 'responsive_admin' to your installed apps before 'django.contrib.admin', like this:

    INSTALLED_APPS = (
        'responsive_admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        # Your installed apps...
    )

You can set the body max-width in your settings file like this:

    # Default is 1060, use 0 for full-width.
    RESPONSIVE_ADMIN_CONTAINER_MAX_WIDTH = 1280


Please feel free to send bug reports or pull-requests. Next release I will be adding a simple way to build a menu.


Screenshots
-----------

![Screenshot 1](http://github.com/pdr/django-responsive-admin/raw/master/img/screenshot1.png)
![Screenshot 2](http://github.com/pdr/django-responsive-admin/raw/master/img/screenshot2.png)
![Screenshot 3](http://github.com/pdr/django-responsive-admin/raw/master/img/screenshot3.png)
![Screenshot 4](http://github.com/pdr/django-responsive-admin/raw/master/img/screenshot4.png)