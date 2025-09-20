from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog, messagebox
import sys
import os


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ImageUtils:
    def __init__(self, m_page, canvas,text_utils):
        self.canvas = canvas
        self.m_page = m_page
        self.text_utils = text_utils
        self.image_placeholder()
        self.buttons_placeholder()

    def image_placeholder(self):
        self.pil_img = None
        self.tk_img = None
        self.canvas_img = None
        self.dosya_yolu = None
        self.logo_yolu = None
        self.font = None
        self.canvas_logo = None
        self.create_placeholder_image()

    def buttons_placeholder(self):
        self.load_image_button = None
        self.load_logo_button = None
        self.save_image_button = None

    def create_placeholder_image(self):
        placeholder = Image.open(resource_path("Buttons/placeholder.png")).resize((750,750))
        self.pil_img = placeholder
        self.tk_img = ImageTk.PhotoImage(placeholder)
        self.canvas_img = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

    def on_logo_press(self, event):
        self.canvas.tag_raise(self.canvas_logo)
        self.last_x, self.last_y = event.x, event.y

    def on_logo_drag(self, event):
        dx = event.x - self.last_x
        dy = event.y - self.last_y
        self.canvas.move(self.canvas_logo, dx, dy)
        self.last_x, self.last_y = event.x, event.y

    def events_image(self):
        self.canvas.tag_bind(self.canvas_logo, "<ButtonPress-1>", self.on_logo_press)
        self.canvas.tag_bind(self.canvas_logo, "<B1-Motion>", self.on_logo_drag)

    def load_foto(self):
        self.dosya_yolu = filedialog.askopenfilename(
            title="Bir resim seçin",
            filetypes=[("Resim Dosyaları", "*.png *.jpg *.jpeg ")]
        )
        if self.dosya_yolu:
            self.pil_img = Image.open(self.dosya_yolu).resize((750, 750))
            self.tk_img = ImageTk.PhotoImage(self.pil_img)
            self.canvas_img = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
            self.canvas.itemconfig(self.canvas_img, image=self.tk_img)
        for i in self.text_utils.text_ids:
            self.canvas.tag_raise(i)
        if self.canvas_logo:
            self.canvas.tag_raise(self.canvas_logo)

    def load_logo(self):
        self.logo_yolu = filedialog.askopenfilename(title="Bir resim seçin",
                                                     filetypes=[("Resim Dosyaları", "*.png")]
        )
        if self.logo_yolu:
            self.pil_logo = Image.open(self.logo_yolu).resize((100, 100))
            self.tk_logo = ImageTk.PhotoImage(self.pil_logo)
            self.canvas_logo = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_logo)
            self.events_image()


    def font_type(self):
        self.file_path = self.text_utils.get_default_font_path()


    def save_image(self):
        if not self.pil_img:
            return

        final_img = self.pil_img.copy()
        draw = ImageDraw.Draw(final_img)

        self.font_type()
        for text_id in self.text_utils.text_ids:
            if self.canvas.itemcget(text_id, "text") != "":
                self.x, self.y = self.canvas.coords(text_id)
                self.text = self.canvas.itemcget(text_id, "text")
                self.color = self.canvas.itemcget(text_id, "fill")
                self.s_font = self.canvas.itemcget(text_id, "font").split(" ")[0]
                try:
                    #72/96 DPI Eşitleme
                    size = self.text_utils.last_size_dict[text_id]
                    pil_size = size * 1.33
                    fark = pil_size - size
                    self.size = size + fark

                except KeyError:
                    size = 14
                    pil_size = size * 1.33
                    fark = pil_size - size
                    self.size = size + fark
                canvas_font_name = self.s_font.lower()
                try:
                    if canvas_font_name in self.text_utils.data:
                        font_file = self.text_utils.data[canvas_font_name]
                        self.font = self.file_path + font_file
                    else:
                        self.font = self.file_path + "arial.ttf"
                        print(f"Font '{canvas_font_name}' bulunamadı, arial kullanılıyor.")
                except Exception as e:
                    print(f"Font hatası: {e}")
                    self.font = self.file_path + "arial.ttf"

                try:
                    self.b_font = ImageFont.truetype(self.font, self.size)
                    print(self.b_font)
                except OSError:
                    messagebox.showwarning("Uyarı", "Sistem fontu yüklenemedi. Varsayılan font kullanılacak.")
                    self.b_font = ImageFont.load_default()

                draw.text((self.x, self.y), self.text, font=self.b_font, fill=self.color)
        try:
            if self.canvas_logo and self.pil_logo:
                x, y = self.canvas.coords(self.canvas_logo)
                if self.pil_logo.mode != "RGBA":
                    self.pil_logo = self.pil_logo.convert("RGBA")
                final_img.paste(self.pil_logo, (int(x), int(y)), self.pil_logo)
        except Exception as e:
            print(f"Logo Gömme Hatası{e}")


        # Kaydet
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            final_img.save(save_path)
            print(f"Resim kaydedildi: {save_path}")
