total = 2
for i in range(1, 20, 3):
    if i % 2 == 0:
        total = total + i
    elif i % 5 == 0:
        total = total - 1
    else:
        total = total + 1
print(total)