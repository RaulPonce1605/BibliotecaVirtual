import json
from PyQt6 import QtCore, QtGui, QtWidgets
from registro_profesor_ui import Ui_Dialog
from servpeticiones import registrar_profesor, obtener_lista_materias  # Asegúrate de que este módulo exista y funcione correctamente

class RegistroApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        self.maximizado = False

        # Conexiones
        self.ui.pushButton_registrar.clicked.connect(self.registrar_profesor)
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_restaurar.clicked.connect(self.restaurar_ventana)

        # Validaciones en tiempo real
        solo_letras = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"))
        solo_numeros = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression("^[0-9]+$"))

        self.ui.lineEdit_nombre.setValidator(solo_letras)
        self.ui.lineEdit_apellido.setValidator(solo_letras)
        self.ui.lineEdit_segundo_Apellido.setValidator(solo_letras)
        self.ui.lineEdit_Telefono.setValidator(solo_numeros)
    
        datos = obtener_lista_materias()
        for materia in datos:
            self.ui.comboBox_materia.addItem(materia['nombre'])

    

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
       
        indexmat = self.ui.comboBox_materia.currentIndex()
        nombre = self.ui.lineEdit_nombre.text()
        primer_apellido = self.ui.lineEdit_apellido.text()
        segundo_apellido = self.ui.lineEdit_segundo_Apellido.text()
        telefono = self.ui.lineEdit_Telefono.text()
        email = self.ui.lineEdit_Email.text()

        datos = {
            "materia": {"idMateria": indexmat + 1},
            "nombre": nombre,
            "apellido": primer_apellido + " " + segundo_apellido,
            "telefono": telefono,
            "email": email
        } 

        respuesta = registrar_profesor(datos)

        if respuesta:
            QtWidgets.QMessageBox.information(self, "Éxito", "Profesor registrado correctamente.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo registrar el profesor.")

        # Animación visual del botón
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
