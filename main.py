import tkinter as tk
import sys

class RedirectText(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Автопрокрутка вниз

    def flush(self):
        pass  # Нужно для совместимости с sys.stdout

# Создаем окно
root = tk.Tk()
root.title("Перехват print в окно")
root.geometry("500x400")

# Создаем текстовое поле (уменьшенное)
text = tk.Text(root, height=10)  # height уменьшен
text.pack(fill='x')

# Поле ввода
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, fill='x', padx=10)

# Кнопка для отправки данных
button = tk.Button(root, text="Envoyer", command=lambda: ask_income(), font=("Arial", 14))
button.pack(pady=5)

# Перенаправляем стандартный вывод
sys.stdout = RedirectText(text)

print("________________Bonjour, svp impôt sur le revenu:____________________")

def ask_income():
    try:
        moneys = int(entry.get())
        if moneys <= 10777:
            print('zero')
        else:
            result = (moneys * 0.11)
            print(result)
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Запускаем главный цикл обработки событий
root.mainloop()













'''
print("________________Bonjour, svp impôt sur le revenu:____________________")


moneys = int(input('Entrez vos revenus:'))
if moneys <= 10777:
    print('zero')
    float (input(moneys <= 10777.1))
    result = (moneys * 0.11)
    print(result)


'''






'''
class Cash():
    def __init__(self):
        try:
            moneys = int(input('Entrez vos revenus:'))
            if moneys <= 10777:
                print('zero')




#tax_calculator = Cash()


'''


'''______________________________________________________

2. Impôt sur le revenu (Подоходный налог)
Прогрессивная шкала (для 2024):

Доход (в год)	Ставка	Налог
До €10,777	0%	Не облагается
€10,778 – €27,478	11%	11% от суммы сверх €10,777
€27,479 – €78,570	30%	30% от суммы сверх €27,478
Свыше €78,570	41%	41% от суммы сверх €78,570
'''

