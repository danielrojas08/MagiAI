def searchGoogle():
	import os
	os.system('cd skills')
	import googleSearch,py
	pass

def searchYoutube():
	import os
	os.system('cd skills')
	import youtubeSearch.py
	pass

def logOut():
	exit()
	pass

def playMusic():
	import os
	os.system('cd skills')
	import playMusic.py
	pass

def openApp():
	import os
	application = input("App Name : ")
	def subprocess_cmd(command):
		process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
		proc_stdout = process.communicate()[0].strip()
		print proc_stdout
	subprocess_cmd('cd ..; cd Applications;')
	os.startfile(aplication)
	pass

def startSystem():
	command = input('Type Command: ')
	while True:
		if command == "search google":
			searchGoogle()
			startSystem()
			pass
		if command == "search youtube":
			searchYoutube()
			startSystem()
			pass
		if command == "log out":
			logOut()
			startSystem()
			pass
		if command == "play music":
			playMusic()
			startSystem()
			pass
		if command == 'help':
			print('Commands are:')
			print('search google')
			print("search youtube")
			print('play music')
			print('log out')
			startSystem()
		if command == 'list music':
			listMusic()
			startSystem()
			pass
		if command == 'clear':
			import os
			clear = os.system('clear')
			print(clear)
		if command == 'open app':
			openApp()
			startSystem()
	pass
	pass

def logIn():
	password = 'Sup Hades'
	attempt = input("Password: ")
	if attempt == password:
		startSystem()
	pass

logIn()
