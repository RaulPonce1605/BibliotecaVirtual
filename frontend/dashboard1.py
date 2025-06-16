from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtGui import QColor
from dashboard_ui import Ui_MainWindow
import sys

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Dashboard Biblioteca")
        self.resize(1000, 700)
        self.setMinimumSize(800, 600)

        self._maximized = False  # Estado actual de la ventana

        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(0)

        # Animación de aparición
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.start()

        # Efecto sombra
        self.sombra_frame(self.ui.frame_2)

        # Página inicial
        self.ui.stackedWidget.setCurrentIndex(0)

        # Ocultar flecha derecha al inicio
        self.ui.bt_menu_dos.hide()

    def setup_connections(self):
        # Botones de navegación
        self.ui.bt_uno.clicked.connect(self.abrir_registro_usuario)
        self.ui.bt_dos.clicked.connect(self.abrir_registro_material)
        self.ui.bt_tres.clicked.connect(self.abrir_registro_prestamos)
        self.ui.bt_cuatro.clicked.connect(lambda: self.cambiar_pagina(3))

        # Menú lateral
        self.ui.bt_menu_uno.clicked.connect(self.toggle_menu)
        self.ui.bt_menu_dos.clicked.connect(self.toggle_menu)

        # Botones de ventana
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_cerrar_2.clicked.connect(self.close)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_restaurar)
        self.ui.bt_restaurar.clicked.connect(self.maximizar_restaurar)

    def sombra_frame(self, widget):
        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(20)
        sombra.setXOffset(0)
        sombra.setYOffset(0)
        sombra.setColor(QColor(0, 0, 0, 120))
        widget.setGraphicsEffect(sombra)

    def toggle_menu(self):
        width = self.ui.frame_2.width()
        normal = 0
        extender = 300

        if width == 0:
            final_width = extender
            self.ui.bt_menu_uno.hide()
            self.ui.bt_menu_dos.show()
        else:
            final_width = normal
            self.ui.bt_menu_uno.show()
            self.ui.bt_menu_dos.hide()

        self.animacion = QPropertyAnimation(self.ui.frame_2, b"maximumWidth")
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(final_width)
        self.animacion.setDuration(400)
        self.animacion.setEasingCurve(QEasingCurve.Type.InQuad)
        self.animacion.start()

    def cambiar_pagina(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)
        titulos = ["Registrar Usuario", "Registrar Material", 
                   "Préstamos/Devoluciones", "Reportes"]
        self.ui.label.setText(titulos[index])

    def maximizar_restaurar(self):
        if self._maximized:
            self.showNormal()
            self._maximized = False
        else:
            self.showMaximized()
            self._maximized = True

    def abrir_registro_usuario(self):
        from registro_usuario import RegistroApp
        self.registro_window = RegistroApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def abrir_registro_material(self):
        from registro_material import RegistroMaterialApp
        self.registro_window = RegistroMaterialApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()

    def abrir_registro_prestamos(self):
        from registro_prestamosdev import RegistroPrestamosDevApp
        self.registro_window = RegistroPrestamosDevApp(dashboard_window=self)
        self.hide()
        self.registro_window.show()