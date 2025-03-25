from main import *

def f(ted1, result):
    two = False
    seven = False
    for i in ted1.toPlainText():
        if i == '2':
            two = True
            result.setText('Есть цифра 2')
        elif i == '7':
            seven = True
            result.setText('Есть цифра 7')
        else:
            result.setText('Нет цифр 2 и 7')
    if two and seven:
            result.setText('Есть цифра 2 и 7')
    
    

app = MyApp(500, 500)

lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, 100, 200, 'Введите число:')
ted1 = app.widget_create('ted', 'red1', 125, 35, 20, 100, 250)
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')
result = app.widget_create('lab', 'result', 200, 35, 20, text='0')

app.move_from(btn1, ted1, 'r')
app.move_from(result, btn1, 'r')

btn1.clicked.connect(lambda: f(ted1, result))

app.run()