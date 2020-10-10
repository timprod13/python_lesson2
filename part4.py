input_str = input("Введите текст ")
res_lst = []
count = 1
for el in range(input_str.count(' ') + 1):
    res_lst = input_str.split()
    print(f" {count}. {res_lst [el] [0:10]}")
    count += 1
