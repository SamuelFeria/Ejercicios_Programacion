total = 0
for i in range(1, 10, 3):
    if total % 2 == 0:
        total = total + i
        if i % 2 == 0:
            total = total - 1
        else:
            total = total + 2
    else:
        print(total + i)
print(total)