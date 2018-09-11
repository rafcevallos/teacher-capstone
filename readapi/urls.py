from django.conf.urls import url
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

app_name = "readapi"
urlpatterns = [
    #####################
    # Index/Home/StudentList URLs
    url(r'^$', views.index, name='index'),
    #####################
    # Login/Register URLs
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    #####################
    # Student URLS
    url(r'^add_student$', views.add_student, name='add_student'),
    url(r'^student/(?P<pk>\d+)$', views.student_detail, name='student_detail'),
    #####################
    # Book URLS
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^books$', views.list_book, name='list_book'),
    url(r'^book/(?P<pk>\d+)$', views.book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
