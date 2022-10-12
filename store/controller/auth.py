from django.contrib.auth import login,logout,authenticate
from store.form import CustomerCreationForm
from django.contrib import messages
from django.shortcuts import redirect,render
from store.models import *



def signupUser(request):
  if request.user.is_authenticated:
    messages.info(request,"Already logged in")
    return redirect('home')
  else:
    form = CustomerCreationForm()
    if request.method == 'POST':
      form = CustomerCreationForm(request.POST)
      if form.is_valid():
        form.save()
        messages.success(request,"Successfully SignedUp | Login to continue ...")
        return redirect('login')
      else:
        messages.warning(request,"SignUp Failed | Enter correct details ..")
        return redirect(request.META.get('HTTP_REFERER'))
    context = {'form':form}
    return render(request,'auth/signup.html',context)
  
def loginUser(request):
  if request.user.is_authenticated:
    messages.info(request,"Hey "+request.user.username+" you are Already logged in")
    return redirect('home')
  else:
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username,password=password)
      if user is not None:
        login(request,user)
        messages.success(request,username+" Successfully Loggedin")
        return redirect('home')
      else:
        messages.error(request,"Invalid credentials ! Try again ..")
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request,'auth/login.html',{})
  
def logoutUser(request):
  if request.user.is_authenticated:
    username = request.user.username
    logout(request)
    messages.success(request,username+" Succesfully Logged Out ")
    return redirect('home')
  else:
    messages.error(request,"Invalid User ! Login first ")
    return redirect('login')