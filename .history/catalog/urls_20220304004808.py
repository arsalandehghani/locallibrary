from unicodedata import name
# from django.contrib import admin
from django.urls import re_path
from . import views

app_name= 'catalog'

urlpatterns = [
    re_path(r'^$', views.Index.as_view(), name='index'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
