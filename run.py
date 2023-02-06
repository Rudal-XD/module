import requests, time, os, re, json, random
from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

# Banner
banner = (f"""[bold red]([bold green]˜”*°•.˜”*°• Mikaz •°*”˜.•°*”˜[bold red])
[bold blue]================================
| [bold yellow][98]. [bold green]WA SAYA LANGSUNG[bold blue]	|
| [bold yellow][99]. [bold green]MY INFORMASI		[bold blue]|
[bold blue]================================
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('git pull')
    os.system('clear')
    print(f"""{banner}|				|
|          [bold red]==  MENU  ==[bold blue]		|
[bold blue]================================
| [bold yellow][1].[bold green] install python[bold blue]		|
[bold blue]| [bold yellow][2].[bold green] Install requests[bold blue]	 	|
[bold blue]| [bold yellow][3].[bold green] install mechanize[bold blue]	|
[bold blue]| [bold yellow][4].[bold red] Keluar (exit)[bold white]	[bold blue]	|
[bold blue]================================
   """)
    masuk = input(f"?.masukan nomor :")
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
      print(f"[bold red]!.[bold red]----- Masukan nomor yang bener-----[bold white]");time.sleep(3);convert()

if __name__=='__main__':
   convert()
