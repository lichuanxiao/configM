from django.db import models
# Create your models here.
class SystemConfig(models.Model):
    sys_url = models.URLField()
    sys_username = models.CharField(max_length=128)
    sys_password = models.CharField(max_length=128)
    sys_type = models.CharField(max_length=20)
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


