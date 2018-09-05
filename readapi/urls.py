from django.conf.urls import url
from django.urls import include, path
from django.views.generic import TemplateView
from . import views

app_name = "readapi"
urlpatterns = [
    #####################
    # Index/Home URLs
    url(r'^$', views.index, name='index'),
    #####################
    # Login/Register URLs
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    #####################
]
