
import tkinter as tk

# Window setup
root = tk.Tk()
root.title("Achal tera rahe maa")
root.geometry("800x450")
root.configure(bg="#3838d8")

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
    ("aAchal  tera  rahe  maa...:","#fd1307"),
    ("Rang  biranga ho....:","#f2750e"),
    ("Ucha asma se ....:","#f3ae0e"),
    ("Tera tiranda......","#f3ae0e"),
    ("Jeene ki ezazt de de ....:","#eef94f"),
    ("ya hukm sahadat de de ....:","#f2750e"),
    ("Mamjoor  hame ....:","#82f94f"),
    ("Jo bhi tu chune...","#2181a8"),

]
    

line = 0
char = 0
# timing setting
char_delay = 10
line_delay = 10000

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
            root.after(50, animate)
        else:
            text.insert("end", "\n")
            line += 1
            char = 0
            root.after(250, animate)

animate()
root.mainloop()