class Materia:
    def __init__(self, nombre, profesor, area,material):
        self.nombre = nombre
        self.profesor = profesor
        self.area = area
        self.material = material

    def __repr__(self):
        return f"Materia(nombre='{self.nombre}', profesor='{self.profesor}', area='{self.area}', material='{self.material}')"
