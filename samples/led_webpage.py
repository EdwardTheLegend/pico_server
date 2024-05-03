import pico_server
from machine import Pin

# declare the internal LED pin
led = Pin("LED", Pin.OUT)

# create the server and connect the server to wifi
server = pico_server.Server()
server.connect_wifi("SSID", "password")

# custom webpage functions
# each function will be called when a certain path is requested from the server
# the return value of the function will be sent to the client


def led_on():
    led.on()
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <div style="display: flex; height: 100vh; width: 100vw;">
    <a href="/ledoff"><button>Off</button></a>
    </div>
    </body>
    </html>
    """


def led_off():
    led.off()
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <div style="display: flex; height: 100vh; width: 100vw;">
    <a href="/ledon"><button>On</button></a>
    </div>
    </body>
    </html>
    """


def my_homepage():
    return "This is my homepage"


# link the page functions to specific path
server.page_add(
    "/", my_homepage
)  # <- NB: my_homepage, not my_homepage(). We are passing the function as an object not executing it right away
server.page_add("/ledon", led_on)
server.page_add("/ledoff", led_off)

# run the server
try:
    print("Press Ctrl+C in the Shell to stop the server")
    server.start()
except KeyboardInterrupt as e:
    pass

# cleanup connections
server.disconnect_wifi()
