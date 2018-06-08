from django.conf.urls import url
from . import views


appname = 'blog'
urlpatterns = [
    url(r'^$', views.user_home, name='user_home'),
    url(r'^(?P<author_name>\w+)/(?P<blog_title>.+)/$', views.blog_detail, name='blog_detail'),
    url(r'^(?P<author_name>\w+)/write_blog$', views.write_blog, name='write_blog'),
    url(r'^(?P<author_name>\w+)/all$', views.recent_blog, name='recent_blog'),
]