from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from bookstore import views

urlpatterns = [
	url(r'^books/$', views.book_list),
	url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
