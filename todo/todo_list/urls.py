from django.conf.urls import patterns, include, url
import todo_list.views
from django.contrib.auth import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'logoutandin', 'todo_list.views.logoutin', name='logoutin'),
    url(r'^index/$', 'todo_list.views.index' , name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', todo_list.views.RegisterUserView.as_view(), name='register'),
    url(r'^addlist/$', 'todo_list.views.addlist', name='addlist'),
)
