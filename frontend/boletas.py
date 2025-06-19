from PyQt6 import QtCore, QtWidgets
from boletas_ui import Ui_Dialog

class BoletaApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        # Conexiones de botones
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_restaurar.clicked.connect(self.restaurar_ventana)
        self.ui.pushButton_registrar.clicked.connect(self.exportar_pdf)

        self.maximizado = False

        # Carga de datos simulada
        self.cargar_tabla_ejemplo()

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

    def exportar_pdf(self):
        QtWidgets.QMessageBox.information(self, "Exportar", "Función de exportación aún no implementada.")

    def cargar_tabla_ejemplo(self):
        datos = [
            ["Español", 9, 8, 10, 9],
            ["Matemáticas", 10, 10, 9, 9.6],
            ["Ciencias", 8, 9, 9, 8.6],
        ]
        self.ui.tableWidget.setRowCount(len(datos))
        for fila, datos_fila in enumerate(datos):
            for columna, valor in enumerate(datos_fila):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(fila, columna, item)

        # Mostrar el promedio final (simulado)
        promedio_general = sum([fila[4] for fila in datos]) / len(datos)
        self.ui.lcdNumber.display(promedio_general)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = BoletaApp()
    ventana.show()
    sys.exit(app.exec())
