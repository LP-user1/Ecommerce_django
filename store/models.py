import datetime
import os
from django.db import models
from django.contrib.auth.models import User



# category_path_folder
def CFile_Path(request,filename):
  OrgFilename = filename
  nowTime = datetime.datetime.now().strftime('%Y/%m%d%H:%M:%S')
  newFilename = '%s%s'%(nowTime,OrgFilename)
  return os.path.join('uploads/category',newFilename)
# product_path_folder
def PFile_Path(request,filename):
  OrgFilename = filename
  nowTime = datetime.datetime.now().strftime('%Y/%m%d%H:%M:%S')
  newFilename = '%s%s'%(nowTime,OrgFilename)
  return os.path.join('uploads/product',newFilename)

class Category(models.Model):
  name = models.CharField(max_length=150,blank=False,null=False)
  image = models.ImageField(upload_to=CFile_Path,blank=True,null=True)
  decription = models.TextField(max_length=500)
  status = models.BooleanField(default=False,help_text='0-show,1-hide')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Product(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=150,blank=False,null=False)
  product_image = models.ImageField(upload_to=PFile_Path,blank=True,null=True)
  decription = models.TextField(max_length=500)
  status = models.BooleanField(default=False,help_text='0-show,1-hide')
  trending = models.BooleanField(default=False,help_text='0-Not,1-trend')
  org_price = models.FloatField(blank=False,null=False)
  sell_price = models.FloatField(blank=False,null=False)
  quantity = models.IntegerField(blank=False,null=False)
  small_decs = models.CharField(max_length=150,null=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  prod_quantity = models.IntegerField(null=False,blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  @property
  def total_cost(self):
    return self.prod_quantity*self.product.sell_price

class Wishlist(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  f_name = models.CharField(max_length=150,null=False,blank=False)
  l_name = models.CharField(max_length=150,null=False,blank=False)
  email = models.CharField(max_length=150,null=False,blank=False)
  mobile_no = models.CharField(max_length=150,null=False,blank=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False,blank=False)
  country = models.CharField(max_length=150,null=False,blank=False)
  state = models.CharField(max_length=150,null=False,blank=False)
  pincode = models.CharField(max_length=150,null=False,blank=False)
  payment_method = models.CharField(max_length=150,null=False,blank=False)
  total_price = models.FloatField(null=False)
  payment_id = models.CharField(max_length=350,null=False)
  orderstatus = {
    ('Pending','pending'),
    ('Cancelled','cancelled'),
    ('Shipped','shipped'),
    ('Out for delivery','out for delivery'),
    ('Delivered','delivered')
  }
  status = models.CharField(max_length=150,choices=orderstatus,default='Pending')
  message = models.TextField(null=True)
  tracking_no = models.CharField(max_length=150,null=False,blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) :
    return '{}-{}'.format(self.tracking_no,self.id)

class OrderItem(models.Model):
  order = models.ForeignKey(Order,on_delete=models.CASCADE)
  product = models.ForeignKey(Product,on_delete=models.CASCADE)
  price = models.FloatField(null=False)
  order_quantity = models.IntegerField(null=False,blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return '{}-{}'.format(self.order.tracking_no,self.id)

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  mobile_no = models.CharField(max_length=150,null=False,blank=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False,blank=False)
  country = models.CharField(max_length=150,null=False,blank=False)
  state = models.CharField(max_length=150,null=False,blank=False)
  pincode = models.CharField(max_length=150,null=False,blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) :
    return self.user.username