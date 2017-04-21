#[Cooking 101](http://s2.quickmeme.com/img/3c/3ca2955b995c2b02bf1d821a8cf7066c5689eb3e2a4ebc7a80bfdf501290669c.jpg)

## Legend

Before we kick of a short explanation about notations used in during the course. In code examples you will see:

#### Commands executed in your shell. Sometimes with example output

```shell
$ echo 'Hello world'
Hello world
```

#### Python code executed in the Python interpreter, also sometimes with example output

```python
>>> print ('Hello universe')
Hello universe
```

#### And Python code that you will edit as a file

```python
class Hello:
    def world(self):
        print('Allo allo')
```

## Introduction

We will learn today to cook with objects in Python 3.6. We will start with creating a list of all objects of a pizzeria.

Because with objects oriented programming you want your code to work like a pizzeria.

- Waiter: You talk to the waiter. He takes your order, serves the food, checks if you want anything else and eventually you can pay the bill.
- Kitchen: In the kitchen the food is prepared.
- Dish: A dish is a collection of ingredients prepared in a certain order.
- Menu: A collection of recipes with available ingredients
- Ingredients: Part of a recipe.
- Stock: Amount of ingredients available
- Storageroom: Holds the stock

As explained on first impression the differences between Python 2 and 3 look minimal. So which version to choose?

Python 3 was released already back in 2008. This was a big thing since your Python 2 code would not just run in
Python 3 out of the box. And think not only of your own codebase, but all the other dependencies that you
have on third party libraries! Are they updated already? You can imagine the pain of this for the Python
community at large.

But! Even though it is a pain now, that is not an argument to postpone and have lot's more pain later. So
by Python's benevolent dictator for life it was so decreed to bite the bullet. Amongst things print became a 
function instead of a language statement  (like assert), strings became unicode instead of ASCII and
having to explicitly define a unicode string with `u"I'm a unicode string"` and the standard library was refactored:
naming was normalized and parts of the library where restructured.

It is now 2017. All libraries that you would use have been ported to Python 3. Hooray! For this project
we will use Python 3.6 (the latest major release). 

Lets start by setting up the project:

- open your terminal
- create a new directory
- go into the directory
- create a .gitignore file with the following setup => https://github.com/github/gitignore/blob/master/Python.gitignore
- initialize a new git repository:
```shell
$ git init
$ git add .
$ git commit -m "Initial commit"
```

## [00] As a developer. I want to have each project that I work on run in an isolated environment, have a user friendly REPL environment and manage dependencies to third party projects easily.

Here we are going to lay the ground work for our project and make sure that the basic tools we are going to use are
operating 'within normal parameters'.

There is a couple of tools that we will use in almost all Python projects:

#### Virtualenv

This used to be a separate project, but is now part of Python itself. Virtualenv creates isolated Python environments. Within
these environments you can safely install or remove packages without affecting any of your other projects.

#### Pip

Pip is Python's package manager. Pip allows you to easily install third party libraries within your project's isolated virtualenv.
Dependencies can be specified in a separate file (or multiple files) that you can manage within your source repository. Also
(especially important for production environments) you can 'version pin' third party dependencies. This ensures that you only
work with versions that are proven to work correctly in all of your deployment environments.

#### IPython

Python's shell is a so called REPL environment: a read-eval-print-loop. An interactive program that runs the code you
enter line by line and evaluates the code after every line, printing any output if required. For the purpose of this
 course this allows us to quickly try out code.

IPython is an extension of the Python shell that adds things like tab-completion and reloading.

**Tasks:**

1. create a virtual environment for our project
2. add a specific version of IPython as a dependency of our project
3. install dependencies using pip


### 1. Create a virtual environment for our project

- Run the following command in your shell:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Your shell prompt should now look something like: `(.venv) > `

**Note:** The last line activates the virtual environment, this means that if you type `python` you will run the Python
 command that is isolated to this virtual environment. You will have to activate the virtual env in every new shell that
 you open with this same command. If you don't do that running the `python` command will use the system installed Python.
 There are tools to automate this, but that is outside of the scope of this course.

### 2. add a specific version of IPython as a dependency of our project

- Create a requirements.txt file in your project folder, this file should contain the following:

```
ipython==5.3.0
```

**Note:** This pins version 5.3.0 of the IPython project as a dependency to our project. Even if newer versions are released
of this project, if we reinstall the dependencies we will install version 5.3.0 until we explicitly upgrade this.

### 3. install dependencies using pip

- In your shell run the following command:

```shell
$ pip install -r requirements.txt
```

This will instruct pip to install the dependencies specified in your `requirements.txt`. Besides the dependency that
**we** have explicitly specified you will also see that pip installs packages like `pygments` amongst others. These are
dependencies that the IPython project needs in order to work correctly.

