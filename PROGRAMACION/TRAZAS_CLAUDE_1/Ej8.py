for i in range(2, 12, 3):
    match i % 4:
        case 0:
            print(i, "cero")
        case r if r < 2:
            print(i, "bajo", r)
        case _:
            print(i, "alto")
print("Fin")