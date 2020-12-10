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
from typing import List, final

# dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.abspath(os.curdir)


contentViewDjango = '''from django.http import HttpResponse\n
# First View
 def index(request):
 # Your Code Here..
    return HttpResponse("Hello, world!!. You are at the {} index.")
'''

contentViewDRF = '''from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# please import you model
# please import you serialzer\n

# First View
class GetAndPost(APIView):
    def get(self, request: Request):
        # Your Code Here..
        return Response(data="Hello, world!!. You are at the {} get.",status = status.HTTP_200_OK)

    def post(self, request):
        # Your Code Here..
        return Response(data="Hello, world!!. You are at the {} post.",status = status.HTTP_201_CREATED)
'''

contentViewDRFDecorator = '''from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
# please import you model
# please import you serialzer

# First View
@api_view(["GET"])
def get(request: Request):
    # Your Code Here..
    return Response(data = "Hello, world!!. You are at the {} get.",status = status.HTTP_200_OK)
'''

contentClassAPiView = '''from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..{}.{} import {}
from ..{}.{} import {}

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

contentClassAPiModel = '''from django.db import models
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

contentClassAPISerializer = '''from rest_framework import serializers
from ..{}.{} import {}

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

contentUrls = '''from django.urls import path
from .{}.{}GetAndPost import GetAndPost

urlspatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
]
'''


@click.group()
def main():
    f = Figlet(font='slant')
    print(f.renderText('Django-CLI'))


@main.command()
@click.option("--name",
              prompt="✨ Name of View",
              help="name of the view to create")
@click.option("--name_app",
              prompt="✨ Name of your App of Django",
              default="myapp")
def make_view(name, name_app):
    if os.path.isdir(name_app):
        dirViews = dir_path + '/' + name_app + "/" + "views"
        optionDjango = "Django"
        optionDRF = "Django Rest Framework"
        optionDRFDec = "Django Rest Framework With Decorators"
        options = [optionDjango, optionDRF, optionDRFDec]
        choice = enquiries.choose(
            'Choose a view structure for the file view: ', options
        )
        try:
            os.mkdir(dirViews)

            MakeFileChoice(choice, dirViews, name, ".py", "view")
        except FileExistsError:
            MakeFileChoice(choice, dirViews, name, ".py", "view")
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name",
               prompt="✨ Name of template",
               help="name of the template to create")
@click.option("--name_app",
              prompt="✨ Name of your App of Django",
              default="myapp")
def make_template(name, name_app):
    if os.path.isdir(name_app):
        dirTemplates = dir_path + '/' + name_app + "/" + "template"
        try:
            os.mkdir(dirTemplates)
            MakeFile(dirTemplates, name, ".html", contentTemplate, "template")
        except FileExistsError:
            MakeFile(dirTemplates, name, ".html", contentTemplate, "template")
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name",
               prompt="✨ Name of serializer",
               help="name of serializer to create")
@ click.option("--name_app",
               prompt="✨ Name of your App of Django",
               default="myapp")
@ click.option("--name_model",
               prompt="✨ Name of Model for the Serializer",
               default="my_model")
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
                                              ), "serializer"
                     )
        except FileExistsError:
            MakeFile(dirSerializers,
                     name,
                     ".py",
                     contentSerializer.format(name_app,
                                              name_model.capitalize(),
                                              name.capitalize(),
                                              name_model.capitalize()
                                              ), "serializer"
                     )
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name",
               prompt="✨ Name of model", help="name of model to create")
@ click.option("--name_app",
               prompt="✨ Name of your App of Django", default="myapp")
def make_model(name, name_app):
    if os.path.isdir(name_app):
        dirModels = dir_path + '/' + name_app + "/" + "models"
        try:
            os.mkdir(dirModels)
            MakeFile(dirModels, name, ".py",
                     contentModel.format(name.capitalize(), name.capitalize()), "model")
        except FileExistsError:
            MakeFile(dirModels, name, ".py",
                     contentModel.format(name.capitalize(), name.capitalize()), "model")
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


@ main.command()
@ click.option("--name",
               prompt="✨ Name of Module of Endpoint",
               help="Name of enpoint to create")
@ click.option("--name_app",
               prompt="✨ Name of your App of Django", default="myapp")
def make_endpoint(name, name_app):
    if os.path.isdir(name_app):
        dirModule = dir_path + '/' + name_app + "/" + name.capitalize()
        structureOne = 'Application/Domain/Infractructure'
        structureTwo = 'View/Model/Serializer'
        options = [structureOne, structureTwo]
        choice = enquiries.choose(
            'Choose a folder structure for the module: ', options
        )
        try:
            os.mkdir(dirModule)
            MakeStrucutreFolderModule(choice,
                                      dirModule,
                                      name,
                                      structures=[structureOne, structureTwo])
        except FileExistsError:
            MakeStrucutreFolderModule(choice,
                                      dirModule,
                                      name,
                                      structures=[structureOne, structureTwo])
    else:
        click.echo(
            "Don't Find a App of Django with this name : {}".format(name_app)
        )


def MakeFile(dir: str, nameFile: str, ext: str, content: str, type: str):
    if not os.path.isfile(dir + "/" + nameFile + ext):
        try:
            f = open(dir + "/" + nameFile + ext, "w+")
            f.write(content)
            f.close()
            click.echo("File {} Created.".format(type))
        except IOError:
            click.echo("File not accessible")
    else:
        click.echo("A file with that name already exists")


def MakeFileChoice(choice: list, dir: str, nameFile: str, ext: str, type: str):
    if not os.path.isfile(dir + "/" + nameFile + ext):
        if choice == "Django":
            try_create_file(dir, nameFile, ext, contentViewDjango, type)
        elif choice == "Django Rest Framework":
            try_create_file(dir, nameFile, ext, contentViewDRF, type)
        elif choice == "Django Rest Framework With Decorators":
            try_create_file(dir, nameFile, ext,
                            contentViewDRFDecorator, type)
    else:
        click.echo("A file with that name already exists")


def MakeStrucutreFolderModule(choice: List, dir: str,
                              name: str, structures: List):
    listFolders = []
    for st in structures:
        if st == choice:
            listFolders = st.split('/')
    name_file_view = name.capitalize() + "GetAndPost"
    name_file_model = "Model" + name.capitalize()
    name_file_serializer = "Serializer" + name.capitalize()
    name_serializer = name.capitalize() + "Serializer"
    folder_model = "Model"
    folder_serializer = "Serializer"
    folder_domain = "Domain"
    folder_infractructure = "Infractructure"

    for folder in listFolders:
        if folder == "View":
            make_file_urls(dir, folder, name.capitalize())
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderView(dir, folder_model, folder_serializer,
                                     folder, name_file_view,
                                     name_file_model, name,
                                     name_file_serializer, name_serializer)
            except FileExistsError:
                MakeFileInFolderView(dir, folder_model, folder_serializer,
                                     folder, name_file_view,
                                     name_file_model, name,
                                     name_file_serializer, name_serializer)
        if folder == "Model":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderModel(dir, folder, name_file_model, name)
            except FileExistsError:
                MakeFileInFolderModel(dir, folder, name_file_model, name)
        if folder == "Serializer":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderSerializer(dir, folder_model, folder,
                                           name_file_serializer,
                                           name_file_model, name,
                                           name_serializer)
            except FileExistsError:
                MakeFileInFolderSerializer(dir, folder_model, folder,
                                           name_file_serializer,
                                           name_file_model, name,
                                           name_serializer)
        if folder == "Application":
            make_file_urls(dir, folder, name.capitalize())
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderApplication(dir, folder_domain,
                                            folder_infractructure,
                                            folder, name_file_view,
                                            name_file_model,
                                            name, name_file_serializer,
                                            name_serializer)
            except FileExistsError:
                MakeFileInFolderApplication(dir, folder_domain,
                                            folder_infractructure,
                                            folder, name_file_view,
                                            name_file_model,
                                            name, name_file_serializer,
                                            name_serializer)
        if folder == "Domain":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderDomain(dir, folder, name_file_model, name)
            except FileExistsError:
                MakeFileInFolderDomain(dir, folder, name_file_model, name)
        if folder == "Infractructure":
            try:
                os.mkdir(dir + "/" + folder)
                MakeFileInFolderInfractructure(dir, folder_domain,
                                               folder, name_file_serializer,
                                               name_file_model, name,
                                               name_serializer)
            except FileExistsError:
                MakeFileInFolderInfractructure(dir, folder_domain,
                                               folder, name_file_serializer,
                                               name_file_model, name,
                                               name_serializer)
    click.echo("Please Created inside of module the File for URLS")


def MakeFileInFolderApplication(dir: str, folder_domain: str,
                                folder_infractructure: str,
                                folder: str, name_file_view: str,
                                name_file_model: str, name: str,
                                name_file_serializer: str,
                                name_serializer: str):
    MakeFile(dir + "/" + folder, name_file_view, ".py",
             contentClassAPiView.format(folder_domain,
                                        name_file_model,
                                        name.capitalize(),  # name of model
                                        folder_infractructure,
                                        name_file_serializer,
                                        name_serializer,
                                        name.lower() + "s",
                                        name.capitalize(),  # name of model
                                        name_serializer,
                                        name.lower() + "s",
                                        name_serializer,
                                        ),
             "Endpoint Folder Application"
             )


def MakeFileInFolderDomain(dir: str, folder: str,
                           name_file_model: str, name: str):
    MakeFile(dir + "/" + folder, name_file_model, ".py",
             contentClassAPiModel.format(
                 name.capitalize(),
                 name.capitalize(),
                 name.capitalize(),
             ),
             "Endpoint Folder Domain"
             )


def MakeFileInFolderInfractructure(dir: str, folder_domain: str, folder: str,
                                   name_file_serializer: str,
                                   name_file_model: str, name: str,
                                   name_serializer: str):
    MakeFile(dir + "/" + folder, name_file_serializer, ".py",
             contentClassAPISerializer.format(folder_domain,
                                              name_file_model,
                                              name.capitalize(),
                                              name_serializer,
                                              name.capitalize(),
                                              ),
             "Endpoint Folder Infractructure"
             )


def MakeFileInFolderView(dir: str, folder_model: str, folder_serializer: str,
                         folder: str, name_file_view: str,
                         name_file_model: str, name: str,
                         name_file_serializer: str,
                         name_serializer: str):
    MakeFile(dir + "/" + folder, name_file_view, ".py",
             contentClassAPiView.format(folder_model,
                                        name_file_model,
                                        name.capitalize(),  # name of model
                                        folder_serializer,
                                        name_file_serializer,
                                        name_serializer,
                                        name.lower() + "s",
                                        name.capitalize(),  # name of model
                                        name_serializer,
                                        name.lower() + "s",
                                        name_serializer,
                                        ),
             "Endpoint Folder View"
             )


def MakeFileInFolderModel(dir: str, folder: str,
                          name_file_model: str, name: str):
    MakeFile(dir + "/" + folder, name_file_model, ".py",
             contentClassAPiModel.format(
                 name.capitalize(),
                 name.capitalize(),
                 name.capitalize(),
             ),
             "Endpoint Folder Model"
             )


def MakeFileInFolderSerializer(dir: str, folder_model: str, folder: str,
                               name_file_serializer: str,
                               name_file_model: str, name: str,
                               name_serializer: str):
    MakeFile(dir + "/" + folder, name_file_serializer, ".py",
             contentClassAPISerializer.format(folder_model,
                                              name_file_model,
                                              name.capitalize(),
                                              name_serializer,
                                              name.capitalize(),
                                              ),
             "Endpoint Folder Serializer"
             )


def make_file_urls(dir: str, folder_name_view: str, name: str):
    if not os.path.isfile(dir + "/" + "urls.py"):
        try:
            f = open(dir + "/" + "urls.py", "w+")
            f.write(contentUrls.format(folder_name_view, name))
            f.close()
            click.echo("File urls created")
        except IOError:
            click.echo("File not accessible")
    else:
        click.echo("A file urls already exists")


def try_create_file(dir: str, nameFile: str, ext: str, content: str, type: str):
    try:
        f = open(dir + "/" + nameFile + ext, "w+")
        f.write(content.format(nameFile, nameFile))
        f.close()
        click.echo("File {} Created.".format(type))
    except IOError:
        click.echo("File not accessible")
    finally:
        f.close()


if __name__ == '__main__':
    main()
