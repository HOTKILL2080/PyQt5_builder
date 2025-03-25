from main import MyApp

def f(ted1, ted2, ted3, ted4, result):
    p = int(ted1.toPlainText())
    ch = int(ted2.toPlainText())
    tr = int(ted3.toPlainText())
    dv = int(ted4.toPlainText())
    num = 0
    sr_bal = (p*5+ch*4+tr*3+dv*2)/(p+ch+tr+dv)
    if 5 >= sr_bal:
        num += p
    elif 4 >= sr_bal:
        num += ch
    elif 3 >= sr_bal:
        num += tr
    elif 2 >= sr_bal:
        num += dv
    result.setText(f'Получило больше\nсреднего бала: {num}')

app = MyApp(500, 500)

ted1 = app.widget_create('ted', 'ted1', 150, 35, 20, 100, 200)
ted2 = app.widget_create('ted', 'ted2', 150, 35, 20, 100, 200)
ted3 = app.widget_create('ted', 'ted3', 150, 35, 20, 100, 200)
ted4 = app.widget_create('ted', 'ted4', 150, 35, 20, 100, 200)
lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, text='Введите число')
result = app.widget_create('lab', 'result', 250, 100, 20, text='0')
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted2, ted1, 'd')
app.move_from(ted3, ted2, 'd')
app.move_from(btn1, ted2, 'r')
app.move_from(result, btn1, 'r')
app.move_from(lab1, ted1, 'u')
app.move_from(ted4, ted3, 'd')

btn1.clicked.connect(lambda: f(ted1, ted2, ted3, ted4, result))

app.run()