from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton
import sys

class QLabel_Moded(QLabel):
    def __init__(self, win, name, text):
        QLabel.__init__(self, text, win)
        self.name = name

class QPushButton_Moded(QPushButton):
    def __init__(self, win, name, text):
        QPushButton.__init__(self, text, win)
        self.name = name

class QTextEdit_Moded(QTextEdit):
    def __init__(self, win, name, text):
        QTextEdit.__init__(self, text, win)
        self.name = name

class MyApp(QApplication):
    def __init__(self, width, height):
        QApplication.__init__(self, sys.argv)
        self.win = QMainWindow()
        self.win.setGeometry(750, 250, width, height)
    
        self.label_array = []
        self.btn_array = []
        self.textedit_array = []

    def widget_create(self, type, name, width, height, x, y, text):
        if type == 'lab':
            self.widget = QLabel_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.move(x, y)
            self.label_array.append(self.widget)
        elif type == 'btn':
            self.widget = QPushButton_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.move(x, y)
            self.btn_array.append(self.widget)
        elif type == 'ted':
            self.widget = QTextEdit_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.move(x, y)
            self.textedit_array.append(self.widget)

    def move_from(self, name_widget, name_fromwidget, side, indentation=10):
        self.widget = self.widget_find(name_widget)
        self.fromwidget = self.widget_find(name_fromwidget)
        if side == 'r':
            self.widget.move(self.fromwidget.x() + self.fromwidget.width() + indentation, self.fromwidget.y() + self.fromwidget.height() // 2 - self.widget.height() // 2)
        elif side == 'l':
            self.widget.move(self.fromwidget.x() - self.widget.width() - indentation , self.fromwidget.y() + self.fromwidget.height() // 2 - self.widget.height() // 2)
        elif side == 'u':
            self.widget.move(self.fromwidget.x() + self.fromwidget.width() // 2 - self.widget.width() // 2, self.fromwidget.y() - self.widget.height() - indentation)
        elif side == 'd':
            self.widget.move(self.fromwidget.x() + self.fromwidget.width() // 2 - self.widget.width() // 2, self.fromwidget.y() + self.fromwidget.height() + indentation)

    def widget_find(self, name_widget):
        for i in self.btn_array, self.label_array, self.textedit_array:
            for e in i:
                if e.name == name_widget:
                    return e

    def run(self):
        self.win.show()
        sys.exit(self.exec_())