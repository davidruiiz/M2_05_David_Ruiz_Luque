#1) Realiza un programa que lea tres números por teclado y permita evaluar lo siguiente:
#Si los números están en orden ascendente
#Si los números no están en orden ascendente
#Si hay un error debido a que el primer número introducido es 0

def evaluar_tres_numeros(num1,num2,num3):
    if num1==0:
        return "Error"
    elif num1<num2<num3:
        return "Los números están en orden ascendente."
    else:
        return "Los números no están en orden ascendente."

#Ejemplos
print(evaluar_tres_numeros(0,0,1))
print(evaluar_tres_numeros(1,0,1))
print(evaluar_tres_numeros(1,2,3))
print(evaluar_tres_numeros(3,2,1))

#2) Realiza el ejercicio anterior pero introduciendo los numeros en una lista:

def evaluar_tres_numeros_lista(numeros : list[float]):
    if numeros[0]==0:
        return "Error"
    elif numeros[0]<numeros[1]<numeros[2]:
        return "Los números están en orden ascendente."
    return "Los números no están en orden ascendente."


 #Ejemplos
print(evaluar_tres_numeros_lista([0,0,0]))
print(evaluar_tres_numeros_lista([1,0,1]))
print(evaluar_tres_numeros_lista([1,2,3]))
print(evaluar_tres_numeros_lista([3,2,1]))
print(evaluar_tres_numeros_lista([2.3,2.4,2.5]))


#3) Realiza un programa que lea letras y cuente con una variable contador las letras "a" que se introducen.
# Para salir del programa, introducir el carácter ".". 
# Al finalizar mostrar el número de veces que se ha pulsado la letra "a".

def cuenta_letras(texto:str):
    contador=0
    for i in range(len(texto)):
        if texto[i]=='.':
            break
        if texto[i]=='a':
            contador+=1
    return contador

#Ejemplos
print(cuenta_letras('ayer me comí una hamburguesa.'))
print(cuenta_letras('ayer. me comí una hamburguesa.'))

#4) Crea una lista de palabras, recorre la lista y muestra cada palabra junto con su longitud.
# Al final, indicar cual fue la palabra con más caracteres.

lista_palabras=['cama','escritorio','silla','mesa','lápiz']

for index in range(len(lista_palabras)):
    print(lista_palabras[index] ,len(lista_palabras[index]))

longitud_mayor=0
palabra_mas_larga=[]

for palabra in lista_palabras:
    if len(palabra)>longitud_mayor:
        longitud_mayor=len(palabra)
        palabra_mas_larga=palabra

print("La palabra con más caracteres es:\n",palabra_mas_larga)

