# Python 1 — Lecture 12: Inheritance & Polymorphism

- [Русский](#русский)
- [Тоҷикӣ](#тоҷикӣ)
- [English](#english)

---

# Русский

## 10 задач: Наследование и полиморфизм

### Задача 1. Простое наследование
Создайте класс `Vehicle` с методом `move()`, который печатает `"Транспорт движется"`. Создайте класс `Car(Vehicle)` с собственным методом `honk()`, который печатает `"Би-би!"`.
Создайте объект `Car` и вызовите у него оба метода.

```
Транспорт движется
Би-би!
```

### Задача 2. Переопределение метода (Overriding)
Создайте класс `Employee` с методом `work()`, который печатает `"Сотрудник работает"`. Создайте дочерние классы `Programmer` и `Teacher`. В каждом из них переопределите `work()`, чтобы он печатал `"Пишет код"` и `"Проводит урок"` соответственно.
Вызовите `work()` у объектов всех трёх классов.

### Задача 3. `super()` и конструктор
Создайте класс `Person` с конструктором `__init__(self, name, age)`. Создайте класс `Student(Person)` с дополнительным полем `group`. Конструктор `Student` должен вызывать конструктор родителя через `super().__init__()`.
Добавьте в `Student` метод `info()`:

```python
s = Student("Али", 19, "Python-1")
s.info()
# Студент: Али, 19 лет, группа Python-1
```

### Задача 4. `super()` внутри обычного метода
Создайте класс `Animal` с методом `speak()` → `"Животное издаёт звук"`. Создайте `Cat(Animal)`, в котором `speak()` **сначала вызывает родительский метод через `super().speak()`**, а потом печатает `"Мяу"`.

```
Животное издаёт звук
Мяу
```

### Задача 5. Многоуровневое наследование
Постройте цепочку: `Device` → `Phone` → `Smartphone`.
- `Device` имеет метод `power_on()` → `"Устройство включено"`
- `Phone` добавляет метод `call(number)` → `"Звоню на номер ..."`
- `Smartphone` добавляет метод `take_photo()` → `"Фото сделано"`

Создайте объект `Smartphone` и вызовите все три метода. Ответьте в комментарии: какой это тип наследования?

### Задача 6. Множественное наследование
Создайте класс `Flyer` с методом `fly()` и класс `Swimmer` с методом `swim()`. Создайте класс `Duck(Flyer, Swimmer)` со своим методом `quack()`.
Вызовите у утки все три метода.
**Дополнительно:** выведите `Duck.__mro__` и объясните, что это означает.

### Задача 7. Иерархическое наследование
Создайте базовый класс `User` с конструктором `__init__(self, name, email)` и методом `get_info()`, который возвращает `"Имя: ..., Email: ..."`.
Создайте три дочерних класса от `User`:
- `Admin` — дополнительное поле `level` (уровень доступа)
- `Customer` — дополнительное поле `balance`
- `Guest` — без дополнительных полей

Каждый дочерний класс вызывает `super().__init__()` и переопределяет `get_info()`, добавляя к результату `super().get_info()` свою информацию.

```python
print(Admin("Али", "ali@mail.tj", 3).get_info())
# Имя: Али, Email: ali@mail.tj, Уровень: 3
```

### Задача 8. Полиморфизм
Создайте классы `Circle`, `Rectangle`, `Triangle`. У каждого есть метод `area()`, который возвращает площадь (данные передаются в конструктор).
Поместите объекты в один список и в цикле выведите площадь каждой фигуры **без использования `if/else` и `isinstance`**.

```python
shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
for s in shapes:
    print(type(s).__name__, s.area())
```

### Задача 9. «Перегрузка» через аргументы по умолчанию + Enum
**Часть А.** Создайте класс `Calculator` с методом `multiply(a, b=1, c=1)`, чтобы работали все варианты:

```python
calc.multiply(5)        # 5
calc.multiply(5, 2)     # 10
calc.multiply(5, 2, 3)  # 30
```

**Часть Б.** Создайте `Enum` `OrderStatus` со значениями `NEW = 1`, `PAID = 2`, `SHIPPED = 3`, `DELIVERED = 4`. Напишите функцию `next_status(status)`, которая возвращает следующий статус (для `DELIVERED` возвращает его же). Выведите `.name` и `.value` результата.

### Задача 10. Итоговая: всё вместе
Создайте систему оплаты:
1. `Enum` `PaymentStatus` со значениями `SUCCESS` и `FAILED`.
2. Базовый класс `Payment` с конструктором `__init__(self, owner)` и методом `pay(amount)`, который печатает `"Неизвестный способ оплаты"` и возвращает `PaymentStatus.FAILED`.
3. Дочерние классы `CardPayment`, `CashPayment`, `WalletPayment`, которые переопределяют `pay()`:
   - `CardPayment` принимает дополнительный параметр `card_number` и вызывает `super().__init__(owner)`; печатает последние 4 цифры карты.
   - `CashPayment` просто печатает сумму.
   - `WalletPayment` имеет поле `balance`; если денег не хватает — возвращает `FAILED`, иначе уменьшает баланс.
4. Во всех классах: если сумма ≤ 0, `pay()` возвращает `FAILED`.
5. Пройдите циклом по списку разных способов оплаты, вызовите `pay()` у каждого и выведите `.name` полученного статуса (полиморфизм).

```
Али оплатил 200 сомони картой ****4321 -> SUCCESS
Вали оплатил 150 сомони наличными -> SUCCESS
Сино: недостаточно средств в кошельке -> FAILED
```

---

# Тоҷикӣ

## 10 масъала: Мерос ва полиморфизм

### Масъалаи 1. Мероси оддӣ
Синфи `Vehicle`-ро бо методи `move()` созед, ки `"Нақлиёт ҳаракат мекунад"`-ро чоп мекунад. Синфи `Car(Vehicle)`-ро бо методи худаш `honk()` созед, ки `"Би-би!"`-ро чоп мекунад.
Объекти `Car` созед ва ҳарду методро даъват кунед.

```
Нақлиёт ҳаракат мекунад
Би-би!
```

### Масъалаи 2. Аз нав муайян кардани метод (Overriding)
Синфи `Employee`-ро бо методи `work()` созед, ки `"Корманд кор мекунад"`-ро чоп мекунад. Синфҳои фарзандии `Programmer` ва `Teacher`-ро созед. Дар ҳар яки онҳо `work()`-ро аз нав муайян кунед, то мувофиқан `"Код менависад"` ва `"Дарс мегузаронад"`-ро чоп кунад.
`work()`-ро барои объектҳои ҳар се синф даъват кунед.

### Масъалаи 3. `super()` ва конструктор
Синфи `Person`-ро бо конструктори `__init__(self, name, age)` созед. Синфи `Student(Person)`-ро бо майдони иловагии `group` созед. Конструктори `Student` бояд конструктори волидро тавассути `super().__init__()` даъват кунад.
Ба `Student` методи `info()` илова кунед:

```python
s = Student("Алӣ", 19, "Python-1")
s.info()
# Донишҷӯ: Алӣ, 19 сола, гурӯҳи Python-1
```

### Масъалаи 4. `super()` дар дохили методи оддӣ
Синфи `Animal`-ро бо методи `speak()` → `"Ҳайвон овоз мебарорад"` созед. Синфи `Cat(Animal)`-ро созед, ки дар он `speak()` **аввал методи волидро тавассути `super().speak()` даъват мекунад**, баъд `"Миёв"`-ро чоп мекунад.

```
Ҳайвон овоз мебарорад
Миёв
```

### Масъалаи 5. Мероси бисёрсатҳа
Занҷир созед: `Device` → `Phone` → `Smartphone`.
- `Device` методи `power_on()` дорад → `"Дастгоҳ фаъол шуд"`
- `Phone` методи `call(number)`-ро илова мекунад → `"Ба рақами ... занг мезанам"`
- `Smartphone` методи `take_photo()`-ро илова мекунад → `"Акс гирифта шуд"`

Объекти `Smartphone` созед ва ҳар се методро даъват кунед. Дар шарҳ ҷавоб диҳед: ин кадом навъи мерос аст?

### Масъалаи 6. Мероси бисёркарата
Синфи `Flyer`-ро бо методи `fly()` ва синфи `Swimmer`-ро бо методи `swim()` созед. Синфи `Duck(Flyer, Swimmer)`-ро бо методи худаш `quack()` созед.
Ҳар се методро барои мурғобӣ даъват кунед.
**Иловагӣ:** `Duck.__mro__`-ро чоп кунед ва фаҳмонед, ки он чӣ маъно дорад.

### Масъалаи 7. Мероси иерархӣ
Синфи асосии `User`-ро бо конструктори `__init__(self, name, email)` ва методи `get_info()` созед, ки `"Ном: ..., Email: ..."`-ро бармегардонад.
Се синфи фарзандӣ аз `User` созед:
- `Admin` — майдони иловагии `level` (сатҳи дастрасӣ)
- `Customer` — майдони иловагии `balance`
- `Guest` — бе майдонҳои иловагӣ

Ҳар як синфи фарзандӣ `super().__init__()`-ро даъват мекунад ва `get_info()`-ро аз нав муайян мекунад: ба натиҷаи `super().get_info()` маълумоти худашро илова мекунад.

```python
print(Admin("Алӣ", "ali@mail.tj", 3).get_info())
# Ном: Алӣ, Email: ali@mail.tj, Сатҳ: 3
```

### Масъалаи 8. Полиморфизм
Синфҳои `Circle`, `Rectangle`, `Triangle`-ро созед. Ҳар яки онҳо методи `area()` дорад, ки масоҳатро бармегардонад (маълумот ба конструктор дода мешавад).
Объектҳоро ба як рӯйхат гузоред ва дар давра масоҳати ҳар як шаклро **бе истифодаи `if/else` ва `isinstance`** чоп кунед.

```python
shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
for s in shapes:
    print(type(s).__name__, s.area())
```

### Масъалаи 9. «Overloading» бо аргументҳои пешфарз + Enum
**Қисми А.** Синфи `Calculator`-ро бо методи `multiply(a, b=1, c=1)` созед, то ҳамаи вариантҳо кор кунанд:

```python
calc.multiply(5)        # 5
calc.multiply(5, 2)     # 10
calc.multiply(5, 2, 3)  # 30
```

**Қисми Б.** `Enum`-и `OrderStatus`-ро бо қиматҳои `NEW = 1`, `PAID = 2`, `SHIPPED = 3`, `DELIVERED = 4` созед. Функсияи `next_status(status)`-ро нависед, ки ҳолати навбатиро бармегардонад (барои `DELIVERED` худашро бармегардонад). `.name` ва `.value`-и натиҷаро чоп кунед.

### Масъалаи 10. Ҷамъбастӣ: ҳама якҷоя
Системаи пардохт созед:
1. `Enum`-и `PaymentStatus` бо қиматҳои `SUCCESS` ва `FAILED`.
2. Синфи асосии `Payment` бо конструктори `__init__(self, owner)` ва методи `pay(amount)`, ки `"Усули пардохт номаълум аст"`-ро чоп мекунад ва `PaymentStatus.FAILED`-ро бармегардонад.
3. Синфҳои фарзандии `CardPayment`, `CashPayment`, `WalletPayment`, ки `pay()`-ро аз нав муайян мекунанд:
   - `CardPayment` параметри иловагии `card_number` мегирад ва `super().__init__(owner)`-ро даъват мекунад; 4 рақами охири кортро чоп мекунад.
   - `CashPayment` танҳо маблағро чоп мекунад.
   - `WalletPayment` майдони `balance` дорад; агар пул нарасад — `FAILED` бармегардонад, вагарна балансро кам мекунад.
4. Дар ҳамаи синфҳо: агар маблағ ≤ 0 бошад, `pay()` `FAILED`-ро бармегардонад.
5. Дар давра аз рӯйхати усулҳои гуногуни пардохт гузаред, барои ҳар кадом `pay()`-ро даъват кунед ва `.name`-и ҳолати гирифташударо чоп кунед (полиморфизм).

```
Алӣ 200 сомонӣ бо корти ****4321 пардохт кард -> SUCCESS
Валӣ 150 сомонӣ нақд пардохт кард -> SUCCESS
Сино: дар ҳамён маблағ нокифоя аст -> FAILED
```

---

# English

## 10 Tasks: Inheritance & Polymorphism

### Task 1. Simple inheritance
Create a class `Vehicle` with a method `move()` that prints `"Vehicle is moving"`. Create a class `Car(Vehicle)` with its own method `honk()` that prints `"Beep beep!"`.
Create a `Car` object and call both methods on it.

```
Vehicle is moving
Beep beep!
```

### Task 2. Method overriding
Create a class `Employee` with a method `work()` that prints `"Employee is working"`. Create child classes `Programmer` and `Teacher`. In each of them, override `work()` so it prints `"Writing code"` and `"Teaching a lesson"` respectively.
Call `work()` on objects of all three classes.

### Task 3. `super()` and the constructor
Create a class `Person` with a constructor `__init__(self, name, age)`. Create a class `Student(Person)` with an extra field `group`. The `Student` constructor must call the parent constructor using `super().__init__()`.
Add an `info()` method to `Student`:

```python
s = Student("Ali", 19, "Python-1")
s.info()
# Student: Ali, 19 years old, group Python-1
```

### Task 4. `super()` inside a regular method
Create a class `Animal` with a method `speak()` → `"Animal makes a sound"`. Create `Cat(Animal)` where `speak()` **first calls the parent method via `super().speak()`** and then prints `"Meow"`.

```
Animal makes a sound
Meow
```

### Task 5. Multilevel inheritance
Build a chain: `Device` → `Phone` → `Smartphone`.
- `Device` has a method `power_on()` → `"Device is on"`
- `Phone` adds a method `call(number)` → `"Calling number ..."`
- `Smartphone` adds a method `take_photo()` → `"Photo taken"`

Create a `Smartphone` object and call all three methods. Answer in a comment: what type of inheritance is this?

### Task 6. Multiple inheritance
Create a class `Flyer` with a method `fly()` and a class `Swimmer` with a method `swim()`. Create a class `Duck(Flyer, Swimmer)` with its own method `quack()`.
Call all three methods on the duck.
**Bonus:** print `Duck.__mro__` and explain what it means.

### Task 7. Hierarchical inheritance
Create a base class `User` with a constructor `__init__(self, name, email)` and a method `get_info()` that returns `"Name: ..., Email: ..."`.
Create three child classes of `User`:
- `Admin` — extra field `level` (access level)
- `Customer` — extra field `balance`
- `Guest` — no extra fields

Each child class calls `super().__init__()` and overrides `get_info()`, adding its own information to the result of `super().get_info()`.

```python
print(Admin("Ali", "ali@mail.tj", 3).get_info())
# Name: Ali, Email: ali@mail.tj, Level: 3
```

### Task 8. Polymorphism
Create classes `Circle`, `Rectangle`, `Triangle`. Each has a method `area()` that returns the area (the data is passed to the constructor).
Put the objects in one list and, in a loop, print the area of each shape **without using `if/else` or `isinstance`**.

```python
shapes = [Circle(3), Rectangle(4, 5), Triangle(6, 2)]
for s in shapes:
    print(type(s).__name__, s.area())
```

### Task 9. "Overloading" with default arguments + Enum
**Part A.** Create a class `Calculator` with a method `multiply(a, b=1, c=1)` so that all of these work:

```python
calc.multiply(5)        # 5
calc.multiply(5, 2)     # 10
calc.multiply(5, 2, 3)  # 30
```

**Part B.** Create an `Enum` `OrderStatus` with values `NEW = 1`, `PAID = 2`, `SHIPPED = 3`, `DELIVERED = 4`. Write a function `next_status(status)` that returns the next status (for `DELIVERED` it returns the same status). Print the `.name` and `.value` of the result.

### Task 10. Final task: everything together
Build a payment system:
1. An `Enum` `PaymentStatus` with values `SUCCESS` and `FAILED`.
2. A base class `Payment` with a constructor `__init__(self, owner)` and a method `pay(amount)` that prints `"Unknown payment method"` and returns `PaymentStatus.FAILED`.
3. Child classes `CardPayment`, `CashPayment`, `WalletPayment` that override `pay()`:
   - `CardPayment` takes an extra parameter `card_number` and calls `super().__init__(owner)`; it prints the last 4 digits of the card.
   - `CashPayment` just prints the amount.
   - `WalletPayment` has a `balance` field; if there is not enough money it returns `FAILED`, otherwise it decreases the balance.
4. In all classes: if the amount is ≤ 0, `pay()` returns `FAILED`.
5. Loop over a list of different payment methods, call `pay()` on each one and print the `.name` of the returned status (polymorphism).

```
Ali paid 200 somoni by card ****4321 -> SUCCESS
Vali paid 150 somoni in cash -> SUCCESS
Sino: not enough money in the wallet -> FAILED
```
