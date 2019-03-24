"""
test_sub.py is an example of a subscriber to a topic
"""

import paho.mqtt.client as mqtt
import time
import base64
import PIL.Image
import segmentation
import pubPlateProc

logfile = None

def on_connect(client, userdata, flags, rc):
    m = "Connected flags " + str(flags) + " Result code "\
    + str(rc) + " Client_id  " + str(client)
    print(m)

def on_message(client, userdata, msg):
    global logfile
    
    image_result = open('image-raw.jpg', 'wb')
    image_64_decode = base64.decodestring(msg.payload)
    image_result.write(image_64_decode)
    image_result.close()
    
    # process image
    segmentation
    
    # use unused variable^ but we can use this to generate the plate.jpg image,
    # which we will now publish on the processedImageData channel
    pubPlateProc
    

def test_sub(logfilename=None):   
    global logfile

    #TODO: PLEASE ENTER THE ACCOUND/PASSWORD and TOPIC FROM THE I3 MARKETPLACE	

    account = 'ayush96'
    #topic = 'JMC_AH1MaTemp.'
    topic = 'Aviato-rawImageData'
    pw = '0tqkf0'
    
    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker [I3 BROKER INFORMATION IS HARD CODED HERE]

    sub_client.subscribe(topic)
    
    if not logfilename is None:
        logfile = open(logfilename, 'w')
        
    rc = 0
    while rc == 0:
        rc = sub_client.loop()
        time.sleep(1)
        
if __name__ == '__main__':
    test_sub('sub.log')
