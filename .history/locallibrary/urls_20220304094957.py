from django.contrib import admin
from django.urls import include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(url='/catalog/')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^catalog/', include('catalog.urls')),

]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')), # new
]