# N1
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self,amount):
#         self.balance += amount
        
#     def withdraw(self,amount):
#         if amount < 0:
#             return "Sum just +"
#         if amount > self.balance:
#             return "No money"
        
        
#         self.balance -= amount
#         return self.balance
    
# acount = BankAccount("Ali",1000)
# acount.withdraw(25)
# print(acount.balance)


# N2

# from   math import pi
# class Shape:
#     def __init__(self,):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.height = height
#         self.width = width
        
#     def area(self):
#         return self.width * self.height
    
# class Circle(Shape):
#     def __init__(self,radius):
#         if radius <= 0:
#             raise ValueError("Радиус должен быть положительным")

#         self.radius = radius
        
#     def area(self):
#         return pi * self.radius ** 2
    
# r = Rectangle(12,14)
# print(r.area())
# c = Circle(5)
# print(c.area())

# N3/

# class Product:
#     def __init__(self,name,category,price,rating,stock):
#         self.name = name
#         self.category = category
#         self.price = price
#         self.rating = rating
#         self.stock = stock
        
#     def info(self):
#         print(f'{self.name} -- {self.category} -- {self.price} -- {self.rating} -- {self.stock}')
        
#     def change_price(self, new_price):
#         if new_price < 0:
#             print("Цена не может быть отрицательной")
#             return
#         self.price = new_price
        
#     def add_stock(self, amount):
#         if amount <= 0:
#             print("Количество для добавления должно быть больше нуля")
#             return
#         self.stock += amount
        
#     def remove_stock(self, amount):
#         if amount <= 0:
#             print("Количество для списания должно быть больше нуля")
#             return

#         if amount > self.stock:
#             print("На складе недостаточно товара")
#             return

#         self.stock -= amount
        
#     def set_rating(self, rating):
#         if rating < 1 or rating > 5:
#             print("Рейтинг должен быть от 1 до 5")
#             return

#         self.rating = rating

#     def is_available(self):
#         return self.stock > 0

#     def apply_discount(self, percent):
#         if percent < 0 or percent > 100:
#             print("Скидка должна быть от 0 до 100 процентов")
#             return

#         self.price = self.price * (1 - percent / 100)


# class Customer:
#     def __init__(self, name, email, balance=0):
#         self.name = name
#         self.email = email
#         self.balance = balance
#         self.purchased_products = []
#         self.is_vip = False
#         self.total_spent = 0

#     def add_balance(self, amount):
#         if amount <= 0:
#             print("Сумма пополнения должна быть больше нуля")
#             return

#         self.balance += amount
        
#     def can_afford(self, product):
#         return self.balance >= product.price

#     def buy_product(self, product):
#         if not product.is_available():
#             print(f"Товара «{product.name}» нет в наличии")
#             return False

#         if not self.can_afford(product):
#             print("Недостаточно денег")
#             return False

#         product.remove_stock(1)
#         self.balance -= product.price
#         self.purchased_products.append(product)
#         self.total_spent += product.price

#         print(f"{self.name} купил(а) товар «{product.name}»")
#         return True  



    
        
# phone=Product("Iphon","Electro",500,4.8,3)
# phone.info()
# phone.change_price(450)
# phone.add_stock(2)
# phone.remove_stock(1)
# phone.set_rating(5)
# phone.apply_discount(10)
# print(phone.is_available())
# phone.info()

# customer = Customer("Аня", "anya@mail.com", 100)
# customer.add_balance(50)

# print(customer.balance) 
# customer.buy_product(phone)

# print("Баланс:", customer.balance)
# print("Осталось на складе:", phone.stock)



    

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Store:
#     def __init__(self):
#         self.products = []

#     # Create: добавить товар
#     def add_product(self, product):
#         self.products.append(product)

#     # Read: показать товары
#     def show_products(self):
#         for product in self.products:
#             print(product.name, product.price)

#     # Update: изменить цену товара
#     def change_price(self, name, new_price):
#         for product in self.products:
#             if product.name == name:
#                 product.price = new_price
#                 return
#         print("Товар не найден")

#     # Delete: удалить товар по названию
#     def remove_product(self, name):
#         for product in self.products:
#             if product.name == name:
#                 self.products.remove(product)
#                 return
#         print("Товар не найден")
        
# store = Store()

# phon = Product("Phone",600)
# phone = Product("Телефон", 500)
# store.add_product(phone)   
# store.add_product(phon)# Create

