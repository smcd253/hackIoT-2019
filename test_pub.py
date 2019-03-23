"""
test_sub.py is an example of a publisher subscribing to a topic
"""

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    """print out result code when connecting with the broker

    Args:
        client: publisher
        userdata:
        flags:
        rc: result code

    Returns:

    """

    m="Connected flags"+str(flags)+"result code "\
    +str(rc)+"client1_id  "+str(client)
    print(m)



def on_message(client1, userdata, message):
    """print out recieved message

    Args:
        client1: publisher
        userdata:
        message: recieved data

    Returns:

    """
    print("message received  "  ,str(message.payload.decode("utf-8")))


if __name__ == '__main__':

    #TODO: modify topic from email messagE
    #TODO: PLEASE ENTER THE ACCOUND/PASSWORD FROM THE I3 MARKETPLACE	
    account = 'admin'
    topic = ['test_i3']
    pw = 'yrjxn1'

    try:
        pub_client = mqtt.Client(account)
        pub_client.on_connect = on_connect
        pub_client.on_message = on_message
        pub_client.username_pw_set(account, pw)
        pub_client.connect('18.217.227.236', 1883)      #connect to broker [I3 broker address and host number are hard coded here.]
    
    except Exception as e:
        print ("Exception" + str(e))

    #pub_client.subscribe(topic)
    #pub_client.loop_start()

    count = 0
    while count < 100:
        count += 1
        pub_client.publish(topic[0], 'Hello World')
        time.sleep(2)

    pub_client.disconnect()

