# Eric "Morty" Lau, Junhee Lee
# SoftDev1 pd1
# K16 -- Oh yes, perhaps I do…
# 2019-10-03

from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = "Test_Key"

team_name = "Plumbus"
roster = "Eric \"Morty\" Lau and Junhee Lee"

username = "user"
password = "passwd"

@app.route("/", methods=["GET"])
def root():
    if not 'login' in session:
        session['login'] = False 
    if(session['login']):
        return redirect(url_for("welcome"))
    else:
        return render_template(
            "landing.html",
            team = team_name,
            names = roster,
            title = "Login Page"
            )

@app.route("/welcome")
def welcome():
    return render_template(
            "response.html",
            team = team_name,
            names = roster,
            # username = request.args['username'],
            username = session['user'],
            method = request.method,
            url = url_for("logout"),
            title = "Welcome Page"
    )

@app.route("/auth", methods=["POST"])
def auth():
	# print("this is the app name", app, end="\n")
	# print("this is the request", request, end="\n")
	# print("this is the request headers", request.headers)
	# print("this is the request method", request.method, end="\n")
	# print("this is the request args", request.args, end="\n")
	# print("this is the request form", request.form, end="\n")
    if(request.form['username'] != username):
        flash("Failed login!")
        session['reason'] = 'username'
        return redirect(url_for("failure"))
    elif(request.form['password'] != password):
        flash("Failed login!")
        session['reason'] = "password"
        return redirect(url_for("failure"))
    else:
        session['login'] = True
        session['user'] = request.form['username']
        flash("You have successfully logged in!")
        return redirect(url_for("welcome"))


@app.route("/failure")
def failure():
    print("bad login")
    return render_template(
        "fail.html",
        reason = session['reason'],
        team = team_name,
        names = roster,
        title = "Bad Login"
    )

@app.route("/logout")
def logout():
    flash("You have successfully logged out!")
    session['login'] = False
    return redirect("/")
    
if __name__ == "__main__":
	app.debug = True
	app.run()
