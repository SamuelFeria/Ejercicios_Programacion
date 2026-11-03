num = "8445448"
capicua = True
pos = 0
posMedia = len(num)//2
while capicua and pos < posMedia:
    if num[pos] != num[len(num)-1-pos]:
        capicua = False
    pos = pos+1
print("¿Es capicua:?", capicua)

