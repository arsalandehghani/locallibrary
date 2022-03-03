from django.contrib import admin
from django.urls import include, re_path
# from django.shortcuts import redirect
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^catalog/', include('catalog.urls')),
    # re_path(r'^$', redirect('/catalog')),
    re_path(r'^$', RedirectView.as_view(url='/catalog/')),
    # re_path(r'^$', include('catalog.urls')),

]