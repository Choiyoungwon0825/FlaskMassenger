from flask import Flask, render_template,url_for, redirect, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/friends")
def friends():
    return render_template('friends.html')

@app.route("/chats")
def chats():
    return render_template('chats.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')