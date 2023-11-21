from flask import Flask, render_template, request, redirect, url_for,session
import mysql.connector
# from mysql import MySql


app = Flask(__name__)
app.secret_key = 'Evolve_design2023!'

#mysql configuration
# mydbcon = mysql.connector.connect(host="localhost", user="root", password="", database="myprofiledb")

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
