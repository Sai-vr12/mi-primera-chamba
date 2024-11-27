opcion=1
#En un ciclo while realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
    num1=int(input("ingresa el primer numero"))
    num2=int(input("ingresa el segundo numero"))
    print("ingresa 1. sumar")
    print("ingresa 2. restar")
    print("ingresa 3. multiplicar")
    print("ingresa 4. dividir")
    op=int(input("¿que operacion quieres hacer con los numeros?"))
    if (op==1):
        res=num1+num2
        print("la suma de los numeros  es: ", res)
    elif(op==2):
        res2=num1-num2
        print("la resta es: ", res2)
    elif(op==3):
        res3=num1*num2
        print("la multiplicacion de los numeros es: ", res3)
    elif(op==4):
        res4=num1/num2
        print("la division de los numeros es: ", res4)
    else:
        print("no valido")
    opcion=int(input("deseas continuar, sino presiona 0 para salir"))