# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_Actual.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1500, 720))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setMinimumSize(QSize(1280, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"/* Estilo para QTabWidget */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #C73659;\n"
"    background-color: #1b1717;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Estilo para QTabBar */\n"
"QTabBar::tab {\n"
"    background: #1b1717;\n"
"    color: white;\n"
"    border: 2px solid #BACDDB;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    padding: 10px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #C73659;\n"
"    border-color: #aaaaaa;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #666666;\n"
"    border-color: #aaaaaa;\n"
"}\n"
"")
        self.tabTalentoHumano = QWidget()
        self.tabTalentoHumano.setObjectName(u"tabTalentoHumano")
        sizePolicy2.setHeightForWidth(self.tabTalentoHumano.sizePolicy().hasHeightForWidth())
        self.tabTalentoHumano.setSizePolicy(sizePolicy2)
        self.tabTalentoHumano.setMinimumSize(QSize(1280, 720))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(155, 240, 233, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush3)
        brush4 = QBrush(QColor(205, 247, 244, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        brush5 = QBrush(QColor(78, 120, 117, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush5)
        brush6 = QBrush(QColor(103, 160, 155, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        brush7 = QBrush(QColor(27, 23, 23, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        brush10 = QBrush(QColor(78, 120, 117, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(222, 255, 252, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.tabTalentoHumano.setPalette(palette1)
        self.tabTalentoHumano.setAutoFillBackground(True)
        self.tabTalentoHumano.setStyleSheet(u"QTabBar::tab {\n"
"    background: #1b1717;\n"
"}")
        self.hwTalentoHumano_1 = QWidget(self.tabTalentoHumano)
        self.hwTalentoHumano_1.setObjectName(u"hwTalentoHumano_1")
        self.hwTalentoHumano_1.setGeometry(QRect(0, 0, 1481, 641))
        self.horizontalLayout = QHBoxLayout(self.hwTalentoHumano_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fBTalentoHumano_1 = QFrame(self.hwTalentoHumano_1)
        self.fBTalentoHumano_1.setObjectName(u"fBTalentoHumano_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fBTalentoHumano_1.sizePolicy().hasHeightForWidth())
        self.fBTalentoHumano_1.setSizePolicy(sizePolicy3)
        self.fBTalentoHumano_1.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        brush12 = QBrush(QColor(38, 0, 27, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.fBTalentoHumano_1.setPalette(palette2)
        self.fBTalentoHumano_1.setAcceptDrops(False)
        self.fBTalentoHumano_1.setAutoFillBackground(False)
        self.fBTalentoHumano_1.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #C73659;\n"
"    border: 2px solid #888888;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CE5959;\n"
"    border: 2px solid #aaaaaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CE5959;\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #BACDDB;\n"
"    border: 2px solid #444444;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: 1px solid #26001B;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #26001B;\n"
"}")
        self.fBTalentoHumano_1.setFrameShape(QFrame.StyledPanel)
        self.fBTalentoHumano_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.fBTalentoHumano_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.botonNomina = QPushButton(self.fBTalentoHumano_1)
        self.botonNomina.setObjectName(u"botonNomina")
        sizePolicy2.setHeightForWidth(self.botonNomina.sizePolicy().hasHeightForWidth())
        self.botonNomina.setSizePolicy(sizePolicy2)
        self.botonNomina.setMinimumSize(QSize(156, 0))
        icon = QIcon()
        icon.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/box.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonNomina.setIcon(icon)
        self.botonNomina.setCheckable(False)
        self.botonNomina.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.botonNomina, 4, 0, 1, 1)

        self.botonBonificaciones = QPushButton(self.fBTalentoHumano_1)
        self.botonBonificaciones.setObjectName(u"botonBonificaciones")
        sizePolicy2.setHeightForWidth(self.botonBonificaciones.sizePolicy().hasHeightForWidth())
        self.botonBonificaciones.setSizePolicy(sizePolicy2)
        self.botonBonificaciones.setMinimumSize(QSize(156, 0))
        icon1 = QIcon()
        icon1.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/save-money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonBonificaciones.setIcon(icon1)
        self.botonBonificaciones.setCheckable(False)
        self.botonBonificaciones.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.botonBonificaciones, 3, 0, 1, 1)

        self.botonEmpleados = QPushButton(self.fBTalentoHumano_1)
        self.botonEmpleados.setObjectName(u"botonEmpleados")
        sizePolicy2.setHeightForWidth(self.botonEmpleados.sizePolicy().hasHeightForWidth())
        self.botonEmpleados.setSizePolicy(sizePolicy2)
        self.botonEmpleados.setMinimumSize(QSize(156, 0))
        icon2 = QIcon()
        icon2.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/customer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonEmpleados.setIcon(icon2)
        self.botonEmpleados.setCheckable(False)
        self.botonEmpleados.setChecked(False)
        self.botonEmpleados.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.botonEmpleados, 0, 0, 1, 1)

        self.botonDescuentos = QPushButton(self.fBTalentoHumano_1)
        self.botonDescuentos.setObjectName(u"botonDescuentos")
        sizePolicy2.setHeightForWidth(self.botonDescuentos.sizePolicy().hasHeightForWidth())
        self.botonDescuentos.setSizePolicy(sizePolicy2)
        self.botonDescuentos.setMinimumSize(QSize(156, 0))
        icon3 = QIcon()
        icon3.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/income.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonDescuentos.setIcon(icon3)
        self.botonDescuentos.setCheckable(False)
        self.botonDescuentos.setAutoExclusive(False)

        self.gridLayout_4.addWidget(self.botonDescuentos, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.fBTalentoHumano_1)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(154, 270))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_2, 5, 0, 1, 1)


        self.horizontalLayout.addWidget(self.fBTalentoHumano_1)

        self.hSTalentoHumano_1 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.hSTalentoHumano_1)

        self.fVTablasTalentoHumano_1 = QFrame(self.hwTalentoHumano_1)
        self.fVTablasTalentoHumano_1.setObjectName(u"fVTablasTalentoHumano_1")
        sizePolicy1.setHeightForWidth(self.fVTablasTalentoHumano_1.sizePolicy().hasHeightForWidth())
        self.fVTablasTalentoHumano_1.setSizePolicy(sizePolicy1)
        self.fVTablasTalentoHumano_1.setMinimumSize(QSize(1250, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.fVTablasTalentoHumano_1.setPalette(palette3)

        self.fVTablasTalentoHumano_1.setFrameShape(QFrame.StyledPanel)
        self.fVTablasTalentoHumano_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.fVTablasTalentoHumano_1)

        self.tabWidget.addTab(self.tabTalentoHumano, icon2, "")
        self.tabVentas = QWidget()
        self.tabVentas.setObjectName(u"tabVentas")
        self.hwVentas_1 = QWidget(self.tabVentas)
        self.hwVentas_1.setObjectName(u"hwVentas_1")
        self.hwVentas_1.setGeometry(QRect(0, 0, 1481, 641))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.hwVentas_1.setPalette(palette4)
        self.horizontalLayout_3 = QHBoxLayout(self.hwVentas_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fBTalentoHumano_2 = QFrame(self.hwVentas_1)
        self.fBTalentoHumano_2.setObjectName(u"fBTalentoHumano_2")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.fBTalentoHumano_2.setPalette(palette5)
        self.fBTalentoHumano_2.setAcceptDrops(False)
        self.fBTalentoHumano_2.setAutoFillBackground(False)
        self.fBTalentoHumano_2.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: #C73659;\n"
"    border: 2px solid #888888;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #CE5959;\n"
"    border: 2px solid #aaaaaa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CE5959;\n"
"    border: 2px solid #666666;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #BACDDB;\n"
"    border: 2px solid #444444;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: 1px solid #26001B;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: #26001B;\n"
"}")
        self.fBTalentoHumano_2.setFrameShape(QFrame.StyledPanel)
        self.fBTalentoHumano_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.fBTalentoHumano_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.botonFACTxDETAILS = QPushButton(self.fBTalentoHumano_2)
        self.botonFACTxDETAILS.setObjectName(u"botonFACTxDETAILS")
        sizePolicy2.setHeightForWidth(self.botonFACTxDETAILS.sizePolicy().hasHeightForWidth())
        self.botonFACTxDETAILS.setSizePolicy(sizePolicy2)
        self.botonFACTxDETAILS.setMinimumSize(QSize(156, 0))
        icon4 = QIcon()
        icon4.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/invoice.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonFACTxDETAILS.setIcon(icon4)
        self.botonFACTxDETAILS.setCheckable(False)
        self.botonFACTxDETAILS.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.botonFACTxDETAILS, 1, 0, 1, 1)

        self.botonProductos = QPushButton(self.fBTalentoHumano_2)
        self.botonProductos.setObjectName(u"botonProductos")
        sizePolicy2.setHeightForWidth(self.botonProductos.sizePolicy().hasHeightForWidth())
        self.botonProductos.setSizePolicy(sizePolicy2)
        self.botonProductos.setMinimumSize(QSize(156, 0))
        icon5 = QIcon()
        icon5.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/order.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonProductos.setIcon(icon5)
        self.botonProductos.setCheckable(False)
        self.botonProductos.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.botonProductos, 2, 0, 1, 1)

        self.botonClientes = QPushButton(self.fBTalentoHumano_2)
        self.botonClientes.setObjectName(u"botonClientes")
        sizePolicy2.setHeightForWidth(self.botonClientes.sizePolicy().hasHeightForWidth())
        self.botonClientes.setSizePolicy(sizePolicy2)
        self.botonClientes.setMinimumSize(QSize(156, 0))
        icon6 = QIcon()
        icon6.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/account.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonClientes.setIcon(icon6)
        self.botonClientes.setCheckable(False)
        self.botonClientes.setChecked(False)
        self.botonClientes.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.botonClientes, 0, 0, 1, 1)

        self.frame = QFrame(self.fBTalentoHumano_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.fBTalentoHumano_2)

        self.hSVentas_1 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.hSVentas_1)

        self.fVTablasVentas_1 = QFrame(self.hwVentas_1)
        self.fVTablasVentas_1.setObjectName(u"fVTablasVentas_1")
        sizePolicy1.setHeightForWidth(self.fVTablasVentas_1.sizePolicy().hasHeightForWidth())
        self.fVTablasVentas_1.setSizePolicy(sizePolicy1)
        self.fVTablasVentas_1.setMinimumSize(QSize(1250, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        self.fVTablasVentas_1.setPalette(palette6)
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

        self.horizontalLayout_3.addWidget(self.fVTablasVentas_1)

        icon7 = QIcon()
        icon7.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/bill.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabVentas, icon7, "")
        self.tabIniciarSesion = QWidget()
        self.tabIniciarSesion.setObjectName(u"tabIniciarSesion")
        sizePolicy2.setHeightForWidth(self.tabIniciarSesion.sizePolicy().hasHeightForWidth())
        self.tabIniciarSesion.setSizePolicy(sizePolicy2)
        self.tabIniciarSesion.setMinimumSize(QSize(1280, 720))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush12)
        self.tabIniciarSesion.setPalette(palette7)
        self.tabIniciarSesion.setAutoFillBackground(True)
        self.vWIniciarSesion_1 = QWidget(self.tabIniciarSesion)
        self.vWIniciarSesion_1.setObjectName(u"vWIniciarSesion_1")
        self.vWIniciarSesion_1.setGeometry(QRect(500, 210, 681, 181))
        self.verticalLayout_3 = QVBoxLayout(self.vWIniciarSesion_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layoutWidget = QWidget(self.tabIniciarSesion)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(440, 210, 659, 170))
        self.vWIniciarSesion_2 = QVBoxLayout(self.layoutWidget)
        self.vWIniciarSesion_2.setObjectName(u"vWIniciarSesion_2")
        self.vWIniciarSesion_2.setContentsMargins(0, 0, 0, 0)
        self.labelIniciarSesion_1 = QLabel(self.layoutWidget)
        self.labelIniciarSesion_1.setObjectName(u"labelIniciarSesion_1")
        sizePolicy2.setHeightForWidth(self.labelIniciarSesion_1.sizePolicy().hasHeightForWidth())
        self.labelIniciarSesion_1.setSizePolicy(sizePolicy2)
        self.labelIniciarSesion_1.setMinimumSize(QSize(657, 33))
        self.labelIniciarSesion_1.setStyleSheet(u"QLabel {\n"
"    color: palette(window-text);\n"
"    font-size: 14px;\n"
"    padding: 2px;\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    background-color: palette(window);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: palette(base);\n"
"    color: palette(text);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #555555;\n"
"}\n"
"")
        self.labelIniciarSesion_1.setAlignment(Qt.AlignCenter)

        self.vWIniciarSesion_2.addWidget(self.labelIniciarSesion_1)

        self.gLIniciarSesion_1 = QGridLayout()
        self.gLIniciarSesion_1.setObjectName(u"gLIniciarSesion_1")
        self.labelClave_1 = QLabel(self.layoutWidget)
        self.labelClave_1.setObjectName(u"labelClave_1")
        self.labelClave_1.setStyleSheet(u"QLabel {\n"
"    color: palette(window-text);\n"
"    font-size: 14px;\n"
"    padding: 2px;\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    background-color: palette(window);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: palette(base);\n"
"    color: palette(text);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #555555;\n"
"}\n"
"")
        self.labelClave_1.setAlignment(Qt.AlignCenter)

        self.gLIniciarSesion_1.addWidget(self.labelClave_1, 2, 0, 1, 1)

        self.entryUsuario_1 = QLineEdit(self.layoutWidget)
        self.entryUsuario_1.setObjectName(u"entryUsuario_1")
        self.entryUsuario_1.setAlignment(Qt.AlignCenter)

        self.gLIniciarSesion_1.addWidget(self.entryUsuario_1, 1, 1, 1, 1)

        self.labelUsuario_1 = QLabel(self.layoutWidget)
        self.labelUsuario_1.setObjectName(u"labelUsuario_1")
        self.labelUsuario_1.setStyleSheet(u"QLabel {\n"
"    color: palette(window-text);\n"
"    font-size: 14px;\n"
"    padding: 2px;\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    background-color: palette(window);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #888888;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: palette(base);\n"
"    color: palette(text);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #555555;\n"
"}\n"
"")
        self.labelUsuario_1.setAlignment(Qt.AlignCenter)

        self.gLIniciarSesion_1.addWidget(self.labelUsuario_1, 1, 0, 1, 1)

        self.entryClave_1 = QLineEdit(self.layoutWidget)
        self.entryClave_1.setObjectName(u"entryClave_1")
        self.entryClave_1.setAlignment(Qt.AlignCenter)

        self.gLIniciarSesion_1.addWidget(self.entryClave_1, 2, 1, 1, 1)


        self.vWIniciarSesion_2.addLayout(self.gLIniciarSesion_1)

        self.hLIniciarSesion_1 = QHBoxLayout()
        self.hLIniciarSesion_1.setObjectName(u"hLIniciarSesion_1")
        self.botonCerrarSesion_1 = QPushButton(self.layoutWidget)
        self.botonCerrarSesion_1.setObjectName(u"botonCerrarSesion_1")
        icon8 = QIcon()
        icon8.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonCerrarSesion_1.setIcon(icon8)

        self.hLIniciarSesion_1.addWidget(self.botonCerrarSesion_1)

        self.botonIniciarSesion_1 = QPushButton(self.layoutWidget)
        self.botonIniciarSesion_1.setObjectName(u"botonIniciarSesion_1")
        icon9 = QIcon()
        icon9.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonIniciarSesion_1.setIcon(icon9)

        self.hLIniciarSesion_1.addWidget(self.botonIniciarSesion_1)


        self.vWIniciarSesion_2.addLayout(self.hLIniciarSesion_1)

        icon10 = QIcon()
        icon10.addFile(u"../Universidad/4to Semestre/Bases de Datos 1/Unidad 4/Proyectos/Python/EmpleadosExoneracion/Imagenes/iconos/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tabIniciarSesion, icon10, "")
        self.ManejoArchivos = QWidget()
        self.ManejoArchivos.setObjectName(u"ManejoArchivos")
        self.tabWidget.addTab(self.ManejoArchivos, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botonNomina.setText(QCoreApplication.translate("MainWindow", u"NOMINA", None))
        self.botonBonificaciones.setText(QCoreApplication.translate("MainWindow", u"BONIFICACION", None))
        self.botonEmpleados.setText(QCoreApplication.translate("MainWindow", u"EMPLEADOS", None))
        self.botonDescuentos.setText(QCoreApplication.translate("MainWindow", u"DESCUENTOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTalentoHumano), QCoreApplication.translate("MainWindow", u"TALENTO HUMANO", None))
        self.botonFACTxDETAILS.setText(QCoreApplication.translate("MainWindow", u"FACTxDETAILS", None))
        self.botonProductos.setText(QCoreApplication.translate("MainWindow", u"PRODUCTOS", None))
        self.botonClientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVentas), QCoreApplication.translate("MainWindow", u"VENTAS", None))
        self.labelIniciarSesion_1.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesion en tu usuario", None))
        self.labelClave_1.setText(QCoreApplication.translate("MainWindow", u"Clave", None))
        self.labelUsuario_1.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.botonCerrarSesion_1.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.botonIniciarSesion_1.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIniciarSesion), QCoreApplication.translate("MainWindow", u"INICIAR SESION", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ManejoArchivos), QCoreApplication.translate("MainWindow", u"Utileria", None))
    # retranslateUi

