from django.db import models

# Create your models here.
# Press Confrence table
class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

# Guest Table
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now = True)

    class Meat:
        unique_together = ('event','phone')

    def _str_(self):
        return self.realname