from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import createPollForm , SignUpForm , LoginForm
from django.contrib.auth import authenticate , login , logout
from .models import Vote

# Create your views here.
def home(request):
    ques = Vote.objects.all()
    return render(request,'vote/home.html',{'ques':ques})

def about(request):
    return render(request,'vote/about.html')

def create(request):
        if request.method == 'POST':
            form = createPollForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = createPollForm()
        return render(request,'vote/create.html',{'form':form})

def createst(request , id ):
    Poll = Vote.objects.get(pk=id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option_one':
            Poll.option_one_count += 1 
        elif selected_option == 'option_two':
            Poll.option_two_count += 1 
        elif selected_option == 'option_three':
            Poll.option_three_count += 1 
        else:
            return HttpResponse(400 , 'Invalid Form') 

        Poll.save()
        return redirect('results',Poll.id)

    else:
     

        Poll = Vote.objects.get(pk=id)
        return render(request,'vote/createst.html',{'Poll':Poll})

def results(request , id ):
    pi = Vote.objects.get(pk=id)
    return render(request,'vote/results.html',{'poll':pi})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

    else:
     form = SignUpForm()
    return render(request,'vote/signup.html',{'form':form})

def user_login(request):
        if request.method == 'POST':
          form = LoginForm(request = request ,data = request.POST)
          if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname , password = upass)
                if user is not None:
                 login(request,user)
                return HttpResponseRedirect ('/')
        else:
            form = LoginForm()
        return render(request,'vote/login.html',{'form':form})


