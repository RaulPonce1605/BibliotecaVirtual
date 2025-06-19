from PyQt6 import QtCore, QtWidgets
from registro_prestamosdev_ui import Ui_Dialog
from servpeticiones import registrar_calificacion  # Asegúrate de que este módulo exista y funcione correctamente

class RegistroPrestamosDevApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexiones de botones
        self.ui.pushButton_registrar_Libros.clicked.connect(self.guardar_calificacion)
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

    def guardar_calificacion(self):
        materia = self.ui.comboBox_Materias.currentText()
        id_alumno = self.ui.comboBox_idalumno.currentText()
        grado = self.ui.comboBox_idalumno_2.currentText()
        calificacion = self.ui.spinBox_calificacion.value()
        fecha_evaluacion = self.ui.dateEdit_Devolucion.date().toString("yyyy-MM-dd")

        datos = {
            "materia": materia,
            "id_alumno": id_alumno,
            "grado": grado,
            "calificacion": calificacion,
            "fecha_evaluacion": fecha_evaluacion
        }

        respuesta = registrar_calificacion(datos)

        if respuesta and respuesta.get("status") == "ok":
            QtWidgets.QMessageBox.information(self, "Éxito", "Calificación registrada correctamente.")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo registrar la calificación.")
            
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
    ventana = RegistroPrestamosDevApp()
    ventana.show()
    sys.exit(app.exec())
