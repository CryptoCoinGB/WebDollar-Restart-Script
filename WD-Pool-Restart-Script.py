#Import required libraries
import json
import requests
import time
import subprocess

#Set our error flag to 0 to start with, we'll use this
#to  terminate the script if it errors too many times
errorflag = 0

#Infinite loop, end with CTRL+C
while True:

 #Get last 30 block details from the first two block pages of webdollar.network
 jsonresponse1 = json.loads(requests.get("https://webdollar.network:5001/block?p
age_number=1").text)
 jsonresponse2 = json.loads(requests.get("https://webdollar.network:5001/block?p
age_number=2").text)
 #Convert to string so we can search the whole text
 jsonresponsestr = str(jsonresponse1) + str(jsonresponse2)
 #Check if the string contains infomration on a PoW block
 jrspow = 'pow' in jsonresponsestr
 #If it does contain PoW blocks...
 if jrspow == True:
   print ("There has been a recent PoW block... Checking current block details...")
   #Sleep 1 second to reduce server loading
   time.sleep(1)
   #Find current block number
   curblocknum = jsonresponse1['blocks_number']
   print ("Current Block Number: " + str(curblocknum))
   #Find current block type
   curblocktyperes = json.loads(requests.get("https://webdollar.network:5001/block/" + str(curblocknum)).text)
   curblocktype = curblocktyperes['algorithm']
   print ("Current Block Type: " + str(curblocktype))
   #If current block type is PoW
   if curblocktype == "pow":
     #Wait 1 minute before checking again, we don't need to do anything as the miner is running
     print ("Still mining a PoW block, waiting 1 minute before checking again...")
     print (" ")
     time.sleep(60)
     continue

   #If current block type is POS
   elif curblocktype == "pos":
     print ("PoS block after PoW, restarting miner now...")
     #Open screen session and terminate miner
     subprocess.call(["screen", "-S",  "miner", "-p", "0", "-X", "stuff", "^C"])
     #Wait 10 seconds then open screen session and start miner instance
     time.sleep(10)
     subprocess.call(["screen", "-S",  "miner", "-p", "0", "-X", "stuff", "SERVER_PORT=8080 npm run commands^M"])
     #Wait 20 seconds then open screen session and enter 10 to mine in a pool
     time.sleep(20)
     subprocess.call(["screen", "-S",  "miner", "-p", "0", "-X", "stuff", "10^M"])
     #Wait 10 seconds then open screen session and confirm to use existing pool
     time.sleep(10)
     subprocess.call(["screen", "-S",  "miner", "-p", "0", "-X", "stuff", "y^M"])
     #Wait 45 minutes before checking again
     print ("Miner restarted, waiting 45 minutes before checking again...")
     print (" ")
     time.sleep(2700)
     continue

   #If current block type is neither PoW or PoS something is wrong, we'll check again 6 times before exiting with an error
   else:
     #Check if the flag is less than 6, if it is
     if errorflag < 6:
       #Increment the errorflag by one
       errorflag = (errorflag + 1)
       #Wait 5 minutes before checking again
       print ("Somethings not right, I can't find a block type. Check your internet connection. I'll try again in 5 minutes...")
       print (" ")
       time.sleep(300)
       continue
     else:
       #If all else fails, terminate the script
       print ("I've tried again six times and failed. Sorry. Terminating script...")
       break

 #If it doesn't contain PoW blocks...
 else:
   #Wait 5 minutes before checking again
   print ("No recent PoW blocks, waiting 5 minutes before checking again...")
   time.sleep(300)
   continue
