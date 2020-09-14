import os
import click
from contents import contentView, contentTemplate, contentSerializer, contentModel
dir_path = os.path.dirname(os.path.realpath(__file__))


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
            MakeFile(dirViews, name, ".py", contentView.format(name))
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
            MakeFile(dirTemplates, name, ".html", contentTemplate)
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
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of model", help="name of model to create")
@ click.option("--name_app", prompt="Name of your App of Django", default="myapp")
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
        print(f"Don't Find a App of Django with this name : {name_app}")


@ main.command()
@ click.option("--name", prompt="Name of Module of Endpoint", help="Name of enpoint to create")
def make_endpoint(name):
    print("Working Progress")


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
