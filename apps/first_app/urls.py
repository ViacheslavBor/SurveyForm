from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^surveys$', views.surveys),
	url(r'^surveys/process$', views.process),
	url(r'^result$', views.result)
]