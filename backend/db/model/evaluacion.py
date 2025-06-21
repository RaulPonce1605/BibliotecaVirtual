class evaluacion:
    def __init__(self, id, alumno, materia, cal1, cal2, cal3,):
        self.id = id
        self.alumno = alumno
        self.materia = materia
        self.cal1 = cal1
        self.cal2 = cal2    
        self.cal3 = cal3

    def __repr__(self):
        return f"Evaluacion(id={self.id}, alumno={self.alumno}, materia={self.materia}, cal1={self.cal1}, cal2={self.cal2}, cal3={self.cal3})"