from flask import Flask, render_template, request, send_file
import ssl

from nogi import nogi
from sakura import sakura
from hinata import hinata

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask("BlogScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Nogizaka")
def toNogi():
    link = request.args.get("link","")
    if link:
        blog = nogi(link)
        return render_template("links.html", blog=blog)
    return render_template("nogi.html")

@app.route("/Sakurazaka")
def toSakura():
    link = request.args.get("link","")
    if link:
        blog = sakura(link)
        return render_template("links.html", blog=blog)
    return render_template("sakura.html")

@app.route("/Hinatazaka")
def toHinata():
    link = request.args.get("link","")
    if link:
        blog = hinata(link)
        return render_template("links.html", blog=blog)
    return render_template("hinata.html")

app.run(debug=True)