import tkinter as tk
    

def snake():
    import snake.py

def minesweeper():
    from nachomines.scripts.main import run
    if __name__ == "__main__":
        run()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Snake",
                   command= snake)
slogan.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Minesweeper",
                   command= minesweeper)
slogan.pack(side=tk.LEFT)
root.mainloop()