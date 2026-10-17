for i in range(1, 8):
    match i % 4:
        case 0:
            print(i, "cero")
        case r if r < 3:
            print(i, "pequeño", r)
        case _:
            print(i, "otro")
print("Terminado")