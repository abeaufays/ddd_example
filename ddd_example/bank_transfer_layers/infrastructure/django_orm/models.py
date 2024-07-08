from django.db import models

class AccountModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True) # type: ignore
    balance = models.DecimalField(max_digits=20, decimal_places=2) # type: ignore
