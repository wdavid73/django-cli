import os
import click
dir_path = os.path.dirname(os.path.realpath(__file__))


@click.group()
def main():
    print(f"Welcome to my Django-Cli")


@main.command()
@click.option("--name", prompt="Name of View", help="name of the view to create")
@click.option("--name_app", prompt="Name of your App of Django", default="myapp")
def make_view(name, name_app):
    if os.path.isdir(name_app):
        path = dir_path + '/' + name_app + "/"
        dirTempalte = path + "views"
        try:
            os.mkdir(dirTempalte)
        except FileExistsError:
            if not os.path.isfile(dirTempalte+"/"+name+".py"):
                try:
                    print("Creating View File...")
                    f = open(dirTempalte+"/"+name+".py", "w+")
                    f.write(
                        'from django.http import HttpResponse\n\n'
                        '#First View\n'
                        'def index(request):\n'
                        '   #Your Code Here..\n'
                        '   return HttpResponse("Hello, world!!. You are at the ' +
                        name+' index.")'
                    )
                    f.close()
                    print(f"View Created.")
                except IOError:
                    print("File not accessible")
                finally:
                    f.close()
            else:
                print(f"A file with that name already exists")

    else:
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of template", help="name of the template to create")
@click.option("--name_app", prompt="Name of your App of Django", default="myapp")
def make_template(name, name_app):
    if os.path.isdir(name_app):
        path = dir_path + '/' + name_app + "/"
        dirTempalte = path + "template"
        try:
            os.mkdir(dirTempalte)
        except FileExistsError:
            if not os.path.isfile(dirTempalte+"/"+name+".html"):
                try:
                    print("Creating View File...")
                    f = open(dirTempalte+"/"+name+".html", "w+")
                    f.write(
                        '{% extends "dir_of_yout_layout" %}\n'
                        '{% load staticfiles %}\n\n'
                        '{% block title %} ' +
                        name.upper()
                        + ' Template {% endblock %}\n'
                        '{% block content %}\n'
                        '<div>\n'
                        'Your content HTML here for you Template '+name+'\n'
                        '</div>\n'
                        '{% endblock %}'
                    )
                    f.close()
                    print(f"View Created.")
                except IOError:
                    print("File not accessible")
                finally:
                    f.close()
            else:
                print(f"A file with that name already exists")

    else:
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of serializer", help="name of serializer to create")
def make_serializer(name):
    print("Creating serializer...")
    print(f"make serializer {name}")


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


if __name__ == '__main__':
    main()
