from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 300, 500, 500)
    
    edit_x = QTextEdit(win)
    edit_x.setFixedSize(100, 25)
    edit_x.move(125, 225)

    edit_y = QTextEdit(win)
    edit_y.setFixedSize(100, 25)
    edit_y.move(125, 275)

    edit_price = QTextEdit(win)
    edit_price.setFixedSize(100, 25)
    edit_price.move(250, 225)

    label_x = QLabel('X конфеты', win)
    label_x.setFixedSize(100, 25)
    label_x.move(125, 200)

    label_y = QLabel('Y конфеты', win)
    label_y.setFixedSize(100, 25)
    label_y.move(125, 250)

    label_price_x = QLabel('Цена за X', win)
    label_price_x.setFixedSize(100, 25)
    label_price_x.move(250, 200)

    label_price_y = QLabel('Цена за Y:', win)
    label_price_y.setFixedSize(100, 25)
    label_price_y.move(250, 275)

    btn = QPushButton('ok', win)
    btn.setFixedSize(50, 50)
    btn.move(215, 325)

    btn.clicked.connect(lambda: result(edit_x, edit_price, edit_y, label_price_y))

    win.show()
    sys.exit(app.exec())


def result(edit_x, edit_price, edit_y, label_price_y):
    price_y = int(edit_price.toPlainText()) / int(edit_x.toPlainText())
    value = price_y * int(edit_y.toPlainText())
    label_price_y.setText(str(value))


window()