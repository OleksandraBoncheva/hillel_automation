# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.
#
# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict

input_str = input("Введіть щось:")
len_str = len(input_str.split())
print(f"Кількість слів: {len_str}")

def words_count(input_str):
    counts1 = dict()
    dict_str = input_str.split()
    for word in dict_str:
        if word in counts1:
            counts1[word] += 1
        else:
            counts1[word] = 1
    return counts1
print(f"Статистика слів: {words_count(input_str)}")

def letter_count(input_str):
    counts2 = dict()
    for letter in input_str:
        if letter in counts2:
         counts2[letter] += 1
        else:
         counts2[letter] = 1
    return counts2
print(f"Статистика літер: {letter_count(input_str)}")
