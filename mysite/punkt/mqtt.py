from http.client import TEMPORARY_REDIRECT
from django.forms import PasswordInput
import paho.mqtt.client as mqtt
import time

'''
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected to broker")
        
        global Connected
        Connected=True
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    print("Message received: " + str(message.payload))

Connected = False
port = 1883 
broker_address = "broker.emqx.io" 

user = "gruppe1" 
password = "Superman123" 
    
client = mqtt.Client("Python")
client.username_pw_set(user, password=password)

client.on_connect= on_connect
client.on_message= on_message
  
client.connect(broker_address, port=port)

client.loop_start()



while Connected != True:
    time.sleep(0.1)

client.subscribe("test123")

teller = 0
try:
    while True:
        
        time.sleep(2)
        teller += 1
        print(teller)
        if teller>= 10:
            print("avslutt")
            client.disconnect()
            client.loop_stop()
            
    
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

'''
    

'''
except teller >=10:
    print("exiting")
    client.disconnect()
    client.loop_stop()
'''