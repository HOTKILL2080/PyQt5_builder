from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLabel, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 450, 500, 500)

    edit_wid = QTextEdit(win)
    edit_wid.setFixedSize(100, 25)
    edit_wid.move(100, 125)

    edit_len = QTextEdit(win)
    edit_len.setFixedSize(100, 25)
    edit_len.move(100, 175)

    label = QLabel('Периметр прямоугольника:', win)
    label.setFixedSize(200, 25)
    label.move(225, 150)

    btn = QPushButton('P', win)
    btn.setFixedSize(35, 35)
    btn.move(275, 175)

    btn.clicked.connect(lambda: result(edit_wid, edit_len, label))

    win.show()
    sys.exit(app.exec())


def result(edit_wid, edit_len, label):
    value = (int(edit_wid.toPlainText()) + int(edit_len.toPlainText())) * 2
    label.setText('Периметр прямоугольника: ' + str(value))


window()