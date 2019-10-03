# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceDetector.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import cv2
from neural import Neural
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
gui = QtGui


class Ui_MainWindow(object):

    def __init__(self):
        self.image = None
        self.state = 1
        self.neural = Neural()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(24, 380, 81, 31))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 471, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 451, 341))
        self.graphicsView.setObjectName("graphicsView")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 380, 161, 31))
        self.textEdit.setObjectName("textEdit")
        # print(dir(self.textEdit))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 380, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.clicked.connect(self.actualizar)
        self.pushButton_3.clicked.connect(self.save_person)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FaceDetector"))
        self.pushButton.setText(_translate("MainWindow", "Detener"))
        self.textEdit.setPlaceholderText(
            _translate("MainWindow", "Ingrese el nombre"))
        self.pushButton_3.setText(_translate("MainWindow", "Guardar"))

    def actualizar(self):
        self.state = not(self.state)
        name = "Detener"if(self.state) else"Iniciar"
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", name))
        print("cambiando estado: " + str(self.state))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def run_neural(self):
        while (True):
            if(self.state):
                try:
                    frame = self.neural.neural_detector()
                    cv2.imshow('Video', frame[0])
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                except IndexError as identifier:
                    print('an error ocurred', identifier)
        # Release handle to the webcam
        self.neural.videoCapture.release()
        cv2.destroyAllWindows()

    def save_person(self):
        self.name = self.textEdit.toPlainText()
        self.frame = self.neural.frame
        hilo2 = threading.Thread(target=self.runRecognition)
        hilo2.daemon = True
        hilo2.start()

    def runRecognition(self):
        self.neural.neural_recognition(self.name, self.frame)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    hilo2 = threading.Thread(target=ui.run_neural)
    hilo2.daemon = True
    hilo2.start()
    sys.exit(app.exec_())
    ui.neural.videoCapture.release()
    cv2.destroyAllWindows()
