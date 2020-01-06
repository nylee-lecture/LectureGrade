from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager)
from django.db import models
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=10, verbose_name="학번")
    sname = models.CharField(max_length=10, verbose_name="이름")
    password = models.CharField(max_length=200, verbose_name="비밀번호")
    date_joined = models.DateField(auto_now_add=True, verbose_name="가입일")
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    email = models.EmailField('이메일주소')


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['sname']

    class Meta:
        verbose_name = _('accounts')
        verbose_name_plural = _('accounts')
        swappable = 'AUTH_USER_MODEL'


# 생략