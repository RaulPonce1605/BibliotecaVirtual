import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from login import Ui_Dialog  # Importa la clase del archivo generado

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conectar botón "Sign In" a la función de login
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if email == "admin" and password == "1234":
            QMessageBox.information(self, "Login Correcto", f"¡Bienvenido, {email}!")
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())
