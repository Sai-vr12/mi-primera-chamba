#crear funciones

#funcion llamada saludar, va a recibir el nombre
def saludar(nombre):
    print("holaaaaaa", nombre)

nom=input("ingresa tu nombre")
saludar(nom)

#funcion llamada sumita, va arecibir 5 numeros
#va a regresar el valor de la suma
def sumita(n1,n2,n3,n4,n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma

num1=int(input("ingresa el primer numero"))
num2=int(input("ingresa el segundo numero"))
num3=int(input("ingresa el tercer numero"))
num4=int(input("ingresa el cuarto numero"))
num5=int(input("ingresa el quinto numero"))

#mandar a llamar a la funcion/ usarla
print(sumita(num1,num2,num3,num4,num5))

#crear una funcion llamada area_triangulo
#que reciba base y altura
#regrese el resultado del area 
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#usar la funcion
print(area_triangulo(4,5))

#####ejercicios
'''1)Crear una funcion llamada multiplicar que reciba 3 numeros, regresar el resultado'''

def multiplicar(num1,num2, num3):
    resultado=num1*num2*num3 
    return resultado
#usar la funcion
print(multiplicar(4,5,6))
'''2)crear una funcion llamada largo_cadena que reciba un texto y devuelva la cantidad de caracteres de la misma len()'''

def largo_cadena(texto):
    cantidad=len(texto)
    return cantidad
#usar funcion
print(largo_cadena("el mundo es bonito"))
'''3)crear una funcion llamada promedio que reciba 2 calificaciones y devuelva el promedio'''

#pedir calif. primer y segundo parcial

def promedio(calif1, calif2):
    resultado=(calif1+calif2)/2
    return resultado
    cal1=float(input)(("ingresa calif1"))
    cal2=float(input("ingresa calif2"))
    print("el promedio es: ", promedio(cal1, cal2))

    #crear una funcion que reciba el nombre
    #de la persona, su edad y el mes de nacmiento
    #devuelva:
    #las dos primeras letras del nombre-edad-promedio
    #letra del mes
    #Ejemplo: MA170
    print("ingresa tu nombre: ")
    print("ingresa tu edad: ")
    

    def disk_Curp(nombre,edad,mes):
        letras=nombre[0:2]
        print(letras)

        disk_Curp("saira", 30, "octubre")