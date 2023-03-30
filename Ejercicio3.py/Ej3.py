class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f'Se ha creado el alumno {self.nombre} con éxito.')
    
    def calificacion(self):
        if self.nota >= 5:
            print(f'El alumno {self.nombre} ha aprobado con un {self.nota}.')
        else:
            print(f'El alumno {self.nombre} ha suspendido con un {self.nota}.')

alumno1 = Alumno('David', 7)
alumno1.calificacion()

