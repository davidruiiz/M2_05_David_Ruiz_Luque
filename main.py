#1) Realiza un programa que lea tres números por teclado y permita evaluar lo siguiente:
#Si los números están en orden ascendente
#Si los números no están en orden ascendente
#Si hay un error debido a que el primer número introducido es 0

def evaluar_tres_números(num1,num2,num3):
    if num1==0:
        return "Error"
    elif num1<num2<num3:
        return "Los números están en orden ascendente."
    else:
        return "Los números no están en orden ascendente."

#Ejemplos
print(evaluar_tres_números(0,0,1))
print(evaluar_tres_números(1,0,1))
print(evaluar_tres_números(1,2,3))
print(evaluar_tres_números(3,2,1))


