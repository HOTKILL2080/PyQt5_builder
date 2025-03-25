from main import MyApp
import random

def f(ted1, result):
    text = ted1.toPlainText().split()
    pigs = ['ниф-ниф', 'наф-наф', 'нуф-нуф']
    text = pigs + text
    num = 1
    value = ''
    for i in text:
        value += f'{i}-{text[-num]}\n'
        if num == len(text) // 2:
            break
        num += 1

    result.setText(value)

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите числа')
result = app.widget_create('lab', 'lab1', 200, 70, 20, 100, 200, '0')
ted1 = app.widget_create('ted', 'ted1', 150, 35, 20)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted1, lab1, 'd')
app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()