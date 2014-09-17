#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file mnWindow.py
## \brief Main application window
from Tkinter import *
import ttk

if __name__ == "__main__":
	class App:
		""" \brief Class containing gui
		"""
		def __init__(self,r):
			""" Constructor od the class
			\param self Pointer on class
			\param r Pointer on Tkinker window
			"""
			## Ukazatel na okno Tk
			self.root=r
			self.root.title("Media DBase")
			self.root.geometry(("%dx%d")%(460,300))
			self.root.wm_iconbitmap('@./gnusk.xbm')
			self.root.protocol("WM_DELETE_WINDOW",self.qquit)
			self.root.resizable(0,0)
		def paintLayout(self):
			""" Metoda vykreslující grafické prvky okna
			Slouží jako komplexní metoda pro vykreslení a je hlavní metodou s práci s oknem
			\param self Ukazatel na objekt
			"""
			gpMan = LabelFrame(self.root, text="Service stop/start", padx=5, pady=5)
			gpMan.place(relx=0.01, rely=0.01)
			Button(gpMan,height=1, width=19,text="Start").pack()
			
			gpLst = LabelFrame(self.root, text="DBase listing", padx=5, pady=5)
			gpLst.place(relx=0.01, rely=0.24)
			
			self.ew=StringVar()
			en=Entry(gpLst,width=21,textvariable=self.ew)
			en.pack(side=TOP)
			#en.bind("<Return>", self.keyEn)
			scrol= Scrollbar(gpLst)
			## List pro výpis změn v systému
			self.tl = Listbox(gpLst,height=10, width=21, bd=0, yscrollcommand=scrol.set)
			self.tl.pack(side=LEFT)
			scrol.pack(side=RIGHT, fill=Y)
			scrol.config(command=self.tl.yview)
			# Name of new media
			self.en=StringVar()
			nn=Entry(self.root,width=15,textvariable=self.en)
			nn.place(relx=0.68, rely=0.08)
			Label(self.root,height=1,text="Name:").place(relx=0.48, rely=0.08)
			#en.bind("<Return>", self.keyEn)
			# Notices to user
			gpTh = LabelFrame(self.root, text="Just done:", padx=5, pady=5)
			gpTh.place(relx=0.48, rely=0.18)
			scrollbar = Scrollbar(gpTh)
			## List pro výpis změn v systému
			self.to = Listbox(gpTh,height=10, width=24, bd=0, yscrollcommand=scrollbar.set)
			self.to.pack(side=LEFT)
			self.to.insert('end', "Nothing so far...")
			scrollbar.pack(side=RIGHT, fill=Y)
			scrollbar.config(command=self.to.yview)
			# Progress
			Label(self.root,height=1, width=21,text="Medium indexing:").place(relx=0.42, rely=0.82)
			## Ukazatel vytížení počítače
			self.progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
			self.progressbar.place(relx=0.5, rely=0.91)
			self.progressbar["value"]=0
			self.progressbar["maximum"]=100
		
		def qquit(self):
			""" Metoda pro ukončení okna
			Je nutné vypnout vlákno, které vykonává příkazy na pozadí okna
			\param self Ukazatel na objekt
			"""
			self.root.destroy()
	## Instance TK okna
	win = Tk()
	## Instance okna třídy aplikace
	pp = App(win)
	pp.paintLayout()
	win.mainloop()
	