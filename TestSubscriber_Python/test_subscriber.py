import paho.mqtt.client as mqtt
import base64
from PIL import Image  
import pygame 
import time


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MQTT Subscriber')
  
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 


im = None

img_received = False

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("username/feeds/camera")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("received message")
    print(msg.topic)
    message = msg.payload
    print(type(message))

    print(message)

    with open("imageToSave.jpg", "wb") as fh:
        fh.write(base64.decodebytes(message))

    global img_received
    img_received = True
    # if im is not None:
    #     im.close()
    # im = Image.open(r"imageToSave.jpg")  
    # im.show() 
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set(username="mqtt_username",password="mqtt_password")
client.connect("io.adafruit.com", 1883, 60)
# client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()

while True:
    # print("in loop")
    time.sleep(0.1)

    try:
    	if img_received:
	        print("Image received")
	        img_received = False
	        carImg = pygame.image.load("imageToSave.jpg")
	        gameDisplay.blit(carImg, (0,0))
    except Exception as e:
    	print(e)
    

    pygame.display.update()
