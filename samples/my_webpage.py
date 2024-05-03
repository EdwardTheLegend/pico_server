import pico_server

server = pico_server.Server()
server.connect_wifi("SSID", "password")


def my_homepage():
    return "This is my homepage"


server.page_add("/", my_homepage)
server.start()
