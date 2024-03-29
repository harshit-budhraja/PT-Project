try:
	import requests
	import psutil
except ImportError:
	if(os.name=='posix'):
		ch = str(input('You are running a Linux-based OS and some dependencies are not found in your system. Install them ? (y/n)'))
		if(ch=='y' or ch=='Y'):
			os.system('sudo pip3 install requests psutil')
			print('System setup complete')
		elif(ch=='n' or ch=='N'):
			os.system('exit')
	elif(os.name=='nt'):
		ch = str(input('You are running a Windows-based OS and some dependencies are not found in your system. Install them ? (y/n)'))
		if(ch=='y' or ch=='Y'):
			os.system('pip install requests psutil')
			print('System setup complete')
		elif(ch=='n' or ch=='N'):
			os.system('exit')

import requests
import psutil
import getpass
import os
import socket
url = 'https://apps.arachnis.org/pt-project/'
for i in range(0,10):
	publicip = requests.get('http://ip.42.pl/raw').text
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	data = str(getpass.getuser()) + '@' + str(socket.gethostname()) + ' (' + str(os.name) + ') is running at ' + str(psutil.cpu_percent(interval=1)) + '% CPU right now [' + str(publicip) + ']' + '[' + str(s.getsockname()[0]) + ']'
	payload = {'Name': data}
	r = requests.post(url, data=payload)
	print(data)
