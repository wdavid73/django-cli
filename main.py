import os
import click
dir_path = os.path.dirname(os.path.realpath(__file__))

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


@click.group()
def main():
    print(f"Welcome to my Django-Cli")


@main.command()
@click.option("--name", prompt="Name of View", help="name of the view to create")
@click.option("--name_app", prompt="Name of your App of Django", default="myapp")
def make_view(name, name_app):
    if os.path.isdir(name_app):
        dirViews = dir_path + '/' + name_app + "/" + "views"
        try:
            os.mkdir(dirViews)
        except FileExistsError:
            MakeFile(dirViews, name, ".py", contentView.format(name))
    else:
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of template", help="name of the template to create")
@click.option("--name_app", prompt="Name of your App of Django", default="myapp")
def make_template(name, name_app):
    if os.path.isdir(name_app):
        dirTemplates = dir_path + '/' + name_app + "/" + "template"
        try:
            os.mkdir(dirTemplates)
        except FileExistsError:
            MakeFile(dirTemplates, name, ".html", contentTemplate)
    else:
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of serializer", help="name of serializer to create")
@ click.option("--name_app", prompt="Name of your App of Django", default="myapp")
@ click.option("--name_model", prompt="Name of Model for the Serializer", default="my_model")
def make_serializer(name, name_app, name_model):

    if os.path.isdir(name_app):
        dirSerializers = dir_path + '/' + name_app + "/" + "serializers"
        try:
            os.mkdir(dirSerializers)
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
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of model", help="name of model to create")
def make_model(name):
    print("Creating model...")
    print(f"make model {name}")


@ main.command()
@ click.option("--name", prompt="Name of Module of Endpoint", help="Name of enpoint to create")
def make_endpoint(name):
    print("Creating Endpoint...")
    print("make endpoint {name}")


""" @ click.command()


@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    Simple program that greets NAME for a total of COUNT times.
    for _ in range(count):
        click.echo(f"Hello, {name}!") """


def MakeFile(dir, nameFile, ext, content):
    if not os.path.isfile(dir + "/" + nameFile + ext):
        try:
            print("Creating File...")
            f = open(dir + "/" + nameFile + ext, "w+")
            f.write(content)
            f.close()
            print(f"File Created.")
        except IOError:
            print("File not accessible")
        finally:
            f.close()
    else:
        print(f"A file with that name already exists")


if __name__ == '__main__':
    main()
