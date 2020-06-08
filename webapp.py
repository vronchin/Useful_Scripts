from flask import Flask, redirect, url_for,render_template, send_from_directory, request, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello {}!".format(request.cookies.get("name"))

@app.route("/whoiswho")
def whoiswho():
    return render_template("whoiswho.html")

@app.route("/sayhello", methods = ["POST"])
def sayhello():
    resp = make_response(render_template("sayhello.html", nm = request.form["nm"], age = int(request.form["age"]), gender =  request.form["gender"]))
    resp.set_cookie("name",  request.form["nm"])
    return resp

@app.route("/goodbye/<name>")
@app.route("/goodbye/<name>/<lang>")
def goodbye(name, lang="en"):
    if lang=="fr" :
        return "<html><body><h1>Salut {}!</h1><p>Moi c'est Christophe.</p></body></html>".format(name)
    else :
        return render_template("goodbye.html", nm= name)

@app.route("/img/<filename>")
def send_image(filename):
    return send_from_directory("img",filename)

@app.route("/add/<int:number1>/<int:number2>", methods = ["POST", "PUT"])
def addroute(number1, number2):
    if number1 == 42 or number2 == 42 :
        return redirect(url_for("goodbye", name= "Christophe", lang="fr"))
    else :
        return str(number1 + number2)        

if __name__ == '__main__':
   app.run("0.0.0.0",debug = True)