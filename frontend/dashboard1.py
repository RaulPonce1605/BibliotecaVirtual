import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtGui import QColor
from dashboard_ui import Ui_MainWindow
from servpeticiones import obtener_lista_alumnos, obtener_lista_profesores, obtener_lista_materias  

# Importaciones de tus módulos
from registro_usuario import RegistroApp
from registro_materias import RegistroMateriaApp
from registro_prestamosdev import RegistroPrestamosDevApp

import sys


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Dashboard Biblioteca")
        self.resize(1000, 700)
        self.setMinimumSize(800, 600)

        self._maximized = False

        self.init_ui()
        self.setup_connections()


    def init_ui(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0)

        # Animación de entrada
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

        # Sombra
        self.sombra_frame(self.ui.frame_2)

        # Página inicial
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.bt_menu_dos.hide()

        self.actualizar_toolbox_labels()

    def setup_connections(self):
        # Botones de navegación lateral
        self.ui.bt_uno.clicked.connect(lambda: self.abrir_registro_usuario())
        self.ui.bt_dos.clicked.connect(lambda: self.abrir_registro_materia())
        self.ui.bt_tres.clicked.connect(lambda: self.abrir_calificaciones())
        self.ui.bt_cuatro.clicked.connect(lambda: self.boletas())
        self.ui.pushButton.clicked.connect(lambda: self.abrir_registro_profesor())

        # Menú lateral animado
        self.ui.bt_menu_uno.clicked.connect(self.toggle_menu)
        self.ui.bt_menu_dos.clicked.connect(self.toggle_menu)

        # Botones de control de ventana
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_cerrar_2.clicked.connect(self.close)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_restaurar)
        self.ui.bt_restaurar.clicked.connect(self.maximizar_restaurar)

        # Buscador
        self.ui.lineEdit.textChanged.connect(self.buscar_contenido)

    def sombra_frame(self, widget):
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(20)
        sombra.setXOffset(0)
        sombra.setYOffset(0)
        sombra.setColor(QColor(0, 0, 0, 120))
        widget.setGraphicsEffect(sombra)

    def toggle_menu(self):
        width = self.ui.frame_2.width()
        final_width = 300 if width == 0 else 0
        self.ui.bt_menu_uno.setVisible(final_width == 0)
        self.ui.bt_menu_dos.setVisible(final_width == 300)

        self.animacion = QPropertyAnimation(self.ui.frame_2, b"maximumWidth")
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(final_width)
        self.animacion.setDuration(400)
        self.animacion.setEasingCurve(QEasingCurve.Type.InQuad)
        self.animacion.start()

    def cambiar_pagina(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        titulos = ["Registrar Usuario", "Registrar Materia", "Préstamos/Devoluciones", "Reportes"]
        self.ui.label.setText(titulos[index])

    def maximizar_restaurar(self):
        if self._maximized:
            self.showNormal()
        else:
            self.showMaximized()
        self._maximized = not self._maximized

    def abrir_registro_usuario(self):
        self.registro_window = RegistroApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def abrir_registro_materia(self):
        self.registro_window = RegistroMateriaApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def abrir_calificaciones(self):
        self.registro_window = RegistroPrestamosDevApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def abrir_registro_profesor(self):
        from registro_profesor import RegistroApp
        self.registro_window = RegistroApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def boletas(self):
        from boletas import BoletaApp
        self.boleto_window = BoletaApp(dashboard_window=self)
        self.hide()
        self.boleto_window.show()

    def actualizar_toolbox_labels(self):
        # Alumnos
        alumnos = obtener_lista_alumnos()
        if not alumnos:
            texto_alumnos = "No hay alumnos registrados"
            self.ui.label_ventas.setText(texto_alumnos)


        texto_alumnos = ""
        for a in alumnos:
            print(a)
            texto_alumnos = texto_alumnos + "\n" + a["nombre"]
        self.ui.label_ventas.setText(texto_alumnos)

        # Profesores
        profesores = obtener_lista_profesores()
        if not profesores:
            texto_profesores = "No hay profesores registrados"
            self.ui.label_comentarios.setText(texto_profesores)

        texto_profesore = ""
        for p in profesores:
            print(p)
            texto_profesore = texto_profesore + "\n" + p["nombre"]
        self.ui.label_comentarios.setText(texto_profesore)

        # Materias
        materias = obtener_lista_materias()
        if not materias:
            texto_materias = "No hay materias registradas"
            self.ui.label_libros.setText(texto_materias)

        texto_materia = ""
        for e in materias:
            print(e)
            texto_materia = texto_materia + "\n" + e["nombre"]
        self.ui.label_libros.setText(texto_materia)

    def buscar_contenido(self, texto):
        texto = texto.lower()
        pagina_actual = self.ui.stackedWidget.currentIndex()

        if pagina_actual == 0:  # Alumnos
            alumnos = obtener_lista_alumnos()
            filtrados = [a for a in alumnos if texto in a.lower()]
            self.ui.label_ventas.setText("\n".join(filtrados) if filtrados else "No hay coincidencias.")

        elif pagina_actual == 1:  # Profesores
            profesores = obtener_lista_profesores()
            filtrados = [p for p in profesores if texto in p.lower()]
            self.ui.label_comentarios.setText("\n".join(filtrados) if filtrados else "No hay coincidencias.")

        elif pagina_actual == 5:  # Materias
            materias = obtener_lista_materias()
            filtrados = [m for m in materias if texto in m.lower()]
            self.ui.label_libros.setText("\n".join(filtrados) if filtrados else "No hay coincidencias.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DashboardWindow()
    ventana.show()
    sys.exit(app.exec())
