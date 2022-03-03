from unicodedata import name
# from django.contrib import admin
from django.urls import re_path
from . import views

app_name= 'catalog'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('catalog/', include('catalog.urls')),
    # path('catalog/', include('catalog.urls')),
    re_path(r'^$', views.index, name='index'),
    # url(r'^$', views.index, name='index')
]
