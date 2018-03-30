import calendar
import datetime
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from itertools import zip_longest

class TtkCalendar(ttk.Frame):
    def __init__(self, master=None, **kw):
        now = datetime.datetime.now()
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', now.year)
        month = kw.pop('month', now.month)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        super().__init__(master, **kw)

        self.selected = None
        self.date = datetime.date(year, month, 1)
        self.cal = calendar.TextCalendar(fwday)
        self.font = tkfont.Font(self)
        self.header = self.create_header()
        self.table = self.create_table()
        self.canvas = self.create_canvas(sel_bg, sel_fg)
        self.build_calendar()

    def create_header(self):
        left_arrow = {'children': [('Button.leftarrow', None)]}
        right_arrow = {'children': [('Button.rightarrow', None)]}
        style = ttk.Style(self)
        style.layout('L.TButton', [('Button.focus', left_arrow)])
        style.layout('R.TButton', [('Button.focus', right_arrow)])

        hframe = ttk.Frame(self)
        btn_left = ttk.Button(hframe, style='L.TButton',
                              command=lambda: self.move_month(-1))
        btn_right = ttk.Button(hframe, style='R.TButton',
                               command=lambda: self.move_month(1))
        label = ttk.Label(hframe, width=15, anchor='center')

        hframe.pack(pady=5, anchor=tk.CENTER)
        btn_left.grid(row=0, column=0)
        label.grid(row=0, column=1, padx=12)
        btn_right.grid(row=0, column=2)
        return label

    def move_month(self, offset):
        self.canvas.place_forget()
        month = self.date.month - 1 + offset
        year = self.date.year + month // 12
        month = month % 12 + 1
        self.date = datetime.date(year, month, 1)
        self.build_calendar()

    def create_table(self):
        cols = self.cal.formatweekheader(3).split()
        table = ttk.Treeview(self, show='', selectmode='none',
                             height=7, columns=cols)
        table.bind('<Map>', self.minsize)
        table.pack(expand=1, fill=tk.BOTH)
        table.tag_configure('header', background='grey90')
        table.insert('', tk.END, values=cols, tag='header')
        for _ in range(6):
            table.insert('', tk.END)

        width = max(map(self.font.measure, cols))
        for col in cols:
            table.column(col, width=width, minwidth=width, anchor=tk.E)
        return table

    def minsize(self, e):
        width, height = self.master.geometry().split('x')
        height = height[:height.index('+')]
        self.master.minsize(width, height)

    def create_canvas(self, bg, fg):
        canvas = tk.Canvas(self.table, background=bg,
                           borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=fg, anchor=tk.W)
        handler = lambda _: canvas.place_forget()
        canvas.bind('<ButtonPress-1>', handler)
        self.table.bind('<Configure>', handler)
        self.table.bind('<ButtonPress-1>', self.pressed)
        return canvas

    def build_calendar(self):
        year, month = self.date.year, self.date.month
        month_name = self.cal.formatmonthname(year, month, 0)
        month_weeks = self.cal.monthdayscalendar(year, month)

        self.header.config(text=month_name.title())
        items = self.table.get_children()[1:]
        for week, item in zip_longest(month_weeks, items):
            week = week if week else [] 
            fmt_week = ['%02d' % day if day else '' for day in week]
            self.table.item(item, values=fmt_week)

    def pressed(self, event):
        x, y, widget = event.x, event.y, event.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)
        items = self.table.get_children()[1:]

        if not column or not item in items:
            # clicked te header or outside the columns
            return

        index = int(column[1]) - 1
        values = widget.item(item)['values']
        text = values[index] if len(values) else None
        bbox = widget.bbox(item, column)
        if bbox and text:
            self.selected = '%02d' % text
            self.show_selection(bbox)

    def show_selection(self, bbox):
        canvas, text = self.canvas, self.selected
        x, y, width, height = bbox
        textw = self.font.measure(text)
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(x=x, y=y)

    @property
    def selection(self):
        if self.selected:
            year, month = self.date.year, self.date.month
            return datetime.date(year, month, int(self.selected))

def main():
    root = tk.Tk()
    root.title('Tkinter Calendar')
    ttkcal = TtkCalendar(firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

if __name__ == '__main__':
    main()
