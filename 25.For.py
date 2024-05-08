#Loops: For
'''
for element in range(1,20):
    print(element)
'''
my_list= [23,45,67,34,65]
for element in my_list:
    print(element)
    
my_tuple= ('luis','ana','franco','emilio')
for element in my_tuple:
    print(element)
    
producto = {
    'nombre':'Joahan',
    'apellido':'Nuñez Soto',
    'edad': 32
}
for key in producto:
    print(key, '=>' ,producto[key])
    
for key,value in producto.items():
    print(key,'=>',value)

people = [
    {
        'nombre': 'Luis',
        'edad': 23
    },
    {
        'nombre':'Ana',
        'edad': 34
    },
    {
        'nombre':'Miguel',
        'edad': 45
    }
]
for person in people:
    print('Nombre =>',person['nombre'])
    