**Note:** When working with dependencies always only explicitly declare the dependencies and versions of them that
**you** need. Leave it up to pip to resolve all other dependencies.

### 4. Test if it all works

- In your terminal start IPython:

```shell
$ ipython
```

You should now see something like:

```
Python 3.6.0 (default, Dec 24 2016, 00:01:50)
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
```

You should see the above text and be able to run Python commands. Type: `print('Hello world')` and press enter to execute
the first (obligatory Hello World) Python code of your project. To exit press `CTRL-D`

Great! We are ready to get going!

## [01] As a guest. I want to be greeted by the waiter when I enter the pizzeria. So that I feel like I am welcome.

**Tasks:**

1. create a waiter
2. add a method to the waiter to greet a guest
3. create a pizzeria
4. import the waiter in the pizzeria
5. make an instance of the waiter in the pizzeria
6. call the greeting method
7. test if it all works
8. save your progress

### 1. Create a waiter

- Create a file `waiter.py`
- Create a class in this new file. We create a class like:

```python
class Waiter:
    pass
```

A thing to note here is the statement `pass`. Python defines its scope using indentation. 
PEP8: https://www.python.org/dev/peps/pep-0008/ which is the Python style guide defines indentation
as 4 spaces. To say that a scope doesn't have any content yet `pass` is required. This would be equivalent
to `public class Waiter{}` in Java.

In Python 2 code you will always see classes defined as: `class Waiter(object)`. Very old versions of Python
had something dubbed old-style classes. These classes did not have `object` as the root class. Don't ask! ;) 

Python 3 completely removed that so `class Waiter` now inherits from `object`. Python does multiple inheritance
if you want to for example define a RobotWaiter, that is a Robot which is also a Waiter you can write a class
definition like:

```python
class Robot:
    pass
    
class RobotWaiter(Robot, Waiter):
    pass
```

This is of course quite a simple class hierarchy, having multiple classes inheriting from one another
can quickly turn into something much more complex. What code will be run when? Python defines an explicit
method resolution order (MRO) based on an algorithm called C3. For our RobotWaiter class the MRO is:

```python
>>> RobotWaiter.__mro__
(<class '__main__.RobotWaiter'>, <class '__main__.Robot'>, <class '__main__.Waiter'>, <class 'object'>)
```

The class `RobotWaiter` will first 

### 2. Add a method to the Waiter to greet a guest

- add a method `greet_guest`
- the method should print a greeting

```python
class Waiter:

    def greet_guest(self):
        print("Good day. Welcome to our lovely little restaurant.")
```

### 3. Create a pizzeria

- create a file `__init__.py`. The __init__.py files are required to make Python treat the directories as containing packages, and enable you to import modules inside a directory;
- create a file `pizzeria.py`

### 4. Import the waiter in the pizzeria

- at the top of `pizzeria.py` add `from waiter import Waiter` to include the Waiter class.

### 5. Make an instance of the waiter in the pizzeria

An instance is when we create an object from a class. You can create an object by calling the constructor method, `Waiter()`, and by default it takes no arguments.

- Create a new instance of `Waiter` and assign it to a variable `w = Waiter()`

### 6. Call the greeting method

- Call a method on an object by placing it after a dot. Like `object.method()`. So to call the `greet_guest` method on the object stored in `w` you can call `w.greet_guest()`

### 7. Test if it all works

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display: `"Good day. Welcome to our lovely little restaurant"`

### 8. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'Added greetings'`

## [02] As a guest. I would like the waiter to help me. So that I can have a bite to eat

**Tasks:**

1. Create a method for the waiter to serve_guests.
2. The serve_guests method should print a list of options for the guests
3. A guest should be able to choose from the options by their number.
4. After a choice is made, the waiter can take action
5. Call the serve_guest method from the pizzeria
6. Test if it all works
7. save your progress

### 1. Create a method for the waiter to serve_guests.

```python
  def serve_guest(self):
```

### 2. The serve_guests method should print a list of options for the guests

Add a small menu to the body of the `serve_guest()` method. For example

```
def serve_guest(self):
    print("How can I be of service?")
    print("1. Would you like to order a pizza?")
    print("2. Would you like to leave?")
```    

### 3. A guest should be able to choose from the options by their number.

Call the `input` method at the bottom of the serve_guest method

```python
choice = input()
```

### 4. After a choice is made, the waiter can take action

- create a method to handle the input of the `input()` method. When we create a method that needs input from another method, you have to add this data to its arguments list.

```python
def take_order(self, order_number):
```

- call the `take_order()` method using your choice variable. By default, `input()` parses input params as strings, so be sure to convert the choice to an integer using `int()`.

```python
self.take_order(order_number=int(choice))
```

- if the choice is 1 or 2 or none of these, give appropriate response. To easily do this we can use an if/elif/else statement. Add the following content to the take_order() function.

