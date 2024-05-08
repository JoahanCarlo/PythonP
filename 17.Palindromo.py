# Palindromo 

palabra = input("Ingresar palabra a probar => ").lower()

if palabra == palabra[::-1]:
    print("Es palindromo ")

else:
    print("No es palindromo")
