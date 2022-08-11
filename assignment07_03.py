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

data = [i if K > N:
    K %= N for i in range(N) i % K != 0]
del list[::K]

print(list)

if word in counts1:
    counts1[word] += 1
else:
    counts1[word] = 1
    counts2 = dict()
    for i in input_str:
        counts2[i] = counts2.get(i, 0) + 1