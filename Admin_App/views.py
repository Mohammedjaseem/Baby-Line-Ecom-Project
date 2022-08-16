from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if get_user_model().objects.filter(username=request.POST['username']).exists():
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_superuser:
                        login(request, user)
                        return redirect('./')
                    else:
                        return HttpResponse('You are not an admin')
                else:
                    messages.error(request, 'Username or Password is incorrect')
                    form = AuthenticationForm()
                    context = {
                        'form': form
                        }
                    template = ('Admin_panel/sign-in.html') 
                    return render(request, template, context)
            else:
                messages.error(request, 'Password is incorrect')
                form = AuthenticationForm()
                context = {
                    'form': form
                    }
                template = ('Admin_panel/sign-in.html') 
                return render(request, template, context)
        else:
            messages.error(request, 'User does not exist')
            form = AuthenticationForm()
            context = {
                'form': form
                }
            template = ('Admin_panel/sign-in.html') 
            return render(request, template, context)    
    #case if not post
    form = AuthenticationForm()
    context = {
        'form': form
        }
    template = ('Admin_panel/sign-in.html') 
    return render(request, template, context)

#admin panel main
@login_required(login_url='/babyline_admin/admin_login')
def admin_panel(request):
    template = 'Admin_panel/index.html'
    return render(request, template)


#logout admin
def logout_request(request):
    logout(request)
    return redirect('/babyline_admin/admin_login')

#main_category here
@login_required(login_url='/babyline_admin/admin_login')
def main_category(request):

    template = 'Admin_panel/main-category.html'
    return render(request, template)


#sub_category here
@login_required(login_url='/babyline_admin/admin_login')
def sub_category(request):

    template = 'Admin_panel/sub-category.html'
    return render(request, template)

@login_required(login_url='/babyline_admin/admin_login')
def user_grid(request):
    template = 'Admin_panel/user-card.html'
    return render(request, template)




