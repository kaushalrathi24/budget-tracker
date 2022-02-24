from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='prof')
    income = models.FloatField(default=0)
    expense = models.FloatField(default=0)

    def __str__(self):
        return self.user.get_username()

    @property
    def balance(self):
        return self.income - self.expense


class Transactions(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    amount = models.FloatField()
    to = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=30, default="general")
    type = models.CharField(max_length=7)  #income or expense

    def __str__(self):
        return self.title



