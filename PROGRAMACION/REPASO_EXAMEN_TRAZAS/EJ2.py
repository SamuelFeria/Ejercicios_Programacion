n = int(input("Número: "))
factorial = 1
i = n
while i > 1:
    factorial = factorial * i
    i = i - 1
print(n, "! =", factorial)
