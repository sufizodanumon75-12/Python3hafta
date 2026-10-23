# class Children:
#     school = "School number 34"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"{self.name} -- {self.age} -- {self.school}")

#     @classmethod
#     def sc(cls):
#         print("School:", cls.school)
    
#     @staticmethod
#     def new():
        


    
# st=Children("Ali",18)
# st1=Children("Qobil",20)

# Children.sc()

# st.info()
# st1.info()


# class StudentManger:
#     def __init__(self):
#         self.next_id = 0
#         self.students = []

#     def create(self, name, age):
#         user = {
#             'id': self.next_id,
#             'name': name,
#             'age': age
#         }
#         self.students.append(user)
#         self.next_id += 1
#         return user

#     def show_students(self):
#         for student in self.students:
#             print(student)

#     def update(self, id, new_name):
#         for student in self.students:
#             if student['id'] == id:
#                 student['name'] = new_name
#                 return True

#         print('user not found')
#         return False

#     def delete(self, id):
#         for student in self.students:
#             if student['id'] == id:
#                 self.students.remove(student)
#                 return True

#         print('user not found')
#         return False


# st1 = StudentManger()
# st1.create('Sibghatullo', 18)
# st1.create('Arsen', 15)
# st1.create('Abduvvahob', 17)

# st1.delete(2)
# st1.show_students()

# st1.update(2, 'Qobil')
# st1.show_students()

# ---------------------Biblioteka---------------------------------------

class Book:
    count = 0

    def __init__(self, title, author, year):
        Book.count += 1
        self.id = Book.count
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(';')
        return cls(title, author, int(year))

    @staticmethod
    def is_valid_year(year):
        return 1450 <= year <= 2026

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __str__(self):
        return f"#{self.id} '{self.title}' by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not Book.is_valid_year(book.year):
            print('Error: invalid year')
            return False
        if book in self.books:
            print('Error: book already exists')
            return False
        self.books.append(book)
        return True

    def find_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def update_year(self, book_id, new_year):
        if not Book.is_valid_year(new_year):
            print('Error: invalid year')
            return False
        for book in self.books:
            if book.id == book_id:
                book.year = new_year
                return True
        return False

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


lib = Library()
lib.add_book(Book("1984", "George Orwell", 1949))
lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
lib.add_book(Book("Dune", "Frank Herbert", 1965))
lib.add_book(Book("1984", "George Orwell", 1950))  
lib.add_book(Book("Future Book", "Unknown", 3000)) 
lib.add_book(Book("Одина","Садриддин Айни" ,2018))

print(len(lib))
print(lib[0])

for b in lib.find_by_author("George Orwell"):
    print(b)

lib.update_year(3, 1966)
print(lib[2])

lib.remove_book(1)
print(len(lib))
print(Book.count)


# -------------------------------------Magazin---------------------------------------------------


class Product:
    def __init__(self, name, price, quantity):
        if not Product.is_valid_price(price):
            raise ValueError("Price must be positive")
        self.name=name
        self.price=price
        self.quantity=quantity

    @staticmethod
    def is_valid_price(price):
        return price > 0

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["quantity"])

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.price} TJS x {self.quantity}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    def get_product(self, name):
        return self.products.get(name)

    def __getitem__(self, name):
        return self.products[name]

    def update_price(self, name, new_price):
        if not Product.is_valid_price(new_price):
            raise ValueError("Price must be positive")
        product = self.get_product(name)
        if product is None:
            return False
        product.price = new_price
        return True

    def apply_discount(self, percent):
        for product in self.products.values():
            product.price = round(product.price * (1 - percent / 100), 2)

    def delete_product(self, name):
        if name not in self.products:
            return False
        del self.products[name]
        return True

    def total_value(self):
        return sum(product.total_value() for product in self.products.values())

    def __len__(self):
        return len(self.products)

    def __add__(self, other):
        new_store = Store(f"{self.name} + {other.name}")

        for product in self.products.values():
            new_store.add_product(
                Product(product.name, product.price, product.quantity)
            )

        for product in other.products.values():
            new_store.add_product(
                Product(product.name, product.price, product.quantity)
            )

        return new_store

    def __str__(self):
        return (
            f"Store '{self.name}': {len(self)} products, "
            f"total {self.total_value()} TJS"
        )


a = Store("Dushanbe")
a.add_product(Product("Laptop", 5000, 2))
a.add_product(Product.from_dict({
    "name": "Mouse",
    "price": 100,
    "quantity": 10
}))
a.add_product(Product("Mouse", 100, 5))

print(a)
print(a["Mouse"])
print(repr(a["Laptop"]))

a.update_price("Laptop", 4500)
a.apply_discount(10)
print(a["Laptop"])
print(a["Mouse"])

b = Store("Khujand")
b.add_product(Product("Keyboard", 250, 4))
b.add_product(Product("Mouse", 90, 3))

c = a + b
print(c)
print(c.delete_product("Keyboard"))
print(len(c))

