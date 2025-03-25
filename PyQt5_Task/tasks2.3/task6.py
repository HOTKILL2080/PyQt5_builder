from main import MyApp

def f(ted1, ted2, result):
    sister1 = int(ted1.toPlainText())
    sister2 = int(ted2.toPlainText())
    num = 0
    if sister1 == sister2:
        result.setText(f'У них одинаковое\nкол-во {sister2}')
    elif sister1 < sister2:
        while sister1 != sister2:
            num += 1
            sister1 += 1
        result.setText(f'2-я сестра\nдолжна отдать {num}')
    else:
        while sister1 != sister2:
            num += 1
            sister1 -= 1
        result.setText(f'1-я сестра\nдолжна отдать {num}')


app = MyApp(500, 500)

ted1 = app.widget_create('ted', 'ted1', 150, 35, 20, 100, 200)
ted2 = app.widget_create('ted', 'ted2', 150, 35, 20, 100, 200)
lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, text='Введите числа')
result = app.widget_create('lab', 'result', 250, 100, 20, text='0')
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted2, ted1, 'd')
app.move_from(btn1, ted2, 'r')
app.move_from(result, btn1, 'r')
app.move_from(lab1, ted1, 'u')

btn1.clicked.connect(lambda: f(ted1, ted2, result))

app.run()