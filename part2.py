el_amount = int(input("Введите количество элементов списка "))
lst = []
i = 0
while i < el_amount:
    lst.append(int(input("Введите значение очередного элемента ")))
    i += 1
print(f"Введённый список: {lst}")
i = 0
for el in range(int(len(lst)/2)):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    i += 2
print(f"Полученный список: {lst}")


