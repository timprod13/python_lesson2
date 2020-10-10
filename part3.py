season_list = ["Зима", "Весна", "Лето", "Осень"]
season_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
month = int(input("Введите месяц в виде целого числа от 1 до 12 "))
answer = "Данный месяц относится ко времени года"
if 1 <= month <= 2 or month == 12:
    print(f"{answer} {season_dict.get(1)}")
    print(f"{answer} {season_list[0]}")
elif 3 <= month <= 5:
    print(f"{answer} {season_dict.get(2)}")
    print(f"{answer} {season_list[1]}")
elif 6 <= month <= 8:
    print(f"{answer} {season_dict.get(3)}")
    print(f"{answer} {season_list[2]}")
elif 9 <= month <= 11:
    print(f"{answer} {season_dict.get(4)}")
    print(f"{answer} {season_list[3]}")
else:
    print("Введено неправильное число")
