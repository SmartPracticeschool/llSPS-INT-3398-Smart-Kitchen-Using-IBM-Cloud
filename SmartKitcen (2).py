#try to use jupyter notebook while executing the program wait for atleast 40 seconds for the entire program to run

import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "gdkg96"
deviceType = "Raspberrypi"
deviceId = "0002"
authMethod = "token"
authToken = "abcdefgh"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect() #try with different values

leakstatus=['Leakage','Good']


while True:
        ul1=random.randint(0,100)    # gives the level of item(salt) in container, 7 being threshold minimum 
        ul2 =random.randint(0,100)   # gives the level of item(sugar) in container ,7 being threshold minimum
        
        cyl=random.randint(0,30)    # gives the weight of the cylinder 5kg being empty weight of cylinder minimum
        leak=random.choice(leakstatus)  #detect the leakage of CNG in kitchen
        #enter your mobile number
        if ul1<=15:
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=2lhGxE6vBDIHkQ1jAyrtcqapNRUYoMOS5dn0fsmw7F3CLeT4z8Ot6TMq8uFHfZEVycsB3GCz9wx2piNa&sender_id=FSTSMS&message=YOUR SALT IS ABOUT TO COMPLETE&language=english&route=p&numbers=9652784551')
        if ul2<=15:
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=2lhGxE6vBDIHkQ1jAyrtcqapNRUYoMOS5dn0fsmw7F3CLeT4z8Ot6TMq8uFHfZEVycsB3GCz9wx2piNa&sender_id=FSTSMS&message=YOUR SUGAR IS ABOUT TO COMPLETE&language=english&route=p&numbers=9652784551')
        if cyl<=5:
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=2lhGxE6vBDIHkQ1jAyrtcqapNRUYoMOS5dn0fsmw7F3CLeT4z8Ot6TMq8uFHfZEVycsB3GCz9wx2piNa&sender_id=FSTSMS&message=CYLINDER IS OVER&language=english&route=p&numbers=9652784551')
        if leak=='leakage':
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=2lhGxE6vBDIHkQ1jAyrtcqapNRUYoMOS5dn0fsmw7F3CLeT4z8Ot6TMq8uFHfZEVycsB3GCz9wx2piNa&sender_id=FSTSMS&message=GAS IS BEING LEAKED FROM CYLINDER AND EXHAUST FAN HAS BEEN SWITCHED ON&language=english&route=p&numbers=9652784551')
        data = { 'ultrasonic1' : ul1, 'ultrasonic2': ul2 , 'cylwt':cyl ,'mq6':leak}
        #print (data)
        def myOnPublishCallback():
            print ("Published ultrasonic1 = %s " % ul1, "ultrasonic2 = %s " % ul2,"cylwt = %s" % cyl,"mq6 = %s" % leak,"to IBM Watson")

        success = deviceCli.publishEvent("kitchen", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(30)
        
        deviceCli.commandCallback = myCommandCallback


# Disconnect the device and application from the cloud
deviceCli.disconnect()
