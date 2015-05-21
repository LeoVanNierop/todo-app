from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from forms import UserForm, AddListForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import logout_then_login
from django.views.decorators.http import require_POST
from models import List, Task
from django.http import HttpResponse
import json


@login_required(login_url='/todo_list/login/')
def index(request):
    print 1
    current_user = request.user
    user_lists = current_user.list_set.all()
    addList = AddListForm()
    ctx = {'user': current_user, 'lists': user_lists, 'AddListForm': addList, 'AddListAction': '../addlist/', 'GetListAction': '../getlist/'}
    return render(request, 'todo_list/index.html', ctx)

@require_POST
def addlist(request):
    print request.POST
    form = AddListForm(request.POST)
    if request.user.is_authenticated():
        if form.is_valid():
            newlist = List()
            newlist.user = request.user
            newlist.listname = form.cleaned_data['listname']
            newlist.save()
            return HttpResponse(status=204)
        else:
            return HttpResponse("form validation failed", status=400)
    else:
        return HttpResponse("Url is only available to logged in users", status=401)

@require_POST       
def getlist(request):
    if request.user.is_authenticated():
        listname = request.POST.get("listname", None)
        if listname is not None:
            list = request.user.list_set.filter(listname=listname).get()
            
            if not list:
                return HttpResponse("list name not found", status=400)
            tasks = list.task_set.all()
            data = []
            for task in tasks:
                data.append({"list": task.list, "description": task.task_description, 
                             "deadline": task.deadline, "finished": task.finished})   
            if not data:
                data = [{"results": "Nothing"}]
            return HttpResponse(json.dumps(data) ,content_type="application/json")                 
                     
        else:
            return HttpResponse("list name not specified correctly", status=400)
    else:
        return HttpResponse("Url is only available to logged in users", status=401)
        
def logoutin(request):
    return logout_then_login(request, login_url='/todo_list/login/?next=/todo_list/index/')
    
class RegisterUserView(FormView):
    template_name = 'registration/register_user.html'
    form_class = UserForm
    success_url = '../index'
    
    def form_valid(self, form):
        #create user from succesful data.
        print form.cleaned_data
        user = User.objects.create_user(form.cleaned_data["username"],
                                        form.cleaned_data["email"],
                                        form.cleaned_data["password"]
                                       )
        user.save()
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        #log the user in.
        login(self.request, user)
        return super(RegisterUserView, self).form_valid(form)
    

