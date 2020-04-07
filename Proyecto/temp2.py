from PyQt5 import QtCore, QtGui, QtWidgets

validos = []
noValidos = []
num = []
ident = []
palRes = []
ope = []
sig = []  

class Ui_secondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.setEnabled(True)
        secondWindow.resize(959, 324)
        secondWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtPane2 = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPane2.setEnabled(True)
        self.txtPane2.setGeometry(QtCore.QRect(40, 50, 431, 241))
        self.txtPane2.setObjectName("txtPane2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 57, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 57, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 20, 57, 15))
        self.label_3.setObjectName("label_3")
        self.textPane3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textPane3.setGeometry(QtCore.QRect(530, 50, 391, 241))
        self.textPane3.setObjectName("textPane3")
        secondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(secondWindow)
        self.statusbar.setObjectName("statusbar")
        secondWindow.setStatusBar(self.statusbar)
        self.retranslateUi(secondWindow)
        self.textPane3.clear()
        self.txtPane2.clear()
        self.imprimir()
        QtCore.QMetaObject.connectSlotsByName(secondWindow)

    def limpiarListas():
            noValidos.clear()
            num.clear()
            ident.clear()
            ope.clear()
            sig.clear()
            validos.clear()
            palRes.clear()
    
    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "Resultados"))
        self.label.setText(_translate("secondWindow", "Token"))
        self.label_2.setText(_translate("secondWindow", "Tipo"))
        self.label_3.setText(_translate("secondWindow", "Cantidad"))
        
    def verificar(texto, c):
        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        palabraReservada = ['entero', 'decimal', 'booleano', 'cadena', 'si', 'sino', 'mientras', 'hacer',
                            'verdadero', 'falso', ' ']
        operador = ['+', '-', '*', '/', '%', '=', '==', '<', '>', '>=', '<=', ' ']
        signo = ['(', ')', '{', '}', '"', ';', ' ']
        # Lista donde se van a guardar las palabras validas
        conta = 0
        conta = c
        # Ciclo para verificar las palabras del archivo de texto
        n = 0
        palabra = ''
        while n < len(texto):
            if texto[n] == ' ':
                cont = len(validos)
                # Agregar palabras Reservadas
                t1 = 0
                while t1 < len(palabraReservada):
                    if palabra == palabraReservada[t1]:
                        m = 0
                        r1 = 0
                        while r1 < len(palRes):
                            if palabra == palRes[r1]:
                                r1 = r1 + 1
                                palRes[r1] = palRes[r1] + 1
                                validos.append(palabra)
                                m = m + 1
                                r1 = len(palRes)
                            else:
                                r1 = r1 + 1
                        if m == 0:
                            palRes.append(palabra)
                            palRes.append(1)
                            validos.append(palabra)
                        palabra = ''
                        n = n + 1
                        t1 = len(palabraReservada)
                    else:
                        t1 = t1 + 1
                # Agregar operadores
                t2 = 0
                while t2 < len(operador):
                    if palabra == operador[t2]:
                        m1 = 0
                        r2 = 0
                        while r2 < len(ope):
                            if palabra == ope[r2]:
                                r2 = r2 + 1
                                ope[r2] = ope[r2] + 1
                                validos.append(palabra)
                                m1 = m1 + 1
                                r2 = len(ope)
                            else:
                                r2 = r2 + 1
                        if m1 == 0:
                            ope.append(palabra)
                            ope.append(1)
                            validos.append(palabra)
                        palabra = ''
                        n = n + 1
                        t2 = len(operador)
                    else:
                        t2 = t2 + 1
                # Agregar signos
                t3 = 0
                while t3 < len(signo):
                    if palabra == signo[t3]:
                        m2 = 0
                        r3 = 0
                        while r3 < len(sig):
                            if palabra == sig[r3]:
                                r3 = r3 + 1
                                sig[r3] = sig[r3] + 1
                                validos.append(palabra)
                                m2 = m2 + 1
                                r3 = len(sig)
                            else:
                                r3 = r3 + 1
                        if m2 == 0:
                            sig.append(palabra)
                            sig.append(1)
                            validos.append(palabra)
                        palabra = ''
                        n = n + 1
                        t3 = len(signo)
                    else:
                        t3 = t3 + 1
                # Agregar numeros
                p = 0
                palabra2 = ''
                co = len(palabra)
                while p < len(palabra):
                    t4 = 0
                    while t4 < len(numeros):
                        if palabra[p] == numeros[t4]:
                            palabra2 = palabra2 + palabra[p]
                            t4 = len(numeros)
                        else:
                            t4 = t4 + 1
                    p = p + 1
                    if len(palabra2) == co:
                        m3 = 0
                        r4 = 0
                        while r4 < len(num):
                            if palabra == num[r4]:
                                r4 = r4 + 1
                                num[r4] = num[r4] + 1
                                validos.append(palabra)
                                m3 = m3 + 1
                                r4 = len(num)
                            else:
                                r4 = r4 + 1
                        if m3 == 0:
                            num.append(palabra)
                            num.append(1)
                            validos.append(palabra)
                        palabra = ''
                        n = n + 1
                # Agregra identificadores
                palabra3 = ''
                co2 = len(palabra)
                p2 = 0
                vali = 0
                while p2 < len(palabra):
                    t5 = 0
                    if vali == 0:
                        while t5 < 26:
                            if palabra[p2] == letras[t5]:
                                palabra3 = palabra3 + palabra[p2]
                                vali = 2
                                t5 = 26
                            else:
                                t5 = t5 + 1
                                vali = 1
                    elif vali == 1:
                        p2 = len(palabra)
                    elif vali == 2:
                        while t5 < 26:
                            if palabra[p2] == letras[t5]:
                                palabra3 = palabra3 + palabra[p2]
                                vali = 2
                                t5 = 26
                            elif palabra[p2] == numeros[t5]:
                                palabra3 = palabra3 + palabra[p2]
                                vali = 2
                                t5 = 26
                            else:
                                t5 = t5 + 1
                                vali = 2
                    p2 = p2 + 1
                    if len(palabra3) == co2:
                        m4 = 0
                        r5 = 0
                        while r5 < len(ident):
                            if palabra == ident[r5]:
                                r5 = r5 + 1
                                ident[r5] = ident[r5] + 1
                                validos.append(palabra)
                                m4 = m4 + 1
                                r5 = len(ident)
                            else:
                                r5 = r5 + 1
                        if m4 == 0:
                            ident.append(palabra)
                            ident.append(1)
                            validos.append(palabra)
                        palabra = ''
                        n = n + 1
                # Si no se agrego ninguna palabra avanza a la siguiente
                if cont == len(validos):
                    noValidos.append(palabra)
                    noValidos.append(conta)
                    palabra = ''
                    n = n + 1
            else:
                palabra = palabra + texto[n]
                n = n + 1
                
    # imprimir en el panel de resultados
    def imprimir(self):
        if len(noValidos) == 0:
            j = 0
            while j < len(num): 
                self.txtPane2.setText(self.txtPane2.toPlainText() + '---------- ' + num[j] + ' -------------------------- ' + 'Numero' ' ------------------ ' + str(num[j + 1]) +'\n')
                j = j + 2
            j1 = 0
            while j1 < len(ident):
                self.txtPane2.setText(self.txtPane2.toPlainText() + '--------- ' + ident[j1] + ' ----------------------- ' + 'Identificador' + ' ------------------ ' + str(ident[j1 + 1]) +'\n')
                j1 = j1 + 2
            j2 = 0
            while j2 < len(palRes):
                self.txtPane2.setText(self.txtPane2.toPlainText() + '-------- ' + palRes[j2] + ' ------------------ ' + 'PalabraReservada' + ' ------------------ ' + str(palRes[j2 + 1]) +'\n')
                j2 = j2 + 2
            j3 = 0
            while j3 < len(ope):    
                self.txtPane2.setText(self.txtPane2.toPlainText() + '------------ '+ ope[j3] + ' -------------------------- ' + 'Operador' ' --------------------- ' + str(ope[j3 + 1]) +'\n')
                j3 = j3 + 2
            j4 = 0
            while j4 < len(sig):
                self.txtPane2.setText(self.txtPane2.toPlainText() + '------------ ' + sig[j4] + ' -------------------------- ' + 'Signo' ' ---------------------- ' + str(sig[j4 + 1]) +'\n')
                j4 = j4 + 2
        # Imprime los errores
        else:
            j5 = 0
            while j5 < len(noValidos):
                self.textPane3.setText(self.textPane3.toPlainText() + 'Error:       ' + noValidos[j5] + '       en linea:       ' + str(noValidos[j5 + 1]) + '                 ' +'\n')
                j5 = j5 + 2
            