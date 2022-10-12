from django.shortcuts import render , redirect
from store.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def orderHistory(request):
  history = Order.objects.filter(user=request.user)
  context = {'history':history}
  return render(request,'order-section/order-history.html',context)

