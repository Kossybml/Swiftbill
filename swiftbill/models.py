from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, default='pending')

    # def __str__(self):
    #     return f'{self.user.username} - Balance: {self.balance}'

class Api_config(models.Model):
    PAYSTACK_SECRET_KEY = models.CharField(max_length = 150, null=True, blank=True)
    PAYSTACK_PUBLIC_KEY = models.CharField(max_length = 150, null=True, blank=True)
    GIFTBILL_API_KEY = models.CharField(max_length = 150, null=True, blank=True)

    class Meta:
        verbose_name = 'Api_config'
        verbose_name_plural = 'Api_configs'

    def __str__(self):
        return "Api_configuration"

class wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# class wallet(AbstractUser):
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   