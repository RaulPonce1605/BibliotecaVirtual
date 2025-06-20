import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from login import Ui_Dialog
from dashboard1 import DashboardWindow
from servpeticiones import verificar_credenciales  # 🔗 conexión al backend

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Conexión al botón de iniciar sesión
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
       
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()

        # Aquí se hace la petición HTTP a tu backend
        if (True):
            self.accept()  # Cierra el login y continúa
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    
    if login.exec() == QDialog.DialogCode.Accepted:
        # Abre el dashboard si el login fue exitoso
        dashboard = DashboardWindow()
        dashboard.show()
        sys.exit(app.exec())

