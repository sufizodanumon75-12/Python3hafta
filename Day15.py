# ----------------------------------------------------  Polymorphism --------------------------------------------------
# class Cat:
#     def cat(self):
#         print("This is a cat")
    
# class Dog(Cat):
#     def cat(self):
#         print("This a Dog")
        

# c=Cat()
# c.cat()


# d=Dog()
# d.cat()

# ------------------------------------------------Class Work-------------------------------------------
# 
# N1
# 
# class Vehicle():
#     def move(self):
#         print("Транспорт движется")
        
# class Car(Vehicle):
#     def honk(self):
#         print("Bi-Bi!")
        
# d=Vehicle()
# d.move()

# d=Car()
# d.honk()

# N2
# class Employee():
#     def work(self):
#         print("Сотрудник работает")

# class Programmer:
#     def work(self):
#         print("Работает")

# class Teacher:
#     def work(self):
#         print("Проводит урок")


# d=Employee()
# d.work()

# c=Programmer()
# c.work()

# s=Teacher()
# s.work()
# N3
# class Person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
        
# class Student(Person):
#     def __init__(self,name, age,group):
#         super().__init__(name, age)
#         self.group=group
        
#     def info(self):
#         print(f'{self.name} -- {self.age} -- {self.group}')
        
# a=Student("Qobil",15,6)
# a.info()
# N4
# class Animal:
#     def speak(self):
#         print("Животное издаёт звук")
    
# class Cat(Animal):
#     def speak(self):
#         print("Myau")
        
# d=Animal()
# d.speak()

# c=Cat()
# c.speak()

# N5
# class Device:
#     def  power_on(self):
#         print("Device is on")
        
# class Phone(Device):
#    def  call(self,number):
#     print(f"Calling number ...{number}")
    
# class Smartphone(Phone):
#     def take_photo(self):
#         print("Photo taken")
        
# phone=Smartphone()
# phone.power_on()
# phone.call(1234456)
# phone.take_photo()
        
# N6
# class Flyer:
#     def fly(self):
#         pass
    
# class Swimmer:
#     def  swim(self):
#         pass
    
# class Duck(Flyer,Swimmer):
#     def quack(self):
#         pass
    
# print(Duck.__mro__)
#  N7
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         return f"Name: {self.name}, Email: {self.email}"


# class Admin(User):
#     def __init__(self, name, email, level):
#         super().__init__(name, email)
#         self.level = level

#     def get_info(self):
#         return f"{super().get_info()}, Level: {self.level}"


# class Customer(User):
#     def __init__(self, name, email, balance):
#         super().__init__(name, email)
#         self.balance = balance

#     def get_info(self):
#         return f"{super().get_info()}, Balance: {self.balance}"


# class Guest(User):
#     def get_info(self):
#         return super().get_info()


# print(Admin("Ali", "ali@mail.tj", 3).get_info())
# N8
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Rectangle:
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.width * self.height

# class Triangle:
#     def __init__(self, base, height):
#         self.base=base
#         self.height=height

#     def area(self):
#         return self.base * self.height // 2

# shapes=[Circle(3), Rectangle(4, 5), Triangle(6, 2)]
# for shape in shapes:
#     print(type(shape).__name__, shape.area())
    
# N9
# class Calculator:
#     def multiply(self, a, b=1, c=1):
#         return a * b * c

# calc=Calculator()
# print(calc.multiply(5))
# print(calc.multiply(5, 2))
# print(calc.multiply(5, 2, 3))

# NEW=1
# PAID=2
# SHIPPED=3
# DELIVERED=4

# def next_status(status):
#     if status < DELIVERED:
#         return status + 1
#     return status

# result=next_status(NEW)
# print(result)
# N10
# class PaymentStatus:
#     SUCCESS="SUCCESS"
#     FAILED="FAILED"

# class Payment:
#     def __init__(self, owner):
#         self.owner=owner

#     def pay(self, amount):
#         print("Unknown payment method")
#         return PaymentStatus.FAILED

# class CardPayment(Payment):
#     def __init__(self, owner, card_number):
#         super().__init__(owner)
#         self.card_number=card_number

#     def pay(self, amount):
#         if amount<=0:
#             return PaymentStatus.FAILED
#         print(f"{self.owner} paid {amount} somoni by card ****{self.card_number[-4:]}")
#         return PaymentStatus.SUCCESS

# class CashPayment(Payment):
#     def pay(self, amount):
#         if amount<=0:
#             return PaymentStatus.FAILED
#         print(f"{self.owner} paid {amount} somoni in cash")
#         return PaymentStatus.SUCCESS

# class WalletPayment(Payment):
#     def __init__(self, owner, balance):
#         super().__init__(owner)
#         self.balance=balance

#     def pay(self, amount):
#         if amount<=0:
#             return PaymentStatus.FAILED
#         if amount>self.balance:
#             print(f"{self.owner}: not enough money in the wallet")
#             return PaymentStatus.FAILED
#         self.balance-=amount
#         print(f"{self.owner} paid {amount} somoni from the wallet")
#         return PaymentStatus.SUCCESS

# payments=[
#     (CardPayment("Ali", "1234567812344321"), 200),
#     (CashPayment("Vali"), 150),
#     (WalletPayment("Sino", 100), 200)
# ]

# for payment, amount in payments:
#     status=payment.pay(amount)
#     print("->", status)