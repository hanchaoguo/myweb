#coding=utf-8

from django.conf.urls import include, url
#from books import publish, author, book,book2
from licience.views import *

urlpatterns = [
    #url(r'^publishlist/$', publish.PublishListView.as_view(), name='publish_list'),
    #url(r'^publishdetail/(?P<pk>\d+)?/?$', publish.PublishDetailView.as_view(), name='publish_detail'),

    #url(r'^authorlist/$', author.AuthorListView.as_view(), name='author_list'),
    #url(r'^authordetail/(?P<pk>\d+)?/?$', author.AuthorDetailView.as_view(), name='author_detail'),

    url(r'^liciencelist/$', LicienceListView.as_view(), name='licience_list'),
    url(r'^Resourceslist/$', ResourcesListView.as_view(), name='Resources_list'),
    #url(r'^bookdetail/(?P<pk>\d+)?/?$', book.BookDetailView.as_view(), name='book_detail'),
    #url(r'^bookadd/$', book2.BookAddView.as_view(), name='book_add'),
    #url(r'^bookdetail/(?P<pk>\d+)?/?$', book.BookDetailView.as_view(), name='book_detail'),
]
