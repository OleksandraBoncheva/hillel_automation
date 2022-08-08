# Завдання: порахуйте кількість літер строки. Строка та літера
#           даються на вхід користувачем. В залежності від кількости
#           виведіть на екран поясненя: строка містить літеру "с" до 
#           10 разів, строка містить літеру "с" до 20 разid, строка містить
#           символ "c" більше 20 разів. Проінформуйте користувача якщо
#           введено більше ніж одну літеру (літера має довжину більше 1)
#           або повідомляти якщо такої літери взагалі не знайдено.
#
# Підказка:
# * input() - ввод від користувача
# * len(str) - довжина строки
# * str.count(letter) - підрахунок елементів (літер) letter
# * if - elif - else - для логіки виводу на екран
#
# Приклад:
# Введіть текст: Це якийсь рандомний текст
# Введіть літеру: й
# Строка містить літеру "й" до 10 разів.
#
# Введіть текст: аааааааааааааааааааааааа
# Введіть літеру: а
# Строка містить літеру "а" більше 20 разів.

String = input("Введіть текст: ")
Letter = input("Введіть літеру: ")
str_count = String.count(Letter)

if str_count > 1:
    print(f"Строка містить літеру {Letter}")
if 0 < str_count < 10:
    print(f"Строка містить літеру {Letter} до 10 разів")
elif 10 <= str_count < 20:
    print(f"Строка містить літеру {Letter} до 20 разів")
elif 20 <= str_count:
    print(f"Строка містить літеру {Letter} більше 20 разів")
else:
    print(f"Літери {Letter} немає у введенній строці")

