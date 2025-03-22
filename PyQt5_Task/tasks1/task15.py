from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLabel, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 450, 500, 500)

    edit_cash = QTextEdit(win)
    edit_cash.setFixedSize(100, 25)
    edit_cash.move(100, 125)

    edit_price = QTextEdit(win)
    edit_price.setFixedSize(100, 25)
    edit_price.move(100, 175)

    label = QLabel(win)
    label.setFixedSize(200, 25)
    label.move(225, 150)

    btn = QPushButton('P', win)
    btn.setFixedSize(35, 35)
    btn.move(275, 175)

    btn.clicked.connect(lambda: result(edit_cash, edit_price, label))

    win.show()
    sys.exit(app.exec())


def result(edit_cash, edit_price, label):
    amount_product = int(edit_cash.toPlainText()) // int(edit_price.toPlainText())
    change = int(edit_cash.toPlainText()) % int(edit_price.toPlainText())
    label.setText(f'Кол-во товаров: {amount_product} \nСдача: {change}')


window()