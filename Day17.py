# class Student:
#     def __init__(self,grade):
#         self.__grade = grade
    
#     def getter(self):
#         return self.__grade
    
#     def setter(self,new_p):
#         if new_p<0 and new_p<=100:
#             return True
#         return False

# s = Student(30)
# s.getter()
# print(s.setter(100))
            
# ---------------------------------------Class work----------------------------
# ------------------------------------N1-------------------------
# class Book:
#     def __init__(self,tittle,pages):
#         self.__tittle = tittle
#         self.__pages = pages
    
#     def get_tittle(self):
#         return self.__tittle
    
#     def getter_pages(self):
#         return self.__pages
    
#     def setter(self,new_pages):
#         if new_pages > 0:
#             self.__pages = new_pages
#             return True
#         return False
        
         
# s = Book("Python",)
# print(s.get_tittle())
# print(s.getter_pages())
# print(s.get_tittle())
# print(s.getter_pages())

# -------------------------------------------N2--------------------------------
# class Dog:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
        
#     def get_name(self):
#         return self.__name
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,age1):
#         if age1 > 0 and age1 <= 30:
#             self.__age = age1
#             return self.__age
        
# s = Dog("Rex",12)
# print(s.set_age(13))
        
# -------------------------------------N3------------------------------
# class Rectangle:
#     def __init__(self,width,height):
#         self.__width = width
#         self.__height = height
        
#     def getter(self):
#         return self.__width and self.__height
    
#     def area(self):
#         return self.__height*self.__width

# s = Rectangle(12,14)

# print(s.area())    

# -----------------------N4-----------------------------
# class Counter:
#     def __init__(self):
#         self.__count = 0

#     def increment(self):
#         self.__count += 1

#     def decrement(self):
#         if self.__count > 0:
#             self.__count -= 1

#     def get_count(self):
#         return self.__count

# counter = Counter()

# counter.increment()
# counter.increment()
# print(counter.get_count())

# counter.decrement()
# print(counter.get_count())  

# counter.decrement()
# counter.decrement()
# print(counter.get_count())
# -------------------------N5------------------------------
# class Light:
#     def __init__(self):
#         self.__is_on = False

#     def turn_on(self):
#         self.__is_on = True

#     def turn_off(self):
#         self.__is_on = False

#     def is_on(self):
#         return self.__is_on


# light = Light()
# print(light.is_on())

# light.turn_on()
# print(light.is_on())

# light.turn_off()
# print(light.is_on())
# --------------------------------------N6---------------------------


# ----------------------N7-------------------------------
# class Wallet:
#     def __init__(self):
#         self.__money = 0

#     def add_money(self, amount):
#         if amount > 0:
#             self.__money += amount

#     def spend_money(self, amount):
#         if 0 < amount <= self.__money:
#             self.__money -= amount

#     def get_money(self):
#         return self.__money


# wallet = Wallet()
# wallet.add_money(100)
# wallet.spend_money(30)
# print(wallet.get_money())
# ----------------------------------------N8---------------------------------
# class Square:
#     def __init__(self, side):
#         if side <= 0:
#             raise ValueError("Tarafosh ziyod bosha")
#         self.__side = side

#     def get_side(self):
#         return self.__side

#     def set_side(self, side):
#         if side <= 0:
#             raise ValueError("Tarafosh ziyod bosha")
#         self.__side = side

#     def get_area(self):
#         return self.__side ** 2


# square = Square(5)
# print(square.get_side())
# print(square.get_area())

# square.set_side(3)
# print(square.get_area())

# --------------------------------N9--------------------------------------------
# class Phone:
#     def __init__(self):
#         self.__battery = 0

#     def charge(self, amount):
#         self.__battery = min(100, max(0, self.__battery + amount))

#     def use(self, amount):
#         self.__battery = min(100, max(0, self.__battery - amount))

#     def get_battery(self):
#         return self.__battery


# phone = Phone()
# phone.charge(70)
# print(phone.get_battery())

# phone.use(25)
# print(phone.get_battery())

# phone.charge(80)
# print(phone.get_battery())
# ---------------------------N10---------------------------------
# class User:
#     def __init__(self, password):
#         self.set_password(password)

#     def set_password(self, password):
#         if not isinstance(password, str) or len(password) < 6:
#             raise ValueError("Boyad ay 6 raqam ziyod bosha")
#         self.__password = password

