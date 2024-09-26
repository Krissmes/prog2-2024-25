from tests import Cilveks, Sieviete
import tkinter as tk
from tkinter import ttk

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

vecums = tk.StringVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=1, **options)
vecums_entry.focus()

# dzimums entry

dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=2, **options)
dzimums_entry.focus()

def dzimsanasDiena_button_clicked():
    dzimene = vecums 
    vecums += 1




def razot_button_clikced():
    cilveka_vards = vards.get()
    cilveka_vecums = vecums.get()
    cilveka_dzimums = dzimums.get()
    
    visi_cilveki.append(Cilveks(cilveka_vards, cilveka_vecums, cilveka_dzimums))
    result_label.config(text=visi_cilveki[-1].bazarsPaSevi())


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