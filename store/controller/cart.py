from django.shortcuts import redirect,render
from django.contrib import messages
from store.models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

@login_required(login_url='login')
def addCart(request):
  if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      prd_qty = data['prod_qty']
      prd_id = data['id']
      prod_status = Product.objects.get(id=prd_id)
      if prod_status:
        if Cart.objects.filter(user=request.user,product_id=prd_id):
          return JsonResponse({'status':'Product Already in cart'})
        else:
          if prod_status.quantity>=prd_qty:
            Cart.objects.create(user=request.user,product_id=prd_id,prod_quantity=prd_qty)
            return JsonResponse({'status':'Product Added'})
          else:
            return JsonResponse({'status':"Stock is lesser than your request .."})
      else:
        return JsonResponse({'status':'Product not Found'},status=200)
    else:
      return JsonResponse({'status':'Login to continue ..'},status=200)
  else:
    messages.error(request,"Access Invalid ..")
    return redirect('home')

@login_required(login_url='login')
def updateCart(request):
  if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      prd_qty = data['prod_qty']
      prd_id = data['id']
      prod_status = Product.objects.get(id=prd_id)
      if prod_status:
        if prod_status.quantity>=prd_qty:
          if Cart.objects.filter(user=request.user,product_id=prd_id):
            cartItem = Cart.objects.get(user=request.user,product_id=prd_id)
            cartItem.prod_quantity = prd_qty
            cartItem.save()
            return JsonResponse({'status':'Cart updated ..'},status=200)
          else:
            return JsonResponse({'status':"Failed .."},status=200)
        else:
          return JsonResponse({'status':"Stock is lesser than your request .."},status=200)
      else:
        return JsonResponse({'status':'Product not Found'},status=200)
    else:
      return JsonResponse({'status':'Login to continue ..'},status=200)
  else:
    messages.error(request,"Access Invalid ..")
    return redirect('home')
    
    
@login_required(login_url='login')
def viewCart(request):
  cart = Cart.objects.filter(user=request.user)
  context = {'cart':cart}
  return render(request,'order-section/cart.html',context)

@login_required(login_url='login')
def deleteCart(request,id):
  if request.user.is_authenticated:
    cartItem = Cart.objects.get(user=request.user,product_id=id)
    if cartItem:
      cartItem.delete()
      return redirect('Cart')
    else:
      messages.success(request,"Failed to remove")
      return redirect('Cart')
  else:
    messages.success(request,"User Access Invalid ")
    return redirect('home')

@login_required(login_url='login') 
def addWishList(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      data=json.load(request)
      id = data['id']
      favItem = Wishlist.objects.filter(product_id=id)
      if favItem:
        return JsonResponse({'status':'Already in Wishlist'},status=200)
      else:
        Wishlist.objects.create(user=request.user,product_id=id)
        return JsonResponse({'status':'Added to Wishlist'},status=200)
    else:
      return JsonResponse({'status':'Login to continue .. '},status=200)
  else:
    return JsonResponse({'status':'User Access Invalid .. '},status=200)

@login_required(login_url='login')
def deleteWish(request,id):
  if request.user.is_authenticated:
    wishItem = Wishlist.objects.get(user=request.user,product_id=id)
    if wishItem:
      wishItem.delete()
      return redirect('wishList')
    else:
      messages.success(request,"Failed to remove")
      return redirect('wishList')
  else:
    messages.success(request,"User Access Invalid .. ")
    return redirect('home')

@login_required(login_url='login')
def viewWish(request):
  wishlist = Wishlist.objects.filter(user=request.user)
  context = {'wishlist':wishlist}
  return render(request,'order-section/wishlist.html',context)