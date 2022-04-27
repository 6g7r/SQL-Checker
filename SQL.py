import os
clear = lambda: os.system('cls')
clear()
try:

    from googlesearch import search
    
except ImportError: 

    print("No module named 'google' found")
    try:
      os.system('pip install google')
    except :
      print("pip install google")
      input("Enter For Exit")
 
try:

    from colorama import Fore
    
except ImportError: 

    print("No module named 'colorama' found")
    try:
      os.system('pip install colorama ')
    except :
      
      print("pip install colorama")
      input("Enter For Exit")
try:

    import requests
    
except ImportError: 

    print("No module named 'requests' found")
    try:
      os.system("pip install requests")
    except :
      
    print("pip install requests")
    input("Enter For Exit")
class sql:
  def __init__(self):
    self.r=requests.Session()
    print(f"""{Fore.RED}
$$$$$$$$$$$$$$$$$$$$$$$$$ By 6g7r 
$$$$$$$$$$$$$$$$$$$$$$$$$ telegram : @l6g7rl
$$$'`$$$$$$$$$$$$$'`$$$$$ insta : @6g7r
$$$$  $$$$$$$$$$$  $$$$$$ 
$$$$. `$' \' \$`  $$$$$$$
$$$$$. !\  i  i .$$$$$$$$
$$$$$$   `--`--.$$$$$$$$${Fore.LIGHTRED_EX}
$$$$$$L        `$$$$$^^$$
$$$$$$$.   .'   ""~   $$$
$$$$$$$$.  ;      .e$$$$$
$$$$$$$$$   `.$$$$$$$$$$$
$$$$$$$$    .$$$$$$$$$$$$
$$$$$$$     $$$$$$$by$TL$
-------------------------
     X SQL Checker X
-------------------------
    """)
    self.g=f" {Fore.GREEN} [X] Hit Sql Site ! "
    self.b=f"{Fore.RED} [X] Bad Sql Site "
    self.chek= '"'
    self.dork = input(f"{Fore.RED} -+- Dork : ")
    for j in search(self.dork, tld="co.in", num=50000, stop=9000, pause=1):
      print(j)
      try:
        self.oo=self.r.get(f"{j}{self.chek}").text
      except :
        print(f"{Fore.RED}Error ! ")
      if "mysql" in self.oo:
        print(self.g)
        with open("Hit Sql Site.txt", "a") as mix:
          mix.write(f"Hit Sql Site —> : {j}\n")
          mix.close()
      elif  "MySQL" in self.oo:
        print(self.g)
        with open("Hit Sql Site.txt", "a") as mix:
          mix.write(f"Hit Sql Site —> : {j}\n")
          mix.close()
      else :
        print(self.b)

sql()
