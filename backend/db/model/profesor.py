class Profesor:
    def __init__(self, nombre, apellido, email):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __repr__(self):
        return f"Profesor(id_profesor={self.id_profesor}, nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')"
