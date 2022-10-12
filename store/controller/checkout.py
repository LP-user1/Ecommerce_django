from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from store.models import *
from django.contrib import messages
import random

@login_required(login_url="login")
def viewCheckout(request):
  if request.user.is_authenticated:
    totalcart = Cart.objects.filter(user=request.user)
    for item in totalcart:
      if item.prod_quantity > item.product.quantity:
        Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price=0
    for item in  cartitems:
      total_price = total_price + item.product.sell_price * item.prod_quantity
    userProfile = Profile.objects.filter(user=request.user).first()
    context = {'cartitems':cartitems,'total_price':total_price,'userprofile':userProfile}
    return render(request,'order-section/checkout.html',context)
  else:
    messages.error(request,"INVALID User ..")

@login_required(login_url="login")
def placeOrder(request):
  if request.method == 'POST':
    cuuser = User.objects.filter(id=request.user.id).first()

    if not cuuser.first_name:
      cuuser.first_name = request.POST.get('f_name')
      cuuser.last_name = request.POST.get('l_name')
      cuuser.save()

    if not Profile.objects.filter(user=request.user):
      userProf = Profile()
      userProf.user = request.user
      userProf.address = request.POST.get('address')
      userProf.city = request.POST.get('city')
      userProf.mobile_no = request.POST.get('mobile_no')
      userProf.pincode = request.POST.get('pincode')
      userProf.country = request.POST.get('country')
      userProf.state = request.POST.get('state')
      userProf.email = request.POST.get('email')
      userProf.save()

    newOrder = Order()
    newOrder.user = request.user
    newOrder.f_name = request.POST.get('f_name')
    newOrder.l_name = request.POST.get('l_name')
    newOrder.email = request.POST.get('email')
    newOrder.mobile_no = request.POST.get('mobile_no')
    newOrder.address = request.POST.get('address')
    newOrder.city = request.POST.get('city')
    newOrder.state = request.POST.get('state')
    newOrder.country = request.POST.get('country')
    newOrder.pincode = request.POST.get('pincode')
    newOrder.payment_method = request.POST.get('payment_method')

    cart = Cart.objects.filter(user=request.user)
    cartTotal = 0
    for item in cart:
      cartTotal = cartTotal + item.product.sell_price * item.prod_quantity 

    newOrder.total_price = cartTotal

    trackno = str(random.randint(1111111,9999999))+'shop@'+str(random.randint(1111111,9999999))+'cOm'
    while Order.objects.filter(tracking_no=trackno) is None:
        trackno = str(random.randint(1111111,9999999))+'shop@'+str(random.randint(1111111,9999999))+'cOm'

    newOrder.tracking_no = trackno
    newOrder.save()

    newOrderItems = Cart.objects.filter(user=request.user)
    for item in newOrderItems:
      OrderItem.objects.create(order=newOrder,
      product=item.product,
      order_quantity=item.prod_quantity,
      price=item.product.sell_price)

      orderProd = Product.objects.filter(id=item.product_id).first()
      orderProd.quantity = orderProd.quantity - item.prod_quantity
      orderProd.save()
    Cart.objects.filter(user=request.user).delete()
    messages.success(request,"Order has been Placed")
    return redirect('home')
  else:
    messages.error(request,"INVALID Access ..")
    return redirect('home')