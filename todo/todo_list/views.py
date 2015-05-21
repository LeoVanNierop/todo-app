from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from forms import UserForm
from django.views.generic.edit import FormView
from django.contrib.auth.views import logout_then_login

@login_required(login_url='/todo_list/login/')
def index(request):
    current_user = request.user
    
    return render(request, 'todo_list/index.html', {"user": current_user})

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
        
        #log the user in.
        return super(RegisterUserView, self).form_valid(form)
    

