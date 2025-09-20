from tkinter import *
from text_utils import TextUtils
from image_utils import ImageUtils
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class ImageEditor:
    def __init__(self, window):
        # -------- Ekran Ayarları --------
        self.window = window
        self.window.title("Image Editor")
        window_width = 1440
        window_height = 900
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2) -50
        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        self.window.resizable(False, False)

        # -------- Frames --------
        self.m_page = Frame(self.window, bg="#1f2024")
        self.m_page.pack(fill="both", expand=True)

        self.menu()
        self.mainpage()

    def menu(self):
        self.menubar = Menu(self.window)
        self.dosya = Menu(self.menubar, tearoff=0)

        self.dosya.add_command(label="Add Image", command=self.load_foto)
        self.dosya.add_command(label="Add Logo", command=self.load_logo)
        self.dosya.add_command(label="Save Image", command=self.save_image)

        self.menubar.add_cascade(label="File", menu=self.dosya)
        self.window.config(menu=self.menubar)

        self.popup_menu = Menu(self.window, tearoff=0)
        self.popup_menu.add_command(label="Edit", command=self.text_edit)
        self.popup_menu.add_command(label="Delete", command=self.delete_text)
        self.popup_menu.add_command(label="Font", command=self.font_combobox)
        self.popup_menu.add_command(label="Color", command=self.renk_sec)
        self.popup_menu.add_command(label="Font Size", command=self.font_size_scale)

    def button_images(self):
        add_button_img = Image.open(resource_path("Buttons/addtext.png")).resize((60, 60))
        self.add_img = ImageTk.PhotoImage(add_button_img)

        edit_button_img = Image.open(resource_path("Buttons/edittext.png")).resize((60, 60))
        self.edit_img = ImageTk.PhotoImage(edit_button_img)

        delete_button_img = Image.open(resource_path("Buttons/deletetext.png")).resize((60, 60))
        self.delete_img = ImageTk.PhotoImage(delete_button_img)

        load_img_button_img = Image.open(resource_path("Buttons/loadbutton.png")).resize((60, 60))
        self.load_img_img = ImageTk.PhotoImage(load_img_button_img)

        load_logo_button_img = Image.open(resource_path("Buttons/loadlogo.png")).resize((60, 60))
        self.load_logo_img = ImageTk.PhotoImage(load_logo_button_img)

        save_image_button_img = Image.open(resource_path("Buttons/savebutton.png")).resize((60, 60))
        self.save_image_img = ImageTk.PhotoImage(save_image_button_img)

        font_type_button_img = Image.open(resource_path("Buttons/fonttype.png")).resize((60, 60))
        self.font_type_img = ImageTk.PhotoImage(font_type_button_img)

        font_size_button_img = Image.open(resource_path("Buttons/fontsize.png")).resize((60, 60))
        self.font_size_img = ImageTk.PhotoImage(font_size_button_img)

        color_panel_button_img = Image.open(resource_path("Buttons/colorpanel.png")).resize((60, 60))
        self.color_panel_button = ImageTk.PhotoImage(color_panel_button_img)

    def create_button(self):
        self.button_images()

        labe_img = Image.open(resource_path("Buttons/palet.png")).resize((570, 60))
        self.xx_img = ImageTk.PhotoImage(labe_img)

        label = Label(self.m_page, image=self.xx_img, bd=0, highlightthickness=0)
        label.place(x=440, y=10)


        #LoadImageButton
        self.image_utils.load_image_button = Button(self.m_page, command=self.load_foto, image=self.load_img_img, bd=0)
        self.image_utils.load_image_button.place(x=460, y=15, width=50, height=50)
        #LoadLogoButton
        self.image_utils.load_logo_button = Button(self.m_page, command=self.load_logo, image=self.load_logo_img, bd=0)
        self.image_utils.load_logo_button.place(x=520, y=15, width=50, height=50)
        #SaveImageButton
        self.image_utils.save_image_button = Button(self.m_page, command=self.save_image, image=self.save_image_img, bd=0)
        self.image_utils.save_image_button.place(x=580, y=15, width=50, height=50)
        #AddTextButton
        self.text_utils.text = Button(self.m_page, command=self.text_entry, image=self.add_img, bd=0)
        self.text_utils.text.place(x=640, y=15, width=50, height=50)
        #TextEditButton
        self.text_utils.edit_text_button = Button(self.m_page, command=self.text_edit, image=self.edit_img, bd=0)
        self.text_utils.edit_text_button.place(x=700, y=15, width=50, height=50)
        #TextDeleteButton
        self.text_utils.delete_text_button = Button(self.m_page, command=self.delete_text, image=self.delete_img, bd=0)
        self.text_utils.delete_text_button.place(x=760, y=15, width=50, height=50)
        #FontTypeButton
        self.text_utils.font_change_button = Button(self.m_page, command=self.font_combobox, image=self.font_type_img, bd=0)
        self.text_utils.font_change_button.place(x=820, y=15, width=50, height=50)
        #FontSizeButton
        self.text_utils.font_size_button = Button(self.m_page, command=self.font_size_scale, image=self.font_size_img , bd=0)
        self.text_utils.font_size_button.place(x=880, y=15, width=50, height=50)
        #ColorPanelButton
        self.text_utils.color_change_button = Button(self.m_page, command=self.renk_sec, image=self.color_panel_button, bd=0)
        self.text_utils.color_change_button.place(x=940, y=15, width=50, height=50)



        self.text_utils.buttons.append(self.text_utils.text)
        self.text_utils.buttons.append(self.text_utils.edit_text_button)
        self.text_utils.buttons.append(self.text_utils.delete_text_button)
        self.text_utils.buttons.append(self.image_utils.load_image_button)
        self.text_utils.buttons.append(self.image_utils.load_logo_button)
        self.text_utils.buttons.append(self.image_utils.save_image_button)
        self.text_utils.buttons.append(self.text_utils.font_change_button)
        self.text_utils.buttons.append(self.text_utils.font_size_button)
        self.text_utils.buttons.append(self.text_utils.color_change_button)


    def mainpage(self):
        self.canvas = Canvas(self.m_page, width=750, height=750, bg="white", highlightthickness=0)
        self.canvas.pack(padx=25, pady=75)

        self.text_utils = TextUtils(self.m_page, self.canvas, self.popup_menu, self.dosya)
        self.image_utils = ImageUtils(self.m_page, self.canvas, self.text_utils)

        self.create_button()

    def load_foto(self):
        self.image_utils.load_foto()

    def load_logo(self):
        self.image_utils.load_logo()

    def save_image(self):
        self.image_utils.save_image()

    def text_entry(self):
        self.text_utils.text_entry()

    def renk_sec(self):
        self.text_utils.renk_sec()

    def text_edit(self, event=None):
        self.text_utils.text_edit(event)

    def font_combobox(self):
        self.text_utils.font_combobox()

    def delete_text(self, event=None):
        self.text_utils.delete_text(event)

    def font_size_scale(self):
        self.text_utils.font_size_scale()


window = Tk()
app = ImageEditor(window)
window.mainloop()
