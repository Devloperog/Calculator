import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphical Calculator")
        self.root.configure(bg="#f0f0f0")

        self.entry = tk.Entry(root, font=('Arial', 18), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=('Arial', 14), command=lambda t=text: self.on_button_click(t),
                               bg="#ffa500", activebackground="#ff8c00", padx=15, pady=15)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)  # Increase terminal height
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                messagebox.showerror("Error", "Invalid expression")
        elif value == 'C':
            self.entry.delete(0, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
