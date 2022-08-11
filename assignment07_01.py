# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
data = {
	'colors': ['red', 'green', 'blue', 'purple'],
  	'fruits': ['pineapple', 'orange', 'banana'],
  	'clothes': ['coat', 'tshirt']
}
data = {v: k for k in data.keys() for v in data[k]}
print(data)

# Завдання: перебудувати словник таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника. Вирішити за допомогою dict
#           comprehensions.

