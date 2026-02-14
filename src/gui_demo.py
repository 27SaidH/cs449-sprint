import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Sprint 0 GUI Demo")
    root.geometry("420x260")

    # TEXT
    title = tk.Label(root, text="Solitaire Sprint #0 GUI Demo", font=("Arial", 14))
    title.pack(pady=10)

    # LINE (Canvas)
    canvas = tk.Canvas(root, width=380, height=20)
    canvas.pack()
    canvas.create_line(10, 10, 370, 10, width=2)

    # CHECKBOX
    sound_var = tk.BooleanVar(value=True)
    chk = tk.Checkbutton(root, text="Enable sound", variable=sound_var)
    chk.pack(pady=10)

    # RADIO BUTTONS
    difficulty_var = tk.StringVar(value="Normal")
    tk.Label(root, text="Difficulty:").pack()

    rb_frame = tk.Frame(root)
    rb_frame.pack(pady=5)

    tk.Radiobutton(rb_frame, text="Easy", value="Easy", variable=difficulty_var).pack(side="left", padx=10)
    tk.Radiobutton(rb_frame, text="Normal", value="Normal", variable=difficulty_var).pack(side="left", padx=10)
    tk.Radiobutton(rb_frame, text="Hard", value="Hard", variable=difficulty_var).pack(side="left", padx=10)

    # small status text so the UI looks "alive"
    status = tk.Label(root, text="(Take a screenshot of this window running.)")
    status.pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    main()
