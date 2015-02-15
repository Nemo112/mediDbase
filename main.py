#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file main.py
## \brief Louncher method

import os.path
import subprocess

class Chdir:
	""" \brief Class for rewriting path
	"""
	def __init__( self, newPath ):
		""" Constructor of the class
		\param self Pointer on class
		\param newPath New path
		"""
		## Saved path
		self.savedPath = os.getcwd()
		os.chdir(newPath)
	def __del__( self ):
		""" Desctructor on class
		\param self Pointer on class
		"""
		os.chdir( self.savedPath)

if __name__ == "__main__":
	## Instantion of new path
	cd=Chdir("/usr/share/mediDbase")
	## return code
	bc=subprocess.call("./mnWindow.py", shell=True)
	exit(bc)


##
##\mainpage Documentation
##
##\section About
## Use make to install.
##
## Small app for indexing CDs, USB Flashes, ...
##
##\section Contact
## Development guided by Martin Beránek martin.beranek112@gmail.com
##
