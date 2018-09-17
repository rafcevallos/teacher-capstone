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
    url(r'^edit_student/(?P<pk>\d+)$', views.edit_student, name='edit_student'),
    url(r'^student/(?P<pk>\d+)$', views.student_detail, name='student_detail'),
    #####################
    # Book URLS
    url(r'^add_book$', views.add_book, name='add_book'),
    url(r'^edit_book/(?P<pk>\d+)$', views.edit_book, name='edit_book'),
    url(r'^book/(?P<pk>\d+)/delete$', views.delete_book, name='delete_book'),
    url(r'^books$', views.list_book, name='list_book'),
    url(r'^books/(?P<search_terms>\d+)$', views.list_book, name='search_results'),
    url(r'^book/(?P<pk>\d+)$', views.book_detail, name='book_detail'),
    #####################
    # Conference Log URLS
    url(r'^add_conference$', views.add_conference, name='add_conference'),
    url(r'^edit_conference/(?P<pk>\d+)$', views.edit_conference, name='edit_conference'),
    url(r'^conference/(?P<pk>\d+)/delete$', views.delete_conference, name='delete_conference'),
    url(r'^conference/(?P<pk>\d+)$', views.conference_detail, name='conference_detail'),
    #####################
    # Skill URLS
    url(r'^list_skill/(?P<pk>\d+)$', views.list_skill, name='list_skill'),
    #####################
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
