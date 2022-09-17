from django.db import models


# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=50, verbose_name="Bank_name")
    location = models.TextField(max_length=30, verbose_name="Bank_location")


class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name="Customer_name")
    address = models.TextField(max_length=30, verbose_name="Customer_address")
    phone_No = models.IntegerField( verbose_name="Customer_PhoneNo")
    account_No = models.IntegerField(verbose_name="Customer_AccountNo")
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)


class Teller(models.Model):
    name = models.TextField(max_length=30, verbose_name="Teller_name")


class Account(models.Model):
    ACCOUNT_TYPE = (
        ('S', 'Savings'),
        ('C', 'Current')
    )


class Loan(models.Model):
    loan_type = models.TextField(max_length=30)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
