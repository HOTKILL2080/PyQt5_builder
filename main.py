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
    def __init__(self, width: int, height: int):
        QApplication.__init__(self, sys.argv)
        self.win = QMainWindow()
        self.win.setGeometry(750, 250, width, height)
    
        self.label_array = []
        self.btn_array = []
        self.textedit_array = []

    def widget_create(self, type: str, name: str, width=0, height=0, font_size=11, x=0, y=0, text=''):
        if type == 'lab':
            self.widget = QLabel_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.setStyleSheet(f'font-size: {str(font_size)}px')
            self.widget.move(x, y)
            self.label_array.append(self.widget)
        elif type == 'btn':
            self.widget = QPushButton_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.setStyleSheet(f'font-size: {str(font_size)}px')
            self.widget.move(x, y)
            self.btn_array.append(self.widget)
        elif type == 'ted':
            self.widget = QTextEdit_Moded(self.win, name, text)
            self.widget.setFixedSize(width, height)
            self.widget.setStyleSheet(f'font-size: {str(font_size)}px')
            self.widget.move(x, y)
            self.textedit_array.append(self.widget)
        return self.widget

    def move_from(self, widget: object, fromwidget: object, side: str, indentation=10):
        if side == 'r':
            widget.move(fromwidget.x() + fromwidget.width() + indentation, fromwidget.y() + fromwidget.height() // 2 - widget.height() // 2)
        elif side == 'l':
            widget.move(fromwidget.x() - widget.width() - indentation , fromwidget.y() + fromwidget.height() // 2 - widget.height() // 2)
        elif side == 'u':
            widget.move(fromwidget.x() + fromwidget.width() // 2 - widget.width() // 2, fromwidget.y() - widget.height() - indentation)
        elif side == 'd':
            widget.move(fromwidget.x() + fromwidget.width() // 2 - widget.width() // 2, fromwidget.y() + fromwidget.height() + indentation)

    def widget_find(self, name_widget: str):
        for i in self.btn_array, self.label_array, self.textedit_array:
            for e in i:
                if e.name == name_widget:
                    return e

    def run(self):
        self.win.show()
        sys.exit(self.exec_())