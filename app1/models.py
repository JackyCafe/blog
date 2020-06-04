from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30,null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    card_id = models.TextField(max_length=10,null=False)
    authority = models.TextField(max_length=1,null=False)
    position = models.TextField(max_length=10,null=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='userprofile')

    def __str__(self):
        return  self.card_id


#教室名稱
class Classroom(models.Model):
    id = models.AutoField(primary_key = True)
    classname = models.CharField(max_length=20,null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classname


# 活動
class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,null=False,verbose_name='活動名稱')
    group = models.ManyToManyField(Group,related_name='activity')
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,related_name='activity')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    id = models.AutoField(primary_key = True)
    idea_title = models.CharField(max_length=20,null=True,verbose_name='點子標題')
    no = models.CharField(max_length=7,null=False,verbose_name='No')
    sub_title = models.CharField(max_length=20,null= True,verbose_name='標題')
    sketch = models.ImageField(upload_to='cards/image/')
    description= models.TextField(null=True,verbose_name='描述')
    feature = models.TextField(null=True,verbose_name='特點')
    author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='作者簽名')
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE,related_name='card')
    group = models.ManyToManyField(Group,  related_name='card')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.idea_title

    def delete(self, using=None, keep_parents=False):
        self.sketch.delete()
        super().delete()