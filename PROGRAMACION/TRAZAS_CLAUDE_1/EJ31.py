for i in range(1, 12, 3):
    match i % 5:
        case 0:
            print(i, "cero")
        case r if r >= 3:
            print(i, "grande", r)
        case _:
            print(i, "pequeño")
print("Fin")