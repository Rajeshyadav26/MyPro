"""
The container which can hold the multiple python objects is called module
Every python file will consider as package, module, library
The process of accessing the data from one file to another file is known as modularity

module has been divided into three types
1.user defined:
The modules which created by the user are called user defined modules
import : These keyword is used to import all the properties of one module into another
Irespect of usage, all the properties will get assigned the memory
From import : These keyword is used to import the specific properties of one module into another


built in modules : The modules which comes with the default programming language are called built in modules

os, sys, datetime,

The modules which comes neither the default programming language nor created by the developer are called third party modules
oops stands object oriented programming structure
The group of python objects which forms an entity(structure) which will provide the special features like
1.security
2.extendability
3.Reusability

object oriented programming comes with major two components they are
1.class
2.object/instance
class is an entity(structure)which can hold the multiple properties of the class
use the built in function called "class" to create a class in python
class ClassName:
    property1
    proprrty2

instance is a reference of a class which is used to access the class properties
instance_name = ClassName()
to access the class properties use the below syntax
instance_name.property1
ClassName.property2
The class variables defined/declared in the directly are called "class variabeles"
The properties are defined with the help of instance are called instance variables
class variables can also accessed with the help of ClassName
The properties created at the class level they can get modified with the help of class name only

for updation and creation python will consider two different memories and for
deletion it will consider the class and instance memory





"""


class A:
    a = 10
    b = [2, 4, 5]
    c = "hello"


obj = A()
# print(obj.a)
print(A().a)
print(A().b)
print(A.b)
print(A.c)

obj.a = 20
print(obj.a)
print(A.a)
A.a = 30
print(A.a)
print(obj.a)
obj.d = (1, 3)
print(obj.d)


class MyClass:
    a = 100
    b = [1, 3, 5]
    c = "yeswanth"

    # def func(self, x, y):  # func(obj, 10, 20)
    #     return x + y

    def func(self, x, y):
        print(self.a)
        return x * y


