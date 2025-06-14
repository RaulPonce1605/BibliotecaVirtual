import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from login import Ui_Dialog
from dashboard1 import DashboardWindow

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        usuario = self.ui.lineEdit.text()
        contrasena = self.ui.lineEdit_2.text()

        if (usuario, contrasena) == ("admin", "1234"):
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    
    if login.exec() == QDialog.DialogCode.Accepted:
        # Abrir dashboard después del login exitoso
        dashboard = DashboardWindow()
        dashboard.show()

        sys.exit(app.exec())
