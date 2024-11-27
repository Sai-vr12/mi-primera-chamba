print("holiii")
deportes=["futbol","voleibol","natacion","basquetbol"]
print(deportes)
print(deportes[2])
#posicion de natacion 
pos=deportes.index("natacion")
print("la  posicion de natacion es:",pos)

#agregar otro deporte al final
deportes.append("hanball")
print(deportes)
#para agregar elementos
deportes.append("2")
deportes.insert(2, "2eyyyy")

cantidad_saludos=int(input("cuantos saludos quieres?"))

for i in range(cantidad_saludos):
    print("hola")

num_deportes=int(input("cuantos deportes agregaras"))
for i in (range(num_deportes)):
    dep=input("ingresa el deporte ")
    deportes.append(dep)

    print(deportes)

    
