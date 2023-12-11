"""URLs module for the website app."""

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='pages/website/home.html'),
        name='home',
    ),
]
