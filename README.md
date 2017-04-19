#[Cooking 101](http://s2.quickmeme.com/img/3c/3ca2955b995c2b02bf1d821a8cf7066c5689eb3e2a4ebc7a80bfdf501290669c.jpg)

We will learn today to cook with objects. We will start with creating a list of all objects of a pizzeria.

Because with objects oriented programming you want your code to work like a pizzeria.

- Waiter: You talk to the waiter. He takes your order, serves the food, checks if you want anything else and eventually you can pay the bill.
- Kitchen: In the kitchen the food is prepared.
- Dish: A dish is a collection of ingredients prepared in a certain order.
- Menu: A collection of recipes with available ingredients
- Ingredients: Part of a recipe.
- Stock: Amount of ingredients available
- Storageroom: Holds the stock

Lets start by setting up the project:

- open your terminal
- create a new directory
- go into the directory
- create a .gitignore file with the following setup => https://github.com/github/gitignore/blob/master/Python.gitignore
- initialize a new git repository `git init`

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
class Waiter(object):
```

### 2. Add a method to the Waiter to greet a guest

- add a method `greet_guest`
- the method should print a greeting

```python
class Waiter(object):

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
- Commit the files to your local git `git commit -m 'greetings'`

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
class Menu(object):
```

###2. create a class for dish

- Create a file `dish.py`
- Create a class in this new file

```python
class Dish(object):
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
class Kitchen(object):
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
class Ingredient(object):
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

class Kitchen(object):
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
class Check(object):

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
