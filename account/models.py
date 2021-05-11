from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    email=models.EmailField(unique=True,verbose_name='ایمیل')
    is_author = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
    special_user=models.DateTimeField(default=timezone.now,verbose_name='کاربر ویژه تازمان')
    branch_Id=models.CharField(max_length=20,null=True,verbose_name='کد شعبه')
    branch_name=models.CharField(max_length=100,null=True,verbose_name='نام شعبه')

    def is_special_user(self):
        if self.special_user > timezone.now() :
            return True
        else:
            return False
    is_special_user.boolean=True
    is_special_user.short_description = "وضعیت کاربر ویژه"
