## [03] As a waiter. I would like to know the menu. So that I can help the guests

A menu is a combination of dishes.

**Tasks:**

1. create a class for menu
2. create a class for dish
3. add a initialize method to the menu to create a array of dishes
4. add a initialize method to the dish
5. create a array of dishes calling its constructor with a name
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


###3. add a initialize method to the menu to create a array of dishes

When a object is constructed, its initialize method is called. So when you call Menu() to create a object of the menu class, it searches for the initialize method in the Menu class.

- Add the initialize method to the Menu class

```python
def __init__(self):
	pass
```

- Inside the initialize method of Menu we are going create the following dishes. Margherita, Napoletana, Peperoni

###4. Add a initialize method to the dish

- To create a `Dish` with a name, you can use the initialize method again. Add a initialize method (constructor) to the `Dish` class that takes a `dish_name` as a argument.

```python
def __init__(self, dish_name):
	pass
```

- Assign the argument of the constructor to a instance variable `@name`

```python
def __init__(self, dish_name)
  self.name = dish_name
end
```

A *instance variable* is available to all methods of a class instance (object). Unlike a normal variable which is only available inside the method where it was created.

###5. Create a array of dishes calling its constructor with a name

- require the file containing the dish class inside the file containing the menu class

```python
from dish import Dish
```

- create a array inside the initialize method of the Menu class and assign it to a instance variable

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

- require the file containing the menu in the pizzeria file.

```python
from menu import Menu
```

- Create a instance of the menu class by calling its constructor.

```python
menu = Menu()
```

- Add a constructor method to the waiter class that takes a argument for menu.
- Assign the argument to a instance variable.

```python
def __init__(self, menu):
  self.menu = menu
end
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
end
```


- create a `list_menu` method in the `Waiter` class to list all the dishes

```python
  def list_menu(self):
  	  for dish in self.menu.contents():
    	  print(dish)
```
- call the `list_menu` method in the case statement

```python
  def take_order(self, order_number):
        if order_number == 1:
            answer = "Let me get the menu"
            self.list_menu()
```

###8. test your progress

- Open the terminal
- Run the pizzeria class with ruby `python pizzeria.py`
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
- Run the pizzeria class with ruby `python pizzeria.py`
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




## [04] As a waiter. I would like to be able to order a item from the kitchen. So that the guests stop bothering me

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
    pass
```

### 5. Add a method to the kitchen so a order can be sent

```python
def order(self, dish):
    print("KITCHEN: Order received for {0}".format(dish.name))
end
```

### 6. Let the waiter know about the kitchen

- In the `pizzeria.py` file add an import for the file containing the kitchen
- Create a new instance of the `Kitchen` class and assign it to a variable

```python
kitchen = Kitchen()
```

- Add the option to `Waiter` to receive a kitchen in its initializer method. Assign this argument to a instance variable

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

### 2. Add a initializer to the ingredient class that can take a name and amount

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

- Add a ingredients list to the initializer of the Dish class

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
- Run the pizzeria class with ruby `python pizzeria.py`
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
"0. Margherita"
"1. Napoletana"
"2. Peperoni"
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
