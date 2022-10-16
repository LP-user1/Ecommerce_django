from django.urls import path
from store.views import *
from store.controller.auth import *
from store.controller.cart import *
from store.controller.checkout import *
from store.controller.order import *
urlpatterns = [
    path('',home,name="home"),
    
    path('collections',collection,name="collections"),
    path('collections/<str:name>',productView,name="collections"),
    path('collections/<str:cname>/<int:pid>',product,name="product"),

    path('signup/user/*s',signupUser,name="signup"),
    path('login/user/*l',loginUser,name="login"),
    path('logout/user/*lo',logoutUser,name="logout"),

    path('addCart',addCart,name="addCart"),
    path('updateCart',updateCart,name="updateCart"),
    path('cart',viewCart,name="Cart"),
    path('deleteCart/<int:id>',deleteCart,name="deleteCart"),

    path('addWishlist',addWishList,name="addWish"),
    path('wishList',viewWish,name="wishList"),
    path('deleteWishList/<int:id>',deleteWish,name="deleteWish"),

    path('checkOut',viewCheckout,name="checkout"),
    path('placeOrder/*',placeOrder,name="placeorder"),

    path('orderHistory/user',orderHistory,name="orderHistory"),
    path('orderHistoryView/user/<str:t_no>',historyView,name="historyView"),
]
