for i in range(2, 13, 3):
    match i % 5:
        case 0:
            print(i, "cero")
        case r if r > 2:
            print(i, "grande", r)
        case r:
            print(i, "pequeño", r)
print("Terminado")