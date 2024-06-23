# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_Nominas.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class NominaMasterForm(object):
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
        brush = QBrush(QColor(38, 0, 27, 255))
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
"    border: 1px solid #26001B;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #26001B;\n"
"}\n"
"\n"
"QFrame#fVTablasVentas_1::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.fVTablasVentas_1.setFrameShape(QFrame.StyledPanel)
        self.fVTablasVentas_1.setFrameShadow(QFrame.Raised)
        self.frame_tabla_1_1_Nom = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_1_1_Nom.setObjectName(u"frame_tabla_1_1_Nom")
        self.frame_tabla_1_1_Nom.setGeometry(QRect(400, 150, 821, 311))
        self.frame_tabla_1_1_Nom.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_3 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_3 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_1_1_Nom.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_1_1_Nom.setFrameShadow(QFrame.Raised)
        self.frame_tabla_1_0_DesBon = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_1_0_DesBon.setObjectName(u"frame_tabla_1_0_DesBon")
        self.frame_tabla_1_0_DesBon.setGeometry(QRect(20, 150, 371, 311))
        self.frame_tabla_1_0_DesBon.setStyleSheet(u"\n"
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
        self.frame_tabla_1_0_DesBon.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_1_0_DesBon.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_tabla_1_0_DesBon)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 341, 251))
        self.gL_organizador_DesBon_1 = QGridLayout(self.gridLayoutWidget)
        self.gL_organizador_DesBon_1.setObjectName(u"gL_organizador_DesBon_1")
        self.gL_organizador_DesBon_1.setContentsMargins(0, 0, 0, 0)
        self.label_desBonDescripcion_DesBon = QLabel(self.gridLayoutWidget)
        self.label_desBonDescripcion_DesBon.setObjectName(u"label_desBonDescripcion_DesBon")

        self.gL_organizador_DesBon_1.addWidget(self.label_desBonDescripcion_DesBon, 1, 0, 1, 1)

        self.label_desBonValor_DesBon = QLabel(self.gridLayoutWidget)
        self.label_desBonValor_DesBon.setObjectName(u"label_desBonValor_DesBon")

        self.gL_organizador_DesBon_1.addWidget(self.label_desBonValor_DesBon, 2, 0, 1, 1)

        self.lEdit_desBonDescripcion_DesBon = QLineEdit(self.gridLayoutWidget)
        self.lEdit_desBonDescripcion_DesBon.setObjectName(u"lEdit_desBonDescripcion_DesBon")
        self.lEdit_desBonDescripcion_DesBon.setEnabled(False)

        self.gL_organizador_DesBon_1.addWidget(self.lEdit_desBonDescripcion_DesBon, 1, 2, 1, 1)

        self.cBox_desBonCodigo_DesBon = QComboBox(self.gridLayoutWidget)
        self.cBox_desBonCodigo_DesBon.setObjectName(u"cBox_desBonCodigo_DesBon")

        self.gL_organizador_DesBon_1.addWidget(self.cBox_desBonCodigo_DesBon, 0, 2, 1, 1)

        self.label_desBonCodigo_DesBon = QLabel(self.gridLayoutWidget)
        self.label_desBonCodigo_DesBon.setObjectName(u"label_desBonCodigo_DesBon")

        self.gL_organizador_DesBon_1.addWidget(self.label_desBonCodigo_DesBon, 0, 0, 1, 1)

        self.boton_Buscar_DesBon = QPushButton(self.gridLayoutWidget)
        self.boton_Buscar_DesBon.setObjectName(u"boton_Buscar_DesBon")

        self.gL_organizador_DesBon_1.addWidget(self.boton_Buscar_DesBon, 0, 3, 1, 1)

        self.lEdit_desBonValor_DesBon = QLineEdit(self.gridLayoutWidget)
        self.lEdit_desBonValor_DesBon.setObjectName(u"lEdit_desBonValor_DesBon")
        self.lEdit_desBonValor_DesBon.setEnabled(False)

        self.gL_organizador_DesBon_1.addWidget(self.lEdit_desBonValor_DesBon, 2, 2, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.frame_tabla_1_0_DesBon)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 260, 188, 41))
        self.hL_organizador_DesBon = QHBoxLayout(self.horizontalLayoutWidget)
        self.hL_organizador_DesBon.setObjectName(u"hL_organizador_DesBon")
        self.hL_organizador_DesBon.setContentsMargins(0, 0, 0, 0)
        self.boton_Confirmar_DesBon = QPushButton(self.horizontalLayoutWidget)
        self.boton_Confirmar_DesBon.setObjectName(u"boton_Confirmar_DesBon")

        self.hL_organizador_DesBon.addWidget(self.boton_Confirmar_DesBon)

        self.boton_Cancelar_DesBon = QPushButton(self.horizontalLayoutWidget)
        self.boton_Cancelar_DesBon.setObjectName(u"boton_Cancelar_DesBon")

        self.hL_organizador_DesBon.addWidget(self.boton_Cancelar_DesBon)

        self.frame_tabla_0_0_Emp = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_0_0_Emp.setObjectName(u"frame_tabla_0_0_Emp")
        self.frame_tabla_0_0_Emp.setGeometry(QRect(20, 10, 371, 131))
        self.frame_tabla_0_0_Emp.setStyleSheet(u"\n"
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
        self.frame_tabla_0_0_Emp.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_0_0_Emp.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_tabla_0_0_Emp)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 10, 341, 101))
        self.gL_organizador_Emp = QGridLayout(self.gridLayoutWidget_2)
        self.gL_organizador_Emp.setObjectName(u"gL_organizador_Emp")
        self.gL_organizador_Emp.setContentsMargins(0, 0, 0, 0)
        self.label_empCodigo_Emp = QLabel(self.gridLayoutWidget_2)
        self.label_empCodigo_Emp.setObjectName(u"label_empCodigo_Emp")

        self.gL_organizador_Emp.addWidget(self.label_empCodigo_Emp, 0, 0, 1, 1)

        self.boton_BuscarCodigo_Emp = QPushButton(self.gridLayoutWidget_2)
        self.boton_BuscarCodigo_Emp.setObjectName(u"boton_BuscarCodigo_Emp")

        self.gL_organizador_Emp.addWidget(self.boton_BuscarCodigo_Emp, 0, 2, 1, 1)

        self.label_empIdentificacion_Emp = QLabel(self.gridLayoutWidget_2)
        self.label_empIdentificacion_Emp.setObjectName(u"label_empIdentificacion_Emp")

        self.gL_organizador_Emp.addWidget(self.label_empIdentificacion_Emp, 1, 0, 1, 1)

        self.lEdit_empIdentificacion_Emp = QLineEdit(self.gridLayoutWidget_2)
        self.lEdit_empIdentificacion_Emp.setObjectName(u"lEdit_empIdentificacion_Emp")
        self.lEdit_empIdentificacion_Emp.setEnabled(False)

        self.gL_organizador_Emp.addWidget(self.lEdit_empIdentificacion_Emp, 1, 1, 1, 1)

        self.cBox_empCodigo_Emp = QComboBox(self.gridLayoutWidget_2)
        self.cBox_empCodigo_Emp.setObjectName(u"cBox_empCodigo_Emp")

        self.gL_organizador_Emp.addWidget(self.cBox_empCodigo_Emp, 0, 1, 1, 1)

        self.frame_tabla_0_1_Nom = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_0_1_Nom.setObjectName(u"frame_tabla_0_1_Nom")
        self.frame_tabla_0_1_Nom.setGeometry(QRect(400, 10, 821, 131))
        self.frame_tabla_0_1_Nom.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_6 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_6 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_0_1_Nom.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_0_1_Nom.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget_2 = QWidget(self.frame_tabla_0_1_Nom)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(130, 10, 671, 174))
        self.fL_organizador_Nom = QFormLayout(self.formLayoutWidget_2)
        self.fL_organizador_Nom.setObjectName(u"fL_organizador_Nom")
        self.fL_organizador_Nom.setContentsMargins(0, 0, 0, 0)
        self.gL_organizardor_Nom_1 = QGridLayout()
        self.gL_organizardor_Nom_1.setObjectName(u"gL_organizardor_Nom_1")
        self.label_nomCodigo_Nom = QLabel(self.formLayoutWidget_2)
        self.label_nomCodigo_Nom.setObjectName(u"label_nomCodigo_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.label_nomCodigo_Nom, 6, 0, 1, 1)

        self.lEdit_nomCodigo_Nom = QLineEdit(self.formLayoutWidget_2)
        self.lEdit_nomCodigo_Nom.setObjectName(u"lEdit_nomCodigo_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.lEdit_nomCodigo_Nom, 6, 1, 1, 3)

        self.label_empNombre_Nom = QLabel(self.formLayoutWidget_2)
        self.label_empNombre_Nom.setObjectName(u"label_empNombre_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.label_empNombre_Nom, 1, 0, 1, 1)

        self.dateEdit_nomFechaFinal_Nom = QDateEdit(self.formLayoutWidget_2)
        self.dateEdit_nomFechaFinal_Nom.setObjectName(u"dateEdit_nomFechaFinal_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.dateEdit_nomFechaFinal_Nom, 5, 3, 1, 1)

        self.dateEdit_nomFechaInicial_Nom = QDateEdit(self.formLayoutWidget_2)
        self.dateEdit_nomFechaInicial_Nom.setObjectName(u"dateEdit_nomFechaInicial_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.dateEdit_nomFechaInicial_Nom, 5, 1, 1, 1)

        self.label_nomFechaFinal_Nom = QLabel(self.formLayoutWidget_2)
        self.label_nomFechaFinal_Nom.setObjectName(u"label_nomFechaFinal_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.label_nomFechaFinal_Nom, 5, 2, 1, 1)

        self.label_nomFechaInicial_Nom = QLabel(self.formLayoutWidget_2)
        self.label_nomFechaInicial_Nom.setObjectName(u"label_nomFechaInicial_Nom")

        self.gL_organizardor_Nom_1.addWidget(self.label_nomFechaInicial_Nom, 5, 0, 1, 1)

        self.lEdit_empNombre_Nom = QLineEdit(self.formLayoutWidget_2)
        self.lEdit_empNombre_Nom.setObjectName(u"lEdit_empNombre_Nom")
        self.lEdit_empNombre_Nom.setEnabled(False)

        self.gL_organizardor_Nom_1.addWidget(self.lEdit_empNombre_Nom, 1, 1, 1, 3)


        self.fL_organizador_Nom.setLayout(0, QFormLayout.FieldRole, self.gL_organizardor_Nom_1)

        self.gL_organizador_Nom_3 = QGridLayout()
        self.gL_organizador_Nom_3.setObjectName(u"gL_organizador_Nom_3")
        self.lEdit_empCargo_Nom = QLineEdit(self.formLayoutWidget_2)
        self.lEdit_empCargo_Nom.setObjectName(u"lEdit_empCargo_Nom")
        self.lEdit_empCargo_Nom.setEnabled(False)

        self.gL_organizador_Nom_3.addWidget(self.lEdit_empCargo_Nom, 0, 1, 1, 1)

        self.lEdit_nomTotalHoras_Nom = QLineEdit(self.formLayoutWidget_2)
        self.lEdit_nomTotalHoras_Nom.setObjectName(u"lEdit_nomTotalHoras_Nom")

        self.gL_organizador_Nom_3.addWidget(self.lEdit_nomTotalHoras_Nom, 1, 1, 1, 1)

        self.label_empCargo_Nom = QLabel(self.formLayoutWidget_2)
        self.label_empCargo_Nom.setObjectName(u"label_empCargo_Nom")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_empCargo_Nom.sizePolicy().hasHeightForWidth())
        self.label_empCargo_Nom.setSizePolicy(sizePolicy2)

        self.gL_organizador_Nom_3.addWidget(self.label_empCargo_Nom, 0, 0, 1, 1)

        self.label_nomTotalHoras_Nom = QLabel(self.formLayoutWidget_2)
        self.label_nomTotalHoras_Nom.setObjectName(u"label_nomTotalHoras_Nom")

        self.gL_organizador_Nom_3.addWidget(self.label_nomTotalHoras_Nom, 1, 0, 1, 1)


        self.fL_organizador_Nom.setLayout(0, QFormLayout.LabelRole, self.gL_organizador_Nom_3)

        self.frame_tabla_2_0_Nom = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_2_0_Nom.setObjectName(u"frame_tabla_2_0_Nom")
        self.frame_tabla_2_0_Nom.setGeometry(QRect(20, 469, 371, 141))
        self.frame_tabla_2_0_Nom.setStyleSheet(u"\n"
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
        self.frame_tabla_2_0_Nom.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_2_0_Nom.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_tabla_2_0_Nom)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(30, 30, 316, 81))
        self.gL_organizador_Nom_1 = QGridLayout(self.gridLayoutWidget_5)
        self.gL_organizador_Nom_1.setObjectName(u"gL_organizador_Nom_1")
        self.gL_organizador_Nom_1.setContentsMargins(0, 0, 0, 0)
        self.boton_CancelarNom_Nom = QPushButton(self.gridLayoutWidget_5)
        self.boton_CancelarNom_Nom.setObjectName(u"boton_CancelarNom_Nom")

        self.gL_organizador_Nom_1.addWidget(self.boton_CancelarNom_Nom, 0, 1, 1, 1)

        self.boton_GenerarNom_Nom = QPushButton(self.gridLayoutWidget_5)
        self.boton_GenerarNom_Nom.setObjectName(u"boton_GenerarNom_Nom")

        self.gL_organizador_Nom_1.addWidget(self.boton_GenerarNom_Nom, 0, 0, 1, 1)

        self.boton_VisualizarNom_Nom = QPushButton(self.gridLayoutWidget_5)
        self.boton_VisualizarNom_Nom.setObjectName(u"boton_VisualizarNom_Nom")

        self.gL_organizador_Nom_1.addWidget(self.boton_VisualizarNom_Nom, 1, 0, 1, 1)

        self.boton_VisualizarLiq_Liq = QPushButton(self.gridLayoutWidget_5)
        self.boton_VisualizarLiq_Liq.setObjectName(u"boton_VisualizarLiq_Liq")

        self.gL_organizador_Nom_1.addWidget(self.boton_VisualizarLiq_Liq, 1, 1, 1, 1)

        self.frame_tabla_2_1_Nom = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_2_1_Nom.setObjectName(u"frame_tabla_2_1_Nom")
        self.frame_tabla_2_1_Nom.setGeometry(QRect(400, 470, 821, 141))
        self.frame_tabla_2_1_Nom.setStyleSheet(u"\n"
"/* Estilo para el QFrame hijo */\n"
"QFrame#frame_8 {\n"
"    border: 1px solid #56003f;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #56003f;\n"
"}\n"
"\n"
"QFrame#frame_8 ::title {\n"
"    color: white;\n"
"    font-size: 18px;\n"
"    padding: 5px;\n"
"}")
        self.frame_tabla_2_1_Nom.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_2_1_Nom.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_6 = QWidget(self.frame_tabla_2_1_Nom)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(330, 10, 481, 135))
        self.gL_organizador_Nom_2 = QGridLayout(self.gridLayoutWidget_6)
        self.gL_organizador_Nom_2.setObjectName(u"gL_organizador_Nom_2")
        self.gL_organizador_Nom_2.setContentsMargins(0, 0, 0, 0)
        self.lEdit_nomSubTotal_Nom = QLineEdit(self.gridLayoutWidget_6)
        self.lEdit_nomSubTotal_Nom.setObjectName(u"lEdit_nomSubTotal_Nom")
        self.lEdit_nomSubTotal_Nom.setEnabled(False)

        self.gL_organizador_Nom_2.addWidget(self.lEdit_nomSubTotal_Nom, 0, 4, 1, 1)

        self.cBox_nomMes_Nom = QComboBox(self.gridLayoutWidget_6)
        self.cBox_nomMes_Nom.setObjectName(u"cBox_nomMes_Nom")

        self.gL_organizador_Nom_2.addWidget(self.cBox_nomMes_Nom, 1, 1, 1, 1)

        self.label_nomSubTotal_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomSubTotal_Nom.setObjectName(u"label_nomSubTotal_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomSubTotal_Nom, 0, 2, 1, 1)

        self.lEdit_nomTotal_Nom = QLineEdit(self.gridLayoutWidget_6)
        self.lEdit_nomTotal_Nom.setObjectName(u"lEdit_nomTotal_Nom")
        self.lEdit_nomTotal_Nom.setEnabled(False)

        self.gL_organizador_Nom_2.addWidget(self.lEdit_nomTotal_Nom, 3, 4, 1, 1)

        self.cBox_nomAnio_Nom = QComboBox(self.gridLayoutWidget_6)
        self.cBox_nomAnio_Nom.setObjectName(u"cBox_nomAnio_Nom")

        self.gL_organizador_Nom_2.addWidget(self.cBox_nomAnio_Nom, 0, 1, 1, 1)

        self.label_nomTotal_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomTotal_Nom.setObjectName(u"label_nomTotal_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomTotal_Nom, 3, 2, 1, 1)

        self.lEdit_nomTotalDes_Nom = QLineEdit(self.gridLayoutWidget_6)
        self.lEdit_nomTotalDes_Nom.setObjectName(u"lEdit_nomTotalDes_Nom")
        self.lEdit_nomTotalDes_Nom.setEnabled(False)

        self.gL_organizador_Nom_2.addWidget(self.lEdit_nomTotalDes_Nom, 2, 4, 1, 1)

        self.lEdit_nomTotalBon_Nom = QLineEdit(self.gridLayoutWidget_6)
        self.lEdit_nomTotalBon_Nom.setObjectName(u"lEdit_nomTotalBon_Nom")
        self.lEdit_nomTotalBon_Nom.setEnabled(False)

        self.gL_organizador_Nom_2.addWidget(self.lEdit_nomTotalBon_Nom, 1, 4, 1, 1)

        self.label_nomTotalBon_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomTotalBon_Nom.setObjectName(u"label_nomTotalBon_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomTotalBon_Nom, 1, 2, 1, 1)

        self.label_nomTotalDes_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomTotalDes_Nom.setObjectName(u"label_nomTotalDes_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomTotalDes_Nom, 2, 2, 1, 1)

        self.label_nomMes_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomMes_Nom.setObjectName(u"label_nomMes_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomMes_Nom, 1, 0, 1, 1)

        self.label_nomAnio_Nom = QLabel(self.gridLayoutWidget_6)
        self.label_nomAnio_Nom.setObjectName(u"label_nomAnio_Nom")

        self.gL_organizador_Nom_2.addWidget(self.label_nomAnio_Nom, 0, 0, 1, 1)

        self.frame_tabla_2_1_Nom.raise_()
        self.frame_tabla_1_1_Nom.raise_()
        self.frame_tabla_1_0_DesBon.raise_()
        self.frame_tabla_0_0_Emp.raise_()
        self.frame_tabla_0_1_Nom.raise_()
        self.frame_tabla_2_0_Nom.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_desBonDescripcion_DesBon.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_desBonValor_DesBon.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.label_desBonCodigo_DesBon.setText(QCoreApplication.translate("MainWindow", u"DESxBON", None))
        self.boton_Buscar_DesBon.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.boton_Confirmar_DesBon.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.boton_Cancelar_DesBon.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_empCodigo_Emp.setText(QCoreApplication.translate("MainWindow", u"EmpCodigo", None))
        self.boton_BuscarCodigo_Emp.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_empIdentificacion_Emp.setText(QCoreApplication.translate("MainWindow", u"Cedula", None))
        self.label_nomCodigo_Nom.setText(QCoreApplication.translate("MainWindow", u"Codigo Nomina", None))
        self.lEdit_nomCodigo_Nom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOM-###", None))
        self.label_empNombre_Nom.setText(QCoreApplication.translate("MainWindow", u"Nombre Emp", None))
        self.label_nomFechaFinal_Nom.setText(QCoreApplication.translate("MainWindow", u"Fecha Final", None))
        self.label_nomFechaInicial_Nom.setText(QCoreApplication.translate("MainWindow", u"Fecha Inicial", None))
        self.lEdit_nomTotalHoras_Nom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"###", None))
        self.label_empCargo_Nom.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.label_nomTotalHoras_Nom.setText(QCoreApplication.translate("MainWindow", u"Total Horas", None))
        self.boton_CancelarNom_Nom.setText(QCoreApplication.translate("MainWindow", u"CANCELAR NOMINA", None))
        self.boton_GenerarNom_Nom.setText(QCoreApplication.translate("MainWindow", u"GENERAR NOMINA", None))
        self.boton_VisualizarNom_Nom.setText(QCoreApplication.translate("MainWindow", u"VISUALIZAR NOMINAS", None))
        self.boton_VisualizarLiq_Liq.setText(QCoreApplication.translate("MainWindow", u"LIQUIDACIONES", None))
        self.label_nomSubTotal_Nom.setText(QCoreApplication.translate("MainWindow", u"SUB TOTAL", None))
        self.label_nomTotal_Nom.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.label_nomTotalBon_Nom.setText(QCoreApplication.translate("MainWindow", u"TOTAL BONIFICACIONES", None))
        self.label_nomTotalDes_Nom.setText(QCoreApplication.translate("MainWindow", u"TOTAL DESCUENTOS", None))
        self.label_nomMes_Nom.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.label_nomAnio_Nom.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
    # retranslateUi

