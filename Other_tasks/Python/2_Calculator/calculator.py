import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')

        # Переменные для вычислений
        self.current_value = "0"
        self.previous_value = ""
        self.operation = ""
        self.new_number = True

        # Создание интерфейса
        self.create_display()
        self.create_buttons()

    def create_display(self):
        # Фрейм для дисплея
        display_frame = tk.Frame(self.root, bg='#f0f0f0')
        display_frame.pack(pady=20, padx=10)

        # Дисплей калькулятора
        self.display = tk.Label(
            display_frame,
            text="0",
            font=('Segoe UI', 32, 'bold'),
            bg='#f0f0f0',
            fg='#000000',
            anchor='e',
            width=12,
            height=1
        )
        self.display.pack()

    def create_buttons(self):
        # Фрейм для кнопок
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack()

        # Определение кнопок (текст, строка, столбец, цвет фона, цвет текста)
        buttons = [
            ('C', 0, 0, '#f0f0f0', '#000000'),
            ('⌫', 0, 1, '#f0f0f0', '#000000'),
            ('%', 0, 2, '#f0f0f0', '#000000'),
            ('÷', 0, 3, '#f0f0f0', '#0078d4'),

            ('7', 1, 0, '#fafafa', '#000000'),
            ('8', 1, 1, '#fafafa', '#000000'),
            ('9', 1, 2, '#fafafa', '#000000'),
            ('×', 1, 3, '#f0f0f0', '#0078d4'),

            ('4', 2, 0, '#fafafa', '#000000'),
            ('5', 2, 1, '#fafafa', '#000000'),
            ('6', 2, 2, '#fafafa', '#000000'),
            ('-', 2, 3, '#f0f0f0', '#0078d4'),

            ('1', 3, 0, '#fafafa', '#000000'),
            ('2', 3, 1, '#fafafa', '#000000'),
            ('3', 3, 2, '#fafafa', '#000000'),
            ('+', 3, 3, '#f0f0f0', '#0078d4'),

            ('±', 4, 0, '#fafafa', '#000000'),
            ('0', 4, 1, '#fafafa', '#000000'),
            (',', 4, 2, '#fafafa', '#000000'),
            ('=', 4, 3, '#0078d4', '#ffffff'),
        ]

        # Создание кнопок
        for (text, row, col, bg_color, fg_color) in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=('Segoe UI', 14),
                width=5,
                height=2,
                bg=bg_color,
                fg=fg_color,
                relief='flat',
                bd=0,
                activebackground='#e0e0e0',
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

        # Настройка весов для растягивания кнопок
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text.isdigit():
            self.handle_number(button_text)
        elif button_text in ['÷', '×', '-', '+']:
            self.handle_operation(button_text)
        elif button_text == '=':
            self.calculate()
        elif button_text == 'C':
            self.clear()
        elif button_text == '⌫':
            self.backspace()
        elif button_text == ',':
            self.handle_decimal()
        elif button_text == '±':
            self.handle_sign()
        elif button_text == '%':
            self.handle_percent()

    def handle_number(self, number):
        if self.new_number:
            self.current_value = number
            self.new_number = False
        else:
            if self.current_value == "0":
                self.current_value = number
            else:
                self.current_value += number
        self.update_display()

    def handle_operation(self, op):
        if self.operation and not self.new_number:
            self.calculate()

        self.previous_value = self.current_value
        self.operation = op
        self.new_number = True

    def calculate(self):
        if not self.operation or not self.previous_value:
            return

        try:
            prev = float(self.previous_value)
            curr = float(self.current_value)

            if self.operation == '+':
                result = prev + curr
            elif self.operation == '-':
                result = prev - curr
            elif self.operation == '×':
                result = prev * curr
            elif self.operation == '÷':
                if curr == 0:
                    self.current_value = "Ошибка"
                    self.update_display()
                    self.operation = ""
                    self.previous_value = ""
                    self.new_number = True
                    return
                result = prev / curr

            # Форматирование результата
            if result == int(result):
                self.current_value = str(int(result))
            else:
                self.current_value = str(round(result, 10))

            self.operation = ""
            self.previous_value = ""
            self.new_number = True
            self.update_display()
        except:
            self.current_value = "Ошибка"
            self.update_display()
            self.operation = ""
            self.previous_value = ""
            self.new_number = True

    def clear(self):
        self.current_value = "0"
        self.previous_value = ""
        self.operation = ""
        self.new_number = True
        self.update_display()

    def backspace(self):
        if len(self.current_value) > 1:
            self.current_value = self.current_value[:-1]
        else:
            self.current_value = "0"
        self.update_display()

    def handle_decimal(self):
        if '.' not in self.current_value:
            if self.new_number:
                self.current_value = "0."
                self.new_number = False
            else:
                self.current_value += '.'
            self.update_display()

    def handle_sign(self):
        if self.current_value != "0" and self.current_value != "Ошибка":
            if self.current_value[0] == '-':
                self.current_value = self.current_value[1:]
            else:
                self.current_value = '-' + self.current_value
            self.update_display()

    def handle_percent(self):
        try:
            value = float(self.current_value) / 100
            if value == int(value):
                self.current_value = str(int(value))
            else:
                self.current_value = str(value)
            self.update_display()
        except:
            pass

    def update_display(self):
        # Ограничение длины отображаемого текста
        display_text = self.current_value
        if len(display_text) > 12:
            display_text = display_text[:12]
        self.display.config(text=display_text)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
