import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


app = Application
app.master.title("BGN to EUR Converter")

app.mainloop()

 class Application(tk.Frame):
    def create_widgets(self):
        self.label = tk.Label(text="Value Converter")
        self.numberEntry = tk.Entry()
        self.convertButton = tk.Button(text="Convert", command=self.convert)


self.label.pack(side="left")
self.numberEntry.pack(side="left")
self

usd_currency = float(input())

bgn_currency = float(usd_currency * 1.79549)

print(bgn_currency)
