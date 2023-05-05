from phew import logging, server, connect_to_wifi
from secret import ssid, password

my_ip = connect_to_wifi(ssid, password)

def index(request):
    response = "Hello World"
    return response

server.add_route('/', index, methods=['GET'])


logging.info("Started Webserver on IP-Address: ", my_ip)

server.run()
