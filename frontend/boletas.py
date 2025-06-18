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
        self.ui.pushButton_registrar.clicked.connect(self.exportar_pdf)  # Botón Exportar

        self.maximizado = False

        # Aquí puedes probar cargar la tabla (simulado por ahora)
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
        # Aquí tu compañero de backend podrá implementar la exportación
        QtWidgets.QMessageBox.information(self, "Exportar", "Funcionalidad aún no implementada.")

    def cargar_tabla_ejemplo(self):
        # Ejemplo para que el backend sepa cómo insertar datos
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = BoletaApp()
    ventana.show()
    sys.exit(app.exec())
