from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class customer(models.Model):
    live=0
    delete=1
    delete_choices=((live,'live'),(delete,'delete'))
    delete_status=models.IntegerField(choices=delete_choices,default=live)
    user=models.OneToOneField(User,related_name='customer_profile',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.name