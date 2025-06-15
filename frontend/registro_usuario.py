from PyQt6 import QtCore, QtGui, QtWidgets
from registro_usuario_ui import Ui_Dialog

class RegistroApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Guardar referencia a la ventana del dashboard
        self.dashboard_window = dashboard_window

        # Conexiones de botones
        self.ui.pushButton_registrar.clicked.connect(self.registrar_usuario)
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)  # Conectamos al método correcto
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

    def registrar_usuario(self):
        tipo_cliente = self.ui.comboBox_cliente.currentText()
        nombre = self.ui.lineEdit_nombre.text()
        primer_apellido = self.ui.lineEdit_apellido.text()
        segundo_apellido = self.ui.lineEdit_segundo_Apellido.text()
        telefono = self.ui.lineEdit_Telefono.text()
        email = self.ui.lineEdit_Email.text()

        print(f"Tipo: {tipo_cliente}, Nombre: {nombre}, Apellidos: {primer_apellido} {segundo_apellido}, Tel: {telefono}, Email: {email}")

        anim = QtCore.QPropertyAnimation(self.ui.pushButton_registrar, b"geometry")
        anim.setDuration(200)
        orig_geom = self.ui.pushButton_registrar.geometry()
        anim.setStartValue(orig_geom)
        anim.setKeyValueAt(0.5, QtCore.QRect(orig_geom.x()-5, orig_geom.y()-5, orig_geom.width()+10, orig_geom.height()+10))
        anim.setEndValue(orig_geom)
        anim.start()

        self.anim_registrar = anim

    def cerrar_y_volver(self):
        self.close()
        if self.dashboard_window:
            self.dashboard_window.show()
