current_number = 0
while True:
    current_number += 1
    if current_number > 10:
        break
    if current_number % 2 == 0:
        continue
    print(current_number)
        