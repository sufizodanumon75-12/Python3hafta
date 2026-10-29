# ---------------------------------------Practic---------------------------------------------
# class Car:
#     country = "Tajikistan"
    
#     def __init__(self,brand,model,price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def drive(self):
#         print("Drive")
    
#     @classmethod
#     def salom(cls):
#         print(f"Salom  {cls.country} ")
        
#     @staticmethod
#     def v(a,b):
#         return a+b
    
#     def __str__(self):
#         return self.brand
    
# car1=Car("Shevrolet","Camaro",1000000)
# print(Car.v("Salom"," Aleykum"))
        
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
        
#     def getter(self):
#         return self.__password
    
#     def setter(self,new_password):
#         self.__password = new_password
        

# user1 = User("Qobil","2333244")
# user1.setter("1314242424242424")
# print(user1.getter())
# -------------------------------------------Homework------------------------------------------------
# N1
# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
        
#     def student_info(self):
#         print(f'He(She)`s name is {self.name}.He(She)`s {self.age} years old.He studing with {self.grade} grade')
        
# student = Student("Ali",17,100)
# student.student_info()

# student = Student("Qobil",16,50)
# student.student_info()

# student = Student("Anora",19,80)
# student.student_info()


# N2
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year  = year
        
#     def display_info(self):
#         print(f'{self.brand} -- {self.model} -- {self.year}')
        
# car = Car("Shewrolet","Camaro",2000)
# car.display_info()


# N3
# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width * self.height
    
#     def perimetr(self):
#         return 2 * (self.width + self.height)
    
# rect = Rectangle(10,12)
# print(rect.area())
# print(rect.perimetr())


# N4
# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
        
#     def read(self,pages):
#         return f'Read pages {pages}'
        
#     def display_info(self):
#         print(f'{self.title} -- {self.author} -- {self.pages}')
        
# kitob = Book("Tojikon","Bobojon Gafurov",480)
# kitob.display_info()
# print(kitob.read(25))


# N5
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
        
#     def deposit(self,amount):
#         if amount <= 0:
#             print("Сумма снятия должна быть больше нуля.")
#             return 
#         self.balance += amount
    
#     def withdraw(self,amount):
#         if amount <= 0:
#             print("Сумма снятия должна быть больше нуля.")
            
#         elif amount > self.balance:
#             print("Недостаточно средств.")
            
#         else:
#             self.balance -= amount

    
#     def display_balance(self):
#         print(f'Владелец: {self.owner} Баланс: {self.balance}')
        
# account = BankAccount("Qobil", 1000)
# account.deposit(300)
# account.withdraw(250)
# account.display_balance()


# N6
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(f"{self.name} eat.")


# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} say: Gaw-Gaw!")


# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} say: Myau-Myau!")


# class Bird(Animal):
#     def fly(self):
#         print(f"{self.name} fly.")



# dog = Dog("Rex", 3)
# cat = Cat("Meni", 2)
# bird = Bird("Jordan", 1)

# dog.eat()
# dog.bark()

# cat.eat()
# cat.meow()

# bird.eat()
# bird.fly()

# N7
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size


# developer = Developer("Ali", 120000, "Python")
# manager = Manager("Vali", 150000, 8)

# print(developer.name, developer.salary, developer.programming_language)
# print(manager.name, manager.salary, manager.team_size)

# # N8
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed


# class Car(Vehicle):
#     def __init__(self, brand, speed, doors):
#         super().__init__(brand, speed)
#         self.doors = doors

#     def display_info(self):
#         print(f"car: {self.brand}, speed: {self.speed} km/t, door: {self.doors}")


# class Motorcycle(Vehicle):
#     def __init__(self, brand, speed, has_sidecar):
#         super().__init__(brand, speed)
#         self.has_sidecar = has_sidecar

#     def display_info(self):
#         sidecar = "have" if self.has_sidecar else "dont have"
#         print(f"Moto: {self.brand}, speed: {self.speed} , sidecar: {sidecar}")


# class Truck(Vehicle):
#     def __init__(self, brand, speed, load_capacity):
#         super().__init__(brand, speed)
#         self.load_capacity = load_capacity

#     def display_info(self):
#         print(f"truck: {self.brand}, speed: {self.speed} km/t, how: {self.load_capacity} т")



# car = Car("Toyota", 180, 4)
# motorcycle = Motorcycle("Honda", 200, False)
# truck = Truck("Volvo", 120, 15)

# car.display_info()
# motorcycle.display_info()
# truck.display_info()

#  N9
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email


# class Admin(User):
#     def manage_users(self):
#         return f"{self.username} is managing users."


# class Teacher(User):
#     def teach(self):
#         return f"{self.username} is teaching a lesson."


# class Student(User):
#     def study(self):
#         return f"{self.username} is studying."


# admin = Admin("alex_admin", "alex@example.com")
# teacher = Teacher("sam_teacher", "sam@example.com")
# student = Student("jordan_student", "jordan@example.com")

# print(admin.manage_users())
# print(teacher.teach())
# print(student.study())

