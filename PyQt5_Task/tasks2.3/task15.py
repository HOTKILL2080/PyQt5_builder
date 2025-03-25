from main import MyApp
import random

def f(ted1, result):
    num = int(ted1.toPlainText())
    print(num%400)
    if num % 400 == 0:
        result.setText(f'{num} - год высокосный')
    else:
        result.setText(f'{num} - год невысокосный')

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите числа')
result = app.widget_create('lab', 'lab1', 250, 35, 20, 100, 200, '0')
ted1 = app.widget_create('ted', 'ted1', 150, 35, 20)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted1, lab1, 'd')
app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

rand = random.randint(1, 10)
btn1.clicked.connect(lambda: f(ted1, result))

app.run()