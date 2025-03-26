#Determina el mayor de tres numeros ingresados por el usuario

def ingresar_datos():
    return [int(input(f"Ingrese el {i+1}° número: ")) for i in range(3)]

lista_numeros=ingresar_datos()

mayor_numero=lista_numeros[0]
for i in range(1,len(lista_numeros)):
   if mayor_numero<lista_numeros[i]: mayor_numero = lista_numeros[i]

#mayor_numero= max(lista_numeros)

print("Lista numeros: ",end=' ')
for i in lista_numeros: print(i, end=" ")
print()
print(f"El numero mayor en la lista es: {mayor_numero}")