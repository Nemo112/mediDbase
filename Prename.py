#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file Prename.py
## \brief Class for getting information from prename.txt

import os
import glob

class Prename:
	""" \brief Class for working with prename.txt
	"""
	def __init__(self):
		""" Constructor of the class
		\param self Pointer on class
		"""
		## Path to prename
		self.pa="./prename.txt"

	def getPrename(self):
		""" Method for getting last prename
		\param self Pointer on class
		\return Last prename
		"""
		if os.path.isfile(self.pa) == False:
			open(self.pa,"w").close()
		f=open(self.pa,"r");
		con=f.readlines();
		f.close();
		if len(con) >= 1:
			return con[0]
		else:
			return ""

	def setPrename(self,name=""):
		""" Method for setting prename
		\param self Pointer on class
		\param name New name for prename
		\return Last prename
		"""
		f=open(self.pa,"w");
		f.write(name);
		f.close();

if __name__=="__main__":
	print("Just for import")

