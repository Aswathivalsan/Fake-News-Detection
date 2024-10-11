from django.db import models

# Create your models here.


class news_table(models.Model):

    newsHeading=models.CharField(max_length=50)
    newsDescription=models.CharField(max_length=50)
    date=models.DateField
    time=models.TimeField
    status=models.CharField(max_length=50)



class login_table(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

