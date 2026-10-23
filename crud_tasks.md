# CRUD Tasks — Attributes and Methods (Python, Lecture 11)

**Languages / Языки / Забонҳо:** [Русский](#русский) · [English](#english) · [Тоҷикӣ](#тоҷикӣ)

---

## Русский

### Что такое CRUD?

**CRUD** — это четыре основные операции с данными:

| Буква | Операция | Что делает |
|---|---|---|
| **C** | Create | Создать / добавить |
| **R** | Read | Прочитать / найти |
| **U** | Update | Изменить |
| **D** | Delete | Удалить |

В каждой задаче нужно написать классы, затем запустить код из блока «Проверка» и сравнить результат с «Ожидаемым выводом».

---

### Задача 1 — Студенты (лёгкая)

**Темы:** атрибуты экземпляра, атрибут класса, методы экземпляра, `__str__`, `__len__`.

**Класс `Student`:**
- атрибут класса `school = "Softclub"`;
- атрибуты экземпляра: `id`, `name`, `age`;
- `__str__` возвращает строку вида `[1] Ali, 20 years, Softclub`.

**Класс `StudentManager`:**
- атрибуты: `students` (пустой список) и `next_id` (начинается с 1);
- **C:** `add_student(name, age)` создаёт студента с автоматическим `id`, добавляет его в список и возвращает;
- **R:** `get_all()` возвращает всех студентов; `get_by_id(student_id)` возвращает студента или `None`;
- **U:** `update_student(student_id, name=None, age=None)` меняет только переданные поля; возвращает `True` или `False`, если студент не найден;
- **D:** `delete_student(student_id)` возвращает `True` или `False`;
- `__len__` возвращает количество студентов.

**Проверка:**

```python
m = StudentManager()
m.add_student("Ali", 20)
m.add_student("Sara", 19)
m.add_student("John", 22)

for s in m.get_all():
    print(s)

print(m.get_by_id(2))
m.update_student(2, age=20)
print(m.get_by_id(2))

print(m.delete_student(1))
print(m.delete_student(10))
print(len(m))
```

**Ожидаемый вывод:**

```
[1] Ali, 20 years, Softclub
[2] Sara, 19 years, Softclub
[3] John, 22 years, Softclub
[2] Sara, 19 years, Softclub
[2] Sara, 20 years, Softclub
True
False
2
```

---

### Задача 2 — Библиотека (средняя)

**Темы:** счётчик в атрибуте класса, `@classmethod`, `@staticmethod`, `__eq__`, `__getitem__`.

**Класс `Book`:**
- атрибут класса `count = 0`; при создании каждой книги он увеличивается на 1, а новое значение становится `id` книги;
- атрибуты экземпляра: `id`, `title`, `author`, `year`;
- `@classmethod from_string(cls, text)` создаёт книгу из строки `"Title;Author;Year"`;
- `@staticmethod is_valid_year(year)` возвращает `True`, если `1450 <= year <= 2026`;
- `__eq__`: две книги равны, если у них одинаковые `title` и `author`;
- `__str__` возвращает `#1 '1984' by George Orwell (1949)`.

**Класс `Library`:**
- **C:** `add_book(book)`:
  - если год неверный, печатает `Error: invalid year` и возвращает `False`;
  - если такая книга уже есть (используй `==`), печатает `Error: book already exists` и возвращает `False`;
- **R:** `find_by_author(author)` возвращает список книг автора;
- **U:** `update_year(book_id, new_year)` меняет год (с проверкой);
- **D:** `remove_book(book_id)`;
- `__len__` и `__getitem__(index)`, чтобы работало `lib[0]`.

**Проверка:**

```python
lib = Library()
lib.add_book(Book("1984", "George Orwell", 1949))
lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
lib.add_book(Book("Dune", "Frank Herbert", 1965))
lib.add_book(Book("1984", "George Orwell", 1950))   # дубликат
lib.add_book(Book("Future Book", "Unknown", 3000))  # неверный год

print(len(lib))
print(lib[0])

for b in lib.find_by_author("George Orwell"):
    print(b)

lib.update_year(3, 1966)
print(lib[2])

lib.remove_book(1)
print(len(lib))
print(Book.count)
```

**Ожидаемый вывод:**

```
Error: book already exists
Error: invalid year
3
#1 '1984' by George Orwell (1949)
#1 '1984' by George Orwell (1949)
#2 'Animal Farm' by George Orwell (1945)
#3 'Dune' by Frank Herbert (1966)
2
5
```

> 💡 Почему `Book.count` равен 5, а не 3? Счётчик считает **все созданные** объекты `Book`, даже те, которые библиотека не приняла.

---

### Задача 3 — Магазин (сложная)

**Темы:** всё вместе: `@classmethod`, `@staticmethod`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__add__`, исключения.

**Класс `Product`:**
- атрибуты: `name`, `price`, `quantity`;
- `@staticmethod is_valid_price(price)` возвращает `True`, если `price > 0`;
- в `__init__`: если цена неверная, выбросить `ValueError("Price must be positive")`;
- `@classmethod from_dict(cls, data)` создаёт товар из словаря `{"name": ..., "price": ..., "quantity": ...}`;
- `total_value()` возвращает `price * quantity`;
- `__str__` возвращает `Laptop: 5000 TJS x 2`;
- `__repr__` возвращает `Product('Laptop', 5000, 2)`.

**Класс `Store`:**
- атрибуты: `name`, `products` (словарь `{название: Product}`);
- **C:** `add_product(product)`: если товар с таким названием уже есть, **прибавить** количество, иначе добавить;
- **R:** `get_product(name)` возвращает товар или `None`; `__getitem__(name)`, чтобы работало `store["Mouse"]`;
- **U:** `update_price(name, new_price)` (с проверкой цены); `apply_discount(percent)` уменьшает цену всех товаров на `percent`% (округлить до 2 знаков: `round(..., 2)`);
- **D:** `delete_product(name)` возвращает `True` или `False`;
- `total_value()` возвращает сумму стоимости всех товаров;
- `__len__` возвращает количество разных товаров;
- `__add__(other)` возвращает **новый** магазин с названием `"A + B"`, где собраны товары обоих магазинов (одинаковые товары объединяются). Исходные магазины не должны измениться;
- `__str__` возвращает `Store 'Dushanbe': 2 products, total 11500 TJS`.

**Проверка:**

```python
a = Store("Dushanbe")
a.add_product(Product("Laptop", 5000, 2))
a.add_product(Product.from_dict({"name": "Mouse", "price": 100, "quantity": 10}))
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

try:
    Product("Broken", -5, 1)
except ValueError as e:
    print("Error:", e)
```

**Ожидаемый вывод:**

```
Store 'Dushanbe': 2 products, total 11500 TJS
Mouse: 100 TJS x 15
Product('Laptop', 5000, 2)
Laptop: 4050.0 TJS x 2
Mouse: 90.0 TJS x 15
Store 'Dushanbe + Khujand': 3 products, total 10720.0 TJS
True
2
Error: Price must be positive
```

> 💡 Подсказка для `__add__`: создавай **копии** товаров (`Product(p.name, p.price, p.quantity)`), иначе при объединении изменится количество в исходном магазине.

---

## English

### What is CRUD?

**CRUD** stands for the four basic operations on data:

| Letter | Operation | What it does |
|---|---|---|
| **C** | Create | Add something new |
| **R** | Read | Get / find |
| **U** | Update | Change |
| **D** | Delete | Remove |

For each task, write the classes, then run the code from the "Test" block and compare your result with the "Expected output".

---

### Task 1 — Students (easy)

**Topics:** instance attributes, class attribute, instance methods, `__str__`, `__len__`.

**Class `Student`:**
- class attribute `school = "Softclub"`;
- instance attributes: `id`, `name`, `age`;
- `__str__` returns a string like `[1] Ali, 20 years, Softclub`.

**Class `StudentManager`:**
- attributes: `students` (empty list) and `next_id` (starts at 1);
- **C:** `add_student(name, age)` creates a student with an automatic `id`, adds it to the list and returns it;
- **R:** `get_all()` returns all students; `get_by_id(student_id)` returns the student or `None`;
- **U:** `update_student(student_id, name=None, age=None)` changes only the fields that were passed; returns `True`, or `False` if the student is not found;
- **D:** `delete_student(student_id)` returns `True` or `False`;
- `__len__` returns the number of students.

**Test:**

```python
m = StudentManager()
m.add_student("Ali", 20)
m.add_student("Sara", 19)
m.add_student("John", 22)

for s in m.get_all():
    print(s)

print(m.get_by_id(2))
m.update_student(2, age=20)
print(m.get_by_id(2))

print(m.delete_student(1))
print(m.delete_student(10))
print(len(m))
```

**Expected output:**

```
[1] Ali, 20 years, Softclub
[2] Sara, 19 years, Softclub
[3] John, 22 years, Softclub
[2] Sara, 19 years, Softclub
[2] Sara, 20 years, Softclub
True
False
2
```

---

### Task 2 — Library (medium)

**Topics:** counter in a class attribute, `@classmethod`, `@staticmethod`, `__eq__`, `__getitem__`.

**Class `Book`:**
- class attribute `count = 0`; every new book increases it by 1, and the new value becomes the book's `id`;
- instance attributes: `id`, `title`, `author`, `year`;
- `@classmethod from_string(cls, text)` creates a book from a string `"Title;Author;Year"`;
- `@staticmethod is_valid_year(year)` returns `True` if `1450 <= year <= 2026`;
- `__eq__`: two books are equal if they have the same `title` and `author`;
- `__str__` returns `#1 '1984' by George Orwell (1949)`.

**Class `Library`:**
- **C:** `add_book(book)`:
  - if the year is invalid, prints `Error: invalid year` and returns `False`;
  - if the same book already exists (use `==`), prints `Error: book already exists` and returns `False`;
- **R:** `find_by_author(author)` returns a list of the author's books;
- **U:** `update_year(book_id, new_year)` changes the year (with validation);
- **D:** `remove_book(book_id)`;
- `__len__` and `__getitem__(index)` so that `lib[0]` works.

**Test:**

```python
lib = Library()
lib.add_book(Book("1984", "George Orwell", 1949))
lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
lib.add_book(Book("Dune", "Frank Herbert", 1965))
lib.add_book(Book("1984", "George Orwell", 1950))   # duplicate
lib.add_book(Book("Future Book", "Unknown", 3000))  # invalid year

print(len(lib))
print(lib[0])

for b in lib.find_by_author("George Orwell"):
    print(b)

lib.update_year(3, 1966)
print(lib[2])

lib.remove_book(1)
print(len(lib))
print(Book.count)
```

**Expected output:**

```
Error: book already exists
Error: invalid year
3
#1 '1984' by George Orwell (1949)
#1 '1984' by George Orwell (1949)
#2 'Animal Farm' by George Orwell (1945)
#3 'Dune' by Frank Herbert (1966)
2
5
```

> 💡 Why is `Book.count` 5 and not 3? The counter counts **every** `Book` object created, even the ones the library rejected.

---

### Task 3 — Store (hard)

**Topics:** everything together: `@classmethod`, `@staticmethod`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__add__`, exceptions.

**Class `Product`:**
- attributes: `name`, `price`, `quantity`;
- `@staticmethod is_valid_price(price)` returns `True` if `price > 0`;
- in `__init__`: if the price is invalid, raise `ValueError("Price must be positive")`;
- `@classmethod from_dict(cls, data)` creates a product from a dict `{"name": ..., "price": ..., "quantity": ...}`;
- `total_value()` returns `price * quantity`;
- `__str__` returns `Laptop: 5000 TJS x 2`;
- `__repr__` returns `Product('Laptop', 5000, 2)`.

**Class `Store`:**
- attributes: `name`, `products` (a dict `{name: Product}`);
- **C:** `add_product(product)`: if a product with the same name exists, **add** to its quantity; otherwise add the product;
- **R:** `get_product(name)` returns the product or `None`; `__getitem__(name)` so that `store["Mouse"]` works;
- **U:** `update_price(name, new_price)` (with price validation); `apply_discount(percent)` lowers the price of every product by `percent`% (round to 2 digits: `round(..., 2)`);
- **D:** `delete_product(name)` returns `True` or `False`;
- `total_value()` returns the total value of all products;
- `__len__` returns the number of different products;
- `__add__(other)` returns a **new** store named `"A + B"` with the products of both stores (same products are merged). The original stores must not change;
- `__str__` returns `Store 'Dushanbe': 2 products, total 11500 TJS`.

**Test:**

```python
a = Store("Dushanbe")
a.add_product(Product("Laptop", 5000, 2))
a.add_product(Product.from_dict({"name": "Mouse", "price": 100, "quantity": 10}))
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

try:
    Product("Broken", -5, 1)
except ValueError as e:
    print("Error:", e)
```

**Expected output:**

```
Store 'Dushanbe': 2 products, total 11500 TJS
Mouse: 100 TJS x 15
Product('Laptop', 5000, 2)
Laptop: 4050.0 TJS x 2
Mouse: 90.0 TJS x 15
Store 'Dushanbe + Khujand': 3 products, total 10720.0 TJS
True
2
Error: Price must be positive
```

> 💡 Hint for `__add__`: create **copies** of the products (`Product(p.name, p.price, p.quantity)`), otherwise merging will change the quantity in the original store.

---

## Тоҷикӣ

### CRUD чист?

**CRUD** — ин чор амали асосӣ бо маълумот аст:

| Ҳарф | Амал | Чӣ кор мекунад |
|---|---|---|
| **C** | Create | Сохтан / илова кардан |
| **R** | Read | Хондан / ёфтан |
| **U** | Update | Тағйир додан |
| **D** | Delete | Нест кардан |

Дар ҳар як масъала классҳоро нависед, баъд коди блоки «Санҷиш»-ро иҷро кунед ва натиҷаро бо «Натиҷаи интизорӣ» муқоиса намоед.

---

### Масъалаи 1 — Донишҷӯён (осон)

**Мавзӯъҳо:** атрибутҳои объект, атрибути класс, методҳои объект, `__str__`, `__len__`.

**Класси `Student`:**
- атрибути класс `school = "Softclub"`;
- атрибутҳои объект: `id`, `name`, `age`;
- `__str__` сатри зеринро бармегардонад: `[1] Ali, 20 years, Softclub`.

**Класси `StudentManager`:**
- атрибутҳо: `students` (рӯйхати холӣ) ва `next_id` (аз 1 сар мешавад);
- **C:** `add_student(name, age)` донишҷӯро бо `id`-и худкор месозад, ба рӯйхат илова мекунад ва онро бармегардонад;
- **R:** `get_all()` ҳамаи донишҷӯёнро бармегардонад; `get_by_id(student_id)` донишҷӯ ё `None`-ро бармегардонад;
- **U:** `update_student(student_id, name=None, age=None)` танҳо майдонҳои додашударо иваз мекунад; `True` ё, агар донишҷӯ ёфт нашавад, `False` бармегардонад;
- **D:** `delete_student(student_id)` `True` ё `False` бармегардонад;
- `__len__` шумораи донишҷӯёнро бармегардонад.

**Санҷиш:**

```python
m = StudentManager()
m.add_student("Ali", 20)
m.add_student("Sara", 19)
m.add_student("John", 22)

for s in m.get_all():
    print(s)

print(m.get_by_id(2))
m.update_student(2, age=20)
print(m.get_by_id(2))

print(m.delete_student(1))
print(m.delete_student(10))
print(len(m))
```

**Натиҷаи интизорӣ:**

```
[1] Ali, 20 years, Softclub
[2] Sara, 19 years, Softclub
[3] John, 22 years, Softclub
[2] Sara, 19 years, Softclub
[2] Sara, 20 years, Softclub
True
False
2
```

---

### Масъалаи 2 — Китобхона (миёна)

**Мавзӯъҳо:** ҳисобкунак дар атрибути класс, `@classmethod`, `@staticmethod`, `__eq__`, `__getitem__`.

**Класси `Book`:**
- атрибути класс `count = 0`; ҳангоми сохтани ҳар китоб он 1 зиёд мешавад ва қимати нав `id`-и китоб мегардад;
- атрибутҳои объект: `id`, `title`, `author`, `year`;
- `@classmethod from_string(cls, text)` китобро аз сатри `"Title;Author;Year"` месозад;
- `@staticmethod is_valid_year(year)` агар `1450 <= year <= 2026` бошад, `True` бармегардонад;
- `__eq__`: ду китоб баробаранд, агар `title` ва `author`-и онҳо якхела бошанд;
- `__str__` бармегардонад: `#1 '1984' by George Orwell (1949)`.

**Класси `Library`:**
- **C:** `add_book(book)`:
  - агар сол нодуруст бошад, `Error: invalid year` чоп мекунад ва `False` бармегардонад;
  - агар чунин китоб аллакай бошад (`==`-ро истифода баред), `Error: book already exists` чоп мекунад ва `False` бармегардонад;
- **R:** `find_by_author(author)` рӯйхати китобҳои муаллифро бармегардонад;
- **U:** `update_year(book_id, new_year)` солро иваз мекунад (бо санҷиш);
- **D:** `remove_book(book_id)`;
- `__len__` ва `__getitem__(index)`, то ки `lib[0]` кор кунад.

**Санҷиш:**

```python
lib = Library()
lib.add_book(Book("1984", "George Orwell", 1949))
lib.add_book(Book.from_string("Animal Farm;George Orwell;1945"))
lib.add_book(Book("Dune", "Frank Herbert", 1965))
lib.add_book(Book("1984", "George Orwell", 1950))   # такрорӣ
lib.add_book(Book("Future Book", "Unknown", 3000))  # соли нодуруст

print(len(lib))
print(lib[0])

for b in lib.find_by_author("George Orwell"):
    print(b)

lib.update_year(3, 1966)
print(lib[2])

lib.remove_book(1)
print(len(lib))
print(Book.count)
```

**Натиҷаи интизорӣ:**

```
Error: book already exists
Error: invalid year
3
#1 '1984' by George Orwell (1949)
#1 '1984' by George Orwell (1949)
#2 'Animal Farm' by George Orwell (1945)
#3 'Dune' by Frank Herbert (1966)
2
5
```

> 💡 Чаро `Book.count` ба 5 баробар аст, на 3? Ҳисобкунак **ҳамаи** объектҳои сохташудаи `Book`-ро ҳисоб мекунад, ҳатто онҳоеро, ки китобхона қабул накард.

---

### Масъалаи 3 — Мағоза (душвор)

**Мавзӯъҳо:** ҳама якҷоя: `@classmethod`, `@staticmethod`, `__str__`, `__repr__`, `__len__`, `__getitem__`, `__add__`, истисноҳо (exceptions).

**Класси `Product`:**
- атрибутҳо: `name`, `price`, `quantity`;
- `@staticmethod is_valid_price(price)` агар `price > 0` бошад, `True` бармегардонад;
- дар `__init__`: агар нарх нодуруст бошад, `ValueError("Price must be positive")` партоед;
- `@classmethod from_dict(cls, data)` молро аз луғати `{"name": ..., "price": ..., "quantity": ...}` месозад;
- `total_value()` `price * quantity`-ро бармегардонад;
- `__str__` бармегардонад: `Laptop: 5000 TJS x 2`;
- `__repr__` бармегардонад: `Product('Laptop', 5000, 2)`.

**Класси `Store`:**
- атрибутҳо: `name`, `products` (луғати `{ном: Product}`);
- **C:** `add_product(product)`: агар моли ҳамном аллакай бошад, миқдорашро **зиёд кунед**, вагарна молро илова кунед;
- **R:** `get_product(name)` мол ё `None`-ро бармегардонад; `__getitem__(name)`, то ки `store["Mouse"]` кор кунад;
- **U:** `update_price(name, new_price)` (бо санҷиши нарх); `apply_discount(percent)` нархи ҳамаи молҳоро `percent`% кам мекунад (то 2 рақам яклухт кунед: `round(..., 2)`);
- **D:** `delete_product(name)` `True` ё `False` бармегардонад;
- `total_value()` арзиши умумии ҳамаи молҳоро бармегардонад;
- `__len__` шумораи молҳои гуногунро бармегардонад;
- `__add__(other)` мағозаи **нав**-ро бо номи `"A + B"` бармегардонад, ки дар он молҳои ҳарду мағоза ҷамъ шудаанд (молҳои якхела муттаҳид мешаванд). Мағозаҳои аслӣ набояд тағйир ёбанд;
- `__str__` бармегардонад: `Store 'Dushanbe': 2 products, total 11500 TJS`.

**Санҷиш:**

```python
a = Store("Dushanbe")
a.add_product(Product("Laptop", 5000, 2))
a.add_product(Product.from_dict({"name": "Mouse", "price": 100, "quantity": 10}))
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

try:
    Product("Broken", -5, 1)
except ValueError as e:
    print("Error:", e)
```

**Натиҷаи интизорӣ:**

```
Store 'Dushanbe': 2 products, total 11500 TJS
Mouse: 100 TJS x 15
Product('Laptop', 5000, 2)
Laptop: 4050.0 TJS x 2
Mouse: 90.0 TJS x 15
Store 'Dushanbe + Khujand': 3 products, total 10720.0 TJS
True
2
Error: Price must be positive
```

> 💡 Маслиҳат барои `__add__`: аз молҳо **нусха** созед (`Product(p.name, p.price, p.quantity)`), вагарна ҳангоми муттаҳидсозӣ миқдор дар мағозаи аслӣ тағйир меёбад.
