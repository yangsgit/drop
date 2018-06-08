from django.conf.urls import url
from . import views


app_name = 'account'
urlpatterns = [
    url('^login/$', views.user_login, name='login'),
    url('^profile/(?P<username>[\w]+)$', views.user_profile, name="profile"),
    url('^logout$', views.user_logout, name='logout'),
    url('^register$', views.user_register, name='register'),

]