#     def check_password(self, p):
#         return self.__password == p


# user = User("secret123")
# print(user.check_password("secret123"))
# print(user.check_password("wrong"))
# ------------------------N11---------------------------
# class Thermostat:
#     def __init__(self, target):
#         self.set_target(target)

#     def get_target(self):
#         return self.__target

#     def set_target(self, value):
#         if not 10 <= value <= 30:
#             raise ValueError("Temperatura ay 10 to 30 bosha")
#         self.__target = value


# thermostat = Thermostat(22)
# print(thermostat.get_target())

# thermostat.set_target(25)
# print(thermostat.get_target())

# # ------------------------N12-------------------------
# class Car:
#     def __init__(self,speed):
#         self.__speed = speed
        
#     def accelerate(self,speed):
#         if speed > 200: 
#             return "Stop"
#         return"Run"     
    
#     def brake(self,n):
#         if n > 0 and n <= 200:
#             self.__speed = n
#             return True
#         return False
    
# d = Car(150)
# print(d.accelerate(150))
# print(d.brake(150))

# -----------------------------------------N13-------------------------------
# class Employee:
#     def __init__(self, salary):
#         self.set_salary(salary)

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, salary):
#         if salary < 0:
#             raise ValueError("Pl nest")
#         self.__salary = salary

#     def raise_salary(self, percent):
#         if percent > 0:
#             self.__salary += self.__salary * percent / 100


# employee = Employee(500)
# print(employee.get_salary())

# employee.raise_salary(10)
# print(employee.get_salary())
# ------------------------------N14------------------------------
# class Triangle:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError("Tarafosh boyad soz bosha")

#         if a + b <= c or a + c <= b or b + c <= a:
#             raise ValueError("Nest inari chz")

#         self.__a = a
#         self.__b = b
#         self.__c = c

#     def perimeter(self):
#         return self.__a + self.__b + self.__c


# triangle = Triangle(3,4, 5)
# print(triangle.perimeter())
# --------------------------------N17---------------------
# class Library:
#     def __init__(self):
#         self.__books = []

#     def add_book(self, book):
#         self.__books.append(book)

#     def remove_book(self, book):
#         if book in self.__books:
#             self.__books.remove(book)

#     def get_books(self):
#         return self.__books.copy()


# library = Library()
# library.add_book("Tojikon")
# library.add_book("Odina")

# books = library.get_books()
# print(books)

# books.append("Yatim")
# print(books)
# print(library.get_books())
# ----------------------------N18---------------------
# class Time:
#     def __init__(self, hours, minutes):
#         self.set_hours(hours)
#         self.set_minutes(minutes)

#     def get_hours(self):
#         return self.__hours

#     def set_hours(self, hours):
#         if not isinstance(hours, int) or not 0 <= hours <= 23:
#             raise ValueError("Soat ay 0 to 23")
#         self.__hours = hours

#     def get_minutes(self):
#         return self.__minutes

#     def set_minutes(self, minutes):
#         if not isinstance(minutes, int) or not 0 <= minutes <= 59:
#             raise ValueError("Minut ay 0 to 59")
#         self.__minutes = minutes

#     def __str__(self):
#         return f"{self.__hours:02d}:{self.__minutes:02d}"


# time = Time(9, 5)
# print(time)
# ----------------------------N20------------------------

# ---------------------------------N21---------------------
# class Email:
#     def __init__(self, address):
#         self.set_address(address)

#     def get_address(self):
#         return self.__address

#     def set_address(self, address):
#         if not isinstance(address, str) or "@" not in address or "." not in address:
#             raise ValueError(" email Kor namekna")
#         self.__address = address

#     def get_domain(self):
#         return self.__address.split("@", 1)[1]


# email = Email("user@example.com")
# print(email.get_address())
# print(email.get_domain())

# email.set_address("name@site.org")
# print(email.get_address())
# print(email.get_domain())

# -----------------------------N25--------------------------
# class Shape:
#     def __init__(self,name):
#         raise ValueError("E hato nanavis")
    
# class Circle(Shape):
#     def area(self,radius):
#         return 3.14 * radius ** 2
    
# class Rectangle(Shape):
#     def area(self,width,height):
#         return width * height


# c = Circle("Circle: ")
# print(f'Circle: area = {c.area(3)}')

# r = Rectangle("Rectangle: ")
# print(f'Rectangle: area = {r.area(4,5)}')




