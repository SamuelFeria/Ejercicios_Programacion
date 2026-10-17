for i in range( 6):
    match i % 3:
        case 0:
            print(i, "Fizz")
        case 1:
            print(i, "uno")
        case _:
            print(i, "otro")
print("Terminado")
