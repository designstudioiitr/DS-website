from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^content_loader', views.content_updater, name='content_loader'),
    url(r'^submit', views.form_submit, name='submit'),
    url(r'^projects', views.projects, name='projects'),
    url(r'^mobile', views.mobile, name='mobile'),
    url(r'^recruitment', views.recruitment, name='recruitment'),
]
