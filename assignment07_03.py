# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#
# підказка:
#  %= N  # compound assignment

N = int(input("N = "))
K = int(input("K = "))

list = [K for K in range(N)]
del list[::K]

print(list)