obj = MyClass()
print(obj.c)
# print(MyClass.func(10, 2))
print(obj.func(10, 20))
# print(obj.func(10, 29))
"""
whenever you calling a function with the help of instance
python internally perfroms instance_name will consider as a first parameter
instance method : The method which have keyword called self init as a parameter is called instance method
the instance method can be executed with the help of instance and
these instance method should have self as the first parameter
self is nothing but an instance of the class, which works like instance from within a class

method overloading:
-------------------
The process of creating multiple function with the same name and different signature(parameters) are called method overloading
python does not support method overloading, but we can achieve it's properties by using default parameters


class A:
    def add(self, a, b, c=0):
        print("i am 1st")
        return a + b

    # def add(self, a, b, c):
    #     print("i am second")
    #     return a * b * c


obj = A()
print(obj.add(10, 20, 34))



method overriding:
---------------------
The process of creating multiple functions with the same name and same signature(parameters) are called method overiding
python does not support method overiding, but we can achieve it is properties by placing them in different classes
class A:
    def add(self, a, b):

        return a + b


class B:
    def add(self, a, b):
        return a + b


obj = A()
print(obj.add(10, 20))
obj = B()
print(obj.add(13, 34))

polymorphism:
------------
The process of creating the properties which can perform multiple functionalities
we can create a polymorphic function with the help of method overiding only
poly : many
morphic : forms(functionalities)


class A:
    def add(self, a, b):

        return a + b


class B:
    def add(self, a, b):
        return a * b


obj = A()
print(obj.add(10, 20))
obj = B()
print(obj.add(13, 34))


constructor :
------------
The function which calls itself automatically, whenever an instance created for the class
__init__ will be consider as a constructor in python

it is mainly used to create pre define data required for other class operation

class A:
    def __init__(self, x, y):
        self.x1 = x  # instance variable
        self.y1 = y
        print(x, y)

    def add(self, a, b):
        print(self.x1 * self.y1)
        return a + b


obj = A(10, 20)
print(obj.add(12, 2))  # calling function




class A:
    def __init__(self, x, y):
        print(x + y)
        print("i am yeswanth")


# The parameters passed through the instance creation will transfered to the constructor
obj = A(10, 20)
scope of a variable:
--------------------
private scope:
---------------
It is specific to the particular location where it has been created are called private scope

Abstraction:
___________
The process of hiding the data is known as abstraction
preceed with the __

abstractio will use the classname as a wrapper to hide the data
_ClassName__property
To access the abstracted properties
instance_name._ClassName__property
class A:
    x = 10
    __y = 20

    def add(self, a, b):
        return a + b


obj = A()
print(obj.x)
print(dir(obj))
print(obj._A__y)

Encapsulation :
----------------
The process of binding the data is known as Encapsulation
in python encapsulation results hiding the data
preceed the property with __

Instance_method:
----------------

self and cls will look different but both of them having a similar property
self and cls is used to access the properties

instance method:
-----------------

The method which invoked with the help of instance only are called instance method
it takes self as the first mandatory parameter
almost every method in a class considered like an instance



class method:
--------------
The method which invoked with the help of either classname or instance are called class method
we have to @classmethod to create a class method
The class method should contain cls as the first mandatory parameter


static method:
-----------
This method will located in the class and will not maintain any relationship with other class properties
use @staticmethod to create static method
no need to define the mandatory parameter like self or cls
the method can be invoked with the help of instance or classname










# class A:
#     def add(self, a, b):
#         return a + b

#     @staticmethod
#     def add(a, b):

#         return a + b

#     @classmethod
#     def mul(cls, x, y):
#         return x * y


# obj = A()
# print(obj.add(10, 2))
# print(A.mul(10, 2))
# print(A.add(10, 2))

inheritance:
----------------
The process of accessing the data or properies from one class to another class is known as inheritance
single inheritance :
-------------------
If the inheritance invokes a single parent and single child class is known as single inheritance

multiple inheritance :
---------------------
if the inheritance invokes a multile parents and single child class is known as
multiple inheritance

method resolution order:
----------------------------
The order of executing the methods or properties which are invoked inheritance is known as method resolution order

according to mro python will look for the properties in the class for which we have created an instance

if the property is not available then it will look at the inherited classes in the direction of left to right



lambda function :
This function is also called anonymous function
The scope of lambda function is very less
one line function in python
to create lambda function we have to use lambda keyword
we dont need to write the return the statement

lambda function are very powerful when we club them with the functional programming tools

name = lambda parameter_section : operation_section

django:
-------
django is a framework, which is used to implement web based applications
The group of individual components interconnects each other
it is a third party library in python


pip install django

django-admin startproject <ProjectName>


manage.py
-----------
It is known as utility file in django
This is used to perform any kind of operation on a django project(like application, database creation, database updation)

__init__.py
-------------
(package initializer)
it will executed automatically when evet the project is executed



settings.py:
-------------
It contains all the settings related to the django project()

urls.py (Mapping file)
----------
it contains all the list of urls and their apporiate functionalities

wsgi.py : web server guided interface
--------------------------------------
this is used to create and active one web server for our django project

asgi.py :
this is used to create asynchrnous server for our django project so we can run multiple application parallely

creating an application:
-----------------------------
python manage.py startapp "Application Name"

Files is available in Application Folder
----------------------------------------
Migrations : A Folder which holds the changes made at Database level

models.py : Represents MODEL in MVT, which can holds all the DATABASE tables

views.py : Represents VIEWS in MVT, which can hold all the programming components like (classes, functions, etc)

admin.py : It is an Adminstrator file for the entire Django Application

test.py : This file which can hold all the test cases implemented by the tester

apps.py : This file is used to integrate the Django Application with the third party Application








Django follows the oldest latest pattern called "MVC"(Model View Controller)

considered like "MVT"(Model View Templates)

MVT: (MODEL VIEW TEMPLATES)
---
Model : The Data Abstraction layer(where we are hiding all the projects related information )
------
*model represents a database in MVT pattern(Database)
views : The Business logic layer(which will be like consider programming language)

Tempalates : Presentation layer (how you are displaying the content to the user) (frontend)


How does MVT works:
-------------------
Whenever the user enters an URL in the browser, Django will look for that URL in URL Mapper file(urls.py)

*if the given url is available in URLs.py file, then django will execute the appropriate functions

*now flow will move like urls.py to Views.py
*Now Views will makes a request to Models to get the data from the Database and
also makes a request to get the frontend related data

*The Consolidated Respones will send back to the browser in vice versa direction




To craeate/refresh the database run the below command from the project directory

python manage.py makemigrations (To detect the changes made at database level)
it is used to identify the changes made at database level

python manage.py migrate(To save the changes)
it is used to save the changes permanently

Running the Django Project:
------------------------
open cmd
cd to project directory
run the below command to run the project

python manage.py runserver(by default it will activate the server in local)

python manage.py runserver(IP : Port )(To run the server intranet or internet)

Intranet: The Application works within a specific network are called intranet


Creating a Table:
----------------
open models.py
To create a table in django, we have to create a class

1 class == 1 table == 1 model

models = group of tables

syntax:
--------
class TableName(models.Model):
    column1
    column2

*To create a python class as a table we have to inherit models.Model

1.IntegerField:

This is used to store the integers
availability in django.db.models.IntegerField

syntax: field_name = models.IntegerField()

2.CharField:
------------
This is used to store the strings or characters

availability in django.db.models.CharField()

syntax: field_name = models.CharField(max_length = 100)

AutoField: ID(Autoincremented Id column)
-----------
which is used to work for serial numbers

Adding a model to admin page
-----------------------------
open admin.py(inside Application Folder)

Add below lines to it

admin.site.register(TableName) and then import the table name
syntax:
from ApplicationName.models import TableName
from MyApp.models import Employee


changing the display name in admin portal for any django model object:
----------------------------------------------------------------------
open models.py
locate your table
create a function like below inside a table

def __str__(self):
    return self.name + "_" + return self.age


Inserting the Data into the Database table
-------------------------------------------
1.using Admin site
2.database tools
2.ORM (OBJECT RELATIONAL MAPPING)
insert into MyApp_Employee(name, age)
values("bharath", 21)


Base_URL:http://127:0:0:1:8000
Extended_Urls = URL patterns

urls.py:
----------
open urls.py
Locate urlpatterns list
create path function which takes two parameters
syntax:path(r'Pattern', view_function),

Regular Expression patterns:
-----------------------------
$ - End of the url
/ - End of the url with extension
^ - start of the url (latest does not required this)
<type:name> => passing parameters through URL


















"""


# class A:

#     def __str__(self):
#         print("i am yeswanth")

#     def __call__(self):
#         print("i am prabhas")


# obj = A()
# obj.__str__()
# obj.__call__()


# class A:
#     a = 10
#     b = 34


# class B:
#     x = 23
#     b = 2


# class C(A, B):
#     y = 10
#     d = "hello"


# obj = C()
# print(obj.x)
# print(obj.b)
# print(obj.y)

# class A:
#     def __call__(self):
#         s = "hello"
#         for i in s:
#             if i in "aeiou":
#                 print(i)


# obj = A()
# obj.__call__()


# a, b = 10, 7
# try:
#     print("i am try block")
#     c = a / b
#     print(c)
# except Exception as e:
#     print(str(e))"""