```python
def take_order(self, order_number):
    if order_number == 1:
        print("Let me get the menu")
    elif order_number == 2:
        print("Thank you for your visit!")
    else:
        print("I really don't understand")
```

### 5. Call the serve_guest method from the pizzeria

- on the waiter object stored in the `w` variable, call the `serve_guest()` method.

```python
w.serve_guest()
```

### 6. Test if it all works

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```
"Good day. Welcome to our lovely little restaurant"`
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Wait for input
- Exit


### 7. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'choices'`


## [03] As a waiter. I would like to know the menu. So that I can help the guests

A menu is a combination of dishes.

**Tasks:**

1. create a class for menu
2. create a class for dish
3. add an initialize method to the menu to create an array of dishes
4. add an initialize method to the dish
5. create an array of dishes calling its constructor with a name
6. let the waiter know about the menu
7. let the waiter tell guests the contents of the menu
8. test your progress
9. Improve the display of dishes
10. test your progress
11. Save your progress

### 1. create a class for menu

- Create a file `menu.py`
- Create a class in this new file

```python
class Menu:
```

###2. create a class for dish

- Create a file `dish.py`
- Create a class in this new file

```python
class Dish:
```


###3. add an initialize method to the menu to create an array of dishes

When an object is constructed, its initialize method is called. So when you call Menu() to create an object of the menu class, it searches for the initialize method in the Menu class.

- Add the initialize method to the Menu class

```python
def __init__(self):
```

- Inside the initialize method of Menu we are going create the following dishes. Margherita, Napoletana, Peperoni

###4. Add an initialize method to the dish

- To create a `Dish` with a name, you can use the initialize method again. Add an initialize method (constructor) to the `Dish` class that takes a `dish_name` as an argument.

```python
def __init__(self, dish_name):
```

- Assign the argument of the constructor to an instance variable `@name`

```python
def __init__(self, dish_name)
    self.name = dish_name
```

An *instance variable* is available to all methods of a class instance (object). Unlike a normal variable which is only available inside the method where it was created.

###5. Create an array of dishes calling its constructor with a name

- import the file containing the dish class inside the file containing the menu class

```python
from dish import Dish
```

- create an array inside the initialize method of the Menu class and assign it to an instance variable

```python
self.menu = []
```

- create instances of the dish class and add them to the variable holding the array

```python
self.menu.append(Dish(dish_name="Margherita"))
self.menu.append(Dish(dish_name="Napoletana"))
self.menu.append(Dish(dish_name="Pepperoni"))
```

###6. let the waiter know about the menu

- import the file containing the menu in the pizzeria file.

```python
from menu import Menu
```

- Create an instance of the menu class by calling its constructor.

```python
menu = Menu()
```

- Add a constructor method to the waiter class that takes an argument for menu.
- Assign the argument to an instance variable.

```python
def __init__(self, menu):
    self.menu = menu
```

- Change the call to the constructor of Waiter in Pizzeria to receive a menu.

```python
w = Waiter(menu=menu)
```


###7. let the waiter tell guests the contents of the menu

- define a method in the `Menu` class to return the value of the instance variable.

```python
def contents(self):
    return self.menu
```


- create a `list_menu` method in the `Waiter` class to list all the dishes

```python
def list_menu(self):
    for dish in self.menu.contents():
        print(dish)
```
- call the `list_menu` method in the if statement

```python
def take_order(self, order_number):
    if order_number == 1:
        answer = "Let me get the menu"
        self.list_menu()
```

###8. test your progress

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```bash
"Good day. Welcome to our lovely restaurant"
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Choose 1
- Should display:

```bash
<dish.Dish object at 0x10f6f7630>
<dish.Dish object at 0x10f724438>
<dish.Dish object at 0x10f724630>
```

###9. Improve the display of dishes


- In the loop printing the dishes, call the `name` property to display the name

```python
def list_menu(self):
   for dish in self.menu.contents():
       print(dish.name)
```

###10. test your program

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```
"Good day. Welcome to our lovely little restaurant"
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Choose 1
- Should display:

```
"Margherita"
"Napoletana"
"Pepperoni"
```

### 11. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'choices'`




## [04] As a waiter. I would like to be able to order an item from the kitchen. So that the guests stop bothering me

**Tasks:**

1. add a number to a dish
2. allow the ordering of food by this number
3. call the order food after the menu was listed and supply the number of the dish
4. add a kitchen class
5. add a method to kitchen so it can receive orders of dishes
6. let the waiter know about the kitchen
7. let the kitchen know about the order
8. test your progress
9. save your progress


### 1. Modify the loop that lists the menu, to also list a number that can be used by a guest

```python
def list_menu(self):
    for index, dish in enumerate(self.menu.contents()):
        print(index, dish.name)
```

### 2. Create a method to order food from the kitchen in waiter based on the guests choice

