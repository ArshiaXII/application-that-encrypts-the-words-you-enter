import random
import string
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.font = QFont("Arial", 18) 
        self.initUI()
    def initUI(self):
        self.label1 = QLabel("Metin Giriniz:")
        self.textbox = QLineEdit()
        self.sifrele_button = QPushButton("Şifrele")
        self.coz_button = QPushButton("Çöz")
        self.coz2_button =QPushButton("Gerçek Şifre")
        self.output = QLabel()
        self.label1.setFont(self.font)
        self.setAutoFillBackground(True)
        palette = self.palette()
        self.setStyleSheet("background: rgb(150, 255, 146);")
        self.setPalette(palette)
        self.textbox.setAutoFillBackground(True)
        palette = self.textbox.palette()
        palette.setColor(self.textbox.backgroundRole(), QColor(Qt.black))
        self.coz_button.setStyleSheet("background:red; border-radius: 15px;")
        self.sifrele_button.setStyleSheet("background:yellow; border-radius: 15px;")
        self.textbox.setStyleSheet("color: black;")
        self.output.setStyleSheet("color: black;")
        self.textbox.setPalette(palette)
        self.coz2_button.setStyleSheet("background-color:blue;")
        
        

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.textbox)
        layout.addWidget(self.sifrele_button)
        layout.addWidget(self.coz_button)
        layout.addWidget(self.output)
        layout.addWidget(self.coz2_button)
        self.coz2_button.clicked.connect(self.gercek_sifre)

        

        self.sifrele_button.clicked.connect(self.sifrele)
        self.coz_button.clicked.connect(self.coz)

        self.setLayout(layout)
        self.setWindowTitle("Şifreleme Uygulaması")

    def sifrele(self):
        input_text = self.textbox.text()
        key = "yourkey" # anahtarınızı buraya girin
        encrypted_text = ""
        for i, c in enumerate(input_text):
            key_c = key[i % len(key)]
            encrypted_c = chr((ord(c) + ord(key_c)) % 582)
            random_chars = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation)
            for _ in range(10))
            encrypted_text += encrypted_c + random_chars
        self.output.setFont(self.font)
        self.output.setText(encrypted_text)
        self.output.setWordWrap(True)

    def gercek_sifre(self):
        input_text = self.textbox.text()
        key = "yourkey" # anahtarınızı buraya girin
        encrypted_text = ""
        for i, c in enumerate(input_text):
            key_c = key[i % len(key)]
            encrypted_c = chr((ord(c) + ord(key_c)) % 582)
            encrypted_text += encrypted_c
        self.output.setFont(self.font)
        self.output.setText(encrypted_text)
        self.output.setWordWrap(True)

    def coz(self):
        input_text = self.textbox.text()
        coz_text = input_text.replace("".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10)),"")
        self.output.setFont(self.font)
        self.output.setText(coz_text)
        self.output.setWordWrap(True)
        
if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

