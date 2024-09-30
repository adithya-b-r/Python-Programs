from tkinter import *
from PIL import Image, ImageTk

# create the main window
window = Tk()

# load the image file and create a PIL image object
pil_image = Image.open("arc.png")

# create a Tkinter-compatible image object
photo = ImageTk.PhotoImage(pil_image)

# create a label for the image and place it in the center of the window
photobox = Label(window, image=photo)
photobox.pack(fill=BOTH, expand=YES)

# define a function to rotate the image clockwise
def rotate_clockwise(degrees):
    rotated_pil_image = pil_image.rotate(degrees)
    rotated_photo = ImageTk.PhotoImage(rotated_pil_image)
    photobox.configure(image=rotated_photo)
    photobox.image = rotated_photo
    window.after(50, rotate_clockwise, (degrees + 1) % 360)

# define a function to rotate the image anticlockwise
def rotate_anticlockwise(degrees):
    rotated_pil_image = pil_image.rotate(degrees)
    rotated_photo = ImageTk.PhotoImage(rotated_pil_image)
    photobox.configure(image=rotated_photo)
    photobox.image = rotated_photo
    window.after(50, rotate_anticlockwise, (degrees - 1) % 360)

# schedule the two functions to be called after 10 seconds each
window.after(0, rotate_clockwise, 0)
window.after(10000, rotate_anticlockwise, 0)

# run the main event loop
window.mainloop()
