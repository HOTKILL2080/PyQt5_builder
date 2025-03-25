from main import MyApp

def f(ted1, ted2, result):
    evelope1 = ted1.toPlainText().split()
    evelope2 = ted2.toPlainText().split()
    if evelope1[0] < evelope2[0] and evelope1[1] < evelope2[1] :
        result.setText('Конверт пролезет 1\nпролезет в 2')
    elif evelope1[0] > evelope2[0] and evelope1[1] > evelope2[1]:
        result.setText('Конверт пролезет 2\nпролезет в 1')
    else:
        result.setText('Конверты непролезут')

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