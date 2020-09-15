
contentView = '''from django.http import HttpResponse\n
#First View
def index(request):
    #Your Code Here..
    return HttpResponse("Hello, world!!. You are at the {} index.")
'''

contentTemplate = '''{% extends "dir_of_yout_layout" %}
{% load staticfiles %}\n
{% block title %}
Title of you Template 
{% endblock %}
{% block content %}
<div>
    Your content HTML here for you Template
</div>
{% endblock %}
'''

contentSerializer = '''from rest_framework import serializers
from {}.models import {}\n
class {}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {}
        fields = ['id', '....']
'''

contentModel = '''from django.db import models
from django.urls import reverse\n
class {}(models.Model):
    ref = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    class Meta:
        db_table = "{}"
'''
