from PyQt6 import QtCore, QtGui, QtWidgets
from registro_material_ui import Ui_Dialog

class RegistroMaterialApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexiones de botones
        self.ui.pushButton_registrar_Libros.clicked.connect(self.registrar_material)
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

    def registrar_material(self):
        genero = self.ui.comboBox_Genero.currentText()
        titulo = self.ui.lineEdit_Titulo.text()
        autor = self.ui.lineEdit_Autor.text()
        tipo_material = self.ui.comboBox_Material.currentText()
        anio = self.ui.lineEdit_anio.text()
        id_material = self.ui.lineEdit_Id.text()

        print(f"Género: {genero}, Título: {titulo}, Autor: {autor}, "
              f"Tipo: {tipo_material}, Año: {anio}, ID: {id_material}")

        anim = QtCore.QPropertyAnimation(self.ui.pushButton_registrar_Libros, b"geometry")
        anim.setDuration(200)
        orig_geom = self.ui.pushButton_registrar_Libros.geometry()
        anim.setStartValue(orig_geom)
        anim.setKeyValueAt(0.5, QtCore.QRect(
            orig_geom.x()-5, orig_geom.y()-5,
            orig_geom.width()+10, orig_geom.height()+10
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
    ventana = RegistroMaterialApp()
    ventana.show()
    sys.exit(app.exec())
