from phew import connect_to_wifi, logging
from secret import ssid, password



logging.info("trying to connect to wifi")
my_ip = connect_to_wifi(ssid, password)

logging.info("successfully connected; my ip: ", my_ip)

