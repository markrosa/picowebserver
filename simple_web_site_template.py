from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secret import ssid, password

my_ip = connect_to_wifi(ssid, password)

@server.route("/")
def index(request):
    return render_template("index.html", name="Mark", title="Mark's Personal Blog", content="This is the content")

@server.route("/about")
def index(request):
    return render_template("about.html", name="Mark", title="About this site")

@server.route("/login", ['POST', 'GET'])
def login_form(request):
    print(request.method)
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        
        if username == "rosa" and password == "password":
            return render_template('index.html', title="Welcome", content = f"<h1 class=\"display-5\">Welcome back, {username}</h1>")
        else:
            return render_template('index.html', title="Not logged in", content = "Invalid username or password")

@server.catchall()
def my_catchall(request):
    return "No matching route", 404

logging.info("Started Webserver on IP-Address: ", my_ip)

server.run()

