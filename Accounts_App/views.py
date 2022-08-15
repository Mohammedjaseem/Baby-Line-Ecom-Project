from django.shortcuts import render
from .forms import NewUserForm, profile_register
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
from django.http import HttpResponseRedirect
from .models import profileregister_model
from .forms import profile_register
# Create your views here.




def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if get_user_model().objects.filter(username=request.POST['username']).exists():
            messages.error(request, 'Username is already in use')
            return redirect('/accounts/register')
        elif get_user_model().objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'Email is already in use')
            return redirect('/accounts/register')
        elif form.is_valid():
            form.save()
            user_name = get_user_model().objects.get(username=request.POST['username'])
            id = user_name.id
            messages.success(request, 'Enter your profile details')
            return redirect('/accounts/profile_register/'+str(id))
        else:
            messages.success(request, 'Enter strong matching password')  
            return redirect('/accounts/register')
    form = NewUserForm()
    context = {
        'form': form
        }
    return render(request, 'Accounts/register/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if get_user_model().objects.filter(username=request.POST['username']).exists():
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                messages.error(request, 'Username or Password is incorrect')
                return redirect('/accounts/login_user')
            else:
                messages.error(request, 'Password is incorrect')
                return redirect('/accounts/login_user')
        else:
            messages.error(request, 'Username is not registered')
            return redirect('/accounts/login_user')
    form = AuthenticationForm()
    context = {
        'form': form
        }
 
    return render(request, 'Accounts/login/login.html', context)
    
def logout_request(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/accounts/login_user')
def profile(request, id):
    if request.user.id == id: 
        if request.method == 'POST':
            form = profile_register(request.POST, request.FILES, instance=profileregister_model.objects.filter(user_id=id).all().first())
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated')
                return redirect('/accounts/profile/'+str(id))
            else:
                messages.success(request, 'form is not valid')  
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        user = User.objects.get(id=id)
        profile = profileregister_model.objects.filter(user_id=id).all().first()
        edit_form = profile_register(instance=profile)
        context = {
            'user': user,
            'profile': profile,
            'edit_form': edit_form 
            }
        return render(request, 'Accounts/profile/profilepage.html', context)
    else:
        return redirect('/accounts/not_authorized')

def not_authorized(request):
    return render(request, 'Accounts/not_authorized/not_authorized.html')

def profile_register_view(request, id):
    if request.method == 'POST':
        form = profile_register(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/accounts/login_user')
        else:
            messages.success(request, 'form is not valid')  
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    form = profile_register
    id = id
    context = {
        'form': form,
        'id' : id,
        }
    return render(request, 'Accounts/register/profile-reg.html', context)


	