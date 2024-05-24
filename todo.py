from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton, QMessageBox
from PyQt6 import uic
import sys
import sqlite3

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)

        self.todo_dict_main = self.load_todo_data()
        self.Todo_List()

        self.btn_plus.clicked.connect(self.New_Todo)

    def load_todo_data(self):
        conn = sqlite3.connect('todo.db')
        cursor = conn.cursor()
        query = "SELECT * FROM todo;"
        cursor.execute(query)
        rows = cursor.fetchall()
        todo_dict = {row[1]: (row[2], row[0]) for row in rows}
        conn.close()
        return todo_dict

    def Todo_List(self):
        for key, (value, idd) in self.todo_dict_main.items():
            form_widget = uic.loadUi('gui/form.ui')
            form_widget.btn_todo.setText(f'{key}')
            form_widget.btn_todo.clicked.connect(lambda _, idd=idd: self.onButtonClicked(idd))
            listWidgetItem = QtWidgets.QListWidgetItem()
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)
            listWidgetItem.setData(32, idd)
            print(f"Added item with ID: {idd}")

    def New_Todo(self):
        form_widget = uic.loadUi('gui/form.ui')
        listWidgetItem = QtWidgets.QListWidgetItem()
        listWidgetItem.setSizeHint(form_widget.sizeHint())
        self.todoList.addItem(listWidgetItem)
        self.todoList.setItemWidget(listWidgetItem, form_widget)

    def onButtonClicked(self, idd):
        self.detail = Detail(idd)
        self.detail.show()
        self.close()

class Detail(QtWidgets.QMainWindow):
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
        row = c.fetchone()
        if row:
            title, content = row[1], row[2]
            self.txt_tiltle.setText(title)
            self.txt_content.setText(content)
        conn.close()
            
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
            self.show_message('Please enter username')
            return
        if not password:
            self.show_message('Please enter password')
            return
        if email == 'minhquan' and password == '09090909':
            self.close()
            MainPage.show()
        else:
            self.show_message('Please check again the password or username')
    
    def show_message(self, message):
        msg_box.setText(message)
        msg_box.exec()
                        
class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/register.ui', self)
        
        self.btn_create.clicked.connect(self.create_account)
        
    def create_account(self):
        username = self.txt_newname.toPlainText()
        password = self.txt_newpass.toPlainText()
        comfi_password = self.txt_compass.toPlainText()
        
        if not username:
            self.show_message('Please enter new username')
            return
        if not password:
            self.show_message('Please enter new password')
            return
        if not comfi_password:
            self.show_message('Please confirm new password')
            return
        if password != comfi_password:
            self.show_message('Passwords do not match')
            return

        MainPage.show()
        self.close()
    
    def show_message(self, message):
        msg_box.setText(message)
        msg_box.exec()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    MainPage = Main()
    LoginPage = Login()
    RegisterPage = Register()

    MainPage.show()
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle('!!!SOMETHING WRONG!!!')
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setStyleSheet("background-color: white; color: black;")
    
    sys.exit(app.exec())
