from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QPushButton, QComboBox,
                               QSizePolicy, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView)


class ProductosDetailsForm(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1251, 342)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(200, 200))
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
        self.fVTablasVentas_1.setGeometry(QRect(0, 0, 1250, 341))
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
        self.frame_Tabla_Producto_Details = QFrame(self.fVTablasVentas_1)
        self.frame_Tabla_Producto_Details.setObjectName(u"frame_Tabla_Producto_Details")
        self.frame_Tabla_Producto_Details.setGeometry(QRect(410, 20, 821, 311))
        self.frame_Tabla_Producto_Details.setStyleSheet(u"\n"
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
        self.frame_Tabla_Producto_Details.setFrameShape(QFrame.StyledPanel)
        self.frame_Tabla_Producto_Details.setFrameShadow(QFrame.Raised)

        self.tableWidget = QTableWidget(self.frame_Tabla_Producto_Details)
        self.tableWidget.setGeometry(QRect(10, 10, 800, 290))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels([
            "Código", "Descripción", "Unidad de Medida", "Valor Unitario",
            "Cantidad", "Descuento", "Subtotal", "Desc. Subtotal", "IVA", "IVA Subtotal"
        ])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.frame_form_Productos_Details = QFrame(self.fVTablasVentas_1)
        self.frame_form_Productos_Details.setObjectName(u"frame_form_Productos_Details")
        self.frame_form_Productos_Details.setGeometry(QRect(30, 20, 371, 311))
        self.frame_form_Productos_Details.setStyleSheet(u"\n"
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
        self.frame_form_Productos_Details.setFrameShape(QFrame.StyledPanel)
        self.frame_form_Productos_Details.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_form_Productos_Details)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 341, 263))
        self.gLProductoDetails = QGridLayout(self.gridLayoutWidget)
        self.gLProductoDetails.setObjectName(u"gLProductoDetails")
        self.gLProductoDetails.setContentsMargins(0, 0, 0, 0)
        self.labelDescripcionProducto = QLabel(self.gridLayoutWidget)
        self.labelDescripcionProducto.setObjectName(u"labelDescripcionProducto")

        self.gLProductoDetails.addWidget(self.labelDescripcionProducto, 1, 0, 1, 1)

        self.labelUMedidaProducto = QLabel(self.gridLayoutWidget)
        self.labelUMedidaProducto.setObjectName(u"labelUMedidaProducto")

        self.gLProductoDetails.addWidget(self.labelUMedidaProducto, 2, 0, 1, 1)

        self.lECantidad = QLineEdit(self.gridLayoutWidget)
        self.lECantidad.setObjectName(u"lECantidad")

        self.gLProductoDetails.addWidget(self.lECantidad, 4, 2, 1, 1)

        self.botonBuscarProducto = QPushButton(self.gridLayoutWidget)
        self.botonBuscarProducto.setObjectName(u"botonBuscarProducto")

        self.gLProductoDetails.addWidget(self.botonBuscarProducto, 0, 3, 1, 1)

        self.lEUMedida = QLineEdit(self.gridLayoutWidget)
        self.lEUMedida.setObjectName(u"lEUMedida")

        self.gLProductoDetails.addWidget(self.lEUMedida, 2, 2, 1, 1)

        self.lEIDentificador = QComboBox(self.gridLayoutWidget)
        self.lEIDentificador.setObjectName(u"lEIDentificador")

        self.gLProductoDetails.addWidget(self.lEIDentificador, 0, 2, 1, 1)

        self.lEVUnitario = QLineEdit(self.gridLayoutWidget)
        self.lEVUnitario.setObjectName(u"lEVUnitario")

        self.gLProductoDetails.addWidget(self.lEVUnitario, 3, 2, 1, 1)

        self.labelCodigoProducto = QLabel(self.gridLayoutWidget)
        self.labelCodigoProducto.setObjectName(u"labelCodigoProducto")

        self.gLProductoDetails.addWidget(self.labelCodigoProducto, 0, 0, 1, 1)

        self.labelCantidad = QLabel(self.gridLayoutWidget)
        self.labelCantidad.setObjectName(u"labelCantidad")

        self.gLProductoDetails.addWidget(self.labelCantidad, 4, 0, 1, 1)

        self.labelVUnitario = QLabel(self.gridLayoutWidget)
        self.labelVUnitario.setObjectName(u"labelVUnitario")

        self.gLProductoDetails.addWidget(self.labelVUnitario, 3, 0, 1, 1)

        self.lEIva = QComboBox(self.gridLayoutWidget)
        self.lEIva.setObjectName(u"lEIva")
        self.lEIva.addItems(["0", "8", "12", "15"])

        self.gLProductoDetails.addWidget(self.lEIva, 7, 2, 1, 1)

        self.labelIva = QLabel(self.gridLayoutWidget)
        self.labelIva.setObjectName(u"labelIva")

        self.gLProductoDetails.addWidget(self.labelIva, 7, 0, 1, 1)

        self.lEUDescripcion = QLineEdit(self.gridLayoutWidget)
        self.lEUDescripcion.setObjectName(u"lEUDescripcion")

        self.gLProductoDetails.addWidget(self.lEUDescripcion, 1, 2, 1, 1)

        self.lEDescuento = QLineEdit(self.gridLayoutWidget)
        self.lEDescuento.setObjectName(u"lEDescuento")

        self.gLProductoDetails.addWidget(self.lEDescuento, 5, 2, 1, 1)

        self.labelDescuento = QLabel(self.gridLayoutWidget)
        self.labelDescuento.setObjectName(u"labelDescuento")

        self.gLProductoDetails.addWidget(self.labelDescuento, 5, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.frame_form_Productos_Details)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 270, 188, 41))
        self.hLBotonesProductoDetails = QHBoxLayout(self.horizontalLayoutWidget)
        self.hLBotonesProductoDetails.setObjectName(u"hLBotonesProductoDetails")
        self.hLBotonesProductoDetails.setContentsMargins(0, 0, 0, 0)
        self.confirmarProductoDetails = QPushButton(self.horizontalLayoutWidget)
        self.confirmarProductoDetails.setObjectName(u"confirmarProductoDetails")

        self.hLBotonesProductoDetails.addWidget(self.confirmarProductoDetails)

        self.cancelarProductoDetails = QPushButton(self.horizontalLayoutWidget)
        self.cancelarProductoDetails.setObjectName(u"cancelarProductoDetails")

        self.hLBotonesProductoDetails.addWidget(self.cancelarProductoDetails)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelDescripcionProducto.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.labelUMedidaProducto.setText(QCoreApplication.translate("MainWindow", u"Unidad Medida", None))
        self.botonBuscarProducto.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.labelCodigoProducto.setText(QCoreApplication.translate("MainWindow", u"Identificador", None))
        self.labelCantidad.setText(QCoreApplication.translate("MainWindow", u"cantidad", None))
        self.labelVUnitario.setText(QCoreApplication.translate("MainWindow", u"Valor Unitario", None))
        self.labelIva.setText(QCoreApplication.translate("MainWindow", u"IVA", None))
        self.labelDescuento.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
        self.confirmarProductoDetails.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.cancelarProductoDetails.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi
