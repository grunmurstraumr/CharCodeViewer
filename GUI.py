import sys
import tkinter as tk
from Converter import Converter
from tkinter.scrolledtext import ScrolledText

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.widgets = {
            'input_label': tk.Label(text='Input'),
            'input': tk.Entry(),
            'output_label': tk.Label(text='Output'),
            'output': ScrolledText(wrap=tk.NONE),
        }
        for widget_key in self.widgets:
            self.widgets[widget_key].pack()

        self.root.bind("<Key>", self.update_output_callback)

    def run(self):
        self.root.mainloop()

    def update_output_callback(self, event):
        self.convert()

    def convert(self):
        out_widget = self.widgets['output']
        out_widget.configure(state=tk.NORMAL)
        out_widget.delete('0.0', tk.END)
        chars = self.widgets['input'].get()
        out_widget.insert(tk.INSERT, self.format_output(Converter.convert_many(chars)))
        out_widget.configure(state=tk.DISABLED)

    def format_output(self, data):
        keys = ['original', 'decimal', 'hex', 'binary']
        output_string = 'Letter \tDecimal \tHex \tBinary'
        for i in data:
            output_string += '\n'
            for key in keys:
                output_string += str(i[key]) + '\t'

        return output_string


if __name__ == '__main__':
    g = GUI()
    if len(sys.argv) > 1:
        g.widgets['input'].insert(0, sys.argv[1])
        g.convert()
    g.run()