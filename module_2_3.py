meaning = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while len(my_list) > meaning:
    if my_list[meaning] < 0:
        break
    if my_list[meaning] > 0:
        print(my_list[meaning])
    meaning += 1