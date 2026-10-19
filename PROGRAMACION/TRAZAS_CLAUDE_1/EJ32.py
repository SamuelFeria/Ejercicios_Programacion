total = 0
for i in range(25, 4, -5):
    if i % 10 == 0:
        total = total + i
    elif i % 3 == 0:
        total = total - 1
    else:
        total = total + 1
print(total)