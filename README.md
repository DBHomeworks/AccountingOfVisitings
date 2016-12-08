# Lab2DBXml
NonSQL databases, second lab

Завдання

1. Розробити схему бази даних на основі предметної галузі з ЛР№2-Ч1 у спосіб, що застосовується в СУБД MongoDB.
2. Розробити модуль роботи з базою даних на основі пакету PyMongo.
3. Реалізувати дві операції на вибір із використанням паралельної обробки даних Map/Reduce.
4. Реалізувати обчислення та виведення результату складного агрегативного запиту до бази даних з використанням функції aggregate() сервера MongoDB.

Варіант 

Основна сутність - таблиця відвідувань. Додаткова сутність - працівник.

Коди функцій Map/Reduce та aggregate()

map/reduce: знайти кількість людей, яка має те, чи інше хобі:
```
map = Code("""function map() {
                for(var i in this.interests) {
                    emit(this.interests[i], 1);
                        } 
              }""")
reduce = Code("function reduce(key, values) {
             var sum = 0;for(var i in values) {
                  sum += values[i];
             }
      return sum;
      }")
result = db.employee_info.map_reduce(map, reduce, "interests")
```
aggregate : знайти сумарну зарплату всіх робітників по компаніях.
```
salaries = employees.aggregate([
            {'$group': {'_id': "$workplace.company", 'salary': {'$sum': "$workplace.salary"}}},
            {'$sort': {'salary': 1}}
])
```
