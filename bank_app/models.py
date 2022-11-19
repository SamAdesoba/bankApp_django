# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(max_length=255, verbose_name='Last Name')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Bank(models.Model):
    code = models.IntegerField(verbose_name='Bank-Code')
    address = models.CharField(max_length=255, verbose_name="Bank Address")
    name = models.CharField(max_length=255, verbose_name='Bank Name')


class Customer(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=255, verbose_name='First Name')
    last_name = models.CharField(blank=False, null=False, max_length=255, verbose_name='Last Name')
    other_name = models.CharField(blank=False, null=False, max_length=255, verbose_name='Other Names')
    email = models.EmailField(blank=False, null=False, max_length=255, verbose_name='Email', unique=True)
    phone = PhoneNumberField(blank=False, null=False)
    password = models.CharField(max_length=255, verbose_name='Password')
    username = models.CharField(max_length=255, verbose_name='Username')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)


class Address(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='House Number')
    street = models.CharField(max_length=255, verbose_name='Street')
    city = models.CharField(max_length=255, verbose_name='City')
    state = models.CharField(max_length=255, verbose_name='State', default='Lagos')
    country = models.CharField(max_length=255, verbose_name='Country', default='Nigeria')
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)


class Account(models.Model):
    ACCOUNT_TYPE = (
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
        ('FIXED', 'Fixed'),
    )
    account_number = models.UUIDField(verbose_name='Account Number', unique=True)
    account_balance = MoneyField(max_digits=40, decimal_places=2, default_currency='₦')
    account_type = models.CharField(max_length=50, choices=ACCOUNT_TYPE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class AtmCard(models.Model):
    holder_name = models.CharField(max_length=255, verbose_name='Card Holder')
    card_no = models.IntegerField(verbose_name='Card Number')
    issued_date = models.DateField(auto_now_add=True, verbose_name='Date Issued')
    expiry_date = models.DateField(auto_now=True, verbose_name='Date Expired')
    cvv_number = models.UUIDField(verbose_name='CVV Number', unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('DEPOSIT', 'Deposit'),
        ('TRANSFER', 'Transfer'),
        ('WITHDRAW', 'Withdraw'),
        ('PAYMENT', 'Payment'),
    )

    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=255, verbose_name='Transaction Type', choices=TRANSACTION_TYPE)
    transaction_amount = MoneyField(max_digits=40, decimal_places=2, default_currency='₦')
    post_balance = MoneyField(max_digits=40, decimal_places=2, default_currency='₦')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


