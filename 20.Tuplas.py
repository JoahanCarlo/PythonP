#Tuplas

numeros =(1,2,3,4,5)
string = ('Horacio','Juan','Miguel')
print(numeros[0])
print('-1 => ',numeros[-1])
print(type(numeros))

print(' 2 =>',string[2])
print(type(string))

#Crud
#numeros.append(10)
#numeros[1] = 'change'
print(numeros)

print(string.index('Juan'))

print(string.count('miguel'))

my_list = list(string)
print(my_list)
print(type(my_list))

my_list[1] = 'Ana Karina'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)