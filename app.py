from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("TextEditor.ui", self)
        self.show()

        self.setWindowTitle("Notepad")
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action18pt.triggered.connect(lambda: self.change_font_size(18))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))
        self.actionOpen.triggered.connect(lambda: self.open_file())
        self.actionSave.triggered.connect(lambda: self.save_file())
        self.actionExit.triggered.connect(lambda: self.exitButton())
        self.actionAbout.triggered.connect(lambda: self.about())

    def about(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Notepad - About")
        dialog.setText("Version: 1.0.0")
        dialog.addButton(QPushButton("Ok"), QMessageBox.YesRole) #0

        answer = dialog.exec_()

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your changes?")
        dialog.addButton(QPushButton("Save"), QMessageBox.YesRole) #0
        dialog.addButton(QPushButton("Don't Save"), QMessageBox.NoRole) #1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) #2

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        if answer == 2:
            event.ignore()

    def exitButton(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your changes?")
        dialog.addButton(QPushButton("Save"), QMessageBox.YesRole) #0
        dialog.addButton(QPushButton("Don't Save"), QMessageBox.NoRole) #1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) #2

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
        if answer == 1:
            quit()

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Files (*.*)", options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Save File", "", "Files (*.*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()
