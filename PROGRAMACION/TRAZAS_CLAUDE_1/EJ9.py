total = 10
for i in range(20, 3, -4):
    if i % 3 == 0:
        total = total + i
    else:
        total = total - 1
print(total)