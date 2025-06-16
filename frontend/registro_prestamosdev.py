from PyQt6 import QtCore, QtGui, QtWidgets
from registro_prestamosdev_ui import Ui_Dialog

class RegistroPrestamosDevApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexiones de botones
        self.ui.pushButton_registrar_Libros.clicked.connect(self.registrar_prestamo)
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

    def registrar_prestamo(self):
        tipo_libro = self.ui.comboBox_Libro.currentText()
        nombre = self.ui.lineEdit_Nombre.text()
        primer_apellido = self.ui.lineEdit_Apellido.text()
        segundo_apellido = self.ui.lineEdit_Segundo_Apellido.text()
        id_libro = self.ui.lineEdit_IdLibro.text()
        fecha_prestamo = self.ui.dateEdit_Prestamo.date().toString("yyyy-MM-dd")
        fecha_devolucion = self.ui.dateEdit_Devolucion.date().toString("yyyy-MM-dd")

        print(f"Tipo de libro: {tipo_libro}, Nombre: {nombre}, "
              f"Apellido Paterno: {primer_apellido}, Apellido Materno: {segundo_apellido}, "
              f"ID Libro: {id_libro}, Fecha préstamo: {fecha_prestamo}, Fecha devolución: {fecha_devolucion}")

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

    def cerrar_y_volver(self):
        self.close()
        if self.dashboard_window:
            self.dashboard_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = RegistroPrestamosDevApp()
    ventana.show()
    sys.exit(app.exec())
