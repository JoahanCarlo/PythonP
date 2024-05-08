
# Indexing

texto = "Ella sabe python"
print(texto[0])
print(texto[1])
#print(texto[100])

size = len(texto)
print('size => ', size)
print(texto[size-1])
print(texto[-1])

# Slicing

print(texto[0:4])
print(texto[10:14])
print(texto[0:10])

print(texto[5:-1])
print(texto[:])
print(texto[::-1])