from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dob = models.DateField()
    phoneNumber = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
