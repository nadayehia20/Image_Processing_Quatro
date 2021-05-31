from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QApplication, QWidget, QLabel, QHBoxLayout, \
     QPushButton,QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from PIL import Image
from pytesseract import pytesseract

x= ""
y=""
z=""
final=[]
class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.the_two_widget()
        self.horizontal_Layout()

    def the_two_widget(self):
        self.ok_button = QPushButton("OK", self)
        self.cancel_button = QPushButton("Cancel", self)

    def horizontal_Layout(self):
        horizontal_bar = QHBoxLayout()
        horizontal_bar.addStretch(1)
        horizontal_bar.addWidget(self.ok_button)
        horizontal_bar.addWidget(self.cancel_button)
        self.setLayout(horizontal_bar)



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def trial_click(self):

        dialog = QFileDialog(self);
        dialog.setNameFilter(("Images (*.png *.jpeg *.jpg)"));
        dialog.setViewMode(QFileDialog.Detail);
        if dialog.exec_():
            fileNames = dialog.selectedFiles();
            x=fileNames[-1]
            final.append(x)
            self.b2.setEnabled(True)
            self.b4.setEnabled(True)
            self.b3.setEnabled(True)
            self.label = QLabel(self)
            self.pngfile = QPixmap(x).scaled(200,200,0,0)# We create the image as a QPixmap widget, using your filename.
            self.label.move(450, 100)
            self.label.resize(200,200)
            self.label.setPixmap(self.pngfile)
            self.label.show()


    def initUI(self):
        self.setGeometry(200, 200, 700, 400)
        self.setStyleSheet("background-color: rgb(99,149,198);")
        self.setWindowTitle("Image Processing")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.resize(400, 50)
        self.label2.setText("Quatro Text Extraction")
        self.label2.setStyleSheet("font-size: 24px;color:rgb(5,40,86);")
        self.label2.move(250, 20)

        #for text file
        self.label3 = QtWidgets.QLabel(self)
        self.label3.resize(400, 50)
        self.label3.setStyleSheet("font-size: 16px;")
        self.label3.move(10, 220)


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(110, 100)
        self.b1.setText("Browse Image")
        self.b1.setStyleSheet("font-size: 14px;background-color:rgb(255, 255, 255);")
        self.b1.clicked.connect(self.trial_click)

        self.output = QtWidgets.QTextEdit(self);
        self.output.resize(200, 200)
        self.output.move(220, 100)
        self.output.setStyleSheet("background-color:rgb(255, 255, 255);")


        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(10, 100)
        self.b2.setText("Get Text")
        self.b2.setEnabled(False)
        self.b2.setStyleSheet("font-size: 14px;background-color:rgb(255, 255, 255);")
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(50, 150)
        self.b3.setText("New Problem")
        self.b3.setEnabled(False)

        self.b3.setStyleSheet("font-size: 14px;background-color:rgb(255, 255, 255);")
        self.b2.clicked.connect(self.btn_clk)
        self.b3.clicked.connect(self.btn_clk)

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.move(25, 200)
        self.b4.resize(150, 20)
        self.b4.setText("Generate Text File")
        self.b4.setEnabled(False)
        self.b4.setStyleSheet("font-size: 14px;background-color:rgb(255, 255, 255);")
        self.b4.clicked.connect(self.btn_clk_2)




    def update(self):
        self.label.adjustSize()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == "Get Text":
            self.output.setText(self.show_text())
        elif sender.text() == "New Problem":
            self.output.clear()
            self.label.clear()
            final.clear()
            self.b4.setEnabled(False)
            self.b2.setEnabled(False)
            self.b3.setEnabled(False)
            self.label3.clear()


    def show_text(self):
        tesseract_exe = r"tesseract.exe" #path of tessract.exe
        z = final[-1]
        image_path = z
        input_image = Image.open(image_path)
        pytesseract.tesseract_cmd = tesseract_exe
        extracted_text2 = pytesseract.image_to_string(input_image)
        return extracted_text2

    def btn_clk_2(self):
        file = "extracted_text.txt"
        with open(file, "w") as outfile:
                outfile.write(self.show_text())
        self.label3.setText("Your Text File is Generated")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()

oi=input()
