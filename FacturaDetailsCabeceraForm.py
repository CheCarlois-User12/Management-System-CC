from PySide6.QtCore import QDate, QMetaObject, QObject, QPoint, QRect, QSize, Qt, QCoreApplication
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QComboBox, QDateEdit, QFrame, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QSizePolicy, QWidget

class FacturaDetailsCabeceraForm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1202, 132)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(10, 10))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setSizeIncrement(QSize(0, 0))
        self.centralwidgetCabecera = QWidget(MainWindow)
        self.centralwidgetCabecera.setObjectName(u"centralwidgetCabecera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidgetCabecera.sizePolicy().hasHeightForWidth())
        self.centralwidgetCabecera.setSizePolicy(sizePolicy1)
        self.centralwidgetCabecera.setMinimumSize(QSize(1280, 720))
        self.frame_Cabecera_Facturacion = QFrame(self.centralwidgetCabecera)
        self.frame_Cabecera_Facturacion.setObjectName(u"frame_Cabecera_Facturacion")
        self.frame_Cabecera_Facturacion.setGeometry(QRect(380, 0, 821, 131))
        self.frame_Cabecera_Facturacion.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_Cabecera_Facturacion {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_Cabecera_Facturacion ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_Cabecera_Facturacion.setFrameShape(QFrame.StyledPanel)
        self.frame_Cabecera_Facturacion.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_Cabecera_Facturacion)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(430, 10, 381, 100))
        self.gLCabecera_0_1 = QGridLayout(self.gridLayoutWidget_3)
        self.gLCabecera_0_1.setObjectName(u"gLCabecera_0_1")
        self.gLCabecera_0_1.setContentsMargins(0, 0, 0, 0)
        self.label_Cliente = QLabel(self.gridLayoutWidget_3)
        self.label_Cliente.setObjectName(u"label_Cliente")

        self.gLCabecera_0_1.addWidget(self.label_Cliente, 0, 0, 1, 1)

        self.lEHora_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.lEHora_Fact.setObjectName(u"lEHora_Fact")

        self.gLCabecera_0_1.addWidget(self.lEHora_Fact, 1, 3, 1, 1)

        self.label_Hora_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_Hora_Fact.setObjectName(u"label_Hora_Fact")

        self.gLCabecera_0_1.addWidget(self.label_Hora_Fact, 1, 2, 1, 1)

        self.label_Fecha_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_Fecha_Fact.setObjectName(u"label_Fecha_Fact")

        self.gLCabecera_0_1.addWidget(self.label_Fecha_Fact, 1, 0, 1, 1)

        self.label_Codigo_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_Codigo_Fact.setObjectName(u"label_Codigo_Fact")

        self.gLCabecera_0_1.addWidget(self.label_Codigo_Fact, 2, 0, 1, 1)

        self.lECodigo_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.lECodigo_Fact.setObjectName(u"lECodigo_Fact")

        self.gLCabecera_0_1.addWidget(self.lECodigo_Fact, 2, 1, 1, 2)

        self.IECliente_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.IECliente_Fact.setObjectName(u"IECliente_Fact")

        self.gLCabecera_0_1.addWidget(self.IECliente_Fact, 0, 1, 1, 2)

        self.dateEditFecha_Fact = QDateEdit(self.gridLayoutWidget_3)
        self.dateEditFecha_Fact.setObjectName(u"dateEditFecha_Fact")

        self.gLCabecera_0_1.addWidget(self.dateEditFecha_Fact, 1, 1, 1, 1)

        self.frame_Cabecera_Credencial = QFrame(self.centralwidgetCabecera)
        self.frame_Cabecera_Credencial.setObjectName(u"frame_Cabecera_Credencial")
        self.frame_Cabecera_Credencial.setGeometry(QRect(0, 0, 371, 131))
        self.frame_Cabecera_Credencial.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_Cabecera_Credencial {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_Cabecera_Credencial ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_Cabecera_Credencial.setFrameShape(QFrame.StyledPanel)
        self.frame_Cabecera_Credencial.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_Cabecera_Credencial)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 10, 341, 101))
        self.dLCabecera_0_0 = QGridLayout(self.gridLayoutWidget_2)
        self.dLCabecera_0_0.setObjectName(u"dLCabecera_0_0")
        self.dLCabecera_0_0.setContentsMargins(0, 0, 0, 0)
        self.botonBuscar_Cliente = QPushButton(self.gridLayoutWidget_2)
        self.botonBuscar_Cliente.setObjectName(u"botonBuscar_Cliente")

        self.dLCabecera_0_0.addWidget(self.botonBuscar_Cliente, 0, 2, 1, 1)

        self.labelRucCedula = QLabel(self.gridLayoutWidget_2)
        self.labelRucCedula.setObjectName(u"labelRucCedula")

        self.dLCabecera_0_0.addWidget(self.labelRucCedula, 1, 0, 1, 1)

        self.lERoC_Cliente = QLineEdit(self.gridLayoutWidget_2)
        self.lERoC_Cliente.setObjectName(u"lERoC_Cliente")

        self.dLCabecera_0_0.addWidget(self.lERoC_Cliente, 1, 1, 1, 1)

        self.labelCredencial = QLabel(self.gridLayoutWidget_2)
        self.labelCredencial.setObjectName(u"labelCredencial")

        self.dLCabecera_0_0.addWidget(self.labelCredencial, 0, 0, 1, 1)

        self.comboBoxCodigo_Cliente = QComboBox(self.gridLayoutWidget_2)
        self.comboBoxCodigo_Cliente.setObjectName(u"comboBoxCodigo_Cliente")

        self.dLCabecera_0_0.addWidget(self.comboBoxCodigo_Cliente, 0, 1, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Cliente.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_Hora_Fact.setText(QCoreApplication.translate("MainWindow", u"HORA", None))
        self.label_Fecha_Fact.setText(QCoreApplication.translate("MainWindow", u"FECHA", None))
        self.label_Codigo_Fact.setText(QCoreApplication.translate("MainWindow", u"Codigo de factura", None))
        self.botonBuscar_Cliente.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.labelRucCedula.setText(QCoreApplication.translate("MainWindow", u"ruc o cedula", None))
        self.labelCredencial.setText(QCoreApplication.translate("MainWindow", u"Credencial", None))
    # retranslateUi
