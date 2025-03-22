from main import *

def f(ted1, result):
    text = ted1.toPlainText().split()
    value = ''
    for i in text:
        if int(i) < 0:
            value += f'{i} - отрицательное\n'
            value += f'{len(i)-1}-значное число\n'
        elif int(i) > 0:
            value += f'{i} - положительное\n'
            value += f'{len(i)}-значное число\n'
        else:
            value += f'{i} - это 0\n'
            value += f'{len(i)}-значное число\n'

        if int(i)%2 == 0:
            value += 'Чётное\n'
        else:
            value += 'Нечётное\n'
        

    result.setText(value)

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите число:')
ted1 = app.widget_create('ted', 'red1', 125, 35, 20, 100, 250)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')
result = app.widget_create('lab', 'result', 230, 150, 20, text='0')


app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()