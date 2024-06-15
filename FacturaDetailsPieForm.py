
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class FacturaDetailsPieForm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1202, 143)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(10, 10))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.FramePieFacturas_0_1 = QFrame(self.centralwidget)
        self.FramePieFacturas_0_1.setObjectName(u"FramePieFacturas_0_1")
        self.FramePieFacturas_0_1.setGeometry(QRect(380, 1, 821, 141))
        self.FramePieFacturas_0_1.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#FramePieFacturas_0_1 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#FramePieFacturas_0_1 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.FramePieFacturas_0_1.setFrameShape(QFrame.StyledPanel)
        self.FramePieFacturas_0_1.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget_3 = QWidget(self.FramePieFacturas_0_1)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(280, 0, 541, 144))
        self.flPieFactuas_1 = QFormLayout(self.formLayoutWidget_3)
        self.flPieFactuas_1.setObjectName(u"flPieFactuas_1")
        self.flPieFactuas_1.setContentsMargins(0, 0, 0, 0)
        self.fLPieFacturas_3 = QFormLayout()
        self.fLPieFacturas_3.setObjectName(u"fLPieFacturas_3")
        self.labelSubTotal_Fact = QLabel(self.formLayoutWidget_3)
        self.labelSubTotal_Fact.setObjectName(u"labelSubTotal_Fact")

        self.fLPieFacturas_3.setWidget(0, QFormLayout.LabelRole, self.labelSubTotal_Fact)

        self.lESubTotal_FACT = QLineEdit(self.formLayoutWidget_3)
        self.lESubTotal_FACT.setObjectName(u"lESubTotal_FACT")

        self.fLPieFacturas_3.setWidget(0, QFormLayout.FieldRole, self.lESubTotal_FACT)

        self.labelTotalDesc_Fact = QLabel(self.formLayoutWidget_3)
        self.labelTotalDesc_Fact.setObjectName(u"labelTotalDesc_Fact")

        self.fLPieFacturas_3.setWidget(1, QFormLayout.LabelRole, self.labelTotalDesc_Fact)

        self.lETotalDes_Fact = QLineEdit(self.formLayoutWidget_3)
        self.lETotalDes_Fact.setObjectName(u"lETotalDes_Fact")

        self.fLPieFacturas_3.setWidget(1, QFormLayout.FieldRole, self.lETotalDes_Fact)

        self.labelTotalIva_Fact = QLabel(self.formLayoutWidget_3)
        self.labelTotalIva_Fact.setObjectName(u"labelTotalIva_Fact")

        self.fLPieFacturas_3.setWidget(2, QFormLayout.LabelRole, self.labelTotalIva_Fact)

        self.lETotalIva_Fact = QLineEdit(self.formLayoutWidget_3)
        self.lETotalIva_Fact.setObjectName(u"lETotalIva_Fact")

        self.fLPieFacturas_3.setWidget(2, QFormLayout.FieldRole, self.lETotalIva_Fact)

        self.labelTotal_Fact = QLabel(self.formLayoutWidget_3)
        self.labelTotal_Fact.setObjectName(u"labelTotal_Fact")

        self.fLPieFacturas_3.setWidget(3, QFormLayout.LabelRole, self.labelTotal_Fact)

        self.lETotal_Fact = QLineEdit(self.formLayoutWidget_3)
        self.lETotal_Fact.setObjectName(u"lETotal_Fact")

        self.fLPieFacturas_3.setWidget(3, QFormLayout.FieldRole, self.lETotal_Fact)


        self.flPieFactuas_1.setLayout(0, QFormLayout.FieldRole, self.fLPieFacturas_3)

        self.fLPieFacturas_2 = QFormLayout()
        self.fLPieFacturas_2.setObjectName(u"fLPieFacturas_2")
        self.labelFormaPago = QLabel(self.formLayoutWidget_3)
        self.labelFormaPago.setObjectName(u"labelFormaPago")

        self.fLPieFacturas_2.setWidget(0, QFormLayout.LabelRole, self.labelFormaPago)

        self.comboBoxFormaPago = QComboBox(self.formLayoutWidget_3)
        self.comboBoxFormaPago.setObjectName(u"comboBoxFormaPago")

        self.fLPieFacturas_2.setWidget(0, QFormLayout.FieldRole, self.comboBoxFormaPago)


        self.flPieFactuas_1.setLayout(0, QFormLayout.LabelRole, self.fLPieFacturas_2)

        self.FramePieFacturas_0_0 = QFrame(self.centralwidget)
        self.FramePieFacturas_0_0.setObjectName(u"FramePieFacturas_0_0")
        self.FramePieFacturas_0_0.setGeometry(QRect(0, 0, 371, 141))
        self.FramePieFacturas_0_0.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#FramePieFacturas_0_0 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#FramePieFacturas_0_0 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.FramePieFacturas_0_0.setFrameShape(QFrame.StyledPanel)
        self.FramePieFacturas_0_0.setFrameShadow(QFrame.Raised)
        self.botonGenerarFactura = QPushButton(self.FramePieFacturas_0_0)
        self.botonGenerarFactura.setObjectName(u"botonGenerarFactura")
        self.botonGenerarFactura.setGeometry(QRect(20, 20, 141, 29))
        self.botonCancelarFactura = QPushButton(self.FramePieFacturas_0_0)
        self.botonCancelarFactura.setObjectName(u"botonCancelarFactura")
        self.botonCancelarFactura.setGeometry(QRect(180, 20, 151, 29))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelSubTotal_Fact.setText(QCoreApplication.translate("MainWindow", u"SUB TOTAL", None))
        self.labelTotalDesc_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL DESC", None))
        self.labelTotalIva_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL IVA", None))
        self.labelTotal_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.labelFormaPago.setText(QCoreApplication.translate("MainWindow", u"FORMA PAGO", None))
        self.botonGenerarFactura.setText(QCoreApplication.translate("MainWindow", u"GENERAR FACTURA", None))
        self.botonCancelarFactura.setText(QCoreApplication.translate("MainWindow", u"CANCELAR FACTURA", None))
    # retranslateUi

