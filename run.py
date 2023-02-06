import os,time

class menu:
	def __init__(self):
		print("""
		1.install python         [ON]
		2.install requests	 [ON]
		3.install mechanize	 [ON]
		4.exit""")
		usna = input('nomor :')
		if usna == ['']:
			print()
		elif usna == ['1']:
			try:
				import python
				print('python telah terinstall')
			except ImportError:
				print('sedang install python...')
				os.system('pkg install python')
		elif usna == ['2']:
			try:
				import requests
				print('requeats telah terinstall')
			except ImportError:
				print('sedang install requests...')
				os.system('pip install requests')
		elif usna == ['3']:
			try:
				import mechanize
				print('mechanize telah terinstall')
			except ImportError:
				print('sedang install mechanize...')
				os.system('pip install mechanize')
		elif usna == ['4']:
			print('terima kasih telah mengunakan tools kami');sleep.time(1);exit()
			
if __name__=='__main__':
	menu()
