from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Time(models.Model):
    date = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.date



class Records(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    time = models.ForeignKey(Time, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

