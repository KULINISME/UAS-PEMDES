from TambahPesanan import FormPesanan
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QTableView,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    QLabel,
    QPushButton
)
import sqlite3
import sys
class show_pesanan(QMainWindow, FormPesanan):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        conn = sqlite3.connect("penjahit.sqlite")
        cur = conn.cursor()
        cur.execute("SELECT id_user, nama FROM users")
        self.comboBox.clear()
        for row in cur.fetchall():
            id_user, nama = row
            self.comboBox.addItem(nama, id_user)
        
        cur.execute("SELECT id_penjahit, nama_penjahit FROM penjahit")
        self.comboBox_2.clear()
        for row in cur.fetchall():
            id_penjahit, nama = row
            self.comboBox_2.addItem(nama, id_penjahit)
        conn.close()
        
        self.pushButton.clicked.connect(self.tambahPesanan)
    
    def tambahPesanan(self):
        print("Button Clicked")