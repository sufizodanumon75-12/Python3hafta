# Python: Абстракция и инкапсуляция — 50 задач / 50 tasks / 50 вазифа

Языки / Languages / Забонҳо: [🇷🇺 Русский](#-русский) · [🇬🇧 English](#-english) · [🇹🇯 Тоҷикӣ](#-тоҷикӣ)

---

# 🇷🇺 Русский

## 🟢 Уровень 1: Базовый

### 1. Класс Book
- Приватные атрибуты `__title` и `__pages`.
- Геттеры для обоих атрибутов.
- `set_pages()` устанавливает значение, только если оно больше 0.

### 2. Класс Dog
- Приватные атрибуты `__name` и `__age`.
- Метод `get_name()`.
- `set_age()` принимает возраст только от 0 до 30.

### 3. Класс Rectangle
- Приватные `__width` и `__height`.
- Свойства `width` и `height` (getter и setter), значения должны быть положительными.
- Метод `area()` возвращает площадь.

### 4. Класс Counter
- Приватный атрибут `__count`.
- Методы `increment()` и `decrement()` (счётчик не может быть меньше 0).
- Метод `get_count()`.

### 5. Класс Light
- Приватный атрибут `__is_on`.
- Методы `turn_on()` и `turn_off()`.
- Метод `is_on()` возвращает состояние.

### 6. Класс Person
- Приватный атрибут `__name`.
- Свойство `name` (getter и setter).
- В сеттере проверяй, что имя — непустая строка.

### 7. Класс Wallet
- Приватное поле `__money`.
- `add_money(amount)` — пополнение (если сумма > 0).
- `spend_money(amount)` — трата (если хватает денег).
- `get_money()` — возвращает остаток.

### 8. Класс Square
- Приватный атрибут `__side` со свойством `side` (только положительные значения).
- Свойство `area` — только геттер (side ** 2).

### 9. Класс Phone
- Приватный атрибут `__battery` (0–100).
- `charge(amount)` и `use(amount)` не выводят заряд за пределы 0–100.
- `get_battery()`.

### 10. Класс User
- Приватный атрибут `__password`.
- `set_password()` принимает пароль не короче 6 символов.
- `check_password(p)` возвращает `True`/`False`; сам пароль наружу не отдаётся.

### 11. Класс Thermostat
- Приватный атрибут `__target`.
- Свойство `target` (getter и setter), допустимый диапазон 10–30.

### 12. Класс Car
- Приватный атрибут `__speed`.
- `accelerate(n)` и `brake(n)` держат скорость в диапазоне 0–200.
- `get_speed()`.

### 13. Класс Employee
- Приватный атрибут `__salary` со свойством `salary` (не меньше 0).
- Метод `raise_salary(percent)` увеличивает зарплату на заданный процент.

### 14. Класс Triangle
- Приватные `__a`, `__b`, `__c`.
- При создании проверяй неравенство треугольника, иначе `ValueError`.
- Метод `perimeter()`.

### 15. Name mangling
- Создай класс `Secret` с приватным атрибутом `__code`.
- Покажи, что `obj.__code` вызывает ошибку.
- Получи значение через `obj._Secret__code` и объясни, почему так работает.

## 🟡 Уровень 2: Средний

### 16. Класс Cart
- Приватный словарь `__items` (название → цена).
- Методы `add_item(name, price)`, `remove_item(name)`, `get_total()`.
- `get_items()` возвращает копию словаря.

### 17. Класс Library
- Приватный список `__books`.
- Методы `add_book()`, `remove_book()`.
- `get_books()` возвращает копию списка (проверь, что внешние изменения не влияют на оригинал).

### 18. Класс ATM
- Приватные `__pin` и `__balance`.
- `withdraw(pin, amount)` проверяет PIN и остаток.
- После 3 неверных попыток карта блокируется.

### 19. Класс Time
- Приватные `__hours` и `__minutes` со свойствами и проверкой диапазонов (0–23, 0–59).
- Метод `__str__` возвращает формат `HH:MM`.

### 20. Класс Inventory
- Приватный словарь `__stock`.
- `add_stock(name, qty)` и `remove_stock(name, qty)` (остаток не может стать отрицательным).
- `get_stock(name)`.

### 21. Класс Logger
- Приватный список `__logs` и приватный метод `__format(msg)` (добавляет время).
- Публичный `log(msg)` использует `__format`.
- `get_logs()` возвращает копию.

### 22. Класс Email
- Свойство `address` с проверкой: есть `@` и `.`.
- Свойство `domain` — только геттер (часть после `@`).

### 23. Класс Stack
- Приватный список `__data`.
- Методы `push()`, `pop()` (ошибка, если пуст), `peek()`, `size()`, `is_empty()`.

### 24. Класс BankAccount с историей
- Приватные `__balance` и `__transactions`.
- `deposit()` и `withdraw()` записывают операции в историю.
- `get_history()` возвращает копию.

### 25. Абстрактный класс Shape
- Используй `ABC` и `@abstractmethod`: методы `area()` и `perimeter()`.
- Реализуй `Circle` и `Rectangle`.
- Создай список фигур и посчитай суммарную площадь.
- Покажи `TypeError` при попытке создать `Shape()`.

### 26. Абстрактный класс Animal
- Абстрактные методы `speak()` и `move()`.
- Реализуй `Dog` и `Bird`.
- В цикле вызови оба метода для списка животных.

### 27. Абстрактный класс Payment
- Абстрактный метод `pay(amount)`.
- `CardPayment` (с лимитом) и `CashPayment`.
- Функция `checkout(payment, amount)` работает с любым способом оплаты.

### 28. Абстрактный класс Vehicle
- Абстрактные методы `start()` и `stop()`.
- Абстрактное свойство `fuel_type`.
- Реализуй `Car` и `ElectricCar`.

### 29. Абстрактный класс Employee
- Абстрактный метод `calculate_salary()`.
- `FullTime` (фиксированная ставка) и `PartTime` (часы × ставка).
- Посчитай общий фонд зарплаты по списку сотрудников.

### 30. Абстрактный класс Notifier
- Абстрактный метод `send(message)`.
- Реализации: `EmailNotifier`, `SmsNotifier`, `TelegramNotifier`.
- Функция `notify_all(notifiers, message)`.

### 31. Абстрактный класс Storage
- Абстрактные методы `save(key, value)` и `load(key)`.
- `MemoryStorage` (словарь) и `FileStorage` (JSON-файл).

### 32. Абстрактный класс Parser
- Абстрактный метод `parse(text)`.
- `JsonParser` и `CsvParser` (простая версия) возвращают список/словарь.

### 33. Абстрактный класс Sorter
- Абстрактный метод `sort(data)`, который не меняет исходный список.
- Реализуй `BubbleSorter` и `SelectionSorter` и сравни результаты.

### 34. Классы Student и Group
- `Student` с приватным списком `__grades`, методами `add_grade()` и `average()`.
- `Group` с приватным списком студентов, методами `add_student()` и `best_student()`.

### 35. Шаблонный метод
- Абстрактный класс `DataProcessor` с абстрактными `read()` и `process()` и конкретным `save()`.
- Метод `run()` вызывает их по порядку.
- Реализуй два наследника.

## 🔴 Уровень 3: Продвинутый

### 36. Заказ со скидками
- Абстрактный класс `Discount` с методом `apply(price)`.
- `PercentDiscount` и `FixedDiscount`.
- `Order` с приватным списком товаров, методом `set_discount()` и `get_final_price()`.

### 37. Банковские счета
- Абстрактный класс `Account` с приватным `__balance` и методами `deposit()`, `withdraw()`, `get_balance()`.
- `SavingsAccount` (метод `add_interest()`).
- `CheckingAccount` (лимит овердрафта).
- Баланс нельзя изменить в обход методов.

### 38. Неизменяемый Config
- Класс `Config`, значения которого нельзя менять после создания (через `__setattr__` или свойства).
- Метод `to_dict()` возвращает копию.
- Попытка изменить значение вызывает `AttributeError`.

### 39. Система плагинов
- Абстрактный класс `Plugin` со свойством `name` и методом `run()`.
- `PluginManager` с приватным реестром и публичными `register()`, `run_all()`, `names()`.
- Запрещай регистрацию плагинов с повторяющимся именем.

### 40. Абстрактная база данных
- Абстрактный класс `Database`: `connect()`, `execute(query)`, `close()`.
- Две имитации (`FakeSqlite`, `FakeMysql`).
- Реализуй поддержку `with` (`__enter__`/`__exit__`) в базовом классе.

### 41. Игровые персонажи
- Абстрактный класс `Character` с приватным `__hp`.
- Методы `take_damage()`, `is_alive()` и абстрактные `attack()`, `defend()`.
- Реализуй `Warrior` и `Mage` и проведи бой до победы одного из них.

### 42. Абстрактное свойство и classmethod
- Абстрактный класс `Document` с абстрактным свойством `extension` и абстрактным `@classmethod from_string(text)`.
- Реализуй `TextDocument` и `MarkdownDocument`.

### 43. Duck typing и Protocol
- Опиши интерфейс `Drawable` через `typing.Protocol`.
- Создай два несвязанных класса, у каждого есть `draw()`.
- Функция `render(items)` работает с любым объектом, соответствующим протоколу.

### 44. Своя последовательность
- Реализуй класс на основе `collections.abc.Sequence` (`__getitem__`, `__len__`).
- Проверь, что работают `len()`, итерация, `in`, `reversed()`.
- Внутренние данные приватные.

### 45. Singleton Settings
- Класс `Settings` с приватным атрибутом класса `__instance`.
- Метод `get_instance()` всегда возвращает один и тот же объект.
- Попытка создать второй экземпляр напрямую вызывает ошибку.

### 46. Дескриптор проверки
- Напиши дескриптор `PositiveNumber` (проверка > 0).
- Используй его в классе `Product` для полей `price` и `quantity`.
- Сообщение об ошибке должно содержать имя поля.

### 47. Школьная система
- Абстрактный класс `Person` с методом `describe()`.
- `Student` с приватными оценками и `Teacher` с приватной зарплатой.
- Отчёт строится только через публичные методы.

### 48. Банк и переводы
- Класс `Bank` с приватным словарём счетов.
- Методы `open_account()`, `transfer(from_id, to_id, amount)`.
- Если перевод не удался, балансы обоих счетов остаются прежними.

### 49. Библиотека с читателями
- Абстрактный класс `Item` с `Book` и `DVD` (срок выдачи у каждого свой).
- `Member` с приватным списком взятых позиций (максимум 3).
- Методы `borrow(item)` и `return_item(item)`.

### 50. Мини-проект: парковка
- Абстрактный класс `Vehicle` с абстрактным методом `fee(hours)`; `Car`, `Truck`, `Motorcycle`.
- `ParkingLot` с приватным списком мест, методами `park(vehicle)` и `leave(vehicle, hours)`.
- Нельзя занять уже занятое место; `leave` возвращает сумму к оплате.

---

# 🇬🇧 English

## 🟢 Level 1: Basic

### 1. Class Book
- Private attributes `__title` and `__pages`.
- Getters for both attributes.
- `set_pages()` sets the value only if it is greater than 0.

### 2. Class Dog
- Private attributes `__name` and `__age`.
- Method `get_name()`.
- `set_age()` accepts an age only between 0 and 30.

### 3. Class Rectangle
- Private `__width` and `__height`.
- Properties `width` and `height` (getter and setter); values must be positive.
- Method `area()` returns the area.

### 4. Class Counter
- Private attribute `__count`.
- Methods `increment()` and `decrement()` (the counter cannot go below 0).
- Method `get_count()`.

### 5. Class Light
- Private attribute `__is_on`.
- Methods `turn_on()` and `turn_off()`.
- Method `is_on()` returns the state.

### 6. Class Person
- Private attribute `__name`.
- Property `name` (getter and setter).
- The setter must check that the name is a non-empty string.

### 7. Class Wallet
- Private field `__money`.
- `add_money(amount)` adds money (if the amount > 0).
- `spend_money(amount)` spends money (if there is enough).
- `get_money()` returns the remainder.

### 8. Class Square
- Private attribute `__side` with a `side` property (positive values only).
- Property `area` is a getter only (side ** 2).

### 9. Class Phone
- Private attribute `__battery` (0–100).
- `charge(amount)` and `use(amount)` keep the level within 0–100.
- `get_battery()`.

### 10. Class User
- Private attribute `__password`.
- `set_password()` accepts a password of at least 6 characters.
- `check_password(p)` returns `True`/`False`; the password itself is never exposed.

### 11. Class Thermostat
- Private attribute `__target`.
- Property `target` (getter and setter), allowed range 10–30.

### 12. Class Car
- Private attribute `__speed`.
- `accelerate(n)` and `brake(n)` keep the speed within 0–200.
- `get_speed()`.

### 13. Class Employee
- Private attribute `__salary` with a `salary` property (not less than 0).
- Method `raise_salary(percent)` increases the salary by the given percent.

### 14. Class Triangle
- Private `__a`, `__b`, `__c`.
- On creation, check the triangle inequality, otherwise raise `ValueError`.
- Method `perimeter()`.

### 15. Name mangling
- Create a class `Secret` with a private attribute `__code`.
- Show that `obj.__code` raises an error.
- Get the value via `obj._Secret__code` and explain why it works.

## 🟡 Level 2: Intermediate

### 16. Class Cart
- Private dict `__items` (name → price).
- Methods `add_item(name, price)`, `remove_item(name)`, `get_total()`.
- `get_items()` returns a copy of the dict.

### 17. Class Library
- Private list `__books`.
- Methods `add_book()`, `remove_book()`.
- `get_books()` returns a copy of the list (check that outside changes don't affect the original).

### 18. Class ATM
- Private `__pin` and `__balance`.
- `withdraw(pin, amount)` checks the PIN and the balance.
- After 3 wrong attempts the card is locked.

### 19. Class Time
- Private `__hours` and `__minutes` with properties and range validation (0–23, 0–59).
- Method `__str__` returns the `HH:MM` format.

### 20. Class Inventory
- Private dict `__stock`.
- `add_stock(name, qty)` and `remove_stock(name, qty)` (stock cannot become negative).
- `get_stock(name)`.

### 21. Class Logger
- Private list `__logs` and private method `__format(msg)` (adds a timestamp).
- Public `log(msg)` uses `__format`.
- `get_logs()` returns a copy.

### 22. Class Email
- Property `address` with validation: contains `@` and `.`.
- Property `domain` is a getter only (the part after `@`).

### 23. Class Stack
- Private list `__data`.
- Methods `push()`, `pop()` (error if empty), `peek()`, `size()`, `is_empty()`.

### 24. Class BankAccount with history
- Private `__balance` and `__transactions`.
- `deposit()` and `withdraw()` record operations in the history.
- `get_history()` returns a copy.

### 25. Abstract class Shape
- Use `ABC` and `@abstractmethod`: methods `area()` and `perimeter()`.
- Implement `Circle` and `Rectangle`.
- Create a list of shapes and compute the total area.
- Show the `TypeError` when trying to create `Shape()`.

### 26. Abstract class Animal
- Abstract methods `speak()` and `move()`.
- Implement `Dog` and `Bird`.
- Call both methods in a loop over a list of animals.

### 27. Abstract class Payment
- Abstract method `pay(amount)`.
- `CardPayment` (with a limit) and `CashPayment`.
- Function `checkout(payment, amount)` works with any payment method.

### 28. Abstract class Vehicle
- Abstract methods `start()` and `stop()`.
- Abstract property `fuel_type`.
- Implement `Car` and `ElectricCar`.

### 29. Abstract class Employee
- Abstract method `calculate_salary()`.
- `FullTime` (fixed rate) and `PartTime` (hours × rate).
- Compute the total payroll for a list of employees.

### 30. Abstract class Notifier
- Abstract method `send(message)`.
- Implementations: `EmailNotifier`, `SmsNotifier`, `TelegramNotifier`.
- Function `notify_all(notifiers, message)`.

### 31. Abstract class Storage
- Abstract methods `save(key, value)` and `load(key)`.
- `MemoryStorage` (dict) and `FileStorage` (JSON file).

### 32. Abstract class Parser
- Abstract method `parse(text)`.
- `JsonParser` and `CsvParser` (simple version) return a list/dict.

### 33. Abstract class Sorter
- Abstract method `sort(data)` that does not modify the original list.
- Implement `BubbleSorter` and `SelectionSorter` and compare the results.

### 34. Classes Student and Group
- `Student` with a private list `__grades` and methods `add_grade()` and `average()`.
- `Group` with a private list of students and methods `add_student()` and `best_student()`.

### 35. Template method
- Abstract class `DataProcessor` with abstract `read()` and `process()` and a concrete `save()`.
- Method `run()` calls them in order.
- Implement two subclasses.

## 🔴 Level 3: Advanced

### 36. Order with discounts
- Abstract class `Discount` with method `apply(price)`.
- `PercentDiscount` and `FixedDiscount`.
- `Order` with a private list of items, method `set_discount()` and `get_final_price()`.

### 37. Bank accounts
- Abstract class `Account` with private `__balance` and methods `deposit()`, `withdraw()`, `get_balance()`.
- `SavingsAccount` (method `add_interest()`).
- `CheckingAccount` (overdraft limit).
- The balance cannot be changed bypassing the methods.

### 38. Immutable Config
- Class `Config` whose values cannot be changed after creation (via `__setattr__` or properties).
- Method `to_dict()` returns a copy.
- Trying to change a value raises `AttributeError`.

### 39. Plugin system
- Abstract class `Plugin` with a `name` property and a `run()` method.
- `PluginManager` with a private registry and public `register()`, `run_all()`, `names()`.
- Reject registering plugins with a duplicate name.

### 40. Abstract database
- Abstract class `Database`: `connect()`, `execute(query)`, `close()`.
- Two mock implementations (`FakeSqlite`, `FakeMysql`).
- Support `with` (`__enter__`/`__exit__`) in the base class.

### 41. Game characters
- Abstract class `Character` with private `__hp`.
- Methods `take_damage()`, `is_alive()` and abstract `attack()`, `defend()`.
- Implement `Warrior` and `Mage` and run a fight until one of them wins.

### 42. Abstract property and classmethod
- Abstract class `Document` with an abstract property `extension` and an abstract `@classmethod from_string(text)`.
- Implement `TextDocument` and `MarkdownDocument`.

### 43. Duck typing and Protocol
- Describe the `Drawable` interface with `typing.Protocol`.
- Create two unrelated classes, each with a `draw()` method.
- Function `render(items)` works with any object that matches the protocol.

### 44. Custom sequence
- Implement a class based on `collections.abc.Sequence` (`__getitem__`, `__len__`).
- Check that `len()`, iteration, `in`, `reversed()` work.
- The internal data is private.

### 45. Singleton Settings
- Class `Settings` with a private class attribute `__instance`.
- Method `get_instance()` always returns the same object.
- Trying to create a second instance directly raises an error.

### 46. Validation descriptor
- Write a descriptor `PositiveNumber` (checks > 0).
- Use it in class `Product` for the `price` and `quantity` fields.
- The error message must contain the field name.

### 47. School system
- Abstract class `Person` with method `describe()`.
- `Student` with private grades and `Teacher` with a private salary.
- The report is built using public methods only.

### 48. Bank and transfers
- Class `Bank` with a private dict of accounts.
- Methods `open_account()`, `transfer(from_id, to_id, amount)`.
- If a transfer fails, both account balances stay unchanged.

### 49. Library with members
- Abstract class `Item` with `Book` and `DVD` (each with its own loan period).
- `Member` with a private list of borrowed items (maximum 3).
- Methods `borrow(item)` and `return_item(item)`.

### 50. Mini-project: parking lot
- Abstract class `Vehicle` with abstract method `fee(hours)`; `Car`, `Truck`, `Motorcycle`.
- `ParkingLot` with a private list of spots, methods `park(vehicle)` and `leave(vehicle, hours)`.
- An occupied spot cannot be taken again; `leave` returns the amount due.

---

# 🇹🇯 Тоҷикӣ

## 🟢 Сатҳи 1: Асосӣ

### 1. Синфи Book
- Атрибутҳои хусусии `__title` ва `__pages`.
- Геттерҳо барои ҳарду атрибут.
- `set_pages()` қиматро танҳо дар сурати аз 0 калон будан таъин мекунад.

### 2. Синфи Dog
- Атрибутҳои хусусии `__name` ва `__age`.
- Усули `get_name()`.
- `set_age()` синнро танҳо аз 0 то 30 қабул мекунад.

### 3. Синфи Rectangle
- `__width` ва `__height`-и хусусӣ.
- Хусусиятҳои `width` ва `height` (getter ва setter), қиматҳо бояд мусбат бошанд.
- Усули `area()` масоҳатро бармегардонад.

### 4. Синфи Counter
- Атрибути хусусии `__count`.
- Усулҳои `increment()` ва `decrement()` (ҳисобкунак аз 0 хурд буда наметавонад).
- Усули `get_count()`.

### 5. Синфи Light
- Атрибути хусусии `__is_on`.
- Усулҳои `turn_on()` ва `turn_off()`.
- Усули `is_on()` ҳолатро бармегардонад.

### 6. Синфи Person
- Атрибути хусусии `__name`.
- Хусусияти `name` (getter ва setter).
- Дар сеттер санҷед, ки ном сатри холӣ нест.

### 7. Синфи Wallet
- Майдони хусусии `__money`.
- `add_money(amount)` — пур кардан (агар маблағ > 0 бошад).
- `spend_money(amount)` — харҷ кардан (агар пул кифоя бошад).
- `get_money()` — боқимондаро бармегардонад.

### 8. Синфи Square
- Атрибути хусусии `__side` бо хусусияти `side` (танҳо қиматҳои мусбат).
- Хусусияти `area` — танҳо геттер (side ** 2).

### 9. Синфи Phone
- Атрибути хусусии `__battery` (0–100).
- `charge(amount)` ва `use(amount)` сатҳро дар доираи 0–100 нигоҳ медоранд.
- `get_battery()`.

### 10. Синфи User
- Атрибути хусусии `__password`.
- `set_password()` паролро на кӯтоҳтар аз 6 аломат қабул мекунад.
- `check_password(p)` `True`/`False` бармегардонад; худи парол берун дода намешавад.

### 11. Синфи Thermostat
- Атрибути хусусии `__target`.
- Хусусияти `target` (getter ва setter), доираи иҷозатдода 10–30.

### 12. Синфи Car
- Атрибути хусусии `__speed`.
- `accelerate(n)` ва `brake(n)` суръатро дар доираи 0–200 нигоҳ медоранд.
- `get_speed()`.

### 13. Синфи Employee
- Атрибути хусусии `__salary` бо хусусияти `salary` (на камтар аз 0).
- Усули `raise_salary(percent)` маошро ба фоизи додашуда зиёд мекунад.

### 14. Синфи Triangle
- `__a`, `__b`, `__c`-и хусусӣ.
- Ҳангоми эҷод нобаробарии секунҷаро санҷед, вагарна `ValueError` занед.
- Усули `perimeter()`.

### 15. Name mangling
- Синфи `Secret`-ро бо атрибути хусусии `__code` эҷод кунед.
- Нишон диҳед, ки `obj.__code` хатогӣ медиҳад.
- Қиматро тавассути `obj._Secret__code` гиред ва шарҳ диҳед, ки чаро кор мекунад.

## 🟡 Сатҳи 2: Миёна

### 16. Синфи Cart
- Луғати хусусии `__items` (ном → нарх).
- Усулҳои `add_item(name, price)`, `remove_item(name)`, `get_total()`.
- `get_items()` нусхаи луғатро бармегардонад.

### 17. Синфи Library
- Рӯйхати хусусии `__books`.
- Усулҳои `add_book()`, `remove_book()`.
- `get_books()` нусхаи рӯйхатро бармегардонад (санҷед, ки тағйироти беруна ба аслӣ таъсир намекунад).

### 18. Синфи ATM
- `__pin` ва `__balance`-и хусусӣ.
- `withdraw(pin, amount)` PIN ва боқимондаро месанҷад.
- Пас аз 3 кӯшиши нодуруст корт басташавад.

### 19. Синфи Time
- `__hours` ва `__minutes`-и хусусӣ бо хусусиятҳо ва санҷиши доираҳо (0–23, 0–59).
- Усули `__str__` формати `HH:MM`-ро бармегардонад.

### 20. Синфи Inventory
- Луғати хусусии `__stock`.
- `add_stock(name, qty)` ва `remove_stock(name, qty)` (боқимонда манфӣ шуда наметавонад).
- `get_stock(name)`.

### 21. Синфи Logger
- Рӯйхати хусусии `__logs` ва усули хусусии `__format(msg)` (вақтро илова мекунад).
- `log(msg)`-и оммавӣ `__format`-ро истифода мебарад.
- `get_logs()` нусха бармегардонад.

### 22. Синфи Email
- Хусусияти `address` бо санҷиш: `@` ва `.` дорад.
- Хусусияти `domain` — танҳо геттер (қисми баъд аз `@`).

### 23. Синфи Stack
- Рӯйхати хусусии `__data`.
- Усулҳои `push()`, `pop()` (агар холӣ бошад, хатогӣ), `peek()`, `size()`, `is_empty()`.

### 24. Синфи BankAccount бо таърих
- `__balance` ва `__transactions`-и хусусӣ.
- `deposit()` ва `withdraw()` амалҳоро дар таърих сабт мекунанд.
- `get_history()` нусха бармегардонад.

### 25. Синфи абстрактии Shape
- `ABC` ва `@abstractmethod`-ро истифода баред: усулҳои `area()` ва `perimeter()`.
- `Circle` ва `Rectangle`-ро амалӣ намоед.
- Рӯйхати шаклҳоро эҷод кунед ва масоҳати умумиро ҳисоб кунед.
- Ҳангоми кӯшиши эҷоди `Shape()` `TypeError`-ро нишон диҳед.

### 26. Синфи абстрактии Animal
- Усулҳои абстрактии `speak()` ва `move()`.
- `Dog` ва `Bird`-ро амалӣ намоед.
- Дар давр ҳарду усулро барои рӯйхати ҳайвонот даъват кунед.

### 27. Синфи абстрактии Payment
- Усули абстрактии `pay(amount)`.
- `CardPayment` (бо лимит) ва `CashPayment`.
- Функсияи `checkout(payment, amount)` бо ҳар гуна усули пардохт кор мекунад.

### 28. Синфи абстрактии Vehicle
- Усулҳои абстрактии `start()` ва `stop()`.
- Хусусияти абстрактии `fuel_type`.
- `Car` ва `ElectricCar`-ро амалӣ намоед.

### 29. Синфи абстрактии Employee
- Усули абстрактии `calculate_salary()`.
- `FullTime` (меъёри собит) ва `PartTime` (соат × меъёр).
- Фонди умумии маошро барои рӯйхати кормандон ҳисоб кунед.

### 30. Синфи абстрактии Notifier
- Усули абстрактии `send(message)`.
- Амалисозиҳо: `EmailNotifier`, `SmsNotifier`, `TelegramNotifier`.
- Функсияи `notify_all(notifiers, message)`.

### 31. Синфи абстрактии Storage
- Усулҳои абстрактии `save(key, value)` ва `load(key)`.
- `MemoryStorage` (луғат) ва `FileStorage` (файли JSON).

### 32. Синфи абстрактии Parser
- Усули абстрактии `parse(text)`.
- `JsonParser` ва `CsvParser` (варианти оддӣ) рӯйхат/луғат бармегардонанд.

### 33. Синфи абстрактии Sorter
- Усули абстрактии `sort(data)`, ки рӯйхати аслиро тағйир намедиҳад.
- `BubbleSorter` ва `SelectionSorter`-ро амалӣ намоед ва натиҷаҳоро муқоиса кунед.

### 34. Синфҳои Student ва Group
- `Student` бо рӯйхати хусусии `__grades` ва усулҳои `add_grade()` ва `average()`.
- `Group` бо рӯйхати хусусии донишҷӯён ва усулҳои `add_student()` ва `best_student()`.

### 35. Усули қолабӣ (template method)
- Синфи абстрактии `DataProcessor` бо `read()` ва `process()`-и абстрактӣ ва `save()`-и муайян.
- Усули `run()` онҳоро пай дар пай даъват мекунад.
- Ду меросгирро амалӣ намоед.

## 🔴 Сатҳи 3: Пешрафта

### 36. Фармоиш бо тахфифҳо
- Синфи абстрактии `Discount` бо усули `apply(price)`.
- `PercentDiscount` ва `FixedDiscount`.
- `Order` бо рӯйхати хусусии маҳсулот, усулҳои `set_discount()` ва `get_final_price()`.

### 37. Ҳисобҳои бонкӣ
- Синфи абстрактии `Account` бо `__balance`-и хусусӣ ва усулҳои `deposit()`, `withdraw()`, `get_balance()`.
- `SavingsAccount` (усули `add_interest()`).
- `CheckingAccount` (ҳадди овердрафт).
- Балансро бе усулҳо тағйир додан мумкин нест.

### 38. Config-и тағйирнопазир
- Синфи `Config`, ки қиматҳояш пас аз эҷод тағйир намеёбанд (тавассути `__setattr__` ё хусусиятҳо).
- Усули `to_dict()` нусха бармегардонад.
- Кӯшиши тағйир додани қимат `AttributeError` медиҳад.

### 39. Системаи плагинҳо
- Синфи абстрактии `Plugin` бо хусусияти `name` ва усули `run()`.
- `PluginManager` бо феҳристи хусусӣ ва `register()`, `run_all()`, `names()`-и оммавӣ.
- Сабти плагинҳоро бо номи такрорӣ манъ кунед.

### 40. Пойгоҳи додаи абстрактӣ
- Синфи абстрактии `Database`: `connect()`, `execute(query)`, `close()`.
- Ду амалисозии тақлидӣ (`FakeSqlite`, `FakeMysql`).
- Дастгирии `with` (`__enter__`/`__exit__`)-ро дар синфи асосӣ амалӣ намоед.

### 41. Қаҳрамонҳои бозӣ
- Синфи абстрактии `Character` бо `__hp`-и хусусӣ.
- Усулҳои `take_damage()`, `is_alive()` ва `attack()`, `defend()`-и абстрактӣ.
- `Warrior` ва `Mage`-ро амалӣ намоед ва ҷангро то ғалабаи яке гузаронед.

### 42. Хусусияти абстрактӣ ва classmethod
- Синфи абстрактии `Document` бо хусусияти абстрактии `extension` ва `@classmethod from_string(text)`-и абстрактӣ.
- `TextDocument` ва `MarkdownDocument`-ро амалӣ намоед.

### 43. Duck typing ва Protocol
- Интерфейси `Drawable`-ро тавассути `typing.Protocol` тавсиф кунед.
- Ду синфи алоқаманднабуда эҷод кунед, ки ҳар кадом `draw()` дорад.
- Функсияи `render(items)` бо ҳар объекти ба протокол мувофиқ кор мекунад.

### 44. Пайдарпайии худӣ
- Синферо дар асоси `collections.abc.Sequence` амалӣ намоед (`__getitem__`, `__len__`).
- Санҷед, ки `len()`, итератсия, `in`, `reversed()` кор мекунанд.
- Маълумоти дохилӣ хусусӣ аст.

### 45. Singleton Settings
- Синфи `Settings` бо атрибути хусусии синфии `__instance`.
- Усули `get_instance()` ҳамеша як объектро бармегардонад.
- Кӯшиши мустақиман эҷод кардани нусхаи дуюм хатогӣ медиҳад.

### 46. Дескриптори санҷиш
- Дескриптори `PositiveNumber`-ро нависед (санҷиши > 0).
- Онро дар синфи `Product` барои майдонҳои `price` ва `quantity` истифода баред.
- Паёми хатогӣ бояд номи майдонро дошта бошад.

### 47. Системаи мактаб
- Синфи абстрактии `Person` бо усули `describe()`.
- `Student` бо баҳоҳои хусусӣ ва `Teacher` бо маоши хусусӣ.
- Ҳисобот танҳо бо усулҳои оммавӣ сохта мешавад.

### 48. Бонк ва интиқолҳо
- Синфи `Bank` бо луғати хусусии ҳисобҳо.
- Усулҳои `open_account()`, `transfer(from_id, to_id, amount)`.
- Агар интиқол нагирад, балансҳои ҳарду ҳисоб бетағйир мемонанд.

### 49. Китобхона бо хонандагон
- Синфи абстрактии `Item` бо `Book` ва `DVD` (ҳар кадом мӯҳлати худро дорад).
- `Member` бо рӯйхати хусусии ашёи гирифташуда (ҳадди аксар 3).
- Усулҳои `borrow(item)` ва `return_item(item)`.

### 50. Мини-лоиҳа: таваққуфгоҳ
- Синфи абстрактии `Vehicle` бо усули абстрактии `fee(hours)`; `Car`, `Truck`, `Motorcycle`.
- `ParkingLot` бо рӯйхати хусусии ҷойҳо, усулҳои `park(vehicle)` ва `leave(vehicle, hours)`.
- Ҷои банд такроран гирифта намешавад; `leave` маблағи пардохтро бармегардонад.
