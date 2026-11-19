import tkinter as tk, html
from tkinter import filedialog
r = tk.Tk(); r.title("Create book app — Strowke Studio")
pages = [""]; cur = [0]
top = tk.Frame(r); top.pack(fill="x")
title = tk.StringVar(value="Моя книга")
tk.Entry(top, textvariable=title, font=("Segoe UI", 14)).pack(side="left", fill="x", expand=True, padx=4, pady=4)
lbl = tk.Label(top, text="Стр. 1/1"); lbl.pack(side="right", padx=6)
t = tk.Text(r, width=80, height=26, font=("Georgia", 13), wrap="word"); t.pack(padx=4, pady=4)
def store(): pages[cur[0]] = t.get("1.0", "end-1c")
def show(i):
    store(); cur[0] = i; t.delete("1.0", "end"); t.insert("1.0", pages[i]); lbl.config(text=f"Стр. {i+1}/{len(pages)}")
def add(): store(); pages.append(""); show(len(pages) - 1)
def nav(d):
    n = cur[0] + d
    if 0 <= n < len(pages): show(n)
def export():
    store(); f = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML", "*.html")])
    if not f: return
    body = "".join("<section><p>" + html.escape(p).replace("\n", "<br>") + "</p><hr></section>" for p in pages)
    h = html.escape(title.get())
    open(f, "w", encoding="utf-8").write(f"<meta charset='utf-8'><title>{h}</title><body style='font:18px Georgia;max-width:640px;margin:auto'><h1>{h}</h1>{body}")
bar = tk.Frame(r); bar.pack()
for tx, f in [("← Назад", lambda: nav(-1)), ("Вперёд →", lambda: nav(1)), ("Новая страница", add), ("Экспорт в HTML", export)]:
    tk.Button(bar, text=tx, command=f).pack(side="left", padx=3, pady=4)
r.mainloop()
