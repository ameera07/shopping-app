from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    live=0
    delete=1
    delete_choices=((live,'live'),(delete,'delete'))
    delete_status=models.IntegerField(choices=delete_choices,default=live)
    priority=models.IntegerField(default=0)
    user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    Tittle=models.CharField(max_length=100)
    Price=models.IntegerField()
    Description=models.TextField()
    image=models.ImageField(upload_to="media/")
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.Tittle