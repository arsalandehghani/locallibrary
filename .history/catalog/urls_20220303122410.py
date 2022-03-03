from unicodedata import name
# from django.contrib import admin
from django.urls import url
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('catalog/', include('catalog.urls')),
    # path('catalog/', include('catalog.urls')),
    url(r'^$', views.index, name='index')
]
