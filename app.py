from flask import Flask, render_template, send_from_directory, redirect, abort
import os
BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=BASE)
REL = "https://github.com/TkachenkoAlex66/Strowkeco/releases/latest/download/"

APPS = [
 {"id": "engine", "file": "StrowkeEngine.exe", "title": "Create game on Strowke Engine",
  "by": "Strowke Engine", "desc": "Редактор уровней: расставляйте стены, монеты и игрока, затем сразу запускайте тест."},
 {"id": "snake3d", "file": "Snake3D.exe", "title": "Snake 3D",
  "by": "Strowke Studio", "desc": "Классическая змейка в изометрическом 3D. Стрелки — управление, R — рестарт."},
 {"id": "draw", "file": "DrawDrawing.exe", "title": "Draw drawing",
  "by": "Strowke Studio", "desc": "Простой редактор рисунков: кисть, ластик, цвета, сохранение."},
 {"id": "book", "file": "CreateBook.exe", "title": "Create book app",
  "by": "Strowke Studio", "desc": "Пишите книгу по страницам и экспортируйте её в HTML."},
]

@app.route("/")
def index():
    for a in APPS:
        a["ready"] = True
        a["size"] = ""
    return render_template("index.html", apps=APPS)

@app.route("/style.css")
def css():
    return send_from_directory(BASE, "style.css")

@app.route("/download/<name>")
def download(name):
    if name not in {a["file"] for a in APPS}:
        abort(404)
    return redirect(REL + name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
