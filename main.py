import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageFont
from PIL import ImageDraw

my_w = tk.Tk()
my_w.geometry("800x800")  # Size of the window
my_w.title('Add Watermarker in image')
my_font1 = ('times', 18, 'bold')
frame = Frame(my_w, bg='#FF0000')

l1 = tk.Label(my_w, text='Add Watermark on your images', width=30, font=my_font1)
l1.grid(row=1, column=1, columnspan=4)
b1 = tk.Button(my_w, text='Upload Files', width=20, command=lambda: upload_file())
b1.grid(row=2, column=1, columnspan=4)


def upload_file():
    f_types = [('JPEG Files', '*.JPEG'), ('Jpg Files', '*.jpg'),
               ('PNG Files', '*.png')]  # type of files to select
    filename = filedialog.askopenfilename(multiple=True, filetypes=f_types)
    col = 1  # start from column 1
    row = 3  # start from row 3
    for f in filename:
        img = Image.open(f)  # read the image file
        img = img.resize((300, 300))  # new width & height
        img = ImageTk.PhotoImage(img)
        e1 = tk.Label(my_w)
        e1.grid(row=row, column=col)
        e1.image = img
        e1['image'] = img  # garbage collection
        if col == 3:  # start new line after third column
            row = row + 1  # start wtih next row
            col = 1  # start with first column
        else:  # within the same row
            col = col + 1  # increase to next column
    row = row + 1
    l1.destroy()
    b1.destroy()
    watermark = Entry(my_w, width=20, font=my_font1)
    # watermark.grid(row=4, column=1, columnspan=4)
    watermark.grid(row=row, column=1)
    row = row + 1
    apply_wm = tk.Button(my_w, text='Appy watermark',
                         width=20, command=lambda: apply_wm_func())
    # apply_wm.grid(row=5, column=1, columnspan=4)
    apply_wm.grid(row=row, column=1)

    def apply_wm_func():

        for f in filename:
            img = Image.open(f)  # read the image file
            img_size = img.size
            print(img_size)
            img_sizes = (img_size[0], img_size[1])
            img = img.resize(img_sizes)  # new width & height
            drawing = ImageDraw.Draw(img)
            black = (3, 8, 12)
            font_type = ImageFont.truetype("Roboto-Black.ttf", 50)
            # text = "varadhan"
            text = watermark.get()
            pos = (0, 0)
            drawing.text(pos, text, fill=black, font=font_type)
            new_image = img
            # new_image.resize((img_size[0], img_size[1]))
            img = ImageTk.PhotoImage(img)
            e2 = tk.Label(my_w)
            e2.grid(row=6, column=1, columnspan=4)
            # e2.grid(row=row, column=col)
            e2.image = img
            e2['image'] = img  # garbage collection
            e1.destroy()
            watermark.destroy()
            apply_wm.destroy()

        def savefile():
            file_name = filedialog.asksaveasfile(mode='w', defaultextension=".JPEG", filetypes=f_types)
            if not file_name:
                return
            new_image.save(file_name)

        btn = Button(my_w, text="Save", command=lambda: savefile(), width=20)
        btn.grid(row=6, column=2, columnspan=4)


my_w.mainloop()  # Keep the window open
