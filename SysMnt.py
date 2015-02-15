#!/usr/bin/python
# -*- coding: utf-8 -*-
## \file SysMnt.py
## \brief Class for mounting and scanning for new devices

import os
import glob
import re
import os
import subprocess
import time
import stat


	
class SysMnt:
	""" \brief Class containing methods for mounting/listing devices
	"""
	def is_block_device(self,filename):
		"""\brief Method to get if file is block file
		\param self Point on class
		\param filename Name of file
		\return False if not, else mode of block device
		"""
		try:
			mode = os.lstat(filename).st_mode
		except OSError:
			return False
		else:
			return stat.S_ISBLK(mode)

	def getList(self):
		"""\brief Method to get list of block devices
		\param self Point on class
		\return List of block devices
		"""
		lst=[]
		dev_pattern = ['sd.*','mmcblk*']
		for device in glob.glob('/sys/block/*'):
			for pattern in dev_pattern:
				if re.compile(pattern).match(os.path.basename(device)):
					if os.path.exists("/dev/" + device.split("/")[-1] + "1"):
						lst.append("/dev/" + device.split("/")[-1]+ "1")
					else:
						lst.append("/dev/" + device.split("/")[-1])
		rt=subprocess.call("blkid /dev/sr0", shell=True, stdout=subprocess.PIPE)
		if rt == 0:
			lst.append("/dev/cdrom")
		return lst
	def tstMount(self,name):
		"""\brief Method to mount device
		\param name Device to be mounted
		\param self Point on class
		\return True if mounted, false if it failed
		"""
		time.sleep(5)
		f = open("/proc/mounts","r")
		cn=f.read()
		f.close()
		d=False
		for ln in cn.split("\n"):
			if name == "/dev/cdrom":
				name = "/dev/sr0"
			if name in ln:
				n=ln.split(" ")[1]
				rt=subprocess.call("mount --bind \""+ n + "\" ./mnt/", shell=True)
				d=True
				break
		if d == False:
			rt=subprocess.call("mount \""+ name + "\" ./mnt/", shell=True)
		if rt == 0:
			return True
		else:
			return False
	def ddSam(self,name,size=100):
		"""\brief Method to create sample of block file
		\param name Name of file
		\param size Size of file in MB
		\param self Point on class
		"""
		subprocess.call("dd if=\"" + name + "\" of=\"./cache/check.bin\" bs=1MB count=" + str(size) + "", shell=True)
	def uMnt(self):
		"""\brief Method to umount
		\param self Point on class
		"""
		subprocess.call("umount ./mnt/", shell=True)
if __name__=="__main__":
	print("Just for import")
	#s=SysMnt()
	#print s.is_block_device("/dev/sdd1")
