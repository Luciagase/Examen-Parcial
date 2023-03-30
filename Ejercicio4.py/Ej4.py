class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f'Se ha creado el alumno {self.nombre} con éxito.')
    
    def calificacion(self):
        if self.nota >= 5:
            return f'El alumno {self.nombre} ha aprobado con una nota de {self.nota}.'
        else:
            return f'El alumno {self.nombre} ha suspendido con una nota de {self.nota}.'
    
    def __str__(self):
        return f'Alumno: {self.nombre}, Nota: {self.nota}'

alumno1 = Alumno('David', 7)
print(alumno1)
alumno2 = Alumno('Marieta', 4)
print(alumno2)
