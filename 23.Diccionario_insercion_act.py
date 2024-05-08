#Diccionarios: inserción y actualización

persona = {
    'name' : 'Joahan',
    'last_name' : 'Nuñez',
    'langs' : ['python','java','php'],
    'age' : 32
}

print(persona)

persona['name'] = 'Carlitos'
persona['age'] -= 23
persona['langs'].append('rust')
print(persona)

del persona['last_name']
print(persona)

persona.pop('age')
print(persona)


print('items')
print(persona.items())

print('keys')
print(persona.keys())

print('values')
print(persona.values())

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}
print(person)
person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
lista_per = list[person]
print(lista_per)
print(person)