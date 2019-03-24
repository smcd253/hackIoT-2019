"""
test_sub.py is an example of a subscriber to a topic
"""

import paho.mqtt.client as mqtt
import time
import base64
import PIL.Image
import io 
from pynput.keyboard import Key, Controller
import readchar  # using module keyboard

logfile = None

def on_connect(client, userdata, flags, rc):
    m = "Connected flags " + str(flags) + " Result code "\
    + str(rc) + " Client_id  " + str(client)
    print(m)

def on_message(client, userdata, msg):
    global logfile

    if (msg.payload):
        # print(msg.payload)
        image_result = open('image-raw.jpg', 'wb')
        image_64_decode = base64.decodestring(msg.payload)
        image_result.write(image_64_decode)
        image_result.close()

        print("msg received") 

        keyboard = Controller()
        keyboard.press('a')
        # keyboard.release('a')
        # process image
        # segmentation

        # use unused variable^ but we can use this to generate the plate.jpg image,
        # which we will now publish on the processedImageData channel
        # pubPlateProc
        # except:
        #     print("image-raw.jpg not available")
    else:
        print("msg empty")
    

def test_sub(logfilename=None):   
    global logfile

    #TODO: PLEASE ENTER THE ACCOUND/PASSWORD and TOPIC FROM THE I3 MARKETPLACE	

    account = 'SpencerMcD'
    #topic = 'JMC_AH1MaTemp.'
    topic = ['Aviato-rawImageData', 'Aviato-processedImageData']
    pw = 'y1ycmu'
    
    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker [I3 BROKER INFORMATION IS HARD CODED HERE]

    sub_client.subscribe(topic[0])
    
    if not logfilename is None:
        logfile = open(logfilename, 'w')
 
    keyboard = Controller()
    rc = 0
    flag = 0
    while flag == 0:
        
        keyboard.press(' ')
        print("waiting for msg")
        rc = sub_client.loop()
        c = readchar.readchar()
        # capturedOutput = io.StringIO()          # Create StringIO object
        # sys.stdout = capturedOutput                   #  and redirect stdout.
        # sys.stdout = sys.__stdout__                   # Reset redirect.
        # print ('Captured' + capturedOutput.getvalue())   # Now works as before.
        # if capturedOutput.getvalue() == "msg received":
        #     flag = 1

        print("c = " + c)
        if str(c)=='a':
            flag = 1

        time.sleep(1)

    import segmentation
    import pubPlateProc

if __name__ == '__main__':
    test_sub('sub.log')
