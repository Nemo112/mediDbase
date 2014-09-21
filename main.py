#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file main.py
## \brief Louncher method

import os.path
import subprocess

def runProcess(exe):
	""" Method for lunching command
	\param exe String containg command
	\return Yielding line by line output from subprocess
	"""
	exe=exe.split()    
	p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	while(True):
		retcode = p.poll()
		line = p.stdout.readline()
		yield line
		if(retcode is not None):
			break

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
	cd=Chdir("/opt/mediDbase/")
	if os.path.isfile("/usr/share/doc/python-tk/README.Tk"):
		## Ansver of call
		bc=subprocess.call("./mnWindow.py", shell=True)
	else:
		print("Python-TK missing, install?")
		## User ask
		var = raw_input("yes(y)/no(n): ")
		## Take on letter
		d=str(var)[0]
		if d == "a":
			for line in runProcess("apt-get install python-tk -y"):
				print line,
			bc=subprocess.call("./mnWindow.py", shell=True)
		else:
			exit(2)
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