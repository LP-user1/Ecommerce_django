from django.contrib import messages
from django.shortcuts import render,redirect
from store.models import *


def home(request):
  products = Product.objects.filter(trending=1,status=0).order_by('-sell_price')[:8]
  context = {'products':products}
  return render(request, "home.html",context)


def collection(request):
  category = Category.objects.filter(status=0)
  if category:
    context = {'category':category}
    return render(request,'collections.html',context)
  else:
    return render(request,'collections.html',{})


def productView(request,name):
  if(Category.objects.filter(name=name,status=0)):
    product = Product.objects.filter(category__name=name).order_by('-sell_price')
    context = {'product':product,'category_name':name}
    return render(request,'product.html',context)
  else:
    messages.warning(request,"No products found !!")
    return redirect('collections')

def product(request,cname,pid):
  if(Category.objects.filter(name=cname,status=0)):
    product = Product.objects.get(category__name=cname,id=pid)
    context = {'product':product,'c_name':cname}
    return render(request,'product-details.html',context)
  else:
    messages.warning(request,"No products found")
    return redirect('home')


