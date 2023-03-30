class Alumno:
    def __init__(self, nombre, nota):#Constructor
        self.nombre=nombre
        self.nota=nota
        print(f'Se ha creado el alumno {self.nombre} con éxito.')

    def calificacion(self):
        if self.nota >= 5:
            return f'El alumno {self.nombre} ha aprobado con un {self.nota}.'
        else:
            return f'El alumno {self.nombre} ha suspendido con un {self.nota}.'
        
    def __str__(self):
        return f'Alumno: {self.nombre}, Nota: {self.nota}'

    