from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')])

    def __str__(self):
        return f'{self.book_name} ({self.status})'

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField()


    def __str__(self):
        return f'{self.fee_type} - {self.amount}'