```python
def order_food(self, choice):
    chosen_dish = self.menu.contents()[choice]
```

this method will assign a dish object to the dish variable.

### 3. Call the `order_food` method after calling the `list_menu` method

```python
print("Let me get the menu")
self.list_menu()
self.order_food(choice=int(input()))
```

### 4. create a class for the kitchen

- Create a file `kitchen.py`
- Create a class in this new file

```python
class Kitchen:
```

### 5. Add a method to the kitchen so an order can be sent

```python
def order(self, dish):
    print("KITCHEN: Order received for {0}".format(dish.name))
```

### 6. Let the waiter know about the kitchen

- In the `pizzeria.py` file add an import for the file containing the kitchen
- Create a new instance of the `Kitchen` class and assign it to a variable

```python
kitchen = Kitchen()
```

- Add the option to `Waiter` to receive a kitchen in its initializer method. Assign this argument to an instance variable

```python
def __init__(self, menu, kitchen):
    self.menu = menu
    self.kitchen = kitchen
```

- Add the variable kitchen to the initialization of the `Waiter` class.

```python
w = Waiter(menu=menu, kitchen=kitchen)
```

### 7. Let the kitchen know about the order

- In the `order_food` method of the Waiter class add a call to the order method of the Kitchen

```python
def order_food(self, choice):
    chosen_dish = self.menu.contents()[choice]
    self.kitchen.order(dish=chosen_dish)
```

### 8. test your program

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```
"Good day. Welcome to our lovely little restaurant"
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Choose 1
- Should display:

```
"0 Margherita"
"1 Napoletana"
"2 Peperoni"
```

- Choose 2
- Should display

```
"KITCHEN: Order received for Peperoni"
```

### 9. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'choices'`



## [05] As a cook. I would like to know which ingredients I have to use and which amounts. So that the dishes taste nice

**Tasks:**

1. create a class for Ingredient
2. ingredients can have a name and amount
3. add constants for the ingredient names
4. When creating a dish, add ingredients
5. print a list of ingredients and their amount
6. let the waiter know about the kitchen
7. let the kitchen know about the order
8. test your progress
9. save your progress


### 1. Create a class for Ingredient

- Create a file `ingredient.py`
- Create a class in this new file

### 2. Add an initializer to the ingredient class that can take a name and amount

```python
def __init__(self, name, amount):
    self.name = name
    self.amount = amount
```

### 3. Add constants for the pizza ingredient names

```python
class Ingredient:
    TOMATO = "Tomato"
    DOUGH = "Dough"
    MOZZARELLA = "Mozzarella"
    ANCHOVIES = "Anchovies"
    PEPPERONI = "Peperoni"

```

Constants are used to prevent misspelling.


### 4. When creating a dish, add ingredients

- Add an ingredients list to the initializer of the Dish class

```python
def __init__(self, dish_name, ingredients):
    self.name = dish_name
    self.ingredients = ingredients
```

- In the menu, where the dishes are initialized, import Ingredient

```python
from ingredient import Ingredient
```

- ...and add ingredients

```python
self.menu.append(Dish(
    dish_name="Margherita",
    ingredients=[
        Ingredient(name=Ingredient.TOMATO, amount=3),
        Ingredient(name=Ingredient.DOUGH, amount=0.25),
        Ingredient(name=Ingredient.MOZZARELLA, amount=0.2)
    ])
)
self.menu.append(Dish(
    dish_name="Napoletana",
    ingredients=[
        Ingredient(name=Ingredient.TOMATO, amount=3),
        Ingredient(name=Ingredient.DOUGH, amount=0.25),
        Ingredient(name=Ingredient.MOZZARELLA, amount=0.2),
        Ingredient(name=Ingredient.ANCHOVIES, amount=0.05)
    ])
)
self.menu.append(Dish(
    dish_name="Pepperoni",
    ingredients=[
        Ingredient(name=Ingredient.TOMATO, amount=3),
        Ingredient(name=Ingredient.DOUGH, amount=0.25),
        Ingredient(name=Ingredient.MOZZARELLA, amount=0.2),
        Ingredient(name=Ingredient.PEPPERONI, amount=0.1)
    ])
)
```

### 5. Get the ingredients and its name from a Dish and print it in the kitchen

- Improve the order method of the Kitchen class to print a list of ingredients for the dish

```python
def order(self, dish):
    print("KITCHEN: Order received for {0}".format(dish.name))
    print("I'm gonna need some:")
    for ingredient in dish.ingredients:
        print("{0} - {1}".format(ingredient.amount, ingredient.name))
```


### 6. test your program

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```bash
"Good day. Welcome to our lovely little restaurant"
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Choose 1
- Should display:

```bash
"0 Margherita"
"1 Napoletana"
"2 Peperoni"
```

- Choose 1
- Should display

```bash
"KITCHEN: Order received for Napoletana"
"Im gonna need some:"
"3 - Tomato"
"0.25 - Dough"
"0.2 - Mozzarella"
"0.05 - Anchovies"
```

### 7. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'choices'`



