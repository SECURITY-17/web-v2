import requests,os,sys
os.system('clear')
print('''\033[1;32m
░██╗░░░░░░░██╗  ███████╗  ██████╗░
░██║░░██╗░░██║  ██╔════╝  ██╔══██╗
░╚██╗████╗██╔╝  █████╗░░  ██████╦╝
░░████╔═████║░  ██╔══╝░░  ██╔══██╗
░░╚██╔╝░╚██╔╝░  ███████╗  ██████╦╝
░░░╚═╝░░░╚═╝░░  ╚══════╝  ╚═════╝░''')
print('''\033[1;32m
------------------------[~~~~~~~~~~~~~~~]-----------------------

          version2        [  SECURITY ]

                          [  WELCOME  ]

Telegram : https://t.me/protection17

------------------------[~~~~~~~~~~~~~~~]-----------------------
''')
try:
	b = input('\033[1;31mEnter web :  ')
	ban = {
	'ban' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
	}
	x = requests.get(b,headers=ban)
	print('\033[1;32m-------------------------------------')
	print(f'\033[1;34m{x.headers}')
	print('\033[1;32m-------------------------------------')
	print('Do you run web')
	a = input('\033[1;35m[ y / n ] ○~~> : ')
	if a == 'y':
		os.system('python3 web.py')
	else:
			if a == 'n':
					os.system('cd $HOME')
					os.system('cd')	
					os.system('clear')
except Exception as NAYZK:
	print('\033[1;36m-'*50)
	print(f'\033[1;31mERROR : ! {NAYZK}')
