import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, qRgb, QPainterPath, QBrush
from PyQt5.QtCore import Qt, QPoint
from random import randint

def get_random_color():
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    return QColor(qRgb(r, g, b))

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  
        self.pushButton.clicked.connect(self.run)
        self.start = False 
        
    def run(self): 
        self.start = True
        self.update()
        
    
    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            center = QPoint(randint(0, 400), randint(0, 400))
            qp.setBrush(get_random_color())
            r = randint(1, 100)
            qp.drawEllipse(center, r, r)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())