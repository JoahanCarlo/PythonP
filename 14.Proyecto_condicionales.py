
#Proyecto: condicionales

opcion = input("Piedra papel o tijera => ")
opcion_computer = 'papel'

if opcion_computer == opcion:
    print('Empate !!!')
elif opcion == 'piedra':
    if opcion_computer == 'tijera':
        print('Gana papel !!!')
        print('El usuario gano')
    else:
        print('Papel gana a piedra !!!')
        print('Ganó la computadora')

elif opcion == 'papel':
    if opcion_computer == 'piedra':
        print('Papel gana a piedra !!!')
        print('El usuario gano')
    else:
        print('Tijera gana a papel')
        print('La computadora gano')

elif opcion == 'tijera':
    if opcion_computer == 'papel':
        print('La tijera gana a papel !!!')
        print('El usuario gano')

else:
    print('No existe la opcion !!')    

    


    