materia ={
    "nombre": "Programación",
    "codigo": "INF20"
    "profesor": "mari garcria",
    "horarios": ["lunes 9:00-11:00","miercoles 9:00-11:00"],
    "creditos": 8,
    "nivel": "intermedio",
    "prerequisitos": ["computación 1"],
    "descripción": "desarrollo de algoritmos"}

print(materia["profesor"])
alumno = {
    "nombre": "saira guajardo alemán",
    "matricula":"A123456789",
    "edad":17,
    "semestre": "quinto",
    "calificaciones": {
        "matematicas": 8.5,
        "fisica": 9.0,
        "programacion": 9.5,
        "Quimica": 8.8,
    },
    "direccion": {
        "calle": "col. lomas 2 #230",
        "ciudad": "calera",
        "codigo_postal": "12345",
    },
    "telefono": "4781143027",
    "email": "sguajardoalemanq@gmail.com"
}
print(alumno["nombre"])
print(alumno["calificaciones"])

print("la calificacion es: ")
print(alumno["calificacoines"]["programacion"])