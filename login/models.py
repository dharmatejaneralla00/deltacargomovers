from django.db import models

# Create your models here.

class clientlist(models.Model):
    clientname = models.CharField(max_length=30)
    fromadd = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    fno = models.IntegerField()
    usercode = models.CharField(max_length=10)

    def __str__(self):
        return self.clientname

class UserLogins(models.Model):
    username = models.CharField(max_length=10)
    usercode = models.CharField(max_length=10)
    area = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Destination(models.Model):
    destination = models.CharField(max_length=30)

    def __str__(self):
        return self.destination