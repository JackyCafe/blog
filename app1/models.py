from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_profile')
    card_id = models.TextField(max_length=10,null=False)
    authority = models.TextField(max_length=1,null=False)
    position = models.TextField(max_length=10,null=False)

    def __str__(self):
        return  self.card_id