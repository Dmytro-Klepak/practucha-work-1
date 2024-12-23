# Створення змінних
message = "hello world"  # Текстова змінна
name = "Дмитро"  # Текстова змінна
surname = "Клепак"  # Текстова змінна
age = 16  # Числова змінна

# Виведення інформації про змінні
print("Змінна 'message' має тип:", type(message), "і значення:", message)
print("Змінна 'name' має тип:", type(name), "і значення:", name)
print("Змінна 'surname' має тип:", type(surname), "і значення:", surname)
print("Змінна 'age' має тип:", type(age), "і значення:", age)
count_int = 0
count_str = 0
count_bool = 0
count_set = 0
count_list = 0
count_tuple = 0
count_float = 0
lst_notnull = []
max_value = -1
types_count = {str, int, bool, set, list, tuple, float}
lst_count_types = [count_set, count_float, count_tuple, count_list, count_bool, count_str, count_int]
lst_name_type = ['set', 'float', 'tuple', 'list', 'bool', str, int]
lst = [name, surname, age]
for item in lst:
    if type(item) == int:
        lst_count_types[-1] += 1
    elif type(item) == str:
        lst_count_types[-2] += 1

for item in lst_count_types:
    if item != 0:
        lst_notnull.append(item)
    if len(lst_notnull) == 0:
        print('Good')
    else:
        if item == max_value:
            print('Not')
            break

        elif item > max_value:
            max_value = item

inn = lst_count_types.index(max_value)

print(lst_name_type[inn])

for item in lst:
    if type(item) != lst_name_type[inn]:
        lst.remove(item)

# if count_str==count_int:
#     print("good")
# if count_str>count_int:
#     remove: type(int) from lst:
