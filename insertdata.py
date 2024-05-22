from PyQt6 import QtCore
import sqlite3
import logging
class InsertData(QtCore.QThread):
    def __init__(self, insert_quene):
        super().__init__()
        self.insert_quene = insert_quene
        self.running = True
        
    def run(self):
        conn = sqlite3.connect('todo.db')
        try:
            while self.running:
                try:
                    new_title, new_content = self.insert_quene.qet()
                    hehe = conn.cursor()
                    hehe.execute("""
                                INSERT INTO todo (id, title, content)
                                VALUES (?,?,?))
                                """, ("", new_title, new_content))
                    conn.commit()
                    self.insert_quene.task_done()
                except Exception as hahah:
                    logging.error("Error in database operation: " + str(hahah))
        finally:
            conn.close()
            
    def stop(self):
        self.running = False
        self.insert_queue.put((None, None))                    