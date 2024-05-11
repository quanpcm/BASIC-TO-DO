from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton
from PyQt6 import uic
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        todo = uic.loadUi('gui/form.ui')
        # for key, value in todo_dict.items():
        #     self.todoList.addItem(f'{key} - {value}')
        
        self.populateList()

        self.btn_plus.clicked.connect(self.populateList)
        self.todo.clicked.connect(self.show_detail)

    def populateList(self):
        count = 1
        for key, value in todo_dict.items():
            form_widget = uic.loadUi('gui/form.ui')
            form_widget.btn_todo.setText(f'Todo {count}: {key}')
            listWidgetItem = QListWidgetItem(self.todoList)
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)
            count += 1
        
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
    todo_dict = {row[1]: row[2] for row in rows}
    print(todo_dict)
    conn.close()
    
    app = QtWidgets.QApplication(sys.argv)
    
    detail = Detail()
    MainPage = Main()

    MainPage.show()
    
    app.exec()    
