import requests, time, sys
from colorama import Fore, init
import subprocess as sp
init()

def main():
	clear()
	print(Fore.BLUE+'*'*36)
	print('+ '+Fore.CYAN+'Dank SoundCloud Username Checker'+Fore.BLUE+' +')
	print('*'*36+Fore.WHITE)
	sp.call('dir', shell=True)
	
	filename = input(Fore.GREEN+'Please Enter Username Filename: '+Fore.RED)
	output = input(Fore.GREEN+'Please Enter Output Filename: '+Fore.RED)

	attempt = 0
	success = 0
	failed = 0
	unknown = 0

	with open(filename, 'r') as f:
		for line in f:
			for word in line.split():
				try:
					attempt += 1
					r = requests.get('https://www.soundcloud.com/'+word)
					if r.status_code == 404:
						with open(output, 'a') as output:
							output.write(word+'\n')
							output.close()
						success += 1
					elif r.status_code == 200:
						failed += 1
					else:
						unknown += 1
				except Exception as e:
					pass
					unknown += 1
				msg = (Fore.CYAN+"Attempts {} | Success {} | Failed {} | Unknown {}".format(str(attempt), str(success), str(failed), str(unknown)))
				sys.stdout.write("\r{:<100}".format(msg))
				sys.stdout.flush()
				time.sleep(1)
	print('\nDone!')

def clear():
	sp.call('cls', shell=True)

if __name__ == '__main__':
	main()
