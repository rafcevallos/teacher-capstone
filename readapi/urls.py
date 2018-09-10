from django.conf.urls import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

app_name = "readapi"
urlpatterns = [
    #####################
    # Index/Home URLs
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.list_students, name='list_students'),
    #####################
    # Login/Register URLs
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    #####################
    # Student URLS
    url(r'^students$', views.list_students, name='list_students'),
    url(r'^add_student$', views.add_student, name='add_student'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)