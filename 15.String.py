
#String recargado

texto = "Ella sabe programar en python"
print('JavaScript' in texto)
print('python' in texto)

if 'python' in texto:
    print("Elegiste bien")
    
if 'pro' in texto:
    print('Elegiste bien otra vez')
    
size = len(texto)
print(size)

print(texto)
print(texto.upper())
print(texto.lower())
print(texto.count('a'))

print(texto.swapcase())
print(texto.startswith('Ella'))
print(texto.endswith('python'))
print(texto.replace('python','html'))

texto2 = "este el el primer dia"
print(texto2.capitalize())