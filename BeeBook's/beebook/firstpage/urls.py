from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about')
]

