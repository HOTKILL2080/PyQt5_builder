from main import *

# v = a^3
def f1():
    lab.setText(str(int(a.toPlainText()) ** 3))

# s = 6a^2
def f2():
    lab.setText(str(6 * int(a.toPlainText()) ** 2))

app = MyApp(500, 500)

app.widget_create('lab', 'lab', 50, 25, 0, 0, '0')
app.widget_create('btn', 'S', 25, 25, 0, 0, 'S')
app.widget_create('btn', 'V', 25, 25, 0, 0, 'V')
app.widget_create('ted', 'ted', 50, 25, 200, 200, '')

s = app.widget_find('S')
v = app.widget_find('V')
a = app.widget_find('ted')
lab = app.widget_find('lab')

app.move_from('S', 'ted', 'd')
app.move_from('V', 'S', 'r')
app.move_from('lab', 'ted', 'r')

s.clicked.connect(f2)
v.clicked.connect(f1)

app.run()