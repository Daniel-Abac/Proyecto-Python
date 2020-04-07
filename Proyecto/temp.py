from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow
from temp2 import Ui_secondWindow

class Ui_mainWindow(object):    
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(641, 394)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Boton para abrir el archivo
        self.btnAbrir = QtWidgets.QPushButton(self.centralwidget)
        self.btnAbrir.setGeometry(QtCore.QRect(300, 340, 83, 31))
        self.btnAbrir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAbrir.setObjectName("btnAbrir")
        self.btnAbrir.clicked.connect(self.getfile)
        self.btnAbrir.clicked.connect(self.correr)
        #Panel de texto
        self.txtPane2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPane = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPane.setGeometry(QtCore.QRect(10, 10, 621, 321))
        self.txtPane.setObjectName("txtPane")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Proyecto"))
        self.btnAbrir.setText(_translate("mainWindow", "Abrir"))
        
    # Abre los archivos
    def getfile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFile)
        fname = list
        contador = 0
        if dlg.exec_():
            fname = dlg.selectedFiles()
            f = open(fname[0], 'r')
            self.txtPane.clear()
            Ui_secondWindow.limpiarListas()
            for linea in f:
                contador = contador + 1
                self.txtPane.setText(self.txtPane.toPlainText() + linea)
                Ui_secondWindow.verificar(linea, contador)
                #Datos.verificar(self, linea, contador)
                
                
    # Muestra la ventana de los resultados
    def correr(self):
        self.window = QMainWindow()
        self.ui = Ui_secondWindow()
        self.ui.setupUi(self.window)
        self.ui
        self.window.show()
