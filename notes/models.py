from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Signup(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,null=True)
    branch=models.CharField(max_length=30)
    role=models.CharField(max_length=15)
    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.DateTimeField(auto_now_add=True)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(upload_to='images/', null=True, blank=True)
    filetype = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} {self.status}"