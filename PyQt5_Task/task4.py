from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLabel, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 450, 500, 500)

    edit = QTextEdit(win)
    edit.move(100, 100)
    edit.setFixedSize(200, 25)
    
    btn = QPushButton('=', win)
    btn.move(300, 100)
    btn.setFixedSize(25, 25)

    label = QLabel('0', win)
    label.move(335, 100)
    label.setFixedSize(50, 25)
    
    btn.clicked.connect(lambda: result(edit, label))

    win.show()
    sys.exit(app.exec())


def result(edit, label):
    sum = eval(edit.toPlainText())
    value = edit.toPlainText()
    elem = list()
    amount = 1
    for i in value:
        if i in '+-/*':
            amount += 1
    value = sum // amount
    label.setText(str(value))


window()