from hashlib import md5

from flask import Flask, session, redirect, request, render_template, flash

app = Flask(__name__)
app.secret_key = b"0281d0fffc15671ac249d70d0bff1604be91bba08d28c74a2f3473b1286455c3"

FAKE_USERDB = {
    "admin": "482c811da5d5b4bc6d497ffa98491e38" #md5 "password123"
}

@app.route("/")
def index():
    if "username" in session:
        return redirect("/admin/")
    else:
        return redirect("/login/")

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in FAKE_USERDB:
            pwsum = md5(password.encode("UTF-8")).hexdigest()
            if pwsum == FAKE_USERDB[username]:
                session["username"] = username
                return redirect("/admin/")
    
    return render_template("login.html")

@app.route("/admin/")
def admin():
    if "username" not in session:
        return redirect("/login/")
    return "ZFun{DONT_use_W3AK_PASSW0RD}"
