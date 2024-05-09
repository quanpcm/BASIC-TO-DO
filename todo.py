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
        self.bt_todo5.clicked.connect(self.show_todo5)
        self.bt_todo6.clicked.connect(self.show_todo6)
        self.bt_todo7.clicked.connect(self.show_todo7)
        
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
        
    def show_todo5(self):
        todo5Page.show()
        self.close()
        
    def show_todo6(self):
        todo6Page.show()
        self.close()
        
    def show_todo7(self):
        todo7Page.show()
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
      
class Todo5(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo5.ui', self)
            
            self.bt_return5.clicked.connect(self.show_Main)
            self.bt_finish5.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close()      
            
class Todo6(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo6.ui', self)
            
            self.bt_return6.clicked.connect(self.show_Main)
            self.bt_finish6.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close()   
            
class Todo7(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('gui todo/todo7.ui', self)
            
            self.bt_return7.clicked.connect(self.show_Main)
            self.bt_finish7.clicked.connect(self.show_Main)
            
        def show_Main(self):
            MainPage.show()
            self.close()  
      
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    todo1Page = Todo1()
    todo2Page = Todo2()
    todo3Page = Todo3()
    todo4Page = Todo4()
    todo5Page = Todo5()
    todo6Page = Todo6()
    todo7Page = Todo7()
    MainPage = Main()

    MainPage.show()
    
    app.exec()    
