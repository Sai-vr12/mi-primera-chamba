#maestra, ya no aguanto ya no aguanto TwT
print("Hola polinesios")
opcion=1
while opcion!=0:
    print("ingresa 1. área del triangulo")
    print("ingresa 2. área del rectandgulo")
    print("ingresa 3. área del circulo")
    print("ingresa 4. convertir temperatura F a C")
    print("ingresa 5. convertir  temperatura C a F")
  
    op=int(input("¿Qué operacion vas a realizar?"))
    if(op==1):
        base=int(input("ingresa la base "))
        altura=int(input("ingresa la altura "))

        res1=base*altura/2
        print("el area del triangulo es: ",res1)
    elif(op==2):
        base=int(input("ingresa la base: "))
        altura=int(input("ingresa la base "))
        res2=base*altura
        print("el area del rectangulo es: ",res2)
    elif(op==3):
        radio=int(input("ingresa el radio: "))
        res3=3.1416*radio**2
        print("el area del circulo es: ",res3)
    elif(op==4):
        fahrenheit=int(input("ingresa los fahrenheit: "))
        res4=(fahrenheit-32)*5/9
        print("la temperatura el celcius es: ",res4)
    elif(op==5):
        celcius=int(input("ingresa los celcius: "))
        res5=(celcius*1.8)+32
        print("la temperatura en fahrenheit es:, ",res5)
else:
    print("no valido")
    opcion=int(input("deseas continuar,sino presiona 0 para salir"))