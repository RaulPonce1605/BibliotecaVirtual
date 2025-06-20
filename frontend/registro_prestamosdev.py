from PyQt6 import QtCore, QtWidgets
from registro_prestamosdev_ui import Ui_Dialog
from servpeticiones import registrar_calificacion, obtener_lista_materias, obtener_lista_alumnos, obtener_calificacion_por_idalumno  # Asegúrate de que este módulo exista y funcione correctamente

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

        
        datos = obtener_lista_materias()
        for materia in datos:
            self.ui.comboBox_Materias.addItem(materia['nombre'])

        datosid = obtener_lista_alumnos()
        for alumno in datosid:
            self.ui.comboBox_idalumno.addItem(alumno['nombre'] + " " + alumno['apellido'])
            

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
        indexmat = self.ui.comboBox_Materias.currentIndex()
        id = self.ui.comboBox_idalumno.currentText()
        index = self.ui.comboBox_idalumno.currentIndex()
        indexgrado = self.ui.comboBox_grado.currentIndex()
        calificacion = self.ui.spinBox_calificacion.value()
        fecha_evaluacion = self.ui.dateEdit_Devolucion.date().toString("yyyy-MM-dd")

        ev = obtener_calificacion_por_idalumno(index + 1)
        datos = {}
        if indexgrado == 0:
            datos = {
                "materia": {"idMateria": indexmat +1},
                "alumno": {"idAlumno": index + 1},
                "cal1": calificacion,
                "cal2": ev["cal2"] if ev else 0,
                "cal3": ev["cal3"] if ev else 0,
                "fecha": fecha_evaluacion
            }
        elif indexgrado == 1:
            datos = {
                "materia": {"idMateria": indexmat + 1},
                "alumno": {"idAlumno": index +1},
                "cal1": ev["cal1"] if ev else 0,
                "cal2": calificacion,
                "cal3": ev["cal3"] if ev else 0,
                "fecha": fecha_evaluacion
            }
        else:
            datos = {
                "materia": {"idMateria": indexmat + 1},
                "alumno": {"idAlumno": index + 1},
                "cal1": ev["cal1"] if ev else 0,
                "cal2": ev["cal2"] if ev else 0,
                "cal3": calificacion,
                "fecha": fecha_evaluacion
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
