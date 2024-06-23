# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_Boton_Despedir.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class LiquidacionMasterForm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1251, 620)
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
        self.fVTablasVentas_1 = QFrame(self.centralwidget)
        self.fVTablasVentas_1.setObjectName(u"fVTablasVentas_1")
        self.fVTablasVentas_1.setGeometry(QRect(0, 0, 1250, 619))
        sizePolicy1.setHeightForWidth(self.fVTablasVentas_1.sizePolicy().hasHeightForWidth())
        self.fVTablasVentas_1.setSizePolicy(sizePolicy1)
        self.fVTablasVentas_1.setMinimumSize(QSize(1250, 0))
        palette = QPalette()
        brush = QBrush(QColor(208, 232, 232, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.fVTablasVentas_1.setPalette(palette)
        self.fVTablasVentas_1.setStyleSheet(u"/* Estilo para el QFrame padre */\n"
"QFrame#fVTablasVentas_1 {\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #d0e8e8;\n"
"}\n"
"\n"
"/* Estilo para los QFrame hijos */\n"
"QFrame#frame_tabla_1_0_Liq, QFrame#frame_tabla_0_0_Liq, QFrame#frame_tabla_2_0_Liq {\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #83b1b1;\n"
"}\n"
"\n"
"QFrame#frame_tabla_1_0_Liq::title, QFrame#frame_tabla_0_0_Liq::title, QFrame#frame_tabla_2_0_Liq::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Estilo para las etiquetas (QLabel) con contorno */\n"
"QLabel {\n"
"    color: black; /* Texto negro */\n"
"    font-size: 14px;\n"
"    border: 1px solid #467a7a; /* Contorno para las etiquetas */\n"
"    padding: 2px; /* A\u00f1adir un poco de padding para separar el texto del borde */\n"
"    background-color: #eaf4f4; /* Fondo de las etiquetas */\n"
"}\n"
"\n"
"/* Est"
                        "ilo para los botones (QPushButton) */\n"
"QPushButton {\n"
"    color: black; /* Texto negro */\n"
"    background-color: #4f9191;\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #83b1b1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #467a7a;\n"
"}\n"
"\n"
"/* Estilo para los ComboBox (QComboBox) */\n"
"QComboBox {\n"
"    background-color: #4f9191;\n"
"    color: black; /* Texto negro */\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/iconos/arrow-down.svg); /* Aseg\u00farate de tener esta imagen en tu recurso */\n"
"}\n"
"\n"
"/* Estilo para el LineEdit (QLineEdit) */\n"
"QLineEdit {\n"
"    background-color: #eaf4f4;\n"
"    color: black; /* Texto negro */\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
""
                        "}\n"
"\n"
"/* Estilo para el DateEdit (QDateEdit) */\n"
"QDateEdit {\n"
"    background-color: #eaf4f4;\n"
"    color: black; /* Texto negro */\n"
"    border: 1px solid #467a7a;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/iconos/calendar.svg); /* Aseg\u00farate de tener esta imagen en tu recurso */\n"
"}\n"
"")
        self.fVTablasVentas_1.setFrameShape(QFrame.StyledPanel)
        self.fVTablasVentas_1.setFrameShadow(QFrame.Raised)
        self.frame_tabla_1_0_Liq = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_1_0_Liq.setObjectName(u"frame_tabla_1_0_Liq")
        self.frame_tabla_1_0_Liq.setGeometry(QRect(20, 150, 1211, 261))
        self.frame_tabla_1_0_Liq.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_4 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_4 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_1_0_Liq.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_1_0_Liq.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_tabla_1_0_Liq)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(100, 50, 1002, 151))
        self.gL_organizador_Liq_2 = QGridLayout(self.gridLayoutWidget)
        self.gL_organizador_Liq_2.setObjectName(u"gL_organizador_Liq_2")
        self.gL_organizador_Liq_2.setContentsMargins(0, 0, 0, 0)
        self.cBox_liqRegion_Liq = QComboBox(self.gridLayoutWidget)
        self.cBox_liqRegion_Liq.setObjectName(u"cBox_liqRegion_Liq")

        self.gL_organizador_Liq_2.addWidget(self.cBox_liqRegion_Liq, 2, 2, 1, 1)

        self.label_nomFechaFinal_Nom = QLabel(self.gridLayoutWidget)
        self.label_nomFechaFinal_Nom.setObjectName(u"label_nomFechaFinal_Nom")

        self.gL_organizador_Liq_2.addWidget(self.label_nomFechaFinal_Nom, 3, 3, 1, 1)

        self.dateEdit_nomFechaInicio_Nom = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_nomFechaInicio_Nom.setObjectName(u"dateEdit_nomFechaInicio_Nom")

        self.gL_organizador_Liq_2.addWidget(self.dateEdit_nomFechaInicio_Nom, 3, 2, 1, 1)

        self.dateEdit_nomFechaFinal_Nom = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_nomFechaFinal_Nom.setObjectName(u"dateEdit_nomFechaFinal_Nom")

        self.gL_organizador_Liq_2.addWidget(self.dateEdit_nomFechaFinal_Nom, 3, 4, 1, 1)

        self.cBox_empCodigo_Emp = QComboBox(self.gridLayoutWidget)
        self.cBox_empCodigo_Emp.setObjectName(u"cBox_empCodigo_Emp")

        self.gL_organizador_Liq_2.addWidget(self.cBox_empCodigo_Emp, 1, 2, 1, 1)

        self.label_nomFechaInicio_Nom = QLabel(self.gridLayoutWidget)
        self.label_nomFechaInicio_Nom.setObjectName(u"label_nomFechaInicio_Nom")

        self.gL_organizador_Liq_2.addWidget(self.label_nomFechaInicio_Nom, 3, 1, 1, 1)

        self.label_liqRegion_Liq = QLabel(self.gridLayoutWidget)
        self.label_liqRegion_Liq.setObjectName(u"label_liqRegion_Liq")

        self.gL_organizador_Liq_2.addWidget(self.label_liqRegion_Liq, 2, 1, 1, 1)

        self.label_empCodigo_Emp = QLabel(self.gridLayoutWidget)
        self.label_empCodigo_Emp.setObjectName(u"label_empCodigo_Emp")

        self.gL_organizador_Liq_2.addWidget(self.label_empCodigo_Emp, 1, 1, 1, 1)

        self.label_infoLabura_Liq = QLabel(self.gridLayoutWidget)
        self.label_infoLabura_Liq.setObjectName(u"label_infoLabura_Liq")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_infoLabura_Liq.sizePolicy().hasHeightForWidth())
        self.label_infoLabura_Liq.setSizePolicy(sizePolicy2)
        self.label_infoLabura_Liq.setMinimumSize(QSize(0, 0))
        self.label_infoLabura_Liq.setLayoutDirection(Qt.LeftToRight)
        self.label_infoLabura_Liq.setAlignment(Qt.AlignCenter)

        self.gL_organizador_Liq_2.addWidget(self.label_infoLabura_Liq, 0, 1, 1, 4)

        self.frame_tabla_0_0_Liq = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_0_0_Liq.setObjectName(u"frame_tabla_0_0_Liq")
        self.frame_tabla_0_0_Liq.setGeometry(QRect(20, 10, 1211, 131))
        self.frame_tabla_0_0_Liq.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_5 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_5 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_0_0_Liq.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_0_0_Liq.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_tabla_0_0_Liq)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(100, 30, 1011, 79))
        self.gL_organizador_Liq = QGridLayout(self.gridLayoutWidget_2)
        self.gL_organizador_Liq.setObjectName(u"gL_organizador_Liq")
        self.gL_organizador_Liq.setContentsMargins(0, 0, 0, 0)
        self.cBox_liqMotivo_Liq = QComboBox(self.gridLayoutWidget_2)
        self.cBox_liqMotivo_Liq.setObjectName(u"cBox_liqMotivo_Liq")

        self.gL_organizador_Liq.addWidget(self.cBox_liqMotivo_Liq, 1, 1, 1, 1)

        self.label_liqMotivo_Liq = QLabel(self.gridLayoutWidget_2)
        self.label_liqMotivo_Liq.setObjectName(u"label_liqMotivo_Liq")
        sizePolicy1.setHeightForWidth(self.label_liqMotivo_Liq.sizePolicy().hasHeightForWidth())
        self.label_liqMotivo_Liq.setSizePolicy(sizePolicy1)

        self.gL_organizador_Liq.addWidget(self.label_liqMotivo_Liq, 1, 0, 1, 1)

        self.label_liqMotivo_Liq_2 = QLabel(self.gridLayoutWidget_2)
        self.label_liqMotivo_Liq_2.setObjectName(u"label_liqMotivo_Liq_2")

        self.gL_organizador_Liq.addWidget(self.label_liqMotivo_Liq_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.frame_tabla_2_0_Liq = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_2_0_Liq.setObjectName(u"frame_tabla_2_0_Liq")
        self.frame_tabla_2_0_Liq.setGeometry(QRect(20, 420, 1211, 191))
        self.frame_tabla_2_0_Liq.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_7 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_7 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_2_0_Liq.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_2_0_Liq.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_tabla_2_0_Liq)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(340, 10, 592, 171))
        self.gL_organizador_Liq_3 = QGridLayout(self.gridLayoutWidget_5)
        self.gL_organizador_Liq_3.setObjectName(u"gL_organizador_Liq_3")
        self.gL_organizador_Liq_3.setContentsMargins(0, 0, 0, 0)
        self.label_liqMensualDCuarta_Liq = QLabel(self.gridLayoutWidget_5)
        self.label_liqMensualDCuarta_Liq.setObjectName(u"label_liqMensualDCuarta_Liq")

        self.gL_organizador_Liq_3.addWidget(self.label_liqMensualDCuarta_Liq, 2, 0, 1, 1)

        self.label_liqMensualDTercera_liq = QLabel(self.gridLayoutWidget_5)
        self.label_liqMensualDTercera_liq.setObjectName(u"label_liqMensualDTercera_liq")

        self.gL_organizador_Liq_3.addWidget(self.label_liqMensualDTercera_liq, 1, 0, 1, 1)

        self.lEdit_liqVacaciones_Liq = QLineEdit(self.gridLayoutWidget_5)
        self.lEdit_liqVacaciones_Liq.setObjectName(u"lEdit_liqVacaciones_Liq")

        self.gL_organizador_Liq_3.addWidget(self.lEdit_liqVacaciones_Liq, 3, 1, 1, 1)

        self.label_seleccionComp_Liq = QLabel(self.gridLayoutWidget_5)
        self.label_seleccionComp_Liq.setObjectName(u"label_seleccionComp_Liq")
        self.label_seleccionComp_Liq.setMaximumSize(QSize(16777215, 28))
        self.label_seleccionComp_Liq.setAlignment(Qt.AlignCenter)

        self.gL_organizador_Liq_3.addWidget(self.label_seleccionComp_Liq, 0, 0, 1, 2)

        self.cBox_liqMensualDCuarta_Liq = QComboBox(self.gridLayoutWidget_5)
        self.cBox_liqMensualDCuarta_Liq.setObjectName(u"cBox_liqMensualDCuarta_Liq")

        self.gL_organizador_Liq_3.addWidget(self.cBox_liqMensualDCuarta_Liq, 2, 1, 1, 1)

        self.cBox_liqMensualDTercera_Liq = QComboBox(self.gridLayoutWidget_5)
        self.cBox_liqMensualDTercera_Liq.setObjectName(u"cBox_liqMensualDTercera_Liq")

        self.gL_organizador_Liq_3.addWidget(self.cBox_liqMensualDTercera_Liq, 1, 1, 1, 1)

        self.label_liqVacaciones_Liq = QLabel(self.gridLayoutWidget_5)
        self.label_liqVacaciones_Liq.setObjectName(u"label_liqVacaciones_Liq")

        self.gL_organizador_Liq_3.addWidget(self.label_liqVacaciones_Liq, 3, 0, 1, 1)

        self.boton_visualizar_Liq = QPushButton(self.gridLayoutWidget_5)
        self.boton_visualizar_Liq.setObjectName(u"boton_visualizar_Liq")

        self.gL_organizador_Liq_3.addWidget(self.boton_visualizar_Liq, 4, 0, 1, 1)

        self.boton_calcular_Liq = QPushButton(self.gridLayoutWidget_5)
        self.boton_calcular_Liq.setObjectName(u"boton_calcular_Liq")

        self.gL_organizador_Liq_3.addWidget(self.boton_calcular_Liq, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_nomFechaFinal_Nom.setText(QCoreApplication.translate("MainWindow", u"Fecha fin de la relaci\u00f3n laboral:", None))
        self.label_nomFechaInicio_Nom.setText(QCoreApplication.translate("MainWindow", u"Fecha de inicio de la relaci\u00f3n laboral:", None))
        self.label_liqRegion_Liq.setText(QCoreApplication.translate("MainWindow", u"Regi\u00f3n Donde Labura:", None))
        self.label_empCodigo_Emp.setText(QCoreApplication.translate("MainWindow", u"Empleado a gestionar", None))
        self.label_infoLabura_Liq.setText(QCoreApplication.translate("MainWindow", u"INFORMACION LABORAL", None))
        self.label_liqMotivo_Liq.setText(QCoreApplication.translate("MainWindow", u"Causales de Terminaci\u00f3n del Contrato Individual", None))
        self.label_liqMotivo_Liq_2.setText(QCoreApplication.translate("MainWindow", u"Causales de Terminaci\u00f3n del Contrato Individual", None))
        self.label_liqMensualDCuarta_Liq.setText(QCoreApplication.translate("MainWindow", u"Tipo de mensualizacion de Decimocuarta Remuneracion", None))
        self.label_liqMensualDTercera_liq.setText(QCoreApplication.translate("MainWindow", u"Tipo de mensualizacion de Decimotercera Remuneracion", None))
        self.label_seleccionComp_Liq.setText(QCoreApplication.translate("MainWindow", u"SELECCIONE Y COMPLETE", None))
        self.label_liqVacaciones_Liq.setText(QCoreApplication.translate("MainWindow", u"Numero de dias de vacaciones sin gozar del ultimo periodo", None))
        self.boton_visualizar_Liq.setText(QCoreApplication.translate("MainWindow", u"VISUALIZAR", None))
        self.boton_calcular_Liq.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
    # retranslateUi

