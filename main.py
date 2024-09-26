from tests import Cilveks, Sieviete
import tkinter as tk
from tkinter import ttk, END

#cilvēki
visi_cilveki = []


#ekrāns
root = tk.Tk()
root.title("Cilvēku ražotne")
root.geometry("300x300")

frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# vards entry
vards = tk.StringVar()

vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()


# vecums entry

vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=1, **options)
vecums_entry.focus()

# dzimums entry

dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=2, **options)
dzimums_entry.focus()




def dzimsanas_diena(): 
    jaunais_teksts=""
    for izveletais in listbox.curselection():

        visi_cilveki[izveletais].dzimene()
        jaunais_teksts += visi_cilveki[izveletais].bazarsPaSevi() + "\n"

    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()
    "vajag ielikt funkciju vecums plus 1"


dzim_diena_button = ttk.Button(frame, text='dzimsanas diena')
dzim_diena_button.grid(column=6, row=2, sticky='w', **options)
dzim_diena_button.configure(command=dzimsanas_diena)

# listbox saraksta atjaunosana
def nomainit_sarakstu():
    listbox.delete(0,END)
    for cilveks in visi_cilveki:
        listbox.insert("end","{},{},{}".format(cilveks.name, cilveks.sex, cilveks.age))   


def razot_button_clikced():
    cilveka_vards = vards.get()
    cilveka_vecums = vecums.get()
    cilveka_dzimums = dzimums.get()
    
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_vecums, cilveka_dzimums))
    result_label.config(text=visi_cilveki[-1].bazarsPaSevi())
    nomainit_sarakstu()
    # listbox.insert("end","{},{},{}".format(cilveka_vards, cilveka_dzimums, cilveka_vecums))


saturs = tk.Variable(value=tuple(visi_cilveki))

listbox = tk.Listbox(
    root,
    listvariable = saturs,
    height=6,
    selectmode=tk.EXTENDED    
)

listbox.grid(row = 4, columnspan=3, **options)

def convert_button_clicked():
    rezultats = vards.get(), vecums.get(), dzimums.get()
    result_label.config(text=rezultats)

convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=razot_button_clikced)

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3, **options)

# razosana button

    

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()