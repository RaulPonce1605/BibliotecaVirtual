

class Alumno:
    def __init__(self, nombre, apellido, email):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __repr__(self):
        return f"Alumno(id_alumno={self.id_alumno}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
    
