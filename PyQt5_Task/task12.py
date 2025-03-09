from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QPushButton, QLabel, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(750, 450, 500, 500)

    edit_five = QTextEdit(win)
    edit_five.setFixedSize(100, 25)
    edit_five.move(100, 125)

    edit_four = QTextEdit(win)
    edit_four.setFixedSize(100, 25)
    edit_four.move(100, 160)

    edit_three = QTextEdit(win)
    edit_three.setFixedSize(100, 25)
    edit_three.move(100, 200)


    label = QLabel(win)
    label.setFixedSize(200, 50)
    label.move(250, 125)

    btn = QPushButton('P', win)
    btn.setFixedSize(35, 35)
    btn.move(275, 175)

    btn.clicked.connect(lambda: result(edit_five, edit_four, edit_three, label))

    win.show()
    sys.exit(app.exec())


def result(edit_five, edit_four, edit_three, label):
    sum = int(edit_five.toPlainText()) + int(edit_four.toPlainText()) + int(edit_three.toPlainText())
    five = round((int(edit_five.toPlainText()) / sum) * 100)
    four = round((int(edit_four.toPlainText()) / sum) * 100)
    three = round((int(edit_three.toPlainText()) / sum) * 100)
    text = f'5 - {str(five)}% \n4 - {str(four)}% \n3 - {str(three)}%'
    label.setText(text)


window()