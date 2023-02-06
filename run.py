import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
# Banner
banner = (f"""{MERAH}({HIJAU}˜”*°•.˜”*°• Mikaz •°*”˜.•°*”˜{MERAH}){PUTIH}
{MERAH}================================
{MERAH}|{HIJAU} [98]. {KUNING}WA SAYA LANGSUNG	|
{MERAH}|{HIJAU} [99]. {KUNING}MY INFORMASI		|
{MERAH}================================
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}|				|
|          {HIJAU}==  MENU  =={MERAH}		|
{MERAH}================================
{HIJAU}[1].{PUTIH} install python
{HIJAU}[2].{PUTIH} Install requests
{HIJAU}[3].{PUTIH} install mechanize
{HIJAU}[4].{PUTIH} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
{MERAH}================================
   """)
    masuk = input(f"{KUNING}?.{PUTIH} masukan nomor :{HIJAU} ")
    if masuk == '98' or masuk == '098':
      try:
      	os.system('xdg-open https://wa.me/qr/C7AKGGQIHROWM1')
      except IOError:
      	print('LINK ERROR')
    elif masuk == '99' or masuk == '099':
      try:
      	os.system('xdg-open https://linktr.ee/mikaz_')
      except IOError:
      	print()
    elif masuk == '1' or masuk == '01':
    	try:
    		import python
    		print('python install succes')
    	except ImportError:
    		print('sedang install python')
    		os.system('pkg install python')
    elif masuk == '2' or masuk == '02':
    	try:
    		import requests
    		print('requests install succes')
    	except ImportError:
    		print('sedang install requests')
    		os.system('pip install requeats')
    elif masuk == '3' or masuk == '03':
    	try:
    		import mechanize
    		print('mechanize install succes')
    	except ImportError:
    		print('sedang install mechanize')
    		os.system('pip install mechanize')
    elif masuk == '4' or masuk == '04':
      exit()
    else:
      print(f"{MERAH}!.{MERAH}----- Masukan nomor yang bener-----");time.sleep(3);convert()

if __name__=='__main__':
   convert()
