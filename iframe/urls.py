from django.conf.urls import url
from . import views

urlpatterns = [
	#ej: /google/
    url(r'^$', views.index, name="index"),
    url(r'([\d]+)/([a-zA-Z0-9]+)/([\d]+)/([\d]+)/([\d]+)/$', views.form, name="tile"),

]
