#Pedirle al usuario que ingrse un numero entero y que se muestren en pantalla los primeros 10 multiplos de ese numero
def multi(a,b)
  for x in range(1,b+1):
    print

n = int(input('porfavor ingrese un numero:'))
m = int(input('¿cuantos multiplos?:'))
for x in range(1,m+1):
    print(n*x)