from tkinter import *
import currency_converter

root = Tk()
root.geometry('160x300')
root.title('Program')
root.resizable(0, 0)


def logic():
    try:
        converter = currency_converter.CurrencyConverter()
        resultConvert = converter.convert(sumInput.get(), str(firstInput.get()), str(secondInput.get()))
        result['text'] = round(resultConvert, 2)
    except Exception:
        result['text'] = 'Ошибка!'


firstCurrency = Label(root, text='Код валюты из:', font=('Segoe', 10))
firstCurrency.place(x=5, y=0)

secondCurrency = Label(root, text='Код валюты в:', font=('Segoe', 10))
secondCurrency.place(x=5, y=50)

number = Label(root, text='Сумма:', font=('Segoe', 10))
number.place(x=5, y=100)

result = Label(root, font=('Segoe', 25), bg='grey', fg='black')
result.place(x=5, y=200, width=150, height=95)


firstInput = Entry(root, font=('Segoe', 15))
firstInput.place(x=5, y=20, width='150')

secondInput = Entry(root, font=('Segoe', 15))
secondInput.place(x=5, y=70, width='150')

sumInput = Entry(root, font=('Segoe', 15))
sumInput.place(x=5, y=120, width='150')


button = Button(root, text='Конвертировать', font=10, bg='#C0C0C0', activebackground='grey', command=logic)
button.place(x=5, y=158, width=150)

root.mainloop()
