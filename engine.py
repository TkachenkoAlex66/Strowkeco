import tkinter as tk, json
from tkinter import filedialog
W, H, T = 24, 16, 30
grid = [[0] * W for _ in range(H)]  # 0 пусто, 1 стена, 2 монета, 3 игрок
COL = {1: "#6b7a90", 2: "#ffc233", 3: "#4f7bff"}
tool = [1]; play = {"on": False, "backup": None}
r = tk.Tk(); r.title("Strowke Engine — Create game")
c = tk.Canvas(r, width=W * T, height=H * T, bg="#14202e"); c.pack()
def draw():
    c.delete("all")
    for y in range(H):
        for x in range(W):
            v = grid[y][x]
            if v == 1: c.create_rectangle(x*T, y*T, x*T+T, y*T+T, fill=COL[1], outline="")
            elif v: c.create_oval(x*T+6, y*T+6, x*T+T-6, y*T+T-6, fill=COL[v])
    if play["on"]: c.create_text(8, 8, anchor="nw", fill="white", text=f"Монет осталось: {sum(row.count(2) for row in grid)}")
def paint(e):
    if play["on"]: return
    x, y = e.x // T, e.y // T
    if 0 <= x < W and 0 <= y < H:
        if tool[0] == 3:
            for row in grid: row[:] = [0 if v == 3 else v for v in row]
        grid[y][x] = tool[0]; draw()
c.bind("<Button-1>", paint); c.bind("<B1-Motion>", paint)
def find():
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 3: return x, y
def key(e):
    d = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}.get(e.keysym)
    p = find()
    if play["on"] and d and p:
        nx, ny = p[0] + d[0], p[1] + d[1]
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != 1:
            grid[p[1]][p[0]] = 0; grid[ny][nx] = 3; draw()
r.bind("<Key>", key)
def toggle():
    play["on"] = not play["on"]; b.config(text="Стоп" if play["on"] else "Тест ▶")
    if play["on"]: play["backup"] = json.dumps(grid)
    else: grid[:] = json.loads(play["backup"])
    draw()
def save():
    f = filedialog.asksaveasfilename(defaultextension=".json")
    if f: json.dump(grid, open(f, "w"))
def load():
    f = filedialog.askopenfilename()
    if f: grid[:] = json.load(open(f)); draw()
bar = tk.Frame(r); bar.pack()
for n, v in [("Стёрка", 0), ("Стена", 1), ("Монета", 2), ("Игрок", 3)]:
    tk.Button(bar, text=n, command=lambda v=v: tool.__setitem__(0, v)).pack(side="left", padx=3, pady=4)
b = tk.Button(bar, text="Тест ▶", command=toggle); b.pack(side="left", padx=8)
tk.Button(bar, text="Сохранить", command=save).pack(side="left"); tk.Button(bar, text="Открыть", command=load).pack(side="left")
draw(); r.mainloop()
