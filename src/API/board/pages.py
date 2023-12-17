from flask import Blueprint, render_template, jsonify, current_app

blueprint = Blueprint("pages", __name__)
words = {}

def setWords(newValue : dict):
    global words
    words = newValue

@blueprint.route("/vocab")
def words():
    return jsonify(words)

@blueprint.route("/")
def home():
    return render_template("pages/home.html")

@blueprint.route("/play")
def play():
    return render_template("pages/play.html")