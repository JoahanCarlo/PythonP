#Loops: While    

'''
cont = 0
while cont <12:
    cont += 1
    print(cont)

n = int(input("Ingrese el número a multiplicar : "))
f = 0
while f<12:
    f += 1
    print(f"{n}x{f} = {n*f}")
    

cont = 1
while cont<23:
    cont +=1
    if cont == 10:
        break
    print(cont)

'''

cont = 1
while cont<23:
    cont +=1
    if cont == 10:
        continue
    print(cont)
    #el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente
    