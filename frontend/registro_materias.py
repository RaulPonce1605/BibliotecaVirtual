from PyQt6 import QtCore, QtWidgets
from registro_materia_ui import Ui_Dialog

class RegistroMateriaApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexión de botones
        self.ui.pushButton_registrar_Libros.clicked.connect(self.registrar_materia)
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

    def registrar_materia(self):
        nombre_materia = self.ui.lineEdit_Titulo_Materia.text()
        clave_materia = self.ui.comboBox_materia_2.currentText()
        profesor = self.ui.comboBox_Profesor.currentText()
        tipo_material = self.ui.comboBox_Material.currentText()
        area = self.ui.comboBox_area.currentText()

        print("📚 Registro de Materia:")
        print(f"  Nombre: {nombre_materia}")
        print(f"  Clave: {clave_materia}")
        print(f"  Profesor: {profesor}")
        print(f"  Tipo de material: {tipo_material}")
        print(f"  Área académica: {area}")

        # Animación visual del botón registrar
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
