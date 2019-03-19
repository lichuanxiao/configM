from django.db import models
#Create your models here.
class SystemConfig(models.Model):
    SYS_Type = (
        ('git','Git 源码管理系统'),
        ('svn','SVN 源码管理系统'),
        ('jenkins','Jenkins 构建服务'),
        ('nexus','Nexus 依赖管理系统'),
        ('others','其他项目管理系统'),
    )
    sys_name = models.CharField(max_length=20,unique=True)
    sys_url = models.URLField()
    sys_api_url = models.URLField(null=True,blank=True)
    sys_username = models.CharField(max_length=128)
    sys_password = models.CharField(max_length=128)
    sys_privatetoken = models.CharField(max_length=50,null=True,blank=True)
    sys_version = models.CharField(max_length=20)
    sys_description = models.TextField(max_length=200)
    sys_type = models.CharField(max_length=20,choices=SYS_Type)
    sys_lable = models.CharField(max_length=20,null=True,blank=True)
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.sys_url
    
    class Meta:
        ordering = ['-c_time']

class DeployHost(models.Model):
    host = models.GenericIPAddressField()
    host_username = models.CharField(max_length=30)
    host_password = models.CharField(max_length=30)
    host_port = models.IntegerField(default=22)
    host_description = models.TextField()
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.host
    
    class Meta:
        ordering = ['-c_time']


class CodeRepo(models.Model):
    repo_name = models.CharField(max_length=128)
    repo_group = models.CharField(max_length=123)
    repo_url = models.URLField()
    rpeo_description = models.TextField()

    def __str__(self):
        return self.repo_name
    
    class Meta:
        ordering = ['-repo_group']