## [06] As a waiter. I would like to know if a dish can still be ordered. So that I don't try sell unavailable dishes.

Add a storage and check before an order can be placed. When a dish is prepared, update the stock.

### 1. Create a class for Storage

- Create a file `storage.py`
- Create a class in this new file

### 2. Add an initialize method to the Storage class that creates stock for a bunch of ingredients

```python
from ingredient import Ingredient
```

```python
def __init__(self):
    self.items = [
        Ingredient(name=Ingredient.TOMATO, amount=8),
        Ingredient(name=Ingredient.DOUGH, amount=2),
        Ingredient(name=Ingredient.MOZZARELLA, amount=1),
        Ingredient(name=Ingredient.PEPPERONI, amount=0.3),
    ]
```

### 3. Add a method to decrease the amount of an ingredient to the Ingredient class

```python
def use(self, amount):
    self.amount -= amount
```

### 4. Add a fetch method to the Storage class

- Create a check_storage method that takes an ingredient as an argument and finds it for you in the storage

```python
def check_storage(self, ingredient):
    for storage_item in self.items:
        if ingredient.name == storage_item.name:
            return storage_item
```

- Create a fetch method that takes a list of ingredients as an argument and checks them out of the storage using the check_storage method

```python
def fetch(self, ingredients):
    for ingredient in ingredients:
        storage_item = self.check_storage(ingredient)
        if storage_item:
            storage_item.use(amount=ingredient.amount)
```

### 5. Let the kitchen create an instance of the storage

- import the file which is declaring the storage class in kitchen

```python
from storage import Storage

class Kitchen:
```

- add an initializer method to the kitchen and create an instance of storage

```python
def __init__(self):
    self.storage = Storage()
```

### 5. Call the fetch method when an order is placed. Add it to the bottom of the order method of Kitchen

```python
return self.storage.fetch(ingredients=dish.ingredients)
```

### 6. Add a check to the `order_food` method of the `Waiter` class and wrap the order in it.

```python
def order_food(self, choice):
    chosen_dish = self.menu.contents()[choice]
    if self.kitchen.order(dish=chosen_dish):
        print("Dish is on the way")
    else:
        print("Sorry, this dish is not available")
```

### 7. Change the fetch method of Storage to return a boolean if a dish is not available

The kitchen has the order method which tries to fetch items from the storage. Make it return False if an item can't be found in the storage, and True otherwise.

```python
def fetch(self, ingredients):
    for ingredient in ingredients:
        storage_item = self.check_storage(ingredient)
        if storage_item:
            storage_item.use(amount=ingredient.amount)
        else:
            return False
    return True
```

### 8. test your program

- Open the terminal
- Run the pizzeria class with python `python pizzeria.py`
- Should display:

```
"Good day. Welcome to our lovely little restaurant"
"How can I be of service?"
"1. Would you like to order a pizza?"
"2. Would you like to leave?"
```

- Choose 1
- Should display:

```
"0. Margherita"
"1. Napoletana"
"2. Pepperoni"
```

- Choose 1
- Should display

```
"KITCHEN: Order received for Napoletana"
"Im gonna need some:"
"3 - Tomato"
"0.25 - Dough"
"0.2 - Mozzarella"
"0.05 - Anchovies"
"Sorry this dish is not available"
```

- Likewise, if you choose pizza #0, the response should be:

```
"KITCHEN: Order received for Margherita"
"Im gonna need some:"
"3 - Tomato"
"0.25 - Dough"
"0.2 - Mozzarella"
"Dish is on the way"
```


### 9. Save your progress

- Open the terminal
- Add all the files in your project to git `git add .`
- Commit the files to your local git `git commit -m 'choices'`


## [07] As a waiter. I would like to keep track of the items that a customer orders. So that I can present the bill afterwards.

### 1. Add a class for check
### 2. Add an initializer method which creates an empty array

 - create an instance variable in the initializer and assign an empty array to it

### 3. Create a method to add items to the check

```python
class Check:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
```

### 4. Add an item to the check if it can be ordered

- import the file containing the check class in the waiter class file
- add an instance variable to the waiter initialize method

```python
self.check = Check()
```

- call the add method on self.check if food can be ordered

```python
self.check.add(item=chosen_dish)
```

### 5. Test && Save

## [08] As a guest. I would like to keep ordering food until there is no stock left or I have had enough. So that I have a good time

### 1. add a method to waiter to check if he is still serving a guest

- add a boolean to the waiter class as an instance variable `self.serving`. Add it to the initializer and give it the value of `True`

```python
self.serving = True
```

### 2. create a loop for waiter in the pizzeria

