import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
# Banner
banner = (f"""     {MERAH}({PUTIH}-rozhak-{MERAH}){PUTIH}
{MERAH}╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐
{MERAH}║  │ ││││└┐┌┘├┤ ├┬┘ │
{PUTIH}╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}
{HIJAU}1.{PUTIH} Mendapatkan token EAAI
{HIJAU}2.{PUTIH} Dapatkan token EAAB
{HIJAU}3.{PUTIH} Cara menggunakan
{HIJAU}4.{PUTIH} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}?.{PUTIH} Choose :{HIJAU} ")
    if masuk == '1' or masuk == '01':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__satu__(cookie)
      else:
        exit(f"{MERAH}!.{MERAH} Periksa cookienya")
    elif masuk == '2' or masuk == '02':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__dua__(cookie)
      else:
        exit(f"{MERAH}!.{MERAH} Periksa cookienya")
    elif masuk == '3' or masuk == '03':
      print(f"{KUNING}?.{PUTIH} Anda akan diarahkan ke youtube...");time.sleep(3);os.system('xdg-open https://youtu.be/Xv0plMtS4Cw');exit()
    elif masuk == '4' or masuk == '04':
      exit()
    else:
      exit(f"{MERAH}!.{MERAH} Wrong input")

if __name__=='__main__':
   convert()
