#Ciclos anidados

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[2][0])

for row in matriz:
    print(row)
    for column in row:
        print(column)