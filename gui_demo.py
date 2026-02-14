import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sprint 0 GUI Demo")
root.geometry("500x350")

title = ttk.Label(root, text="Peg Solitaire — Sprint 0 Demo", font=("Arial", 16))
title.pack(pady=10)

canvas = tk.Canvas(root, width=400, height=150)
canvas.pack()
canvas.create_line(20, 20, 380, 20, width=2)
canvas.create_line(20, 20, 20, 130, width=2)
canvas.create_line(20, 130, 380, 130, width=2)
canvas.create_line(380, 20, 380, 130, width=2)

record_var = tk.BooleanVar()
ttk.Checkbutton(root, text="Record Game", variable=record_var).pack(pady=5)

mode_var = tk.StringVar(value="Manual")
ttk.Label(root, text="Mode:").pack()

frame = ttk.Frame(root)
frame.pack()

ttk.Radiobutton(frame, text="Manual", value="Manual", variable=mode_var).grid(row=0, column=0, padx=10)
ttk.Radiobutton(frame, text="Autoplay", value="Autoplay", variable=mode_var).grid(row=0, column=1, padx=10)

root.mainloop()
