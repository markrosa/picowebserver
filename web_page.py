from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password
from machine import Pin
from examples import blinker, audi_blinker, audi_blinker2, audi_blinker3, vierfarben_audiblinker, all_colors, rotate_right, move_right_left, gradient_bounce, one_pixel
from examples import red, orange, yellow, green, blue, indigo, violet, pink, dark_pink, alternative_pink, other_color

my_ip = connect_to_wifi(ssid, password)


led = Pin("LED", Pin.OUT)
led.off()
mode_text = "OFF"

@server.route("/")
def index(request):
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)


@server.route("/ledon")
def index(request):
    # LED anschalten
    mode_text = "LED ON"
    led.on()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/ledoff")
def index(request):
    # LED ausschalten
    mode_text = "LED OFF"
    led.off()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/blinker")
def index(request):
    mode_text = "Blinker"
    blinker()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/audi_blinker")
def index(request):
    mode_text = "Audi Blinker"
    audi_blinker()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/audi_blinker2")
def index(request):
    mode_text = "Audi Blinker 2"
    audi_blinker2()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/audi_blinker3")
def index(request):
    mode_text = "Audi Blinker 3"
    audi_blinker3()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/vierfarben_audiblinker")
def index(request):
    mode_text = "4-farbiger Audi Blinker"
    vierfarben_audiblinker()
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/all_colors")
def index(request):
    mode_text = "Alle Farben"
    all_colors(5, 25, (red, orange, yellow, green, blue, indigo, violet))
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/rotate_right")
def index(request):
    mode_text = "Rotieren nach rechts"
    rotate_right(10, 20, blue, red)
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/move_right_left")
def index(request):
    mode_text = "rechts links bewegen"
    move_right_left(12, 18, blue, red)
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/gradient_bounce")
def index(request):
    mode_text = "Farbverlaufs-Wippe"
    gradient_bounce(30, 7, red, blue)
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)

@server.route("/one_pixel")
def index(request):
    mode_text = "ein pixel"
    one_pixel(10, 20)
    return render_template("index.html", name="Mark Rosa", title="Lichterkettensteuerung", MODE=mode_text)



@server.route("/about")
def index(request):
    return render_template("about.html", name="Mark Rosa", title="About this site")

# @server.route("/login", ['POST', 'GET'])
# def login_form(request):
#     print(request.method)
#     if request.method == 'GET':
#         return render_template("login.html")
#     if request.method == 'POST':
#         username = request.form.get("username", None)
#         password = request.form.get("password", None)
#         
#         if username == "rosa" and password == "password":
#             return render_template('index.html', title="Welcome", content = f"<h1 class=\"display-5\">Welcome back, {username}</h1>")
#         else:
#             return render_template('index.html', title="Not logged in", content = "Invalid username or password")

@server.catchall()
def my_catchall(request):
    return "No matching route", 404

logging.info("Started Webserver on IP-Address: ", my_ip)

server.run()



