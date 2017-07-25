#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import IntVar, Label, Entry, Button, Text, messagebox, ttk, END, HORIZONTAL
from random import choice

class Sss():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Super Secret Searcher")
        # umieszczenie aplikacji na środka ekranu
        w = 400
        h = 400 # w Windowsach zmienić wartość na 500
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        px = int((ws - w) / 2)
        py = int((hs - h) / 2)
        self.root.geometry("{}x{}+{}+{}".format(w, h, px, py))
        
        self.g = "guest013@myself.com"
        numvar = IntVar()
        self.num = choice([x for x in range(2,51,2)])
        # ustawienie widgetów
        self.L1 = tk.Label(self.root, text="Wyszukiwarka przyszłych programistów").pack()
        self.L2 = tk.Label(self.root, text="ver. 0.666").pack()
        
        self.empty = tk.Label(self.root).pack()

        self.T = tk.Text(self.root, height=4)
        self.T.pack()
        self.T.insert(END,"Witaj w jedynej w swoim rodzaju wyszukiwarce przyszłych \n\
programistów. Za chwilę rozpoczniesz wyszukiwanie, i \n\
aplikacja użyje wymyślnych sposobów na znalezienie \n\
odpowiedniej osoby. Dziękujemy za udzielone nam zaufanie")

        self.B = tk.Button(self.root, text="Zacznij wyszukiwanie", fg='red', font=((),24),
                           command=self.action)
        self.B.pack(pady=20)

        self.P = ttk.Progressbar(self.root, orient=HORIZONTAL, mode='indeterminate', length=250)
        self.P.pack()

        self.L3 = tk.Label(self.root, text="Wyszukiwanie trwa ...")

        self.T2 = tk.Text(self.root, height=6)
        self.T2.insert(END,"\tA teraz sprawdzimy czy nie jesteś robotem. \n\n\
Pomyśl sobie dowolną liczbę całkowitą i ją zapamiętaj. \n\
Pomnóż ją razy dwa, dodaj do niej {}, podziel przez dwa \n\
i od wyniku odejmij liczbę, którą pomyślałeś. Obliczony \n\
Wynik wpisz poniżej. ".format(str(self.num)))

        self.E = tk.Entry(self.root, textvariable=numvar, width=3)

        self.B2 = tk.Button(self.root, text='Sprawdź', fg='red', command=self.check)

    def action(self):
        self.L3.pack(pady=5)
        self.T2.pack()
        self.E.pack(pady=5)
        self.B2.pack()
        self.B['state'] = tk.DISABLED
        self.P.start()

    def check(self):
        if float(self.E.get()) == self.num/2:
            self.P.stop()
            messagebox.showinfo("OK","Znaleziono osobę chętną do zostania programistą. \
Zapytaj go, czy nadal chce nim zostać {}".format(self.g))
            self.root.destroy()
        else:
            messagebox.showerror("WRONG","Hahaha, jednak jesteś robotem bo nie umiesz liczyć.")
            self.root.destroy()

if __name__ == "__main__":    
    Sss()


