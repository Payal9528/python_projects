import tkinter as tk

# Window setup
root = tk.Tk()
root.title("python animation :")
root.geometry("800x450")
root.configure(bg="#0e0e1a")

# Text widget
text = tk.Text(
    root,
    font=("Consolas", 18),
    bg="#0e0e1a",
    bd=0,
    wrap="word"
)
text.pack(padx=30, pady=30)

# Content for animation
content = [
    ("PPython is one of the most powerful", "#f45a0c"),
    ("and easy programming languages. So python is perfect for beginners", "#b5d41c"),
    ("simple rules","#a6e3e9"),
    ("Easy logic:","#a6e3e9"),
    ("Show clear error massages:","#a6e3e9"),
    ("", "white"),

    ("Why Python is EASY?", "#f9c74f"),
    ("• Simple English-like syntax", "#b5e48c"),
    ("• Easy to learn for beginners", "#b5e48c"),
    ("", "white"),

    ("Why Python is POWERFUL?", "#f9844a"),
    ("• Used in AI & Machine Learning", "#ffd6a5"),
    ("• Used in Websites & Apps", "#ffd6a5"),
    ("• Used in Automation", "#ffd6a5"),
    ("", "white"),

    ("Example Python Code:", "#ffafcc"),
    ("def add(a, b):", "#cdb4db"),
    ("    return a + b", "#bde0fe"),
    ("print(add(5, 3))", "#bde0fe"),
    ("", "white"),

    ("Python is used in:", "#f4710d"),
    ("• Google", "#caf0f8"),
    ("• Instagram", "#caf0f8"),
    ("• YouTube", "#caf0f8"),
    ("• AI, Data Science, Games", "#caf0f8"),
]

line = 0
char = 0

def animate():
    global line, char

    if line < len(content):
        text_line, color = content[line]

        if char <= len(text_line):
            text.delete("end-1c linestart", "end-1c")
            text.insert("end", text_line[:char])
            text.tag_add(str(line), "end-%dc" % char, "end")
            text.tag_config(str(line), foreground=color)
            char += 1
            root.after(45, animate)
        else:
            text.insert("end", "\n")
            line += 1
            char = 0
            root.after(250, animate)

animate()
root.mainloop()