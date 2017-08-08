"""
Author: Jeremiah Lantzer

Last Edit: 7/28/2016 - JL

Overview: This is a test of the capabilities of PostgreSQl
          using python for Project Cauldron.

Goal: I am attempting to create a template that we will be able to use over
      that will allow us to load a portion of a database when a certain
      page has been opened.

Sources: https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
"""

# Imports the API that allows for connection with PostgreSQL
import psycopg2
# load the psycopg extras module
import psycopg2.extras
# Imports the Flask library to allow for connection to the front end
# render_template allows for the opening of HTML files and request will be used for html based operations
from flask import Flask, render_template, request

# allows for the use of the app decorator
app = Flask(__name__)


def dbconn():
    # connString contains the basic connection info of the database
    connstring = 'dbname=Cauldron user=postgres password=elephants25 host=localhost port=5433'
    print connstring

    try:
        # tries to connect to the database according to info in the connString above^
        return psycopg2.connect(connstring)

    except:
        # If it fails an error message is printed
        # Could use this for possible recursive connection
        print "Can't connect to database"


"""
dbmain() shall receive different parameters according to the page that is being called
so that the proper section of the database shall be called and the proper information is received
"""


def dbmain(querystring):
    # sets a variable to connect to the Database
    conn = dbconn()

    # executes a query
    try:
        # Defines a cursor to work with
        cur = conn.cursor()
        cur.execute(querystring)
        # All results from the query are stored in the list, rows
        rows = cur.fetchall()
        return rows

    except:
        print "Error executing select"


def dbprint(rows):
    # Displays the results of the query in the console

    if rows is not None:
        print "\nShow me the databases:\n"
        for row in rows:
            print "   ", row[0]


@app.route("/")
def home1():
    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # TODO: Display the amount of schools on index.html

    # prints the information received to the console
    dbprint(rows)

    return render_template("front-page.html", schoolnum=rows)  #


@app.route("/index.html", methods=['POST', 'GET'])
def home2():
    email1 = request.form['email']
    print email1

    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # TODO: Display the amount of schools on index.html

    # prints the information received to the console
    dbprint(rows)

    return render_template("index.html")


@app.route("/about.html")
def about():
    # TODO: change about us in HTML file

    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # prints the information received to the console
    dbprint(rows)

    return render_template("about.html")


@app.route("/me.html")
def me():
    # TODO: Retrieve specific profile information

    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # prints the information received to the console
    dbprint(rows)

    return render_template("me.html")


@app.route("/network.html")
def network():
    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # prints the information received to the console
    dbprint(rows)

    return render_template("network.html")


@app.route("/projects.html")
def projects():
    # TODO: Retrieve project information

    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # prints the information received to the console
    dbprint(rows)

    return render_template("projects.html")


@app.route("/Login.html")
def login():
    # TODO: Store login information in Database

    # receives all information and connects to the database
    rows = dbmain("Querystring")  # TODO: add query string to each dbmain that needs it

    # prints the information received to the console
    dbprint(rows)

    return render_template("Login.html")


@app.route("/signup.html")
def signup():
    # TODO: Store signup information in database

    # # connects to the DB: trying new position to stop crashing
    conn = dbconn()
    # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""INSERT INTO students (school_email, password)
                    VALUES (%s, %s);""",
                    (request.form['email'], request.form['pass']))
    except:
        print "Error inserting into database"
        conn.rollback()

    conn.commit()

    return render_template("signup.html")


if __name__ == "__main__":
    app.run()
