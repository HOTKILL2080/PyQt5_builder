from main import *

def f(ted1, result):
    text = ted1.toPlainText()
    value = int(text[len(text)-1])
    if value%2 == 0:
        result.setText(f'{str(value)} чётная')
    else:
        result.setText(f'{str(value)} нечётная')

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите число:')
ted1 = app.widget_create('ted', 'red1', 125, 35, 20, 100, 250)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')
result = app.widget_create('lab', 'result', 225, 50, 20, text='0')

app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()