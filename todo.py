from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton
from PyQt6 import uic
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        
        # for key, value in todo_dict.items():
        #     self.todoList.addItem(f'{key} - {value}')
        self.populateList()

    def populateList(self):
        for key, value in todo_dict.items():
            form_widget = uic.loadUi('gui/form.ui')
            form_widget.btn_todo.setText(f'{key} - {value}')
            listWidgetItem = QListWidgetItem(self.todoList)
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)
        
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
    
    import sqlite3
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM todo;"
    cursor.execute(query)
    rows = cursor.fetchall()
    todo_dict = {row[0]: row[1] for row in rows}
    print(todo_dict)
    conn.close()
    
    app = QtWidgets.QApplication(sys.argv)
    
    detail = Detail()
    MainPage = Main()

    MainPage.show()
    
    app.exec()    
