from django.db import models
from django.contrib.auth.models import User
from .email import send_initial_email
# Create your models here.
class MyUser(User):

    class Meta:
        permissions = (
            ("edit", "Can edit articles"),
            ("publish", "Can publish articles or request to be edited"),
        )