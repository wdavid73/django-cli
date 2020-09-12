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
        print("Creating View...")
        path = dir_path+'/'+name_app+"/"
        dirName = "views"

        try:
            # Create target Directory
            os.mkdir(path+dirName)
            #print("Directory ", dirName,  " Created ")
            f = open(path+dirName+"/"+name+".py", "w+")
            f.write(
                'from django.shortcuts import render, redirect, get_object_or_404\n\n'
                'from ..models import #your model\n\n'
                '#First View\n'
                'def List'+name+'(request):\n'
                '   #Your Code Here..'
            )
            f.close()
        except FileExistsError:
            #print("Directory ", dirName,  " already exists")
            f = open(path+dirName+"/"+name+".py", "w+")
            f.write(
                'from django.shortcuts import render, redirect, get_object_or_404\n\n'
                'from ..models import #your model\n\n'
                '#First View\n'
                'def List'+name+'(request):\n'
                '   #Your Code Here..'
            )
            f.close()
        print(f"View Created.")
    else:
        print(f"Don't Find a App of Django with this name {name_app}")


@main.command()
@click.option("--name", prompt="Name of template", help="name of the template to create")
def make_template(name):
    print("Creating template...")
    print(f"make template {name}")


@main.command()
@click.option("--name", prompt="Name of serializer", help="name of serializer to create")
def make_serializer(name):
    print("Creating serializer...")
    print(f"make serializer {name}")


@main.command()
@click.option("--name", prompt="Name of model", help="name of model to create")
def make_model(name):
    print("Creating model...")
    print(f"make model {name}")


@main.command()
@click.option("--name", prompt="Name of Module of Endpoint", help="Name of enpoint to create")
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
