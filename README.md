# todo-app
Basic todo list in django + js, login, create/delete lists and tasks, check as done

django must be installed, and python on the path.

to test the project: clone it, cd into the first todo directory, and run: python manage.py runserver. In your browser, visit
http://127.0.0.1:8000/ as entry point to the project.

Using the project inside your website: 
I have not spend time yet making this into a proper python module with easy deployment. However, this should work for now:
1) copy todo_list directory completely into your project (top level)
2) add to your entry point urls.py: url(r'^todo_list/', include('todo_list.urls', namespace='todo_list'))
3) link to the app with  href="{% url 'todo_list:index' %}"
