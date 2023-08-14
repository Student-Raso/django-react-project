from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

routes = [
    '',
    'usuarios',
    'productos',
    'cotizaciones',
    'medias',
    'clientes',
    'empresas'
]


urlpatterns = [
    path('admin/', admin.site.urls),
] + [path(x, TemplateView.as_view(template_name='index.html')) for x in routes]