from django.db import models
from django.urls import reverse

class Client(models.Model):
    ref = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = "Client"
