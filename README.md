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
