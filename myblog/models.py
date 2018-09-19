from django.db import models

class article(models.Model):
    title = models.CharField(max_length=32,null=False)
    content = models.CharField(max_length=100,null=True)
    pub_time =  models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class loginuser(models.Model):
    user_name = models.CharField(max_length=32,unique=True)
    user_pwd = models.CharField(max_length=6,null=False)

    def __str__(self):
        return self.user_name


