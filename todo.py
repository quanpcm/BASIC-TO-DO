from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QListWidgetItem, QPushButton,QMessageBox
from PyQt6 import uic
import sys
import logging
import sqlite3
from queue import Empty

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        # for key, value in todo_dict.items():
        #     self.todoList.addItem(f'{key} - {value}')
    
        self.populateList()

        self.btn_plus.clicked.connect(self.populateList)
        self.listWidget.itemClicked.connect(self.onItemClicked)
        
    def populateList(self):
        for key, value, id in todo_dict.items():
            form_widget = uic.loadUi('gui/form.ui')
            form_widget.btn_todo.setText(f'Todo {value}: {key}')
            listWidgetItem = QListWidgetItem()
            listWidgetItem.setSizeHint(form_widget.sizeHint())
            self.todoList.addItem(listWidgetItem)
            self.todoList.setItemWidget(listWidgetItem, form_widget)
            listWidgetItem.setData(QtCore.Qt.UserRole, id)
    
    def onItemClicked(self, item):
        id = item.data(QtCore.Qt.UserRole) 
        detail = Detail(id)
        detail.show()
        self.close()
        
    def show_detail(self):
        detail.show()
        self.close()
       
class Detail(QtWidgets.QMainWindow, QtCore.QThread):
    def __init__(self, update_queue):
        super().__init__()
        uic.loadUi('gui/detail.ui', self)
        self.update_queue = update_queue
        self.running = True
        
        self.run() 
        self.bt_return1.clicked.connect(self.stop)
        self.bt_finish1.clicked.connect(self.stop)        
        self.bt_return1.clicked.connect(self.show_Main)
        self.bt_finish1.clicked.connect(self.show_Main)
        
    def show_Main(self):
        MainPage.show()
        self.close()
    
    def run(self):
        for key, value in todo_dict.items():
            conn = sqlite3.connect('todo.db')
            try:
                while self.running:
                    try:
                        # Block until an item is available
                        key, value = self.update_queue.get()
                        c = conn.cursor()
                        c.execute("""
                                UPDATE todo
                                SET
                                    id = ?,
                                    title = ?
                                WHERE content = ?
                                """, ("", key, value))
                        conn.commit()
                        self.update_queue.task_done()
                    except Empty:
                        continue
                    except Exception as e:
                        logging.error("Error in database operation: " + str(e))
            finally:
                conn.close()

    def stop(self):
        self.running = False
        self.update_queue.put((None, None, None))
        
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
        
        self.txt_name.toPlainText(self.login)
        self.btn_create.clicked.connect(self.showMain)
        
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
        
    def showMain(self):
        MainPage.show()
        self.close()
        
if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM todo;"
    cursor.execute(query)
    rows = cursor.fetchall()
    todo_dict = {row[2]: (row[1], row[0]) for row in rows}
    print(todo_dict)
    conn.close()
    
    app = QtWidgets.QApplication(sys.argv)
    
    detail = Detail()
    MainPage = Main()
    LoginPage = Login()
    RegisterPage = Register()

    MainPage.show()
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle('!!!SOMETHING WRONG!!!')
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setStyleSheet("background-color: white; color: black;")
    
    app.exec()    