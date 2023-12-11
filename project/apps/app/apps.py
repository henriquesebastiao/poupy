"""App Config for app app."""

from django.apps import AppConfig


class PoupyAppConfig(AppConfig):
    """
    App Config for app.

    This class is used internally by Django to manage the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project.apps.app'
