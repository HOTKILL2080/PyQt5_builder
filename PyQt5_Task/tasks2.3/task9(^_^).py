from main import MyApp

def f(ted1, ted2, ted3, result):
    price = ted1.toPlainText().split()
    duration = ted2.toPlainText().split()
    hum_info = ted3.toPlainText().split()
    best_price = 0
    best_duration = 0
    for p, d in zip(price, duration):
        p = int(p)
        d = int(d)
        if best_price > p and best_duration > d:
            best_price = p
            best_duration = d
        elif int(hum_info[0]) >= p and int(hum_info[1]) >= d:
            best_price = p
            best_duration = d
    result.setText(f'Лучший вариант:\nцена - {best_price}, дни - {best_duration}')

app = MyApp(500, 500)

ted1 = app.widget_create('ted', 'ted1', 150, 35, 20, 100, 200)
ted2 = app.widget_create('ted', 'ted2', 150, 35, 20, 100, 200)
ted3 = app.widget_create('ted', 'ted3', 150, 35, 20, 100, 200)
lab1 = app.widget_create('lab', 'lab1', 150, 35, 20, text='Введите число')
result = app.widget_create('lab', 'result', 250, 100, 20, text='0')
btn1 = app.widget_create('btn', 'btn1', 35, 35, 20, text='=')

app.move_from(ted2, ted1, 'd')
app.move_from(ted3, ted2, 'd', indentation=20)
app.move_from(btn1, ted3, 'r')
app.move_from(result, btn1, 'r')
app.move_from(lab1, ted1, 'u')

btn1.clicked.connect(lambda: f(ted1, ted2, ted3, result))

app.run()