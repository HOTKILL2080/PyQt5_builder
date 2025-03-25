from main import MyApp

def f(ted1, ted2, result):
    frame = ted1.toPlainText().split()
    brick = ted2.toPlainText().split()
    if frame[0] < brick[0] and frame[1] < brick[1] :
        result.setText('Кирпич пролезет в\nотверстие')
    else:
        result.setText('Кирпич жирный')

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