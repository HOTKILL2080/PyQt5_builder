from main import *

def f(ted1, result):
    three = False
    six = False
    nine = False
    for i in ted1.toPlainText():
        if i == '3':
            three = True
            result.setText('Есть цифра 3')
        elif i == '6':
            six = True
            result.setText('Есть цифра 6')
        elif i == '9':
            nine = True
            result.setText('Есть цифра 9')
    if three and six:
        result.setText('Есть цифра 3 и 6')
    elif three and nine:
        result.setText('Есть цифра 3 и 9')
    elif six and nine:
        result.setText('Есть цифра 6 и 9')
    
    

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите число:')
ted1 = app.widget_create('ted', 'red1', 125, 35, 20, 100, 250)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')
result = app.widget_create('lab', 'result', 200, 35, 20, text='0')

app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()