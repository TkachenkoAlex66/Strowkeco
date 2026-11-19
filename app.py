from flask import Flask, render_template, send_from_directory, abort
import os
BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=BASE)

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
        p = os.path.join(BASE, a["file"])
        a["ready"] = os.path.exists(p)
        a["size"] = f"{os.path.getsize(p)/1048576:.1f} МБ" if a["ready"] else ""
    return render_template("index.html", apps=APPS)

@app.route("/style.css")
def css():
    return send_from_directory(BASE, "style.css")

@app.route("/download/<name>")
def download(name):
    if name not in {a["file"] for a in APPS} or not os.path.exists(os.path.join(BASE, name)):
        abort(404)
    return send_from_directory(BASE, name, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
