"""App Config for website app."""

from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    """
    App Config for website.

    This class is used internally by Django to manage the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.website'
