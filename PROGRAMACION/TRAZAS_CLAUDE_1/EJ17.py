total = 5
for i in range(2, 20, 4):
    if total % 2 == 0:
        total = total + i
    elif i % 3 == 0:
        total = 1
    else:
        total = total + 2
print(total)