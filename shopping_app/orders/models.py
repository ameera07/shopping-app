from django.db import models
from customers.models import customer
from products.models import products
# Create your models here.

class order(models.Model):
    live=0
    delete=1
    delete_choices=((live,'live'),(delete,'delete'))
    cart_stage=0
    order_confirm=1
    order_processed=2
    order_delivered=3
    order_reject=4
    status_choice=((order_processed,'order_processed'),
                   (order_delivered,'order_delivered'),
                   (order_reject,'order_reject'))
    order_status=models.IntegerField(choices=status_choice,default=cart_stage)
    delete_status=models.IntegerField(choices=delete_choices,default=live)
    owner=models.ForeignKey(customer,related_name='order',on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    

   
    
class orderedtitem(models.Model):
    product=models.ForeignKey(products,related_name="added_cart",on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,related_name="added_item",on_delete=models.CASCADE)