from PyQt5 import QtCore, QtGui, QtWidgets, QThread, QLabel, QMainWindow, QApplication, QVBoxLayout

import sys


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")

        self.central_widget = QWidget()               
        self.setCentralWidget(self.central_widget)    
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap('gente.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        lay.addWidget(label)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())