from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from ui import Ui_MainWindow
import random

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.setText("Камінь")
        self.ui.label.setText("")
        self.ui.label_2.setText("")
        self.ui.pushButton_2.setText("Ножиці")
        self.ui.pushButton_3.setText("Бумага")
        self.ui.pushButton.clicked.connect(self.kamin)
        self.ui.pushButton_3.clicked.connect(self.bumaga)
        self.ui.pushButton_2.clicked.connect(self.nozhyci)
        self.ui.pushButton.setIcon(QIcon(QPixmap("rock.png")))
        self.ui.pushButton_2.setIcon(QIcon(QPixmap("paper.jpg")))
        self.ui.pushButton_3.setIcon(QIcon(QPixmap("scissors.jpg")))
        self.list = ["Камінь", "Ножиці", "Папір"]
    def kamin(self):
        choices = random.choice(self.list)
        self.ui.label_2.setText(choices)
        if self.ui.label_2.text() == "Папір":
            self.ui.label.setText("Програв")
        elif self.ui.label_2.text() == "Ножиці":
            self.ui.label.setText("Виграв")
        elif self.ui.label_2.text() == "Камінь":
            self.ui.label.setText("Нічия")
    def nozhyci(self):
        choices = random.choice(self.list)
        self.ui.label_2.setText(choices)
        if self.ui.label_2.text() == "Папір":
            self.ui.label.setText("Виграв")
        elif self.ui.label_2.text() == "Ножиці":
            self.ui.label.setText("Нічия")
        elif self.ui.label_2.text() == "Камінь":
            self.ui.label.setText("Програв")
    def bumaga(self):
        choices = random.choice(self.list)
        self.ui.label_2.setText(choices)
        if self.ui.label_2.text() == "Папір":
            self.ui.label.setText("Нічия")
        elif self.ui.label_2.text() == "Ножиці":
            self.ui.label.setText("Програв")
        elif self.ui.label_2.text() == "Камінь":
            self.ui.label.setText("Виграв")
        

    

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()