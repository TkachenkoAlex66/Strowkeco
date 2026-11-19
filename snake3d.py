import tkinter as tk, random
N, S = 14, 22
class Game:
    def __init__(s):
        s.r = tk.Tk(); s.r.title("Snake 3D — Strowke Studio")
        s.c = tk.Canvas(s.r, width=700, height=520, bg="#0e1622"); s.c.pack()
        s.r.bind("<Key>", s.key); s.reset(); s.tick(); s.r.mainloop()
    def reset(s):
        s.snake = [(5, 7), (4, 7), (3, 7)]; s.d = (1, 0); s.nd = s.d; s.score = 0; s.dead = False; s.food()
    def food(s):
        while True:
            s.f = (random.randrange(N), random.randrange(N))
            if s.f not in s.snake: return
    def key(s, e):
        m = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}
        if e.keysym in m and (m[e.keysym][0] + s.d[0], m[e.keysym][1] + s.d[1]) != (0, 0): s.nd = m[e.keysym]
        if e.keysym.lower() == "r": s.reset()
    def iso(s, x, y): return 350 + (x - y) * S, 60 + (x + y) * S // 2
    def cube(s, x, y, h, col, side):
        px, py = s.iso(x, y); py -= h; w, t = S, S // 2
        s.c.create_polygon(px, py, px + w, py + t, px, py + 2 * t, px - w, py + t, fill=col, outline="#0e1622")
        s.c.create_polygon(px - w, py + t, px, py + 2 * t, px, py + 2 * t + h, px - w, py + t + h, fill=side, outline="#0e1622")
        s.c.create_polygon(px + w, py + t, px, py + 2 * t, px, py + 2 * t + h, px + w, py + t + h, fill=side, outline="#0e1622")
    def tick(s):
        if not s.dead:
            s.d = s.nd; hx, hy = s.snake[0]; n = (hx + s.d[0], hy + s.d[1])
            if not (0 <= n[0] < N and 0 <= n[1] < N) or n in s.snake: s.dead = True
            else:
                s.snake.insert(0, n)
                if n == s.f: s.score += 1; s.food()
                else: s.snake.pop()
        s.draw(); s.r.after(max(60, 150 - s.score * 4), s.tick)
    def draw(s):
        s.c.delete("all")
        for x in range(N):
            for y in range(N): s.cube(x, y, 0, "#1b2a40" if (x + y) % 2 else "#223450", "#14202e")
        items = [(s.f, "#ff7a2f", "#c2541a")] + [(p, "#4f7bff" if i else "#9ab4ff", "#2f5bff") for i, p in enumerate(s.snake)]
        for (x, y), c, sd in sorted(items, key=lambda i: i[0][0] + i[0][1]): s.cube(x, y, 14, c, sd)
        s.c.create_text(10, 10, anchor="nw", fill="white", font=("Segoe UI", 14), text=f"Счёт: {s.score}")
        if s.dead: s.c.create_text(350, 40, fill="#ff7a2f", font=("Segoe UI", 20, "bold"), text="Игра окончена — нажмите R")
Game()
