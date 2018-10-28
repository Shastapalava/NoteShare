# Learning Django Lynda Notes

## Installation

- Install the latest version of python, if you don't have it already.

- Install Django with `pip3 install Django==2.1.2` since, as of now, 2.1.2 is the latest edition.

- To create a django project, navigate to a folder in terminal and then issue the command`django-admin.py start project <project name>` 

- to build an app, navigate to your project, then type, `python3 manage.py startapp <name of new app>` 

- the difference between an app and a project according to [stack overflow](https://stackoverflow.com/questions/19350785/what-s-the-difference-between-a-project-and-an-app-in-django-world) :

  > *project* refers to the entire application and all its parts.
  >
  > An *app* refers to a submodule of the project. It's  self-sufficient and not intertwined with the other apps in the project  such that, in theory, you could pick it up and plop it down into another  project without any modification.  An *app* typically has its own *models.py*  (which might actually be empty).  You might think of it as a standalone  python module.  A simple project might only have one app.
  >
  > For your example, the *project* is the whole website. You might structure it so there is an *app* for articles, an *app* for ranking tables, and an *app*  for fixtures and results.  If they need to interact with each other,  they do it through well-documented public classes and accessor methods.
  >
  > The main thing to keep in mind is this level of interdependence between the *apps*. In practice it's all one *project*,  so there's no sense in going overboard, but keep in mind how  co-dependent two apps are.  If you find one app is solving two problems,  split them into two apps.  If you find two apps are so intertwined you  could never reuse one without the other, combine them into a single app.

- whenever you create a new Django, go into the `settings.py` file in your project folder and add your new app to the `INSTALLED_APPS` list.

- each of the files in a django app, has a purpose:

  | File or Folder | Purpose                              |
  | -------------- | ------------------------------------ |
  | apps.py        | configuration and initialization     |
  | models.py      | Data Layer                           |
  | admin.py       | administrative interface             |
  | urls.py        | url routing                          |
  | views.py       | control layer                        |
  | tests.py       | test the app                         |
  | migrations/    | directory that holds migration files |

# Django's MVC

Django uses a different Model-View-Controller architecture than most. Here's the terminology in focus:

- url patterns `urls.py` : details where to go when a url request is made
- views `views.py`: these are functions that take url requests and return views.
- templates `templates/` these are what is returned by functions in views.py
- models `models.py` views may draw upon data structures found here to compute what they need to compute.

## Models

- Models are just python classes that inherit from `models.Model` ; each model represent sql tables (models are an orm?). 

```python
from django.db import models
class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()
```

- there are lots of field types that may or may not correspond to data types in various sql databases
- some fields are used to establish foreign key, or primary key relationships
- `max_length=200`  in line 3 is a field attribute. 
- Keep in mind the difference between field attributes `blank=` and `null=` which canbe set to true or false. `blank` means that the cell is empty, `null` means it contains the python null.
- You can also establish choices (like in a drop-down menu) without making a new model (table) of options, but using the  `choices=` field attribute. `sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank = True)` where `SEX_CHOICES` is a list of tuples `[('M','Male')('F','Female')]`
- For foreign keys do this:

```python
vaccinations = models.ManyToManyField('Vaccine',blank=True)
#here vaccinations is a field in the Pets model and the string argument to the 
#ManyToManyField() function, 'Vaccine', is the name of the table to which this
# key serves as foreign key 
```

## Migrations

- whenever you add a model, add or remove a  field ( column) from a model or whenever you edit a field, you have to migrate those changes to the database.
- migration commands include 
  - `python manage.py makemigrations` creates the migration files (for later use)
  - `python manage.py migrate` actually migrates the models to a database
  - `python3 manage.py showmigrations` is the command you need to show the migrations (duh). When an x appears in the brackets, the migration has been applied, otherwise it hasn't.
- ==Question==: how do you link the models to the sqlite database? Is it automatic when it comes to migrations?

## Django ORM

- say you want to import a pet model into your code. import the file dotted with the class name of the model like so: `from <fileName>.models import <modelName>` for example, importing the pet model from adoptions.py looks like`from adoptions.models import Pet`.
- access all rows of the model with `Pet.object.all()`
- if you want to access all elements of the attribute in question, say the number of vaccinations a pet has, you can use `Pet.vaccinations.all()`
- access the model attributes by dotting them after the model name egoogle.com. `Pet.name`. no parentheses needed. Not a member function. 
- you can query the model with `Pet.objects.get(id=1,name='Pepe')` . The get command will return an error if the query results in two or more records; it's like an assignment with an sql table.