
   

import turtle as tl
import tkinter as tk
import math

root = tk.Tk()
root.title("Colorful Scientific Calculator")
root.geometry("350x450")
root.config(bg="#2c504b")
root.resizable(False, False)

expression = ""

# Entry box
entry = tk.Entry(
    root,
    font=("Arial", 22),
    bg="#ececf1",
    fg="black",
    bd=10,
    justify="right"
)
entry.pack(fill=tk.X, padx=10, pady=15)

# Functions
def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def equal():
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

def square():
    global expression
    try:
        result = float(expression) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def sqrt():
    global expression
    try:
        result = math.sqrt(float(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def sin():
    global expression
    result = math.sin(math.radians(float(expression)))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    expression = str(result)

def cos():
    global expression
    result = math.cos(math.radians(float(expression)))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    expression = str(result)

def tan():
    global expression
    result = math.tan(math.radians(float(expression)))
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    expression = str(result)

# Button frame
frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

def btn(text, row, col, cmd, color):
    tk.Button(
        frame,
        text=text,
        width=6,
        height=2,
        font=("Arial", 12, "bold"),
        bg=color,
        fg="white",
        bd=0,
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

# Number & operator buttons
btn("7",1,0, lambda: press("7"), "#34495e")
btn("8",1,1, lambda: press("8"), "#34495e")
btn("9",1,2, lambda: press("9"), "#34495e")
btn("/",1,3, lambda: press("/"), "#e67e22")

btn("4",2,0, lambda: press("4"), "#34495e")
btn("5",2,1, lambda: press("5"), "#34495e")
btn("6",2,2, lambda: press("6"), "#34495e")
btn("*",2,3, lambda: press("*"), "#e67e22")

btn("1",3,0, lambda: press("1"), "#34495e")
btn("2",3,1, lambda: press("2"), "#34495e")
btn("3",3,2, lambda: press("3"), "#34495e")
btn("-",3,3, lambda: press("-"), "#e67e22")

btn("0",4,0, lambda: press("0"), "#34495e")
btn(".",4,1, lambda: press("."), "#34495e")
btn("=",4,2, equal, "#27ae60")
btn("+",4,3, lambda: press("+"), "#e67e22")

# Scientific buttons
btn("√",5,0, sqrt, "#9b59b6")
btn("x²",5,1, square, "#9b59b6")
btn("sin",5,2, sin, "#2980b9")
btn("cos",5,3, cos, "#2980b9")
btn("tan",6,0, tan, "#2980b9")
btn("C",6,1, clear, "#c0392b")


root.mainloop()