from detailPelanggan import Ui_Dialog as detail
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
import sys

class show_users(QMainWindow, detail):
    recno = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('penjahit.sqlite')
        self.db.open()

        self.model = QSqlQueryModel(self)
        self.model.setQuery("select * from users")
        self.record = self.model.record(0)
        self.lineEdit.setText(str(self.record.value("nama")))
        self.lineEdit_2.setText(str(self.record.value("telp")))
        self.textEdit.setText(str(self.record.value("alamat")))
        self.pushButton_4.clicked.connect(self.dispFirst)
        self.pushButton.clicked.connect(self.dispPrevious)
        self.pushButton_2.clicked.connect(self.dispNext)
        self.pushButton_3.clicked.connect(self.dispLast)
    def displayRec(self):
        self.record=self.model.record(show_users.recno)
        self.lineEdit.setText(str(self.record.value("nama")))
        self.lineEdit_2.setText(str(self.record.value("telp")))
        self.textEdit.setText(str(self.record.value("alamat"))) 
        print(show_users.recno)  
    def dispFirst(self):
        show_users.recno = 0
        self.displayRec()
    def dispPrevious(self):
        show_users.recno -= 1
        if show_users.recno < 0:
            show_users.recno = 0
        self.displayRec()
    def dispLast(self):
        show_users.recno = self.model.rowCount()-1
        self.displayRec()
    def dispNext(self): 
        show_users.recno += 1
        if show_users.recno > self.model.rowCount()-1:
            show_users.recno = self.model.rowCount()-1
        self.displayRec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = show_users()
    app.exec()