# store.show_products()  # Read
# store.show_products()


# store.change_price("Телефон", 450)  # Update
# store.show_products()

# store.remove_product("Телефон")     # Delete
# store.show_products()


# class Book:
#     def __init__(self,id,title,year,price):
#         self.id=int(id)
#         self.title=title
#         self.year=year
#         self.price=price

#     def __str__(self):
#         return f'''
#     ID: {self.id}
#     TITLE: {self.title}
#     YEAR: {self.year}
#     PRICE: {self.price}'''


# class BookManager:
#     def __init__(self):
#         self.next_id=1 
#         self.books=[]
    
#     def create(self,title,year,price):
#         b=Book(self.next_id,title,year,price)
#         self.books.append(b)
#         self.next_id+=1
        
#     def show_all(self):
#         for i in self.books:
#             print(i)
            
#     def get_by_id(self):
#         for b in self.books:
#             if b.id==id:
#                 print(b)
                
#     def update(self,id,new_title,new_year,new_prise):
#         for b in self.books:
#             if b.id==id:
#                 b.title=new_title
#                 b.year=new_year
#                 b.prise=new_prise

#     def  delete(self,id):
#         for b in self.books:
#             if b.id==id:
#                 self.books.remove(b)

# bm=BookManager()

# while True:
#     print('''
#     1.Create book
#     2.Show all books
#     3.Show onae book by id
#     4.Update book
#     5.Delete book
#     6.Exit''')

#     rakam=int(input("Rakamro vorid kuned"))

#     if rakam==1:
#         title=input("Nomi kitoba navis: ")
#         year = int(input("Soli kitoba navis: "))
#         price = int(input("Narxi kitoba navis: "))
#         bm.update(title,year,price)
    
#     if rakam==2:
#         bm.show_all()
        
#     if rakam==3:
#         id=int(input(""))
#         bm.get_by_id(id)
        
#     if rakam==4:
#         id=int(input())
#         new_title=str(input())
#         new_year=int(input())
#         new_price=int(input())
#         bm.update(id,new_title,new_year,new_price)
    
#     if rakam == 5:
#         book_id = int(input("Enter book ID: "))
#         bm.delete(book_id),   

#     if rakam == 6:
#         print("Program ended.")
#         break

# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))
# print(calendar.month(year, month))


from datetime import datetime,date,time,timedelta

class Note:
    next_id =1
    def __init__(self,title,discription):
        self.id = self.next_id
        self.title = title
        self.discription = discription
        self.created_at = datetime.now()
        
        Note.next_id += 1
    
    def __str__(self):
        return self.title
    
    
    
class NoteManager:

    def __init__(self):
        self.notes_list = []

    def create_note(self, title, description) :
        note = Note(title, description)
        self.notes_list.append (note)
        
    def show_all(self):
        for note in self.notes_list:
            print (note)

    def update_note(self, id, title, description):
        for note in self.notes_list:
            if note.id == id:
                note.title = title
        note.description = description
        print('Note updated!')
        return
    
    print('Note with this ID not founded!')

    def delete_note(self, id):
        for note in self.notes_list:
            if note.id == id:
                self.notes_list. remove(note)
        print('Note deleted!')
        return
    print('Note with this ID not founded!')
    
    def count_note(self):
        print(f"Количество заметок: {len(self.notes_list)}")
        
        
    def search_by_title(self, title_keyword):
        found = False
        for note in self.notes_list:
            if title_keyword.lower() in note.title.lower():
                print(f"ID: {note.id} | Title: {note.title} | Description: {note.description}")
                found = True
        if not found:
            print('Note with this title not founded!')

manager = NoteManager()

while True:
    print('''
    1. Create note
    2. Show all
    ''')
    c = int(input('Select one:'))

    if c == 1:
        title = input('Enter note title: ')
        description = input('Enter note description: ')
        manager.create_note(title, description)
        print (manager.notes_list)
    
    elif c == 2:
        manager. show_all()
    elif c == 3:
        id = int(input('Enter note ID to update: '))
        title = input('Enter note title: ')
        description = input('Enter note description:')
        manager.update_note(id, title, description)
    elif c == 4:
        id = int(input('Enter note ID to update: '))
        manager.delete_note(id)
        
    elif c == 5:
        title_keyword = input('Enter title to search: ')
        manager.search_by_title(title_keyword)
        
    elif c== 5:
        break
        