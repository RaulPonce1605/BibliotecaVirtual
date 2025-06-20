from PyQt6 import QtCore, QtGui, QtWidgets
from registro_materia_ui import Ui_Dialog
from servpeticiones import registrar_materia, obtener_lista_profesores  # Asegúrate de que este módulo exista y funcione correctamente


class RegistroMateriaApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        self.maximizado = False

        # Conexiones de botones
        self.ui.pushButton_registrar_Libros.clicked.connect(self.registrar_materia)
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_restaurar.clicked.connect(self.restaurar_ventana)

        datos = obtener_lista_profesores()
        for profesor in datos:
            self.ui.comboBox_Profesor.addItem(profesor['nombre'])

        # Validaciones
        solo_letras = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"))
        self.ui.lineEdit_Titulo_Materia.setValidator(solo_letras)

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

    def registrar_materia(self):
        nombre_materia = self.ui.lineEdit_Titulo_Materia.text()
        indexprofesor = self.ui.comboBox_Profesor.currentIndex()
        tipo_material = self.ui.comboBox_Material.currentText()
        area = self.ui.comboBox_area.currentText()
        

        # Validación de campo obligatorio
        if not nombre_materia.strip():
            QtWidgets.QMessageBox.warning(self, "Campo obligatorio", "Por favor escribe el nombre de la materia.")
            return

        datos = {
            "nombre": nombre_materia,
            "profesor": {"idProfesor": indexprofesor + 1},  # Ajuste para que el índice comience desde 1
            "material": tipo_material,
            "area": area
        }

        respuesta = registrar_materia(datos)

        if respuesta and respuesta.get("status") == "ok":
            QtWidgets.QMessageBox.information(self, "Éxito", "Materia registrada correctamente.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo registrar la materia.")

        # Animación visual del botón
        anim = QtCore.QPropertyAnimation(self.ui.pushButton_registrar_Libros, b"geometry")
        anim.setDuration(200)
        orig_geom = self.ui.pushButton_registrar_Libros.geometry()
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
    ventana = RegistroMateriaApp()
    ventana.show()
    sys.exit(app.exec())
