#!/home/guicho73/venv/bin/python3.8
"""usage: main.py [-h]
optional arguments:
    -h, --help  show this help message and exit

commands:
    make-view
    make-model
    make-serializer
    make-template
    make_endpoint
"""

import os
import click
import enquiries
from pyfiglet import Figlet
from typing import List

dir_path = os.path.dirname(os.path.realpath(__file__))

contentView = '''from django.http import HttpResponse\n
#First View
def index(request):
    #Your Code Here..
    return HttpResponse("Hello, world!!. You are at the {} index.")
'''

contentClassAPiViewADI = '''from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.{} import {}
from ..Infractructure.{} import {}

class GetAndPost(APIView):

    def get(self, request: Request):
        {} = {}.objects.filter(state=1)
        serializer = {}(
            {}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = {}(
            data=request.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

contentClassAPiModelADI = '''from django.db import models
from django.urls import reverse


class {}(models.Model):
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} model"

    class Meta:
        db_table = "{}"
'''

contentClassAPISerializerADI = '''from rest_framework import serializers
from ..Domain.{} import {}

class {}(serializers.ModelSerializer):

    class Meta:
        model = {}
        fields = '__all__'
        
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


@click.group()
def main():
    f = Figlet(font='slant')
    print(f.renderText('Django-CLI'))


@main.command()
@click.option("--name", prompt="✨ Name of View", help="name of the view to create")
@click.option("--name_app", prompt="✨ Name of your App of Django", default="myapp")
def make_view(name, name_app):
    if os.path.isdir(name_app):
        dirViews = dir_path + '/' + name_app + "/" + "views"
        try:
            os.mkdir(dirViews)
            MakeFile(dirViews, name, ".py", contentView.format(name))
        except FileExistsError:
            MakeFile(dirViews, name, ".py", contentView.format(name))
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name", prompt="✨ Name of template", help="name of the template to create")
@click.option("--name_app", prompt="✨ Name of your App of Django", default="myapp")
def make_template(name, name_app):
    if os.path.isdir(name_app):
        dirTemplates = dir_path + '/' + name_app + "/" + "template"
        try:
            os.mkdir(dirTemplates)
            MakeFile(dirTemplates, name, ".html", contentTemplate)
        except FileExistsError:
            MakeFile(dirTemplates, name, ".html", contentTemplate)
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name", prompt="✨ Name of serializer", help="name of serializer to create")
@ click.option("--name_app", prompt="✨ Name of your App of Django", default="myapp")
@ click.option("--name_model", prompt="✨ Name of Model for the Serializer", default="my_model")
def make_serializer(name, name_app, name_model):

    if os.path.isdir(name_app):
        dirSerializers = dir_path + '/' + name_app + "/" + "serializers"
        try:
            os.mkdir(dirSerializers)
            MakeFile(dirSerializers,
                     name,
                     ".py",
                     contentSerializer.format(name_app,
                                              name_model.capitalize(),
                                              name.capitalize(),
                                              name_model.capitalize()
                                              )
                     )
        except FileExistsError:
            MakeFile(dirSerializers,
                     name,
                     ".py",
                     contentSerializer.format(name_app,
                                              name_model.capitalize(),
                                              name.capitalize(),
                                              name_model.capitalize()
                                              )
                     )
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name", prompt="✨ Name of model", help="name of model to create")
@ click.option("--name_app", prompt="✨ Name of your App of Django", default="myapp")
def make_model(name, name_app):
    if os.path.isdir(name_app):
        dirModels = dir_path + '/' + name_app + "/" + "models"
        try:
            os.mkdir(dirModels)
            MakeFile(dirModels, name, ".py",
                     contentModel.format(name.capitalize(), name.capitalize()))
        except FileExistsError:
            MakeFile(dirModels, name, ".py",
                     contentModel.format(name.capitalize(), name.capitalize()))
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name", prompt="✨ Name of Module of Endpoint", help="Name of enpoint to create")
@ click.option("--name_app", prompt="✨ Name of your App of Django", default="myapp")
def make_endpoint(name,name_app):
    if os.path.isdir(name_app):
        dirModule = dir_path + '/' + name_app + "/" + name.capitalize()
        structureOne = 'Application/Domain/Infractruture'
        structureTwo = 'View/Model/Serializer'
        options = [structureOne, structureTwo]
        choice = enquiries.choose('Choose a folder structure for the module: ', options)
        try:
            os.mkdir(dirModule)
            MakeStrucutreFolderModule(choice, dirModule, name, structures=[structureOne , structureTwo])
        except FileExistsError:
            MakeStrucutreFolderModule(choice, dirModule, name, structures=[structureOne , structureTwo])
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )
    


def MakeFile(dir, nameFile, ext, content):
    if not os.path.isfile(dir + "/" + nameFile + ext):
        try:
            click.echo("Creating File...")
            f = open(dir + "/" + nameFile + ext, "w+")
            f.write(content)
            f.close()
            click.echo(f"File Created.")
        except IOError:
            click.echo("File not accessible")
        finally:
            f.close()
    else:
        click.echo("A file with that name already exists")

def MakeStrucutreFolderModule(choice : List, dir : str, name : str, structures : List ):
    listFolders = []
    for st in structures:
        if st == choice:
            listFolders = st.split('/')
    name_file_view = name.capitalize() + "GetAndPost"
    name_file_model = "Model" + name.capitalize()
    name_file_serializer = "Serializer" + name.capitalize()
    name_serializer = name.capitalize() + "Serializer"
    for folder in listFolders:
        if folder == "Application": 
            try:
                os.mkdir(dir + "/" + folder)
                MakeFile(dir + "/" + folder, name_file_view , ".py", 
                    contentClassAPiViewADI.format(
                        name_file_model,
                        name.capitalize(), #name of model
                        name_file_serializer,
                        name_serializer,
                        name + "s",
                        name.capitalize(),#name of model
                        name_serializer,
                        name + "s",
                        name_serializer,
                    ) # content
                )
            except FileExistsError:
                MakeFile(dir + "/" + folder, name_file_view, ".py", 
                    contentClassAPiViewADI.format(
                        name_file_model,
                        name.capitalize(), #name of model
                        name_file_serializer,
                        name_serializer,
                        name + "s",
                        name.capitalize(),#name of model
                        name_serializer,
                        name + "s",
                        name_serializer,
                    ) # content
                )
        if folder == "Domain":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFile(dir + "/" + folder, name_file_model, ".py", 
                    contentClassAPiModelADI.format(
                        name.capitalize(),
                        name.capitalize(),
                        name.capitalize(),
                        
                    ) # content
                )
            except FileExistsError:
                MakeFile(dir + "/" + folder, name_file_model, ".py", 
                    contentClassAPiModelADI.format(
                        name_file_model,
                        name.capitalize(), 
                        name_file_serializer,
                    ) # content
                )
        if folder == "Infractruture":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFile(dir + "/" + folder, name_file_serializer, ".py", 
                    contentClassAPISerializerADI.format(
                        name_file_model,
                        name.capitalize(),
                        name_serializer,
                        name.capitalize(),
                        
                    ) # content
                )
            except FileExistsError:
                MakeFile(dir + "/" + folder, name_file_serializer, ".py", 
                    contentClassAPISerializerADI.format(
                        name_file_model,
                        name.capitalize(),
                        name_serializer,
                        name.capitalize(),
                    ) # content
                )
    pass

if __name__ == '__main__':
    main()
