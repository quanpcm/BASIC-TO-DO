from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton,QMessageBox
from PyQt6 import uic
import sys

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        # for key, value in todo_dict.items():
        #     self.todoList.addItem(f'{key} - {value}')
        
        self.populateList()

        self.btn_plus.clicked.connect(self.populateList)

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

class Login(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/login.ui', self)

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.showRegister)
        
    def showRegister(self):
        RegisterPage.show()
        self.close()
        
    def login(self):
        email = self.txt_name.QPlainTextEdit()
        password = self.txt_pass.QPlainTextEdit()
        if not email:
            msg_box.setText('please enter username')
            msg_box.exec()
            return
        if not password:
            msg_box.setText('please enter password')
            msg_box.exec()
            return
        if email == 'minhquan' and password == '09090909':
            self.close()
            MainPage.show()
        
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/register.ui', self)
        
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
    LoginPage = Login()
    RegisterPage = Register()

    LoginPage.show()
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle('!!!SOMETHING WRONG!!!')
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setStyleSheet("background-color: white; color: black;")
    
    app.exec()    