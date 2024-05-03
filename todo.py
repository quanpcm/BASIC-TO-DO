from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui todo/main.ui', self)
        
        self.bt_todo1.clicked.connect(self.show_todo1)
        self.bt_todo2.clicked.connect(self.show_todo2)
        self.bt_todo3.clicked.connect(self.show_todo3)
        self.bt_todo4.clicked.connect(self.show_todo4)
        
    def show_todo1(self):
        todo1Page.show()
        self.close()
        
    def show_todo2(self):
        todo2Page.show()
        self.close()
        
    def show_todo3(self):
        todo3Page.show()
        self.close()
        
    def show_todo4(self):
        todo4Page.show()
        self.close()
        
class Todo1(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo1.ui', self)
            
            self.bt_return1.clicked.connect(self.show_Main)
            self.bt_finish1.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close()
            
class Todo2(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo2.ui', self)            
            self.bt_return2.clicked.connect(self.show_Main)
            self.bt_finish2.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close()   
            
class Todo3(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo3.ui', self)
            
            self.bt_return3.clicked.connect(self.show_Main)
            self.bt_finish3.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close() 
            
class Todo4(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo4.ui', self)
            
            self.bt_return4.clicked.connect(self.show_Main)
            self.bt_finish4.clicked.connect(self.show_Main)
            
            self
            
        def show_Main(self):
            MainPage.show()
            self.close()  
      
class DuLieu:
    def __int__(self, dulieu):
        self.dulieu = dulieu       
      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    todo1Page = Todo1()
    todo2Page = Todo2()
    todo3Page = Todo3()
    todo4Page = Todo4()
    MainPage = Main()
    
    
    MainPage.show()
    
    app.exec()    
    
