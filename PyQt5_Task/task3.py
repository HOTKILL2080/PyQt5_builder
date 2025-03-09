from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 400, 500, 500)

    edit = QTextEdit(win)
    edit.setFixedSize(100, 25)
    edit.move(200, 250)

    btn_p = QPushButton('C', win)
    btn_p.setFixedSize(25, 25)
    btn_p.move(225, 275)

    btn_s = QPushButton('S', win)
    btn_s.setFixedSize(25, 25)
    btn_s.move(250, 275)

    label = QLabel('0', win)
    label.setFixedSize(100, 25)
    label.move(325, 250)

    btn_p.clicked.connect(lambda: capacity(edit, label))
    btn_s.clicked.connect(lambda: square(edit, label))

    win.show()
    sys.exit(app.exec())


def capacity(edit, label):
    value = int(edit.toPlainText()) ** 3
    label.setText(str(value))


def square(edit, label):
    value = int(edit.toPlainText()) ** 2 * 6
    label.setText(str(value))


window()