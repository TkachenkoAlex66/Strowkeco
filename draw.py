import tkinter as tk
from tkinter import colorchooser, filedialog
r = tk.Tk(); r.title("Draw drawing — Strowke Studio")
col = ["#000000"]; size = tk.IntVar(value=4)
bar = tk.Frame(r); bar.pack(fill="x")
c = tk.Canvas(r, width=900, height=560, bg="white"); c.pack()
def pick():
    x = colorchooser.askcolor()[1]
    if x: col[0] = x
def eraser(): col[0] = "white"
def save():
    f = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript", "*.ps")])
    if f: c.postscript(file=f, colormode="color")
last = [None]
def move(e):
    if last[0]: c.create_line(*last[0], e.x, e.y, fill=col[0], width=size.get(), capstyle="round")
    last[0] = (e.x, e.y)
c.bind("<B1-Motion>", move); c.bind("<ButtonRelease-1>", lambda e: last.__setitem__(0, None))
for t, f in [("Цвет", pick), ("Ластик", eraser), ("Очистить", lambda: c.delete("all")), ("Сохранить", save)]:
    tk.Button(bar, text=t, command=f).pack(side="left", padx=3, pady=3)
tk.Scale(bar, from_=1, to=40, orient="horizontal", variable=size, label="Размер").pack(side="left")
r.mainloop()
