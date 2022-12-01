from tkinter import *
import osztaly

x = osztaly.Nev()


def nevkiiras():
    x.f_vagy_l()
    nem_ertek["state"] = NORMAL
    nem_ertek.delete(1.0, END)
    nem_ertek.insert(1.0, x.nem)
    nem_ertek.grid(row=2, column=2)
    nem_ertek["state"] = DISABLED

    x.vezeteknev_sorsolas = vezetek.get()
    x.veznevgenerator()
    veznev_ertek["state"] = NORMAL
    veznev_ertek.delete(1.0, END)
    veznev_ertek.insert(1.0, x.vezeteknev)
    veznev_ertek.grid(row=1, column=2)
    veznev_ertek["state"] = DISABLED

    if kereszt.get():
        if ferfi_noi.get() == 1:
            x.fiu_sorsolas = True
            x.lany_sorsolas = False
        if ferfi_noi.get() == 2:
            x.lany_sorsolas = True
            x.fiu_sorsolas = False
    else:
        x.lany_sorsolas = False
        x.fiu_sorsolas = False
    x.nevgenerator()
    nev_ertek["state"] = NORMAL
    nev_ertek.delete(1.0, END)
    nev_ertek.insert(1.0, x.nev)
    nev_ertek.grid(row=1, column=3)
    nev_ertek["state"] = DISABLED


ablak = Tk()
ablak.title("Névgenerálás")
ablak.minsize(200, 150)

cim_l = Label(ablak, text="Névgenerálás")
cim_l.grid(row=0, column=2)

nev_l = Label(ablak, text="Név:")
nev_l.grid(row=1, column=0, sticky=E)

veznev_ertek = Text(ablak, height=1, width=10, state=DISABLED)
veznev_ertek.grid(row=1, column=2)

nev_ertek = Text(ablak, height=1, width=10, state=DISABLED)
nev_ertek.grid(row=1, column=3)

nem_l = Label(ablak, text="Férfi/Női:")
nem_l.grid(row=2, column=0, sticky=E)

nem_ertek = Text(ablak, height=1, width=5, state=DISABLED)
nem_ertek.grid(row=2, column=2, sticky=W)

ferfi_noi = IntVar()
ferfi_noi.set(0)
ferfi_radio = Radiobutton(ablak, text="Férfi", variable=ferfi_noi, value=1)
ferfi_radio.grid(row=3, column=0)

noi_radio = Radiobutton(ablak, text="Női", variable=ferfi_noi, value=2)
noi_radio.grid(row=3, column=1)

vezetek = BooleanVar()
vezetek_check = Checkbutton(ablak, text="Vezetéknév", variable=vezetek)
vezetek_check.grid(row=4, column=0, columnspan=2, sticky=W)

kereszt = BooleanVar()
nev_check = Checkbutton(ablak, text="Keresztnév", variable=kereszt)
nev_check.grid(row=4, column=2, columnspan=2, sticky=W)

lezar_g = Button(ablak, text="Bezárás", command=ablak.destroy)
lezar_g.grid(row=5, column=2, columnspan=2)

nev_g = Button(ablak, text="Generálás", command=nevkiiras)
nev_g.grid(row=5, column=0, columnspan=2)

mainloop()
