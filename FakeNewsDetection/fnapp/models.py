from django.db import models

# Create your models here.

class login_table(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)


class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    Lastname= models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    readnews=models.CharField(max_length=50)

class news_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    newsHeading=models.CharField(max_length=50)
    newsDescription=models.CharField(max_length=50)
    date=models.DateField
    time=models.TimeField
    status=models.CharField(max_length=50)

class chat_table(models.Model):
  from_id=models.ForeignKey(user_table,on_delete=models.CASCADE,related_name="kk")
  To_id=models.ForeignKey(user_table,on_delete=models.CASCADE,related_name="lkk")
  discription=models.CharField(max_length=50)
  date=models.DateField
  time = models.TimeField


class comment_table(models.Model):
    NEWS_id = models.ForeignKey(news_table,on_delete=models.CASCADE)
    USER_id = models.ForeignKey(user_table,on_delete=models.CASCADE)
    Comment= models.CharField(max_length=50)
    date = models.DateField
    time = models.TimeField
    status=models.CharField(max_length=50)


class request_table(models.Model):
    Request_id = models.ForeignKey(news_table, on_delete=models.CASCADE)
    FROM_id = models.ForeignKey(user_table, on_delete=models.CASCADE,related_name="ll")
    TO_id = models.ForeignKey(user_table, on_delete=models.CASCADE,related_name="uu")
    date = models.DateField
    time = models.TimeField
    status = models.CharField(max_length=50)

