from main import MyApp

def f(ted1, ted2, ted3, result):
    x = int(ted1.toPlainText())
    y = int(ted2.toPlainText())
    d = int(ted3.toPlainText())
    if d < x and d < y:
        result.setText('Голова пролезет')
    else:
        result.setText('Голова не пролезет')

app = MyApp(500, 500)

ted1 = app.widget_create('ted', 'ted1', 150, 35, 20, 100, 200)
ted2 = app.widget_create('ted', 'ted2', 150, 35, 20, 100, 200)
ted3 = app.widget_create('ted', 'ted3', 150, 35, 20, 100, 200)
lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, text='Введите число')
result = app.widget_create('lab', 'result', 250, 35, 20, text='0')
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted2, ted1, 'd')
app.move_from(ted3, ted2, 'd')
app.move_from(btn1, ted2, 'r')
app.move_from(result, btn1, 'r')
app.move_from(lab1, ted1, 'u')

btn1.clicked.connect(lambda: f(ted1, ted2, ted3, result))

app.run()