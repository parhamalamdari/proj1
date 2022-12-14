from django.db import models

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(Base):
    name =models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()



    def __str__(self):
        return f'{self.name} {self.lastname} {self.age}'



class Customer(Base):
    customer = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20)











