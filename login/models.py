from django.db import models

# Create your models here.

class User(models.Model):

    gender =(
        ('male','男'),
        ('female','女'),
    )
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    fullname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=20,choices=gender, default='男')
    email = models.EmailField(max_length=120,default="chuanxiao.li@jieshunpay.cn")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = '用户'