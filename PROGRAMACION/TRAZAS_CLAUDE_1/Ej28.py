total = 4
for i in range(1, 22, 5):
    if total % 2 == 0:
        total = total + i
    elif i % 3 == 0:
        total = total - 1
    else:
        total = total + 2
print(total)