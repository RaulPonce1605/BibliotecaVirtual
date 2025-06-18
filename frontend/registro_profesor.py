from PyQt6 import QtCore, QtWidgets
from registro_profesor_ui import Ui_Dialog

class RegistroApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexiones
        self.ui.pushButton_registrar.clicked.connect(self.registrar_profesor)
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_restaurar.clicked.connect(self.restaurar_ventana)

        self.maximizado = False

    def maximizar_ventana(self):
        self.showMaximized()
        self.maximizado = True

    def restaurar_ventana(self):
        self.showNormal()
        self.maximizado = False

    def cerrar_y_volver(self):
        self.close()
        if self.dashboard_window:
            self.dashboard_window.show()

    def registrar_profesor(self):
        materia = self.ui.comboBox_materia.currentText()
        nombre = self.ui.lineEdit_nombre.text()
        primer_apellido = self.ui.lineEdit_apellido.text()
        segundo_apellido = self.ui.lineEdit_segundo_Apellido.text()
        telefono = self.ui.lineEdit_Telefono.text()
        email = self.ui.lineEdit_Email.text()

        print("📘 Profesor Registrado:")
        print(f"Materia: {materia}")
        print(f"Nombre: {nombre}")
        print(f"Apellido Paterno: {primer_apellido}")
        print(f"Apellido Materno: {segundo_apellido}")
        print(f"Teléfono: {telefono}")
        print(f"Email: {email}")

        # Animación en el botón
        anim = QtCore.QPropertyAnimation(self.ui.pushButton_registrar, b"geometry")
        anim.setDuration(200)
        orig_geom = self.ui.pushButton_registrar.geometry()
        anim.setStartValue(orig_geom)
        anim.setKeyValueAt(0.5, QtCore.QRect(
            orig_geom.x() - 5, orig_geom.y() - 5,
            orig_geom.width() + 10, orig_geom.height() + 10
        ))
        anim.setEndValue(orig_geom)
        anim.start()
        self.anim_registrar = anim

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = RegistroApp()
    ventana.show()
    sys.exit(app.exec())
