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

from contents import contentView, contentTemplate, contentSerializer, contentModel
dir_path = os.path.dirname(os.path.realpath(__file__))


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
def make_endpoint(name):
    click.echo("Working Progress")
    # ESTRUCTURA DE CARPETAS
    options = ['Do Something 1', 'Do Something 2', 'Do Something 3']
    choice = enquiries.choose('Choose one of these options: ', options)
    print(choice)


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


if __name__ == '__main__':
    main()
