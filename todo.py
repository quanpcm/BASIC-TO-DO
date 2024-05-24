from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton,QMessageBox
from PyQt6 import uic
from insertdata import InsertData
from updatedata import UpdateData
import sys
import logging
import sqlite3
import queue
from queue import Empty

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        # for key, value in todo_dict.items():
        #     self.todoList.addItem(f'{key} - {value}')
        
        self.Todo_List()

        self.btn_plus.clicked.connect(self.New_Todo)
        self.todoList.itemClicked.connect(self.onItemClicked)
        
    def Todo_List(self):
        for key, (value, idd) in todo_dict_main.items():
            form_widget = uic.loadUi('gui/form.ui')
            form_widget.btn_todo.setText(f'{key}')
            listWidgetItem = QListWidgetItem()
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)
            listWidgetItem.setData(QtCore.Qt.ItemDataRole.UserRole, idd)

    def New_Todo(self):
            form_widget = uic.loadUi('gui/form.ui')
            listWidgetItem = QListWidgetItem()
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)

    def onItemClicked(self, item):
        idd = item.data(QtCore.Qt.UserRole) 
        detail = Detail(idd)
        detail.show()
        self.close()
           
class Detail(QtWidgets.QMainWindow, QtCore.QThread):
    def __init__(self, idd):
        super().__init__()
        uic.loadUi('gui/detail.ui', self)
        self.idd = idd
        
        self.load_Data(idd)
        self.bt_return1.clicked.connect(self.show_Main)
        self.bt_finish1.clicked.connect(self.show_Main)
        
    def load_Data(self, idd):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todo WHERE id = ?", (idd,))
        rows = c.fetchall()
        todo_dict_detail = {row[2]: (row[1]) for row in rows}
        print(todo_dict_detail)
        conn.close()
        
        for content, title in todo_dict_detail.items():
            self.txt_tiltle.setText(title)
            self.txt_content.setText(content)
            
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
        email = self.txt_name.toPlainText()
        password = self.txt_pass.toPlainText()
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
        else:
            msg_box.setText('please check again the password or username')
            msg_box.exec()
                        
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/register.ui', self)
        
        self.btn_create.clicked.connect(self.login)
        
    def login(self):
        username = self.txt_newname.toPlainText()
        password = self.txt_newpass.toPlainText()
        comfi_password = self.txt_compass.toPlainText()
        
        if not username:
            msg_box.setText('please enter new username')
            msg_box.exec()
            return
        if not password:
            msg_box.setText('please enter new password')
            msg_box.exec()
            return
        if not comfi_password:
            msg_box.setText('please comfirm new password')
            msg_box.exec()
            return

        MainPage.show()
        self.close()
           
if __name__ == '__main__':
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM todo;"
    cursor.execute(query)
    rows = cursor.fetchall()
    todo_dict_main = {row[1]: (row[2], row[0]) for row in rows}
    print(todo_dict_main)
    conn.close()
    
    app = QtWidgets.QApplication(sys.argv)
    
    for title, (content, idd) in todo_dict_main.items():
        detail = Detail(1)
        MainPage = Main()
        LoginPage = Login()
        RegisterPage = Register()

    detail.show()
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle('!!!SOMETHING WRONG!!!')
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setStyleSheet("background-color: white; color: black;")
    
    app.exec()    