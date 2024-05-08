
#Diccionarios: definición y lectura

my_dic = {}
print(type(my_dic))

my_dic = {
    'avion' : 'blabalaalal',
    'name' : 'Joahan',
    'apellido': 'Nuñez',
    'edad' : '34'
}
print(my_dic)
print(len(my_dic))
print(my_dic['name'])
print(my_dic['apellido'])
print(my_dic.get('edad'))

print('avion' in my_dic)
print('otrsero' in my_dic)