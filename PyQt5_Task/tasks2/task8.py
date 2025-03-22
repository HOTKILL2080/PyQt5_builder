from main import *

def f(ted1, result):
    text = ted1.toPlainText()
    multi = int(ted2.toPlainText())
    num = 0
    for i in text:
        num += int(i)
    enum = num // multi
    if enum*5 == num:
        result.setText(f'{str(num)} кратно {str(multi)}')
    else:
        result.setText(f'{str(num)} некратно, {str(multi)}')

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите число:')
lab2 = app.widget_create('lab', 'lab2', 170, 35*2, 20, 100, 200, 'Введите \nкратность числа:')
ted1 = app.widget_create('ted', 'red1', 125, 35, 20, 100, 250)
ted2 = app.widget_create('ted', 'ted2', 125, 35, 20)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')
result = app.widget_create('lab', 'result', 225, 35, 20, text='0')

app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')
app.move_from(ted2, ted1, 'd')
app.move_from(lab2, ted2, 'd', indentation=1)
app.move_from(lab1, ted1, 'u')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()