total = 2
for i in range(0, 11, 3):
    if total % 2 == 0:
        total = total + i
        if i % 2 == 0:
            total = total + 1
        else:
            total = total - 1
    else:
        print(total + i)
print(total)