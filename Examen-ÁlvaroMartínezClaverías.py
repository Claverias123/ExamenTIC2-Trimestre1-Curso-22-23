'''
4- Crea una función que NO reciba ningún parámetro y que imprima por pantalla las opciones: 1-Sumar 2-Salir
5- Crea una función que reciba dos números y devuelva la suma de estos números.
6- El programa principal tiene que mostrar el menú de la función y hasta que se pulse la opción 2-Salir el programa tiene que funcionar.
7- Si se pulsa la opción 1, el programa pide al usuario dos números y con la ayuda de la función sumar mostrar por pantalla el resultado.
8- Cuando el usuario introduce dos números se puede equivocar e introducir caracteres con lo que el programa se interrumpe. Realiza los cambios necesarios para controlar estos errores.
9- Sube los cambios a tu repositorio y copia la dirección en la entrega del examen.
'''
n=()
#4
def menu():
    print("1-Sumar")
    print("2-Salir")
#5
def sumar(num1,num2):
    suma=num1+num2
    return suma  
#6

while n!=2:
    try:
        menu()
        n=int(input("Que quieres hacer\n"))
        if n==1:
            num1=int(input("Dime el primer numero: "))
            num2=int(input("Dime el segundo numero: "))
            print("El resultado es:",sumar(num1,num2))
    except:
        print("Has puesto una letra, tiene que ser un numero")        
if n==2:
    print("Has salido del programa")

