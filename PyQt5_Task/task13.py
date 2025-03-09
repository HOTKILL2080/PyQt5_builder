from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLabel, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 450, 500, 500)

    edit_cat1 = QTextEdit(win)
    edit_cat1.setFixedSize(100, 25)
    edit_cat1.move(100, 125)

    edit_cat2 = QTextEdit(win)
    edit_cat2.setFixedSize(100, 25)
    edit_cat2.move(100, 175)

    label = QLabel(win)
    label.setFixedSize(200, 25)
    label.move(225, 150)

    btn_s = QPushButton('S', win)
    btn_s.setFixedSize(35, 35)
    btn_s.move(275, 175)

    btn_h = QPushButton('H', win)
    btn_h.setFixedSize(35, 35)
    btn_h.move(325, 175)

    btn_s.clicked.connect(lambda: square(edit_cat1, edit_cat2, label))
    btn_h.clicked.connect(lambda: hypotenuse(edit_cat1, edit_cat2, label))

    win.show()
    sys.exit(app.exec())


def hypotenuse(edit_cat1, edit_cat2, label):
    value = round((int(edit_cat1.toPlainText()) ** 2 * int(edit_cat2.toPlainText()) ** 2) ** 0.5)
    label.setText('H прям.треугольника: ' + str(value))

def square(edit_cat1, edit_cat2, label):
    value = int(edit_cat1.toPlainText()) * int(edit_cat2.toPlainText()) // 2
    label.setText('S прям.треугольника: ' + str(value))


window()