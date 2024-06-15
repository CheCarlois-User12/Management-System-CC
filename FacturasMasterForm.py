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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class FacturasMasterForm(object):
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
        self.frame_tabla_1_1_PDetail = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_1_1_PDetail.setObjectName(u"frame_tabla_1_1_PDetail")
        self.frame_tabla_1_1_PDetail.setGeometry(QRect(400, 150, 821, 311))
        self.frame_tabla_1_1_PDetail.setStyleSheet(u"\n"
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
        self.frame_tabla_1_1_PDetail.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_1_1_PDetail.setFrameShadow(QFrame.Raised)

        # Añadir la tabla
        self.tableWidget = QTableWidget(self.frame_tabla_1_1_PDetail)
        self.tableWidget.setGeometry(QRect(10, 10, 800, 290))
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setHorizontalHeaderLabels(["Código", "Descripción", "Unidad de Medida", "Valor Unitario", "Cantidad", "Descuento", "Subtotal", "Desc. Subtotal", "IVA", "IVA Subtotal", "Editar", "Eliminar"])

        self.frame_tabla_1_0_PDetail = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_1_0_PDetail.setObjectName(u"frame_tabla_1_0_PDetail")
        self.frame_tabla_1_0_PDetail.setGeometry(QRect(20, 150, 371, 311))
        self.frame_tabla_1_0_PDetail.setStyleSheet(u"\n"
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
        self.frame_tabla_1_0_PDetail.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_1_0_PDetail.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_tabla_1_0_PDetail)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 341, 251))
        self.gL_organizador_PDetail = QGridLayout(self.gridLayoutWidget)
        self.gL_organizador_PDetail.setObjectName(u"gL_organizador_PDetail")
        self.gL_organizador_PDetail.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_VUnitario_PDetail = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_VUnitario_PDetail.setObjectName(u"lineEdit_VUnitario_PDetail")

        self.gL_organizador_PDetail.addWidget(self.lineEdit_VUnitario_PDetail, 3, 2, 1, 1)

        self.boton_Buscar_PDetail = QPushButton(self.gridLayoutWidget)
        self.boton_Buscar_PDetail.setObjectName(u"boton_Buscar_PDetail")

        self.gL_organizador_PDetail.addWidget(self.boton_Buscar_PDetail, 0, 3, 1, 1)

        self.label_proCodigo_PDetail = QLabel(self.gridLayoutWidget)
        self.label_proCodigo_PDetail.setObjectName(u"label_proCodigo_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_proCodigo_PDetail, 0, 0, 1, 1)

        self.label_UMedida_PDetail = QLabel(self.gridLayoutWidget)
        self.label_UMedida_PDetail.setObjectName(u"label_UMedida_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_UMedida_PDetail, 2, 0, 1, 1)

        self.lineEdit_Cantidad_PDetail = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Cantidad_PDetail.setObjectName(u"lineEdit_Cantidad_PDetail")

        self.gL_organizador_PDetail.addWidget(self.lineEdit_Cantidad_PDetail, 4, 2, 1, 1)

        self.lineEdit_UMedida_PDetail = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_UMedida_PDetail.setObjectName(u"lineEdit_UMedida_PDetail")

        self.gL_organizador_PDetail.addWidget(self.lineEdit_UMedida_PDetail, 2, 2, 1, 1)

        self.label_Desripcion_PDetail = QLabel(self.gridLayoutWidget)
        self.label_Desripcion_PDetail.setObjectName(u"label_Desripcion_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_Desripcion_PDetail, 1, 0, 1, 1)

        self.label_Cantidad_PDetail = QLabel(self.gridLayoutWidget)
        self.label_Cantidad_PDetail.setObjectName(u"label_Cantidad_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_Cantidad_PDetail, 4, 0, 1, 1)

        self.label_VUnitario_PDetail = QLabel(self.gridLayoutWidget)
        self.label_VUnitario_PDetail.setObjectName(u"label_VUnitario_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_VUnitario_PDetail, 3, 0, 1, 1)

        self.label_Iva_PDetail = QLabel(self.gridLayoutWidget)
        self.label_Iva_PDetail.setObjectName(u"label_Iva_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_Iva_PDetail, 7, 0, 1, 1)

        self.lineEdit_Descripcion_PDetail = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Descripcion_PDetail.setObjectName(u"lineEdit_Descripcion_PDetail")

        self.gL_organizador_PDetail.addWidget(self.lineEdit_Descripcion_PDetail, 1, 2, 1, 1)

        self.lineEdit_Descuento_PDetail = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Descuento_PDetail.setObjectName(u"lineEdit_Descuento_PDetail")

        self.gL_organizador_PDetail.addWidget(self.lineEdit_Descuento_PDetail, 5, 2, 1, 1)

        self.label_Descuento_PDetail = QLabel(self.gridLayoutWidget)
        self.label_Descuento_PDetail.setObjectName(u"label_Descuento_PDetail")

        self.gL_organizador_PDetail.addWidget(self.label_Descuento_PDetail, 5, 0, 1, 1)

        self.cBox_IVA_PDetail = QComboBox(self.gridLayoutWidget)
        self.cBox_IVA_PDetail.setObjectName(u"cBox_IVA_PDetail")

        self.gL_organizador_PDetail.addWidget(self.cBox_IVA_PDetail, 7, 2, 1, 1)

        self.cBox_proCodigo_PDetail = QComboBox(self.gridLayoutWidget)
        self.cBox_proCodigo_PDetail.setObjectName(u"cBox_proCodigo_PDetail")

        self.gL_organizador_PDetail.addWidget(self.cBox_proCodigo_PDetail, 0, 2, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.frame_tabla_1_0_PDetail)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 260, 188, 41))
        self.hL_organizador_PDetail = QHBoxLayout(self.horizontalLayoutWidget)
        self.hL_organizador_PDetail.setObjectName(u"hL_organizador_PDetail")
        self.hL_organizador_PDetail.setContentsMargins(0, 0, 0, 0)
        self.boton_Confirmar_PDetail = QPushButton(self.horizontalLayoutWidget)
        self.boton_Confirmar_PDetail.setObjectName(u"boton_Confirmar_PDetail")

        self.hL_organizador_PDetail.addWidget(self.boton_Confirmar_PDetail)

        self.boton_Cancelar_PDetail = QPushButton(self.horizontalLayoutWidget)
        self.boton_Cancelar_PDetail.setObjectName(u"boton_Cancelar_PDetail")

        self.hL_organizador_PDetail.addWidget(self.boton_Cancelar_PDetail)

        self.frame_tabla_0_0_Cli = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_0_0_Cli.setObjectName(u"frame_tabla_0_0_Cli")
        self.frame_tabla_0_0_Cli.setGeometry(QRect(20, 10, 371, 131))
        self.frame_tabla_0_0_Cli.setStyleSheet(u"\n"
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
        self.frame_tabla_0_0_Cli.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_0_0_Cli.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_tabla_0_0_Cli)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 10, 341, 101))
        self.gL_organizador_Cli = QGridLayout(self.gridLayoutWidget_2)
        self.gL_organizador_Cli.setObjectName(u"gL_organizador_Cli")
        self.gL_organizador_Cli.setContentsMargins(0, 0, 0, 0)
        self.label_CodigoClientes_Cli = QLabel(self.gridLayoutWidget_2)
        self.label_CodigoClientes_Cli.setObjectName(u"label_CodigoClientes_Cli")

        self.gL_organizador_Cli.addWidget(self.label_CodigoClientes_Cli, 0, 0, 1, 1)

        self.boton_BuscarCodigo_Cli = QPushButton(self.gridLayoutWidget_2)
        self.boton_BuscarCodigo_Cli.setObjectName(u"boton_BuscarCodigo_Cli")

        self.gL_organizador_Cli.addWidget(self.boton_BuscarCodigo_Cli, 0, 2, 1, 1)

        self.label_cliIdentificacion_Cli = QLabel(self.gridLayoutWidget_2)
        self.label_cliIdentificacion_Cli.setObjectName(u"label_cliIdentificacion_Cli")

        self.gL_organizador_Cli.addWidget(self.label_cliIdentificacion_Cli, 1, 0, 1, 1)

        self.lineEdit_cliIdentificacion_Cli = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_cliIdentificacion_Cli.setObjectName(u"lineEdit_cliIdentificacion_Cli")

        self.gL_organizador_Cli.addWidget(self.lineEdit_cliIdentificacion_Cli, 1, 1, 1, 1)

        self.cBox_CodigoClientes_Cli = QComboBox(self.gridLayoutWidget_2)
        self.cBox_CodigoClientes_Cli.setObjectName(u"cBox_CodigoClientes_Cli")

        self.gL_organizador_Cli.addWidget(self.cBox_CodigoClientes_Cli, 0, 1, 1, 1)

        self.frame_tabla_0_1_Fact = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_0_1_Fact.setObjectName(u"frame_tabla_0_1_Fact")
        self.frame_tabla_0_1_Fact.setGeometry(QRect(400, 10, 821, 131))
        self.frame_tabla_0_1_Fact.setStyleSheet(u"\n"
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
        self.frame_tabla_0_1_Fact.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_0_1_Fact.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_tabla_0_1_Fact)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(430, 10, 381, 100))
        self.gL_organizardor_Fact = QGridLayout(self.gridLayoutWidget_3)
        self.gL_organizardor_Fact.setObjectName(u"gL_organizardor_Fact")
        self.gL_organizardor_Fact.setContentsMargins(0, 0, 0, 0)
        self.dateEdit_Fecha_Fact = QDateEdit(self.gridLayoutWidget_3)
        self.dateEdit_Fecha_Fact.setObjectName(u"dateEdit_Fecha_Fact")

        self.gL_organizardor_Fact.addWidget(self.dateEdit_Fecha_Fact, 2, 1, 1, 1)

        self.label_Fecha_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_Fecha_Fact.setObjectName(u"label_Fecha_Fact")

        self.gL_organizardor_Fact.addWidget(self.label_Fecha_Fact, 2, 0, 1, 1)

        self.lineEdit_Hora_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_Hora_Fact.setObjectName(u"lineEdit_Hora_Fact")

        self.gL_organizardor_Fact.addWidget(self.lineEdit_Hora_Fact, 2, 3, 1, 1)

        self.label_HoraFact_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_HoraFact_Fact.setObjectName(u"label_HoraFact_Fact")

        self.gL_organizardor_Fact.addWidget(self.label_HoraFact_Fact, 2, 2, 1, 1)

        self.lineEdit_NombreCli_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_NombreCli_Fact.setObjectName(u"lineEdit_NombreCli_Fact")

        self.gL_organizardor_Fact.addWidget(self.lineEdit_NombreCli_Fact, 0, 1, 1, 3)

        self.label_NombreCli_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_NombreCli_Fact.setObjectName(u"label_NombreCli_Fact")

        self.gL_organizardor_Fact.addWidget(self.label_NombreCli_Fact, 0, 0, 1, 1)

        self.label_CodigoFact_Fact = QLabel(self.gridLayoutWidget_3)
        self.label_CodigoFact_Fact.setObjectName(u"label_CodigoFact_Fact")

        self.gL_organizardor_Fact.addWidget(self.label_CodigoFact_Fact, 3, 0, 1, 1)

        self.lineEdit_CodigoFact_Fact = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_CodigoFact_Fact.setObjectName(u"lineEdit_CodigoFact_Fact")

        self.gL_organizardor_Fact.addWidget(self.lineEdit_CodigoFact_Fact, 3, 1, 1, 2)

        self.frame_tabla_2_0_Fact = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_2_0_Fact.setObjectName(u"frame_tabla_2_0_Fact")
        self.frame_tabla_2_0_Fact.setGeometry(QRect(20, 469, 371, 141))
        self.frame_tabla_2_0_Fact.setStyleSheet(u"\n"
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
        self.frame_tabla_2_0_Fact.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_2_0_Fact.setFrameShadow(QFrame.Raised)
        self.boton_GenerarFact_Fact = QPushButton(self.frame_tabla_2_0_Fact)
        self.boton_GenerarFact_Fact.setObjectName(u"boton_GenerarFact_Fact")
        self.boton_GenerarFact_Fact.setGeometry(QRect(20, 20, 141, 29))
        self.boton_Cancelar_Fact = QPushButton(self.frame_tabla_2_0_Fact)
        self.boton_Cancelar_Fact.setObjectName(u"boton_Cancelar_Fact")
        self.boton_Cancelar_Fact.setGeometry(QRect(180, 20, 151, 29))
        self.frame_tabla_2_1_Fact = QFrame(self.fVTablasVentas_1)
        self.frame_tabla_2_1_Fact.setObjectName(u"frame_tabla_2_1_Fact")
        self.frame_tabla_2_1_Fact.setGeometry(QRect(400, 470, 821, 141))
        self.frame_tabla_2_1_Fact.setStyleSheet(u"\n"
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
        self.frame_tabla_2_1_Fact.setFrameShape(QFrame.StyledPanel)
        self.frame_tabla_2_1_Fact.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_tabla_2_1_Fact)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(350, 0, 461, 131))
        self.gL_organizador_Fact_1 = QGridLayout(self.gridLayoutWidget_4)
        self.gL_organizador_Fact_1.setObjectName(u"gL_organizador_Fact_1")
        self.gL_organizador_Fact_1.setContentsMargins(0, 0, 0, 0)
        self.fL_organizador_Fact_1 = QFormLayout()
        self.fL_organizador_Fact_1.setObjectName(u"fL_organizador_Fact_1")
        self.label_FormaPago_Fact = QLabel(self.gridLayoutWidget_4)
        self.label_FormaPago_Fact.setObjectName(u"label_FormaPago_Fact")

        self.fL_organizador_Fact_1.setWidget(0, QFormLayout.LabelRole, self.label_FormaPago_Fact)

        self.cBox_FormaPago_Fact = QComboBox(self.gridLayoutWidget_4)
        self.cBox_FormaPago_Fact.setObjectName(u"cBox_FormaPago_Fact")

        self.fL_organizador_Fact_1.setWidget(0, QFormLayout.FieldRole, self.cBox_FormaPago_Fact)


        self.gL_organizador_Fact_1.addLayout(self.fL_organizador_Fact_1, 0, 0, 1, 1)

        self.fL_organizador_Fact_2 = QFormLayout()
        self.fL_organizador_Fact_2.setObjectName(u"fL_organizador_Fact_2")
        self.label_SubTotal_Fact = QLabel(self.gridLayoutWidget_4)
        self.label_SubTotal_Fact.setObjectName(u"label_SubTotal_Fact")

        self.fL_organizador_Fact_2.setWidget(0, QFormLayout.LabelRole, self.label_SubTotal_Fact)

        self.label_TotalIva_Fact = QLabel(self.gridLayoutWidget_4)
        self.label_TotalIva_Fact.setObjectName(u"label_TotalIva_Fact")

        self.fL_organizador_Fact_2.setWidget(2, QFormLayout.LabelRole, self.label_TotalIva_Fact)

        self.label_Total_Fact = QLabel(self.gridLayoutWidget_4)
        self.label_Total_Fact.setObjectName(u"label_Total_Fact")

        self.fL_organizador_Fact_2.setWidget(3, QFormLayout.LabelRole, self.label_Total_Fact)

        self.lineEdit_TotalIva_Fact = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_TotalIva_Fact.setObjectName(u"lineEdit_TotalIva_Fact")

        self.fL_organizador_Fact_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_TotalIva_Fact)

        self.lineEdit_SubTotal_Fact = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_SubTotal_Fact.setObjectName(u"lineEdit_SubTotal_Fact")

        self.fL_organizador_Fact_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_SubTotal_Fact)

        self.lineEdit_Total_Fact = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_Total_Fact.setObjectName(u"lineEdit_Total_Fact")

        self.fL_organizador_Fact_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_Total_Fact)

        self.label_TotalDesc_Fact = QLabel(self.gridLayoutWidget_4)
        self.label_TotalDesc_Fact.setObjectName(u"label_TotalDesc_Fact")

        self.fL_organizador_Fact_2.setWidget(1, QFormLayout.LabelRole, self.label_TotalDesc_Fact)

        self.lineEdit_totalDesc = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_totalDesc.setObjectName(u"lineEdit_totalDesc")

        self.fL_organizador_Fact_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_totalDesc)


        self.gL_organizador_Fact_1.addLayout(self.fL_organizador_Fact_2, 0, 1, 1, 1)

        self.frame_tabla_2_1_Fact.raise_()
        self.frame_tabla_1_1_PDetail.raise_()
        self.frame_tabla_1_0_PDetail.raise_()
        self.frame_tabla_0_0_Cli.raise_()
        self.frame_tabla_0_1_Fact.raise_()
        self.frame_tabla_2_0_Fact.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_Buscar_PDetail.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_proCodigo_PDetail.setText(QCoreApplication.translate("MainWindow", u"Identificador", None))
        self.label_UMedida_PDetail.setText(QCoreApplication.translate("MainWindow", u"Unidad Medida", None))
        self.label_Desripcion_PDetail.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_Cantidad_PDetail.setText(QCoreApplication.translate("MainWindow", u"cantidad", None))
        self.label_VUnitario_PDetail.setText(QCoreApplication.translate("MainWindow", u"Valor Unitario", None))
        self.label_Iva_PDetail.setText(QCoreApplication.translate("MainWindow", u"IVA", None))
        self.label_Descuento_PDetail.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
        self.boton_Confirmar_PDetail.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.boton_Cancelar_PDetail.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_CodigoClientes_Cli.setText(QCoreApplication.translate("MainWindow", u"Credencial", None))
        self.boton_BuscarCodigo_Cli.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_cliIdentificacion_Cli.setText(QCoreApplication.translate("MainWindow", u"ruc o cedula", None))
        self.label_Fecha_Fact.setText(QCoreApplication.translate("MainWindow", u"FECHA", None))
        self.label_HoraFact_Fact.setText(QCoreApplication.translate("MainWindow", u"HORA", None))
        self.label_NombreCli_Fact.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.label_CodigoFact_Fact.setText(QCoreApplication.translate("MainWindow", u"CODIGO FACTURA", None))
        self.boton_GenerarFact_Fact.setText(QCoreApplication.translate("MainWindow", u"GENERAR FACTURA", None))
        self.boton_Cancelar_Fact.setText(QCoreApplication.translate("MainWindow", u"CANCELAR FACTURA", None))
        self.label_FormaPago_Fact.setText(QCoreApplication.translate("MainWindow", u"FORMA PAGO", None))
        self.label_SubTotal_Fact.setText(QCoreApplication.translate("MainWindow", u"SUB TOTAL", None))
        self.label_TotalIva_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL IVA", None))
        self.label_Total_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.label_TotalDesc_Fact.setText(QCoreApplication.translate("MainWindow", u"TOTAL DESC", None))
    # retranslateUi