```python
while w.serving:
    w.serve_guest()
```

### 3. stop serving if a guest wants to leave

- in the method `take_order()` of Waiter. Set self.serving to `False` if a guest wants to leave.


### 4. Test && Save

## [09] As a waiter. I would like to present the bill after a guest is done. So that I can get payed.

### 1. Add a price field to the dish

- add a price to the arguments of the initializer of the dish class
- assign the price to an instance variable

### 2. Add a price to all the dishes on the menu

- in the menu class initializer, add a price for each of the three dishes

### 3. Add a method to check to calculate the sum of all dishes

- create a method on the check class that loops over all items
- create a local variable sum for this method
- for each dish in the item loop, add the price to the sum
- return the value of sum

```python
def calculate_sum(self):
    total_sum = 0
    for dish in self.items:
        total_sum += dish.price
    return total_sum
```

- let the waiter call this method and tell the value after saying "Thank you for your visit"

### 4. Test && Save


## [10] As storage. I would like to keep track of my ingredients more efficiently, so I don't have to loop over every single item.

### 1. Replace the storage items with a dictionary

- in your Storage class initializer method, remove the list syntax `[]` with dictionary syntax `{}`
- use the ingredient names as keys, and the ingredient objects as values

```python
def __init__(self):
    self.items = {
        Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
        Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
        Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
        Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
    }
```

- comment out the `check_storage` method for now

### 2. Find your storage items using the name of your ingredients

- inside the ingredient loop in `fetch()`, index into `self.items` using the ingredient name
- be sure to use `Try/Except` to catch a potential `KeyError`, as we don't know for sure whether all ingredients will be available in the storage
- if you catch a `KeyError`, be sure to return `False` so the kitchen is updated
- if the ingredient is there, use an `else` statement to update the ingredient, as before

```python
def fetch(self, ingredients):
    for ingredient in ingredients:
        try:
            # look up the ingredient in the storage
            storage_item = self.items[ingredient.name]
        except KeyError:
            # the ingredient isn't there
            return False
        else:
            # we now know it's there, so we can use the storage_item
            storage_item.use(amount=ingredient.amount)
    return True
```

### 3. Test && Save

## [11] As storage. I would like to check for all my ingredients if inventory is sufficient, before informing the kitchen.

So far the storage has only been checking whether an ingredient existed, rather than doing the full check if each ingredient is available before updating amounts. Let's fix this!

### 1. Track available ingredients in a checklist

- create an empty checklist array (list in python).
- while looping over your storage items, if an item is not there, append a boolean `False` to your checklist
- if the ingredient is present, append `True`.

### 2. See if all ingredients are available, and update inventory accordingly

- check if the boolean `False` appears in you checklist, and store this in variable `all_ingredients_are_there`
- if all ingredients are there, loop over each ingredient once again, index into `self.items` and update the ingredient amount via `use()`
- if all ingredients are there, and you've updated the storage items, `print()` the current inventory

```python
print("STORAGE: Inventory is now...")
for ingredient in self.items.values():
    print(ingredient.amount, ingredient.name)
```

### 3. Test && Save

- assuming you still have the same ingredients in your initializer, using the print statement, you can now observe how inventory changes when you order a pizza Margherita or pizza Pepperoni.

### 4. BONUS: Storage Refactoring

There are two things that we can refactor in our storage class:

- During the first loop over our ingredients, we're merely checking whether each ingredient is there, rather than actually using it. as such, we don't really need to index into our dictionary to get the ingredient. Instead, we can just check whether the ingredient is in the `self.items` dictionary. you can do this by looking up the name of the ingredient in `self.items.keys()`, and append the boolean to our `checklist`.

```python
checklist.append(ingredient.name in self.items.keys())
```

- Rather then checking if the boolean `False` doesn't appear in our checklist, we can use the build in `all()` function, which returns `True` if all elements of the iterable are true (or if the iterable is empty).

```python
all_ingredients_are_there = all(checklist)
```

### 5. Test && Save


## [12] As developer. I would like code that is tested automatically.

The saying goes: `untested code is broken code`. In our experience this holds for anything but the most trivial projects.
But doing testing well is in itself also a non trivial exercise. What parts do you test? Are you sure that you are only
testing your code? Are you testing all the edge cases? Besides writing automated tests means introducing more code which
in turn means maintaining a larger codebase.

Python has long ago adopted the so called xUnit testing paradigm, the unit testing work originally introduced in Java
(and Smalltalk) by Kent Beck. Over the years of Python pragmatism has thought us that the xUnit way of working is quite
verbose and sometimes inflexible. Therefore we will use the `pytest` testing framework which is the new `standard` for
writing tests in Python.

In a test first mentality we would have started with writing tests first :) In practice we find that a less dogmatic 
approach works best for us. Writing beautiful code is a craft not a procedure. Part of craftsmanship is guaranteeing the
quality of what you make. How much confidence do you have in running your code in production?

