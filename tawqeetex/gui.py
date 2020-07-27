# TODO: import only necessary widgets
from utils import *
from tkinter import *
from tkinter import messagebox

from data import init_data
from latex import gen_pdf

def generate_callback():

    gui.city = gui.entry_city.get()
    gui.country = gui.entry_country.get()
    gui.month = str(dict_month['en'].index(gui.var_month.get()) + 1)
    gui.year = gui.entry_year.get()
    gui.method = str(list_method.index(gui.var_method.get()) + 1)
    gui.lang = dict_lang[gui.var_lang.get()]
    gui.adj = str(gui.slider_adj.get())

    init_data(gui.city, gui.country, gui.month, gui.year, gui.method, gui.lang, gui.adj)
    gen_pdf()

    messagebox.showinfo("Warning", "The prayer time schedule is being generated")

class GUI:

    city = None
    country = None
    month = None
    year = None
    method = None
    lang = None
    adj = None

    def __init__(self):
        self.root = Tk()
        self.root.title('tawqeeTeX')
        # self.root.iconbitmap('')
        # self.root.geometry("400x400")
        self.var_month = StringVar()
        self.var_method = StringVar()
        self.var_lang = StringVar()
        self.var_month.set(dict_month['en'][0])
        self.var_method.set(list_method[0])
        self.var_lang.set(list_lang[0])

        self.label_city = Label(self.root, text="City")
        self.entry_city = Entry(self.root)

        self.label_country = Label(self.root, text="Country")
        self.entry_country = Entry(self.root)

        self.label_month = Label(self.root, text="Month")
        self.menu_month = OptionMenu(self.root, self.var_month, *dict_month['en'])

        self.label_year = Label(self.root, text="Year")
        self.entry_year = Entry(self.root)

        self.label_method = Label(self.root, text="Method")
        self.menu_method = OptionMenu(self.root, self.var_method, *list_method)

        self.label_adj = Label(self.root, text="Adjustment")
        self.slider_adj = Scale(self.root, from_=-1, to=1, orient=HORIZONTAL)

        self.label_lang = Label(self.root, text="Language")
        self.menu_lang = OptionMenu(self.root, self.var_lang, *list_lang)

        # state=DISABLED,
        self.button_go = Button(self.root, text="Generate", command=generate_callback)

        self.label_city.grid(row=0, column=0)
        self.entry_city.grid(row=0, column=1)
        self.label_country.grid(row=1, column=0)
        self.entry_country.grid(row=1, column=1)
        self.label_month.grid(row=2, column=0)
        self.menu_month.grid(row=2, column=1)
        self.label_year.grid(row=3, column=0)
        self.entry_year.grid(row=3, column=1)
        self.label_method.grid(row=4, column=0)
        self.menu_method.grid(row=4, column=1)
        self.label_adj.grid(row=5, column=0)
        self.slider_adj.grid(row=5, column=1)
        self.label_lang.grid(row=6, column=0)
        self.menu_lang.grid(row=6, column=1)
        self.button_go.grid(row=7, column=0, columnspan=2)

    def run(self):
        self.root.mainloop()

gui = GUI()

def gui_init():
    gui.run()
