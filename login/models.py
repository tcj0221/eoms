from django.db import models

# Create your models here.

class User(models.Model):
    gender = (
        ('dev', '开发'),
        ('admin', '运维'),
    )
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    group = models.CharField(max_length=20, choices=gender, default="开发")
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Host(models.Model):
    gender = (
        ('dwzx', 'dwzx'),
        ('node', 'node')
    )

    ip = models.GenericIPAddressField()
    user = models.CharField(max_length=128, choices=gender, default="普通用户")
    password = models.CharField(max_length=256)
    rootpassword = models.CharField(max_length=256)
    tag = models.CharField(max_length=1024)
    item = models.CharField(max_length=1024)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "主机"
        verbose_name_plural = "主机"