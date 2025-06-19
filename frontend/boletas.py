from PyQt6 import QtCore, QtWidgets
from boletas_ui import Ui_Dialog
from servpeticiones import obtener_boleta

import threading
import time

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
        self.ui.pushButton_registrar_2.clicked.connect(self.generar_boletas_masivas)  # << FALTABA ESTO

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

    def exportar_pdf(self):
        nombre = self.ui.lineEdit_nombre.text().strip()

        if not nombre:
            QtWidgets.QMessageBox.warning(self, "Campo vacío", "Por favor, escribe el nombre del alumno.")
            return

        datos_boleta = obtener_boleta(nombre)

        if not datos_boleta:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo obtener la boleta del backend.")
            return

        self.ui.tableWidget.setRowCount(len(datos_boleta))
        for fila, fila_datos in enumerate(datos_boleta):
            for columna, valor in enumerate(fila_datos):
                item = QtWidgets.QTableWidgetItem(str(valor))
                self.ui.tableWidget.setItem(fila, columna, item)

        try:
            promedios = [float(fila[-1]) for fila in datos_boleta]
            promedio_general = sum(promedios) / len(promedios)
            self.ui.lcdNumber.display(promedio_general)
        except Exception as e:
            print("Error al calcular promedio:", e)
            self.ui.lcdNumber.display(0)

        QtWidgets.QMessageBox.information(self, "Boleta generada", "Boleta cargada correctamente.")

    def generar_boletas_masivas(self):
        thread = threading.Thread(target=self.simular_generacion_boletas)
        thread.start()

    def simular_generacion_boletas(self):
        for i in range(1, 11):
            print(f"🖨️ Generando boleta {i}/10...")
            time.sleep(0.7)
        QtWidgets.QMessageBox.information(self, "Finalizado", "¡Se generaron todas las boletas!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = BoletaApp()
    ventana.show()
    sys.exit(app.exec())
