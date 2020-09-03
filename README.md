# ESP32CAM With Adafruit.io

## Dependencies
- Hardware
  - AI Thinker ESP32 CAM
  - USB UART Programmer (CP2102 or FTDI)
- Libraries
  - PubSubClient@2.7

## Contents
- Publish to Adafruit.IO
  - Using Platform IO
  - Using Arduino IDE
- Customizing The Credentials
- Expected Output
- Subscribe to Topic Using Python

## Publish to Adafruit.IO
1. ### Using Platform IO

    In the file platformio.ini, before the library dependencies, add a build flag to modify the MQTT Packet Size to the required size. The default packet size defined in PubSubClient Library is 128 Bytes. It's increased to 36000 Bytes inorder to satisfy the requirements.

    ```ini
    build_flags = -DMQTT_MAX_PACKET_SIZE=36000

    lib_deps =
    PubSubClient@2.7
    ```
    For additional information, go to [Platform IO build_flags](https://docs.platformio.org/en/latest/projectconf/section_env_build.html#build-flags).

2. ### Using Arduino IDE

    Install the PubSubClient Library from Tools -> Manage Libraries. We used the 2.7 version of the same. After installing the library go to the directory of Libraries related to Arduino, and navigate to PubSubClient Library.

    * #### In Linux
        ```bash
        user@user:~/Arduino/libraries/PubSubClient$ pwd
        /home/user/Arduino/libraries/PubSubClient
        ```
    * #### In Windows
    
        Navigate to `user/Documents/Arduino/libraries/PubSubClient`

    Go to PubSubClient.h residing in the src folder, Find the following codeblock.

    ```cpp
    // MQTT_MAX_PACKET_SIZE : Maximum packet size
    #ifndef MQTT_MAX_PACKET_SIZE
    #define MQTT_MAX_PACKET_SIZE 128
    #endif
    ```
    And modify according to requirements.

    ```cpp
    // MQTT_MAX_PACKET_SIZE : Maximum packet size
    #ifndef MQTT_MAX_PACKET_SIZE
    #define MQTT_MAX_PACKET_SIZE 36000
    #endif
    ```

## Adding The Credentials

In the main.cpp file (If Arduino IDE, ESP32Cam_MQTT.ino),

1. #### Replace the variables with your SSID/Password combination

    ```cpp
    const char *ssid = "WiFi_SSID";
    const char *password = "WiFi_Password";
    ```

2. #### Add MQTT Credentials.
   
   ```cpp
   const char *mqtt_server = "io.adafruit.com";
   const char *mqtt_clientid = "mqtt_clientid";
   const char *mqtt_username = "mqtt_username";
   const char *mqtt_password = "mqtt_password";
   const char *mqtt_publish_topic = "username/feeds/camera";
   ```
   - Replace mqtt_clientid with a unique random id.
   - Replace mqtt_username with the Adafruit Username.
   - Replace mqtt_password with the Adafruit AIO Key.

## Expected Output

```bash
Connecting to Dhanish
.......
WiFi connected
IP address: 
192.168.1.5
Attempting MQTT connection...connected
Camera Captured
Buffer Length: 
22008
Publishing...Published
Camera Captured
Buffer Length: 
21960
Publishing...Published

...
```

## Subscribe to Topic Using Python

A basic python code to subscribe to the topic `username/feeds/camera` and updates realtime.

#### Requirements:
- Python3
- Paho MQTT Client
- PIL (Python Imaging Library)
- PyGame

## Adding Credentials

1. #### Subscribe to Camera Topic in the `on_connect` function,
    ```python
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("username/feeds/camera")
    ```

2. #### Replace MQTT Credentials,
    ```python
    client.username_pw_set(username="mqtt_username",password="mqtt_password"
    client.connect("io.adafruit.com", 1883, 60)
    ```

3. #### Run using python3
    ```bash
    python3 test_subscriber.py 
    ```



