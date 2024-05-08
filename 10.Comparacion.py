
#Comparación de números flotantes

x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x==y)

y_f = format(y,".2g")
print('str =>', y_f)

print(x == y_f)

print('*'*10)

print(x, y_f)

tolerance = 0.0001
print(abs(x-y) < tolerance)