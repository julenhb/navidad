import math
max=21
espacio=5
j=1

for i in range(0,max,2):

    linea=(espacio+math.ceil(max/2)-j)*" "
    linea+=i*"*"
    j+=1
    print(linea)

linea=(espacio+math.ceil(max/2)-3)*" "
linea+=4*"*"
print(linea)
print(linea)

