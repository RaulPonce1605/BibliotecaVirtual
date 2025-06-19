import requests

BASE_URL = "http://localhost:5000"  # Cambia si tu backend está en otro host o puerto

def verificar_credenciales(email, contraseña):
    """
    Envía email y contraseña al backend y retorna True si es válido.
    """
    try:
        datos = {"email": email, "password": contraseña}
        response = requests.post(f"{BASE_URL}/login", json=datos)
        response.raise_for_status()
        resultado = response.json()
        return resultado.get("valido", False)
    except requests.RequestException as e:
        print("❌ Error al verificar login:", e)
        return False

def registrar_alumno(datos):
    """
    Envía un diccionario con los datos del alumno al backend.
    """
    try:
        response = requests.post(f"{BASE_URL}/alumnos", json=datos)
        response.raise_for_status()
        return response.json()  # Puede ser {"mensaje": "...", "status": "ok"}
    except requests.RequestException as e:
        print("❌ Error al registrar alumno:", e)
        return None


def registrar_materia(datos):
    """
    Envía los datos de la materia al backend.
    """
    try:
        response = requests.post(f"{BASE_URL}/materias", json=datos)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al registrar materia:", e)
        return None


def registrar_profesor(datos):
    """
    Envía los datos del profesor al backend.
    """
    try:
        response = requests.post(f"{BASE_URL}/profesores", json=datos)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al registrar profesor:", e)
        return None

def registrar_calificacion(datos):
    """
    Envía los datos de la calificación al backend.
    """
    try:
        response = requests.post(f"{BASE_URL}/calificaciones", json=datos)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al registrar calificación:", e)
        return None

def obtener_boleta(nombre_alumno):
    """
    Solicita la boleta del alumno al backend.
    """
    try:
        response = requests.get(f"{BASE_URL}/boletas/{nombre_alumno}")
        response.raise_for_status()
        return response.json()  # Se espera una lista de materias y promedios
    except requests.RequestException as e:
        print("❌ Error al obtener boleta:", e)
        return None

def obtener_lista_alumnos():
    try:
        response = requests.get(f"{BASE_URL}/alumnos")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al obtener alumnos:", e)
        return []

def obtener_lista_profesores():
    try:
        response = requests.get(f"{BASE_URL}/profesores")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al obtener profesores:", e)
        return []

def obtener_lista_materias():
    try:
        response = requests.get(f"{BASE_URL}/materias")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("❌ Error al obtener materias:", e)
        return []
