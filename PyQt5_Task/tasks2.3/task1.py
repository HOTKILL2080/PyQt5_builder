from main import MyApp

def f(ted1, result):
    text = ted1.toPlainText().split()
    value = ''
    for i in text:
        i = int(i)
        if i >= 7 and i <= 16:
            value += str(i)
    result.setText(value)

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите числа')
result = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, '0')
ted1 = app.widget_create('ted', 'ted1', 150, 35, 20)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted1, lab1, 'd')
app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()