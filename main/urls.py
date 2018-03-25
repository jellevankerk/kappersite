from django.conf.urls import include, url
from . import views
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^contact/', views.contact, name='contact'),
        url(r'^Openingstijden/', views.open, name='openingstijden'),

]
