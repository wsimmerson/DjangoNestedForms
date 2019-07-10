from django.db import models

# Create your models here.


class Parent(models.Model):
    name = models.CharField(max_length=255)


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Address(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
