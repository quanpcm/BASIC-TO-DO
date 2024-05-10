from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        
        # self.bt_todo1.clicked.connect(self.show_todo1)
        
    def show_detail(self):
        detail.show()
        self.close()

        
class Detail(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/detail.ui', self)
        
        self.bt_return1.clicked.connect(self.show_Main)
        self.bt_finish1.clicked.connect(self.show_Main)
        
    def show_Main(self):
        MainPage.show()
        self.close()
      
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    detail = Detail()
    MainPage = Main()

    MainPage.show()
    
    app.exec()    