## 1. Install the `pytest` testing framework.

- Update your requirements.txt and add the following line to it:

```
pytest==3.0.7
```

- Run `pip` to update the dependencies within your virtualenv:

```shell
$ pip install -r requirements.txt
```

- Test that pytest works:

```shell
$ pytest
```

The output should be something like:

```shell
========================================================= test session starts =========================================================
platform darwin -- Python 3.6.0, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /Users/remco/Tmp/boer, inifile:
collected 0 items

==================================================== no tests ran in 0.00 seconds =====================================================
```

## 2. Let's add a test to test `calculate_sum` in the `Check` class

- Add a new directory in your project directory called `tests` inside that directory add `__init__.py`

- Add a new file inside of the `tests` directory called `test_check.py`, inside of it add the following code:

```python
from check import Check
from dish import Dish


def test_calculate_sum():
    pasta = Dish('Pasta', [], 10)
    pizza = Dish('Pizza', [], 15)
    c = Check()

    # Without any items check sum must be 0
    assert c.calculate_sum() == 0

    # Adding an item should have sum equal to the item
    c.add(pasta)
    assert c.calculate_sum() == 10

    # Adding another item should have sum equal sum of both items
    c.add(pizza)
    assert c.calculate_sum() == 25
```

The test workhorse here is a statement called `assert` it tests that the given expression is `True`. It takes an
optional secondary expression to output as a detailed message if the assertion doesn't hold. For example:

```python
>>> assert 1==0, 'No way!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: No way!
```

## 3. Run the tests and enjoy the beauty of the color green:

```shell
$ pytest

========================================================= test session starts =========================================================
platform darwin -- Python 3.6.0, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /Users/remco/Projects/cours/advanced-python/python-cooking-with-objects/12, inifile:
collected 1 items

tests/test_check.py .

====================================================== 1 passed in 0.01 seconds =======================================================
```

## 4. Storage fetch has also turned into a complex beast, let's test

- Add a file in the `tests` directory called `test_storage.py`:

```python
from storage import Storage
from ingredient import Ingredient


def test_fetch_empty_ingredients_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[]) is True


def test_fetch_nonexistent_ingredient_returns_false():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name='Non existent', amount=8)]) is False


def test_fetch_existent_item_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name=Ingredient.TOMATO, amount=1)]) is True


def test_fetch_multiple_items_should_work():
    storage = Storage()
    ingredients = [
        Ingredient(name=Ingredient.TOMATO, amount=1),
        Ingredient(name=Ingredient.DOUGH, amount=1)
    ]
    assert storage.fetch(ingredients) is True
```

- Run the tests again with `pytest`

We are now ready to reap the rewards of automated testing. Refactoring your code without the worries of possible breaking
it!


## [13] As developer. I would like to have a codebase that is readable and maintainable.

In the previous parts we have emphasized implementing functionality for the end users of our system. We will now focus
our efforts on the readability and maintainability of our code. For any serious software during the entire lifetime of 
a project by far the most time is spent in reading, fixing and adapting existing code. Producing code that is 
easy for both your colleague and future you to pick up on is thus vital. Python idioms have been specially crafted for 
maximum expressive power with a minimum of code. Following these idioms is called 'writing code that is Pythonic' in 
the world of Python. 

Also a good ritual to maintain high quality is to refactor existing code. As your understanding of what you are working
on decisions that you made earlier may currently not be the most effective solution. Or you find out that some code
that looks almost the same is used in different parts of your codebase. Luckily during the last part we have invested
some of our time to create tests which guarantee our code still respects the contract, even though the implementation
changes.

Let's refactor some existing code to make it more Pythonic!


### 1. Let's refactor Check's calculate sum:

- Open `check.py` the previous implementation we wrote looks like:

```python
class Check:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def calculate_sum(self):
        total_sum = 0
        for dish in self.items:
            total_sum += dish.price
        return total_sum
```

- Run `pytest` to see that the tests are still working.

- Now change the implementation of the `Check` class to:

```python
class Check:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        
    def calculate_sum(self):
        return sum([dish.price for dish in self.items])
```

That's nice, we have been able to reduce calculate_sum to a oneliner. But what is happening here? In Python the part
within [] is called a list comprehension. Its a short form of building a new list out of an existing `Iterable` (an
Iterable is a collection that you can iterate over) in this case what we are saying to Python is: for all dishes 
in self.items create a new list contains dish.price. The `sum()` function is a function that takes an iterable and
sums all its items.

- Since we changed the implementation let's do a quick `pytest` run. Green? Awesome!

### 2. Storage's fetch contains quite a few lines of code, let's refactor:

- Open `storage.py` this used to be our implementation:

