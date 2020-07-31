from tkinter import *

def main():
    root = Tk()
    root.grid_rowconfigure(1, weight=1)


    canvas = Canvas(root, width=100, height=100, bg="gray")
    canvas.place(relx=0.5, rely=0.0 , relwidth=1, relheight=1)

    root.mainloop()


if __name__ == '__main__':
    main()
