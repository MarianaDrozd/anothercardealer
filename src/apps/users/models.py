from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    DEALER = 'Dealer'
    CUSTOMER = 'Customer'

    ROLE_CHOICES = (
        (DEALER, 'Dealer'),
        (CUSTOMER, 'Customer'),
    )
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
