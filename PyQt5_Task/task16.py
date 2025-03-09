from main import *

def f():
    result.setText(str(int(fact.toPlainText()) / int(plan.toPlainText()) * 100) + '%')

app = MyApp(500, 500)

app.widget_create('ted', 'plan', 50, 25, 200, 200, '')
app.widget_create('ted', 'fact', 50, 25, 200, 200, '')
app.widget_create('btn', 'btn1', 25, 25, 260, 215, '=')
app.widget_create('lab', 'result', 50, 25, 0, 0, '0')

app.move_from('fact', 'plan', 'd')
app.move_from('result', 'btn1', 'r')

btn = app.widget_find('btn1')
plan = app.widget_find('plan')
fact = app.widget_find('fact')
result = app.widget_find('result')

btn.clicked.connect(f)

app.run()