```python
from ingredient import Ingredient


class Storage:

    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    def fetch(self, ingredients):
        checklist = []
        for ingredient in ingredients:
            try:
                # look up the ingredient in the storage
                self.items[ingredient.name]
            except KeyError:
                # the ingredient isn't there, append False
                checklist.append(False)
            else:
                # its there, so append True to our checklist
                checklist.append(True)

        all_ingredients_are_there = False not in checklist
        if all_ingredients_are_there:
            for ingredient in ingredients:
                # we can index into our dictionary without precaution now because
                # we know the ingredients are there
                self.items[ingredient.name].use(amount=ingredient.amount)

            # print an overview of our inventory, so we can keep track
            print("STORAGE: Inventory is now...")
            for ingredient in self.items.values():
                print(ingredient.amount, ingredient.name)

        return all_ingredients_are_there
```

- Let's also optimize this implementation:

```python
class Storage:

    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    def fetch(self, ingredients):
        all_ingredients_are_there = all([i.name in self.items for i in ingredients])

        if all_ingredients_are_there:
            # List needs to be called to evaluate map here
            list(map(lambda x: self.items[x.name].use(amount=x.amount), ingredients))

            print('STORAGE: Inventory is now...')
            print('\n'.join([f'{i.amount} {i.name}' for i in self.items.values()]))

        return all_ingredients_are_there
```

We need to do a bit more explaining here, on the first line of the `fetch` method you see another list comprehension. It
says the following: walk through all the given ingredients, use its name to check whether there is an entry in the
dictionary. What remains is a list consisting of True and False values. The `all()` function here returns True only
if all items in the list are True. Which is the case if all ingredients are there.

Now reading further we see a line which uses a function called `map(function, iterable)`. Map applies a function to
each item in the iterable. For example to calculate the square of 2, 3 and 4 you can do:

```python
def square(x):
    return x * x

assert list(map(square, [2, 3, 4])) == [4, 9, 16]
```

Since a lot of times we just want to use a short helper function that we don't really need outside of the scope of this
specific `map()` call, we can use an anonymous function or `lambda`. To rewrite the simple example, this is equivalent:

```python
assert list(map(lambda x: x * x, [2, 3, 4])) == [4, 9, 16]
```

In our more complex case, in the `Storage` class, we use the `lambda` not to calculate the square of two numbers. But
we just call another method namely `Ingredient.use()` to update all the amounts.

The last line that needs some explaining is:

```python
print('\n'.join([f'{i.amount} {i.name}' for i in self.items.values()]))
```

Again a list comprehension. This loops through the values of the items dictionary in the Storage object. For each item
a string is formatted containing the amount and name of the ingredient. This way of formatting strings is new in
Python 3.6, see: https://www.python.org/dev/peps/pep-0498/ . Strangely enough it took Python a while to really find a
nice syntax for this. What remains is a list of these strings.

`join()` is a string method that you call on the string that will act as a separator and then as its argument you
provide an iterable containing strings. This will join the individual string together with the original string. So 
in a simpler example this works:

```python
assert ', '.join(['Roel', 'Vincent', 'Remco']) == 'Roel, Vincent, Remco'
```

- By now I guess you know what comes next: `pytest`

All green? Great!


### 3. Refactoring tests

Tests are just code. And maintenance of them can be just as much of a headache as with 'regular' code. So let's also
take a moment to rewrite some of our test code into a more clear format.

- Open `tests/test_storage.py`, right now it should look like:

```python
from storage import Storage
from ingredient import Ingredient


def test_fetch_empty_ingredients_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[]) is True


def test_fetch_nonexistent_ingredient_returns_false():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name='Non existent', amount=8)]) is False


def test_fetch_existent_item_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name=Ingredient.TOMATO, amount=1)]) is True


def test_fetch_multiple_items_should_work():
    storage = Storage()
    ingredients = [
        Ingredient(name=Ingredient.TOMATO, amount=1),
        Ingredient(name=Ingredient.DOUGH, amount=1)
    ]
    assert storage.fetch(ingredients) is True
```

- Rewrite the code to be the following:

```python
import pytest

from storage import Storage
from ingredient import Ingredient


@pytest.mark.parametrize('ingredients, expected', [
    [[], True],
    [[Ingredient(name='Non existent', amount=8)], False],
    [[Ingredient(name=Ingredient.TOMATO, amount=1)], True],
    [[Ingredient(name=Ingredient.TOMATO, amount=1), Ingredient(name=Ingredient.DOUGH, amount=1)], True],
])
def test_fetch(ingredients, expected):
    storage = Storage()
    assert storage.fetch(ingredients) == expected
```

`pytest` calls this a parametrized test. It lets you define flexible define parameters that should be given to a
function for every case. And then simple allows you to define the structure of the test once. Saving you a lot of 
overhead for creating separate test functions. 

- Do we have a green light?
