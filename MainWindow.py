from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QMessageBox
from PySide6.QtGui import QIcon
import sys
from EmpleadoGUI import EmpleadoGUI
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EMPLEADOS MANAGEMENT SYSTEM")
        self.setupTabs()
        self.showWelcomeMessage()

    def setupTabs(self):
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.empleado_gui = EmpleadoGUI()
        self.tab_widget.addTab(self.empleado_gui, "Empleados")
    def showWelcomeMessage(self):
        QMessageBox.information(self, "Bienvenido", "Bienvenido a Empleados Managment System !")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
