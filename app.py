import os, urllib, json, random
from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

fromaddr = 'hclwebcam47@gmail.com'
toaddrs  = 'ziv.epstein@yale.edu'
msg = 'There was a terrible error that occured and I wanted you to know!'
username = 'hclwebcam47'
password = 'cooperation47'


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/<idnum>", methods=['POST', 'GET'])
def hello(idnum):
    return render_template('index.html', myID = idnum)

@app.route("/upload/<idnum>", methods=['POST', 'GET'])
def upload(idnum):
    return "good"

@app.route("/go/end")
def goodbye():
    return render_template('end.html')

if __name__ == '__main__':
    app.run()