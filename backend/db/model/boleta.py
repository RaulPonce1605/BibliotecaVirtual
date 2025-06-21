class Boleta:
    def __init__(self, alumno, promedio, fecha):
        self.alumno = alumno
        self.promedio = promedio
        self.fecha = fecha

    def __repr__(self):
        return f"Boleta(alumno={self.alumno}, promedio={self.promedio}, fecha={self.fecha})"
