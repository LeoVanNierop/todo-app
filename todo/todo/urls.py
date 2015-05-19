from django.conf.urls import patterns, include, url
from django.contrib import admin
import todo.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo_list/', include(todo_list.urls)),
)