#------------------------------------- N10-----------------------------------------
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Electronics(Product):
#     def __init__(self, name, price, warranty_years):
#         super().__init__(name, price)
#         self.warranty_years = warranty_years


# class Clothing(Product):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self.size = size


# class Food(Product):
#     def __init__(self, name, price, expiration_date):
#         super().__init__(name, price)
#         self.expiration_date = expiration_date



# products = [
#     Electronics("Smartphone", 599.99, 2),
#     Clothing("T-shirt", 19.99, "M"),
#     Food("Chocolate", 1.99, "2026-12-31"),
# ]

# for product in products:
#     print(f"{product.name}: ${product.price}")

# --------------------------------------------N11------------------------------------------------------------------
# class Dog:
#     def make_sound(self):
#         return "Woof!"


# class Cat:
#     def make_sound(self):
#         return "Meow!"


# class Cow:
#     def make_sound(self):
#         return "Moo!"


# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     print(animal.make_sound())

# -----------------------------------------------------N12---------------------------------------------------------
# class CashPayment:
#     def pay(self, amount):
#         return f"Paid {amount} in cash."


# class CardPayment:
#     def pay(self, amount):
#         return f"Paid {amount} by card."


# class OnlinePayment:
#     def pay(self, amount):
#         return f"Paid {amount} online."


# def process_payment(payment, amount):
#     print(payment.pay(amount))


# payments = [CashPayment(), CardPayment(), OnlinePayment()]

# for payment in payments:
#     process_payment(payment, 100)
# -----------------------------------------------------N13-----------------------------------------
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# shapes = [
#     Circle(5),
#     Rectangle(4, 6),
#     Triangle(3, 8)
# ]

# for shape in shapes:
#     print(shape.area())
# ----------------------------------------------------------N14--------------------------------------------------------------------------
# class Car:
#     def move(self):
#         return "The car drives on the road."


# class Bicycle:
#     def move(self):
#         return "The bicycle rides on the road."


# class Airplane:
#     def move(self):
#         return "The airplane flies through the sky."


# def start_moving(transport):
#     print(transport.move())


# transports = [Car(), Bicycle(), Airplane()]

# for transport in transports:
#     start_moving(transport)
# # ----------------------------------------------N15-------------------------------------------
# class EmailNotification:
#     def send(self, message):
#         print(f"Email: {message}")


# class SMSNotification:
#     def send(self, message):
#         print(f"SMS: {message}")


# class PushNotification:
#     def send(self, message):
#         print(f"Push notification: {message}")


# def send_notification(notification, message):
#     notification.send(message)


# send_notification(EmailNotification(), "Your order has shipped.")
# send_notification(SMSNotification(), "Your order has shipped.")
# send_notification(PushNotification(), "Your order has shipped.")

# -------------------------------------------------------------------N16-----------------------------------------------------------------------
# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass


# class CardPayment(Payment):
#     def process_payment(self, amount):
#         return f"Card payment processed: {amount}"


# class CashPayment(Payment):
#     def process_payment(self, amount):
#         return f"Cash payment processed: {amount}"


# payments = [CardPayment(), CashPayment()]

# for payment in payments:
#     print(payment.process_payment(100))

# ---------------------------------------------------------------------------N17-------------------------------------------------------------------
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

#     def move(self):
#         return "The dog runs."


# class Bird(Animal):
#     def make_sound(self):
#         return "Tweet!"

#     def move(self):
#         return "The bird flies."


# class Fish(Animal):
#     def make_sound(self):
#         return "Blub!"

#     def move(self):
#         return "The fish swims."


# animals = [Dog(), Bird(), Fish()]

# for animal in animals:
#     print(animal.make_sound())
#     print(animal.move())

# ----------------------------------------------------------------------N18-------------------------------------------------------------------
#
# ------------------------------------------------------------------------------------N19-----------------------------------------------------------
# from abc import ABC, abstractmethod

# class Character(ABC):
#     @abstractmethod
#     def attack(self):
#         pass

#     @abstractmethod
#     def defend(self):
#         pass


# class Warrior(Character):
#     def attack(self):
#         return "Warrior attacks with a sword."

#     def defend(self):
#         return "Warrior blocks with a shield."


# class Mage(Character):
#     def attack(self):
#         return "Mage casts a fireball."

#     def defend(self):
#         return "Mage creates a magic barrier."


# class Archer(Character):
#     def attack(self):
#         return "Archer shoots an arrow."

#     def defend(self):
#         return "Archer dodges the attack."


# characters = [Warrior(), Mage(), Archer()]

# for character in characters:
#     print(character.attack())
#     print(character.defend())

# -----------------------------------------------------------------N20----------------------------------------------------------------------
from abc import ABC, abstractmethod
class Exporter:
    @abstractmethod
    def export(data):
        pass
    
class JSONExporter(Exporter):
    def __init__(self):
        super().__init__()
        
class CSVExporter(Exporter):
    def hello(self):
        super().__init__()
        return "Hello"
    
    
cs = CSVExporter()
print(cs.hello())

# -------------------------------------------------N21----------------------------------------

