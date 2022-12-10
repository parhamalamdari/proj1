from django.db import models


class User(models.Model):
    name =models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()




class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


class Address(models.Model):
    address = models.ForeignKey(User,on_delete=models.CASCADE)
    street = models.CharField(max_length=50)

class Website(models.Model):
    website = models.ManyToManyField(User)
    web = models.CharField(max_length=50)