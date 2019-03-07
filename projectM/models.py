from django.db import models
from repoM.models import CodeRepo,DeployHost
from login.models import User

# Create your models here.
class ProjectList(models.Model):
    pro_type = (
        ('Internal','内部项目'),
        ('Outgoing','外部项目'),
    )
    project_name = models.CharField(max_length=128,unique=True)
    project_type = models.CharField(max_length=20,choices=pro_type,default='Internal')
    description = models.TextField()
    code_repo = models.ManyToManyField(CodeRepo, through='ProjectRepo')
    c_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_name
    
    class Meta:
        ordering = ['-c_time']

class ProjectRepo(models.Model):
    ProjectList = models.ForeignKey(ProjectList,on_delete=models.PROTECT)
    CodeRepo = models.ForeignKey(CodeRepo,on_delete=models.PROTECT)
    branch_name = models.CharField(max_length=20,default='branch-dev')
    build_url = models.URLField(null=True)
    deploy_host = models.ForeignKey(DeployHost,on_delete=models.PROTECT)

class ProjectRelease(models.Model):
    ProjectList = models.ForeignKey(ProjectList,on_delete=models.PROTECT)
    c_time = models.DateField(auto_now_add=True)
    release_version = models.CharField(max_length=20)
    release_note = models.TextField()
    author = models.ForeignKey(User,on_delete=models.PROTECT)


class CodeRelease(models.Model):        
    Project_release = models.ForeignKey(ProjectRelease,on_delete=models.PROTECT)
    code_repo = models.ForeignKey(CodeRepo,on_delete=models.PROTECT)
    code_sha = models.CharField(max_length=50)
    release_time = models.DateField(auto_now_add=True)
    env = models.CharField(max_length=20)
    branch = models.CharField(max_length=50)