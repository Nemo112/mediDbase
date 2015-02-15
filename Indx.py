#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file Indx.py
## \brief Class for indexing and information getting

import hashlib
import os
import datetime
import time
import string
import random

class Indx:
	"""\brief Class for indexing and information selecting
	"""
	def hashFile(self,name):
		""" Method for file hashing
		\param self Pointer on class
		\param name Name path to hashed file
		\return String containing hash of file
		"""
		#if os.path.isfile(name) == False:
		#	raise ValueError("Soubor " + name + " neexistuje")
		BLOCKSIZE = 868435456
		hasher = hashlib.sha1()
		with open(name, 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
		return(hasher.hexdigest())
	def makeName(self,name="",db=None):
		""" Method for generating name of file
		\param self Pointer on class
		\param name Name path to hashed file
		\param db Name input
		\return String containing name of new medium
		"""
		if db == None:
			tm = str(int(time.time()))[-4:-1]
			ra = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))
			return (name + ra + tm)
		else:
			print db.getLastName()
			print len(db.getLastName().split("_"))
			if len(db.getLastName().split("_")) >= 2:
				l=db.getLastName().split("_")[1]
			else:
				l=""
			try:
				#print l + ":elko"
				if l == "":
				
					i=0
				else:
					i=int(l)
					i += 1
				#print "ret:" + name + "_" + str(i)
				return name + "_" + str(i)
			except:
				tm = str(int(time.time()))[-4:-1]
				ra = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2))
				return (name + ra + tm)			
	def getTime(self,timestp="[%H:%M:%S %d.%m.%Y]"):
		""" Method for generating timestamp
		\param self Pointer on class
		\param timestp Timestamp
		\return String containing timestamp
		"""
		tm=time.time()
		return (datetime.datetime.fromtimestamp(tm).strftime(timestp))
	def lstFiles(self,path=""):
		""" Method for generating list of files in medium
		\param self Pointer on class
		\param path Path to listing file
		\return List of files
		"""
		if os.path.isdir(path) == False:
			raise ValueError("Soubor " + name + " neexistuje")
		toWr=""
		for root, dirs, files in os.walk(path):
			path = root.split('/')
			toWr += (len(path) - 1) *'---' + os.path.basename(root) + "\n"
			for file in files:
				toWr += len(path)*'---' + file + "\n"
		return toWr
if __name__=="__main__":
	print("Just for import")
