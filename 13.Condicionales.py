
#Condicionales

pet = input("¿Cuál es tu mascota favorita ?")

if pet == 'perro':
    print('Excelente tienes un perro')

elif pet == 'gato':
    print("Tienes un lindo gatito")
    
elif pet == 'pez':
    print("Su nombre es nemo?")



stock = int(input('Digita el stock => '))
if stock<100:
    print("Usted no tiene promocion")
if stock>100:
    print("Usted se ha llevado la licuadora")
    

sueldo = float(input("Ingrese el sueldo : "))
if sueldo<100 and sueldo>50:
    print("Usted se lleva un parlante")
if sueldo>100:
    print("Usted se lleva un celular")
    
num = int(input("Ingresar número"))
if num%2==0:
    print("Es un numero par")
else:
    print("Es un numero impar")