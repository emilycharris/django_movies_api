"""django_movies_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from main.views import MovieListCreateAPIView, RaterListCreateAPIView, RatingListCreateAPIView, RatingRetrieveUpdateDestroyAPIView, RaterRetrieveUpdateDestroyAPIView, MovieRetrieveUpdateDestroyAPIView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MovieListCreateAPIView.as_view(), name='movie_list_create_api_view'),
    url(r'^raters/$', RaterListCreateAPIView.as_view(), name='rater_list_create_api_view'),
    url(r'^ratings/$', RatingListCreateAPIView.as_view(), name='rating_list_create_api_view'),
    url(r'^ratings/(?P<pk>\d+)/$', RatingRetrieveUpdateDestroyAPIView.as_view(), name='rating_retrieve_update_destroy_api_view'),
    url(r'^raters/(?P<pk>\d+)/$', RaterRetrieveUpdateDestroyAPIView.as_view(), name='rater-detail'),
    url(r'^movies/(?P<pk>\d+)/$', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail')
]
