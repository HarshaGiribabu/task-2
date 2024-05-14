number = 1
max_number = 20
rows = 6

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
        if number > max_number:
            break
    print()
    if number > max_number:
        break
