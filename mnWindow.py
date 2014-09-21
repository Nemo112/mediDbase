#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file mnWindow.py
## \brief Main application window
from Tkinter import *
import ttk
import multiprocessing
from SysMnt import SysMnt
from Queue import Empty, Full
from DBHand import DBHand
import subprocess
import re
import os
import tkMessageBox

if __name__ == "__main__":
	class App(object):
		""" \brief Class containing gui
		"""
		def __init__(self,r,qii,qoi):
			""" Constructor od the class
			\param self Pointer on class
			\param r Pointer on Tkinker window
			"""
			## Pointer on TK window
			self.root=r
			self.root.title("Media DBase")
			self.root.geometry(("%dx%d")%(460,320))
			self.root.wm_iconbitmap('@./gnusk.xbm')
			self.root.protocol("WM_DELETE_WINDOW",self.qquit)
			self.root.resizable(0,0)
			## Input quee
			self.qi=qii
			## Output quee
			self.qo=qoi
			## Mounting sys class
			self.sysm=SysMnt()
			## DB handle
			self.db=DBHand()
			## New device detection activation
			self.lo=False
			## Name of currently loading devices
			self.name=""
		def startListen(self):	
			""" Method for starting listening to new media
			\param self Pointer on class
			"""
			if self.lo == False:
				self.dvs=self.sysm.getList()
				self.beg.configure(text="Stop")
				self.lo=True
			else:
				self.beg.configure(text="Start")
				self.lo=False
		def listRes(self,reg="*"):
			"""Method for listing the dbase into window
			\param self Pointer on class
			\param reg Regular expresion
			"""
			print reg
			w=self.v.get()
			self.tl.delete(0, END)
			ls=self.db.getList()
			for i in ls:
				if w == 1:
					try:
						m = re.search(reg,i['name'],re.IGNORECASE)					
					except:
						m = "A"
					if m != "":
						self.tl.insert('end', i['name'])
				elif w == 2:
					if os.path.isfile(i['path']):
						f=open(i['path'],"r")
						cn=f.read()
						f.close()
						for lf in cn.split("\n"):
							ins=lf.replace("-","")
							try:
								m = re.search(reg,ins,re.IGNORECASE)
							except:
								m = "A"
							if m != None:
								self.tl.insert('end', ins)
				elif w == 3:
					try:
						m = re.search(reg,i['date'],re.IGNORECASE)					
					except:
						m = "A"
					if m != "":
						self.tl.insert('end', i['date'])
		def keyEn(self,evt):
			"""Method for enter in entry box for name
			\param self Pointer on class
			\param evt Sended event
			"""
			if self.ew.get() == "":
				return
			self.listRes(self.ew.get())
		def getList(self):
			"""Method for generating a list and calling txt reader from OS to show user
			\param self Pointer on class
			"""
			naed="pluma"
			self.db.buildListTxt("./list.txt")
			x=open("/usr/share/applications/defaults.list","r")
			tx=x.read()
			x.close()
			for ln in tx.split("\n"):
				if "text/plain" in ln:
					co=ln.split("=")[1]
					if ";" in co:
						naed = co.split(";")[1].split(".")[0]
					else:
						naed = co.split(".")[0]
			c=[naed,"list.txt"]
			proc = subprocess.Popen(c)
		def keyNm(self,evt):
			"""Method for enter in entry box for name
			\param self Pointer on class
			\param evt Sended event
			"""
			if self.en.get() == "":
				return
			self.name=self.en.get()
			print self.name
		def OnDub(self,event):
			"""Method for getting event from listbox
			\param self Pointer on class
			\param evt Sended event
			"""
			widget = event.widget
			selection=widget.curselection()
			value = widget.get(selection[0])
			w=self.v.get()
			if w == 1:
				it=self.db.getByName(value)
			elif w == 2:
				it=self.db.getByContFls(value)
			elif w == 3:
				it=self.db.getByDate(value)
			itw = Tk()
			pw = mnItem(itw,it,self)
			pw.paintLayout()
			itw.mainloop()
		def paintLayout(self):
			""" Method painting main window
			\param self Pointer on class
			"""
			gpMan = LabelFrame(self.root, text="Service stop/start", padx=5, pady=5)
			gpMan.place(relx=0.01, rely=0.01)
			## Beggining button
			self.beg=Button(gpMan,height=1, width=19,text="Start",command=self.startListen)
			self.beg.pack()
			
			gpMo = LabelFrame(self.root, text="List by", padx=2, pady=1)
			gpMo.place(relx=0.01, rely=0.22)
			self.v = IntVar()
			## Var telling what to choose
			self.v.set(1)
			languages = [
				("Names",1),
				("Apps",2),
				("Date",3)
			]
			for txt, val in languages:
				Radiobutton(gpMo, text=txt, padx = 0.5, variable=self.v, value=val,command=self.listRes).pack(side=LEFT)
			
			gpLst = LabelFrame(self.root, text="DBase listing", padx=5, pady=5)
			gpLst.place(relx=0.01, rely=0.38)	
			
			self.ew=StringVar()
			self.ew.set("*")
			en=Entry(gpLst,width=21,textvariable=self.ew)
			en.pack(side=TOP)
			en.bind("<KeyPress>", self.keyEn)
			scrol= Scrollbar(gpLst)
			## List of DB items
			self.tl = Listbox(gpLst,height=9, width=21, bd=0, yscrollcommand=scrol.set)
			self.tl.pack(side=LEFT)
			scrol.pack(side=RIGHT, fill=Y)
			scrol.config(command=self.tl.yview)
			self.tl.bind("<Double-Button-1>", self.OnDub)
			
			self.listRes()
			
			Button(self.root,height=1, width=23,text="Get a list",command=self.getList).place(relx=0.5, rely=0.07)
			# Name of new media
			self.en=StringVar()
			nn=Entry(self.root,width=15,textvariable=self.en)
			nn.place(relx=0.68, rely=0.2)
			nn.bind("<KeyPress>", self.keyNm)
			Label(self.root,height=1,text="Prename:").place(relx=0.48, rely=0.2)
			# Notices to user
			gpTh = LabelFrame(self.root, text="Just done:", padx=5, pady=5)
			gpTh.place(relx=0.48, rely=0.3)
			scrollbar = Scrollbar(gpTh)
			## List for user notification
			self.to = Listbox(gpTh,height=8, width=24, bd=0, yscrollcommand=scrollbar.set)
			self.to.pack(side=LEFT)
			self.to.insert('end', "Nothing so far...")
			scrollbar.pack(side=RIGHT, fill=Y)
			scrollbar.config(command=self.to.yview)
			# Progress
			Label(self.root,height=1, width=21,text="Medium indexing:").place(relx=0.42, rely=0.82)
			## Pointer on current progress
			self.progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200, mode='determinate')
			self.progressbar.place(relx=0.5, rely=0.91)
			self.progressbar["value"]=0
			self.progressbar["maximum"]=100
			self.loadProgs(self.qo)
		def loadProgs(self,qc):
			""" Method for progressbar changes and messages passing to user
			\param self Ukazatel na objekt
			\param qc Výstupní fronta
			"""
			try:
				if self.lo == True:
					# finding new devices, if found, send to index
					nw=self.sysm.getList()
					if self.dvs != nw:
						for it in nw:
							if it not in self.dvs:
								qi.put("DO;" + it + ";" + self.name)
						self.dvs=nw
					# progress bar and notices to user
					st=qc.get(0)
					mes=st.split(";")[0]
					loa=int(st.split(";")[1])
					self.to.insert('end',mes)
					self.to.select_clear(self.to.size()-2)
					self.to.yview(END)
					self.progressbar["value"]=loa
					if loa == 100:
						self.listRes()
			except Empty:
				pass
			finally:			
				self.root.after(1000,self.loadProgs,qc)
		def qquit(self):
			""" Metoda pro ukončení okna
			Je nutné vypnout vlákno, které vykonává příkazy na pozadí okna
			\param self Ukazatel na objekt
			"""
			self.qi.put("XXX")
			self.root.destroy()
	class mnItem(App):
		""" \brief Class containing gui for selected item
		"""
		def __init__(self,win,ls,app):
			""" Constructor of window
			\param self Pointer on class
			\param win Pointer on Tkinker window
			\param ls Item in DB
			\param app Upper instance of window
			"""
			## Instance of upper window
			self.app=app
			## Item from database
			self.ls=ls
			## Pointer on TK window
			self.root=win
			## Pointer on DBase
			self.db=DBHand()
			self.root.title(ls['name'])
			self.root.geometry(("%dx%d")%(310,400))
			self.root.wm_iconbitmap('@./gnusk.xbm')
			self.root.resizable(0,0)
		def getBook(self):
			""" Booklet opener
			\param self Pointer on class
			"""
			naed="pluma"
			self.db.buildListTxt("./list.txt")
			x=open("/usr/share/applications/defaults.list","r")
			tx=x.read()
			x.close()
			for ln in tx.split("\n"):
				if "text/plain" in ln:
					co=ln.split("=")[1]
					if ";" in co:
						naed = co.split(";")[1].split(".")[0]
					else:
						naed = co.split(".")[0]
			c=[naed,"./books/"+self.ls['name'] + ".txt"]
			proc = subprocess.Popen(c)
		def errItem(self):
			""" Method for erasing item
			\param self Pointer on class
			"""
			result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning')
			if result == 'yes':
				self.db.errInput(self.ls['name'])
				self.root.destroy()
				self.app.listRes()
		def paintLayout(self):
			""" Method painting main window
			\param self Pointer on class
			"""
			Label(self.root,height=1,text="NAME: " + self.ls['name']).place(relx=0.01, rely=0.01)
			Label(self.root,height=1,text="DATE: " + self.ls['date']).place(relx=0.01, rely=0.06)

			gpLst = LabelFrame(self.root, text="Data in medium:", padx=5, pady=5)
			gpLst.place(relx=0.01, rely=0.12)
			scrol= Scrollbar(gpLst)
			to = Listbox(gpLst,height=17, width=34, bd=0, yscrollcommand=scrol.set)
			to.pack(side=LEFT)
			fl=open(self.ls['path'],"r")
			cn=fl.read()
			fl.close()
			for l in cn.split("\n"):
				to.insert('end',l)
			scrol.pack(side=RIGHT, fill=Y)
			scrol.config(command=to.yview)
			
			Button(self.root,height=1, width=14,text="Show booklet",command=self.getBook).place(relx=0.03, rely=0.9)
			Button(self.root,height=1, width=14,text="Erase medium",command=self.errItem).place(relx=0.5, rely=0.9)
	def genOut(qi,qo):
		""" Funkce vlákna
		\param qi Vstupní fronta
		\param qo Vstupní fronta
		"""
		while True:
			stri = ""
			try:
				stri=qi.get(True)
			except Empty:
				pass
			finally:
				if stri == "XXX":
					break
				elif stri.split(";")[0] == "DO":
					sysm=SysMnt()
					if sysm.tstMount(stri.split(";")[1]):
						db=DBHand()
						db.genNewInput(stri.split(";")[2],stri.split(";")[1],"./mnt/",qo)
						sysm.uMnt()
	## Vstupní fronta pracovního vlákna
	qi = multiprocessing.Queue()
	qi.cancel_join_thread()
	## Výstupní fronta pracovního vlákna
	qo = multiprocessing.Queue()
	qo.cancel_join_thread()
	## Pracovní vlákno
	t=multiprocessing.Process(target=genOut,args=(qi,qo,))
	t.start()

	## Instance TK okna
	win = Tk()
	## Instance okna třídy aplikace
	pp = App(win,qi,qo)
	pp.paintLayout()
	win.mainloop()
	
	t.join()