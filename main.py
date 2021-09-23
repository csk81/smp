import re
from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "queries"


mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("p1.html")


@app.route("/p4.html",methods=["GET","POST"])
def contact():

    if request.method == "POST":
        cur = mysql.connection.cursor()
        req = request.form
        name = req["name"]
        email = str(req["email"])
        contact = req["contactno"]
        message = req["message"]
        cur.execute("INSERT INTO contactus(name,email,contactno,Message) VALUES(%s,%s,%s,%s)",(name,email,contact,message));
        mysql.connection.commit()
        cur.close()
    return render_template("p4.html")


# @app.route("/d.html")
# def display():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM contactus")
#     fetchdata = cur.fetchall()
#     cur.close()
#     return render_template("d.html",data=fetchdata)


@app.route("/adminlogin.html",methods=["GET","POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "admin123":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM contactus")
            fetchdata = cur.fetchall()
            cur.close()
            return render_template("d.html",data=fetchdata)
    return render_template("adminlogin.html")



if __name__ == "__main__":

    app.run(debug=True)