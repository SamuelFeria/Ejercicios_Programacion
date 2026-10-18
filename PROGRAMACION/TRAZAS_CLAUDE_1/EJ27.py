total = 1
for i in range(2, 15, 4):
    if total % 2 == 1:
        total = total + i
        if i % 3 == 0:
            total = total * 2
        else:
            total = total - 1
    else:
        print(total * i)
print(total)