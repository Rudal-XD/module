import os

try:
	import rich
except ImportError:
	print('----------module rich belum terinstall')
	os.system('pip install rich')
	
try:
	import requests
except ImportError:
	print('---------module requests belum terinstall')
	os.system('pip install requests')
	
	
try:
	import bash
except ImportError:
	print('------------module bash belum terinstall')
	os.system('pip install bash')
	
try:
	import nechanize
except ImportError:
	print('----------module mechanize belum terinstall')
	os.system('pip install mechanize')
	
try:
	import python 
except ImportError:
	print('----------module python belum terinstall')
	os.system('pkg install python')
	
try:
	import nodejs
except ImportError:
	print('----------module nodejs belum terinstall')
	os.system('pkg install nodejs')
	
try:
	import git
except ImportError:
	print('-----------module git belum terinstall')
	os.system('pkg install git')
	
try:
	import bs4
except ImportError:
	print('----------module bs4 belum terinstall')
	os.system('pip install bs4')
	
try:
	import wget
except ImportError:
	print('----------0module wget belum terinstall')
	os.system('pip install wget')
