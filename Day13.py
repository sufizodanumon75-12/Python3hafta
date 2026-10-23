# class Employee:
#     def __init__(self,name,position,salary):
#         self.name=name
#         self.position==position
#         self.salary=salary
        
#     def info(self):
#         print(f'{self.name}---{self.position}----{self.salary}')
        
#     def add_salary(self,percent):
#         res=self.salary*percent//100
#         self.salary+=res
        
#         print(f'Now his salary is {self.salary}')
        
#     def new_position(self,p):
#         self.position=self.new_position
#         print(f'New position {self.position}')
        
    
# em1=Employee('Qobil',"CEO",215)

# em1.add_salary(50)
# em1.new_position("Bekor")
        
# class Company:
#     def __init__(self,name):
#         self.name=name
#         self.employe=[]
        
#     def add_employee(self,name):
#         self.employe.append(name)
        
#     def delete_name(self,name):
#         self.employe.remove(name)
        
#     def show_all(self):
#         print(f'Company name - {self.name}')
#         for i in self.employe:
#             print(f'{i} - employe')
    

# c1=Company("Babilon")

# c1.add_employee("Qobil")
# c1.add_employee("Alijon")
# c1.add_employee("Arsen")
# c1.add_employee("Yosin")

# c1.delete_name("Qobil")

# c1.show_all()

class Product:
    def __init__(self, name, category, price, rating, stock):
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating
        self.stock = stock

    def show_info(self):
        print(
            f"{self.name} | {self.category} | "
            f"{self.price} сом | Рейтинг: {self.rating} | "
            f"На складе: {self.stock}"
        )

    def change_price(self, new_price):
        self.price = new_price

    def add_stock(self, amount):
        self.stock += amount

    def remove_stock(self, amount):
        if amount <= self.stock:
            self.stock -= amount
        else:
            print("Недостаточно товара на складе")

    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            print("Рейтинг должен быть от 1 до 5")

    def is_available(self):
        return self.stock > 0

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100


class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
        self.purchases = []
        self.is_vip = False

    def add_balance(self, amount):
        self.balance += amount

    def can_buy(self, product):
        return self.balance >= product.price and product.is_available()

    def buy_product(self, product):
        if self.can_buy(product):
            self.balance -= product.price
            product.remove_stock(1)
            self.purchases.append(product.name)
            print(f"{self.name} купил(а) товар: {product.name}")
        else:
            print(f"{self.name} не может купить {product.name}")

    def show_purchases(self):
        print(f"Покупки {self.name}:")
        if self.purchases:
            for product_name in self.purchases:
                print(f"- {product_name}")
        else:
            print("Покупок пока нет")

    def become_vip(self):
        self.is_vip = True

    def total_spent(self):
        total = 0
        for product_name in self.purchases:
            
            pass
        return total


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []

    def add_product(self, product):
        self.products.append(product)

    def d_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} удалён из магазина")
                return
        print(f"{name} не найден")

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def show_all_products(self):
        print(f"Товары магазина {self.name}:")
        for product in self.products:
            product.show_info()

    def show_category(self, category):
        for product in self.products:
            if product.category == category:
                product.show_info()

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def sell_product(self, customer, product_name):
        product = self.find_product(product_name)

        if product is None:
            print("Такого товара нет в магазине")
        else:
            customer.buy_product(product)

    def show_out_of_stock(self):
        print("Товары, которых нет в наличии:")
        for product in self.products:
            if not product.is_available():
                product.show_info()

    def show_top_products(self):
        sorted_products = sorted(
            self.products,
            key=lambda product: product.rating,
            reverse=True
        )

        print("Топ-3 товара по рейтингу:")
        for product in sorted_products[:3]:
            product.show_info()



store = Store("Tajik.store")

p1 = Product("Телефон", "Электроника", 15000, 4.8, 5)
p2 = Product("Наушники", "Электроника", 2000, 4.5, 10)
p3 = Product("Книга Точикон", "Книги", 800, 4.9, 7)
p4 = Product("Клавиатура", "Электроника", 3000, 4.3, 4)
p5 = Product("Кружка", "Дом", 50, 4.1, 0)
p6 = Product("Книга Одина","Книги",200,5,12)
p7 = Product("Вилка набор","Дом",120,4.6,20)

store.add_product(p1)
store.add_product(p2)
store.add_product(p3)
store.add_product(p4)
store.add_product(p5)
store.add_product(p6)
store.add_product(p7)


c1 = Customer("Qobil", "qobil@gmail.com", 10000)
c2 = Customer("Alijon", "alijon@gmail.com", 5000)
c3 = Customer("Arsen", "arsen@gmail.com", 1000)
c4 = Customer("Numon","numon.12@gmail.com",100000)


store.add_customer(c1)
store.add_customer(c2)
store.add_customer(c3)
store.add_customer(c4)


store.sell_product(c1, "Наушники")
store.sell_product(c2, "Книга Точикон")
store.sell_product(c3, "Телефон")
store.sell_product(c4,"Книга Одина")


c3.add_balance(20000)


c1.become_vip()
c4.become_vip()

p1.apply_discount(10)
p2.apply_discount(5)
p6.apply_discount(6)

store.show_all_products()
store.show_out_of_stock()
store.show_top_products()

c1.show_purchases()
c2.show_purchases()
c3.show_purchases()
c4.show_purchases()