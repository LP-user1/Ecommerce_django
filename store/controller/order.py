from django.shortcuts import render , redirect
from store.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def orderHistory(request):
  history = Order.objects.filter(user=request.user)
  context = {'history':history}
  return render(request,'order-section/order-history.html',context)

@login_required(login_url='login')
def historyView(request,t_no):
  order = Order.objects.filter(tracking_no = t_no).filter(user=request.user).first()
  viewHistory = OrderItem.objects.filter(order = order)
  context = {'viewHistory':viewHistory,'order':order}
  return render(request,'order-section/order_history_view.html',context)