from django.urls import path
from django.views.generic import TemplateView


app_name = 'overwrite'
urlpatterns = [
    path('namespace/',
         TemplateView.as_view(template_name='myapp/url_with_include.html'),
         name='over_app'),
]
