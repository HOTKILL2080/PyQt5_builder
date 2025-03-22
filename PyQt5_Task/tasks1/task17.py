from main import *

def f():
    num = int(ted.toPlainText())
    lab.setText(str(round(num + (num + num * 0.3) * 0.4)))

app = MyApp(500, 500)

app.widget_create('ted', 'ted1', 50, 25, 200, 200, '')
app.widget_create('btn', 'btn1', 50, 25, 200, 200, '=')
app.widget_create('lab', 'lab1', 50, 25, 200, 200, '0')

app.move_from('btn1', 'ted1', 'r')
app.move_from('lab1', 'btn1', 'r')

ted = app.widget_find('ted1')
btn = app.widget_find('btn1')
lab = app.widget_find('lab1')

btn.clicked.connect(f)

app.run()