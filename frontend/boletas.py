from operator import index
from PyQt6 import QtCore, QtGui, QtWidgets
from boletas_ui import Ui_Dialog
from servpeticiones import obtener_boleta, obtener_lista_alumnos, obtener_calificacion_por_idalumno
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import threading
import time
import os 


class BoletaApp(QtWidgets.QDialog):
    def __init__(self, dashboard_window=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dashboard_window = dashboard_window

        self.maximizado = False

        # Conexiones de botones
        self.ui.bt_cerrar_2.clicked.connect(self.cerrar_y_volver)
        self.ui.bt_minimizar.clicked.connect(self.showMinimized)
        self.ui.bt_maximizar.clicked.connect(self.maximizar_ventana)
        self.ui.bt_restaurar.clicked.connect(self.restaurar_ventana)
        self.ui.pushButton_registrar.clicked.connect(self.exportar_pdf)
        self.ui.pushButton_registrar_2.clicked.connect(self.generar_boletas_masivas)

        self.ui.comboBox.currentIndexChanged.connect(self.manejar_cambio_indice)

        datos = obtener_lista_alumnos()

        for alumno in datos:
            self.ui.comboBox.addItem(alumno['nombre'] + " " + alumno['apellido'])
        # Validaciones de entrada
        solo_letras = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"))
        solo_decimales = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^[0-9]+(\\.[0-9]{1,2})?$"))
        solo_enteros = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^[0-9]+$"))

        
        self.ui.comboBox.currentIndexChanged.connect(self.manejar_cambio_indice)
        self.manejar_cambio_indice(0)  # Inicializar con el primer alumno
     
        if hasattr(self.ui, 'lineEdit_promedio'):
            self.ui.lineEdit_promedio.setValidator(solo_decimales)
        if hasattr(self.ui, 'lineEdit_asistencia'):
            self.ui.lineEdit_asistencia.setValidator(solo_enteros)

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
        try:
            index = self.ui.comboBox.currentIndex()
            alumno_nombre = self.ui.comboBox.itemText(index)
            materia = self.ui.tableWidget.item(0, 4).text()
            cal1 = self.ui.tableWidget.item(0, 0).text()
            cal2 = self.ui.tableWidget.item(0, 1).text()
            cal3 = self.ui.tableWidget.item(0, 2).text()
            promedio = self.ui.tableWidget.item(0, 3).text()

            nombre_archivo = f"boleta_{alumno_nombre.replace(' ', '_')}.pdf"
            c = canvas.Canvas(nombre_archivo, pagesize=letter)
            width, height = letter

            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, 750, "📘 Boleta de Calificaciones")

            c.setFont("Helvetica", 12)
            c.drawString(50, 710, f"Alumno: {alumno_nombre}")
            c.drawString(50, 690, f"Materia: {materia}")
            c.drawString(50, 670, f"Calificaciones: {cal1}, {cal2}, {cal3}")
            c.drawString(50, 650, f"Promedio: {promedio}")

            c.save()

            QtWidgets.QMessageBox.information(self, "Boleta generada", f"PDF guardado como: {nombre_archivo}")
        except Exception as e:
            print("❌ Error al generar PDF:", e)
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo generar el archivo PDF.")

    def simular_generacion_boletas(self):
        for i in range(1, 11):
            print(f"🖨️ Generando boleta {i}/10...")
            time.sleep(0.7)
        QtWidgets.QMessageBox.information(self, "Finalizado", "¡Se generaron todas las boletas!")

    def generar_boletas_masivas(self):
        thread = threading.Thread(target=self.simular_generacion_boletas)
        thread.start()


    def manejar_cambio_indice(self, index):
        alumno = obtener_calificacion_por_idalumno(index + 1)

        if not alumno:
            QtWidgets.QMessageBox.warning(self, "Sin datos", "No se encontró información para este alumno.")
            return

        try:
            cal1 = float(alumno.get("cal1", 0))
            cal2 = float(alumno.get("cal2", 0))
            cal3 = float(alumno.get("cal3", 0))
            materia = alumno.get("materia", {}).get("nombre", "Sin materia")

            promedio = round((cal1 + cal2 + cal3) / 3, 2)
            self.ui.lcdNumber.display(promedio)

            # Llenar la tabla con los datos
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Calificación 1", "Calificación 2", "Calificación 3", "Promedio", "Materia"])

            self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(cal1)))
            self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(cal2)))
            self.ui.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(cal3)))
            self.ui.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(promedio)))
            self.ui.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(materia))

            print(f"Alumno: {self.ui.comboBox.itemText(index)} | Materia: {materia} | Promedio: {promedio}")

        except Exception as e:
            print("❌ Error al procesar datos:", e)
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudieron procesar las calificaciones.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = BoletaApp()
    ventana.show()
    sys.exit(app.exec())
