#Métodos de listas

numeros = [1,2,3,4,5,6]
print(numeros[1])
numeros[-1] = 10
print(numeros)

numeros.append(700)
print(numeros)

numeros.insert(0,'Hola')
print(numeros)

numeros.insert(3,'Jueves')
print(numeros)

talks = ['todo 1','todo 2','tod 3']
nuevo = numeros + talks
print(nuevo)

n_index = nuevo.index('todo 2')
print(n_index)
nuevo[n_index]='Amores'
print(nuevo)

nuevo.remove('todo 1')
print(nuevo)

nuevo.pop()
print(nuevo)

nuevo.pop(0)
print(nuevo)

nuevo.reverse()
print(nuevo)


numeros1 = [1,2,8,4,3,0]
numeros1.sort()
print(numeros1)

strings = ['re','ab','ef','mn','wy']
strings.sort()
print(strings)

print(nuevo.sort())