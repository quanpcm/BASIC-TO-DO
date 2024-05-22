from PyQt6 import QtCore
import sqlite3
import logging
from queue import Empty

class UpdateData(QtCore.QThread):
    def __init__(self, update_queue):
        super().__init__()
        self.update_queue = update_queue
        self.running = True
    
    def run(self):
        conn = sqlite3.connect('todo.db')
        try:
            while self.running:
                try:
                    new_title, new_content = self.update_queue.get()
                    hehe = conn.cursor()
                    hehe.execute("""
                              UPDATE todo
                              SET
                                  id = ?
                                  title = ?
                                  content = ?
                              WHERE id = ?
                              """, ("", new_title, new_content))
                    conn.commit()
                    self.update_queue.task_done()
                except Exception as hahah:
                    logging.error("Error in database operation: " + str(hahah))
        finally:
            conn.close()
    
    def stop(self):
        self.running = False
        self.insert_queue.put((None, None))