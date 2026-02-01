import tkinter as tk
import random
import winsound

# ---------------- CONFIG ----------------
ROWS = 8
COLS = 8
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
BLOCK_SIZE = 50

score = 0
level = 1
target = 200

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("🔥 REAL BLOCK BLAST 🔥")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=COLS * BLOCK_SIZE,
    height=ROWS * BLOCK_SIZE + 80,
    bg="#1b1b2f"
)
canvas.pack()

# ---------------- GRID ----------------
grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]

# ---------------- UI ----------------
info = canvas.create_text(
    COLS * BLOCK_SIZE // 2,
    ROWS * BLOCK_SIZE + 30,
    fill="white",
    font=("Arial", 14, "bold"),
    text=""
)

# ---------------- FUNCTIONS ----------------
def play_sound(freq=800, dur=120):
    winsound.Beep(freq, dur)

def draw_grid():
    canvas.delete("block")
    for r in range(ROWS):
        for c in range(COLS):
            color = grid[r][c]
            if color:
                x1 = c * BLOCK_SIZE
                y1 = r * BLOCK_SIZE
                x2 = x1 + BLOCK_SIZE
                y2 = y1 + BLOCK_SIZE
                canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="black",
                    tags="block"
                )
    canvas.itemconfig(
        info,
        text=f"Score: {score}   Level: {level}   Target: {target}"
    )

def find_group(r, c, color, visited):
    if (r, c) in visited:
        return []
    if r < 0 or c < 0 or r >= ROWS or c >= COLS:
        return []
    if grid[r][c] != color:
        return []

    visited.add((r, c))
    group = [(r, c)]

    group += find_group(r+1, c, color, visited)
    group += find_group(r-1, c, color, visited)
    group += find_group(r, c+1, color, visited)
    group += find_group(r, c-1, color, visited)

    return group

def apply_gravity():
    for c in range(COLS):
        stack = []
        for r in range(ROWS):
            if grid[r][c]:
                stack.append(grid[r][c])
        for r in range(ROWS-1, -1, -1):
            grid[r][c] = stack.pop() if stack else random.choice(COLORS)

def click(event):
    global score, level, target

    c = event.x // BLOCK_SIZE
    r = event.y // BLOCK_SIZE

    if r >= ROWS or c >= COLS:
        return

    color = grid[r][c]
    if not color:
        return

    visited = set()
    group = find_group(r, c, color, visited)

    if len(group) >= 2:
        play_sound()
        score += len(group) * 10

        for x, y in group:
            grid[x][y] = None

        apply_gravity()

        if score >= target:
            level += 1
            target += 200
            play_sound(1200, 300)

        draw_grid()

# ---------------- BIND ----------------
canvas.bind("<Button-1>", click)
draw_grid()

root.mainloop()                                                                                                                                