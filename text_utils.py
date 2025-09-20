from tkinter import *
from tkinter import  messagebox, colorchooser, StringVar
from tkinter.ttk import Combobox
import tkinter.font as tkFont
import platform
import json
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class TextUtils:
    def __init__(self, m_page, canvas, popup_menu, dosya):
        self.m_page = m_page
        self.canvas = canvas
        self.popup_menu = popup_menu
        self.dosya = dosya
        self.popup_menu_label = ["Edit", "Delete", "Font", "Color","Font Size"]
        self.dosya_menu_label = ["Add Image", "Add Logo", "Save Image"]
        self.text_placeholder()
        self.buttons = []
        self.fonts()

    def fonts(self):
        self.fontlar_var = StringVar(value="arial")
        json_path = resource_path("matched_fonts.json")  # burası önemli
        with open(json_path, "r") as file:
            self.data = json.load(file)
            font_names = self.data.keys()
            self.fontlar = []
            for font in font_names:
                self.fontlar.append(font)
            self.fontlar.sort()

    def text_placeholder(self):
        self.renk = ("red", "red")
        self.edit_entry = None
        self.cb_font = None
        self.text_id = None
        self.text_ids = []
        self.selected_text_id = None
        self.entry_text = None
        self.secilen_font = None
        self.last_size_dict = {}
        self.font_dict = {}



    # -------- Yazı Hareket Fonksiyonları --------
    def start_move_text(self, event, text_id):
        self.last_mouse_pos = (event.x, event.y)
        self.selected_text_id = text_id

    def move_text(self, event):
        dx = event.x - self.last_mouse_pos[0]
        dy = event.y - self.last_mouse_pos[1]
        if hasattr(self, 'selected_text_id'):
            self.canvas.move(self.selected_text_id, dx, dy)
            self.canvas.update()
        self.last_mouse_pos = (event.x, event.y)

    def get_default_font_path(self):
        system = platform.system()

        if system == "Windows":
            return r"C:\Windows\Fonts\\"
        elif system == "Darwin":  # macOS
            return "/Library/Fonts"
        elif system == "Linux":
            return f"/usr/share/fonts/truetype/{self.secilen_font}/"
        else:
            raise OSError("Bilinmeyen işletim sistemi!")


    def select_text(self, text_id):
        self.selected_text_id = text_id


    def add_text(self, event):
        text = self.entry_text.get("1.0", "end-1c")
        if text == "":
            messagebox.showinfo("Uyarı", "Bu Alan Boş Bırakılamaz")
        else:
            tag = f"text_{self.canvas.find_all().__len__()}"
            self.font_name = "arial"
            self.font_size = 14
            font = (self.font_name, self.font_size)
            self.text_id = self.canvas.create_text(self.x, self.y, text=text, font=font
                                                   , fill="red", anchor="nw", width=1000, tags=(tag,))
            self.canvas.tag_bind(self.text_id, "<Button-3>", lambda e, tid=self.text_id: self.sag_tiklandi(e,tid))
            self.canvas.tag_bind(self.text_id, "<Button-1>", lambda e, tid=self.text_id: self.start_move_text(e, tid))
            self.canvas.tag_bind(self.text_id, "<B1-Motion>", self.move_text)
            self.canvas.tag_bind(tag, "<Button-1>", lambda e, t_id=self.text_id: self.select_text(t_id))
            self.text_ids.append(self.text_id)
            self.font_dict[self.text_id] = font
            self.entry_text.destroy()
            for button in self.buttons:
                button.config(state="normal")

            self.m_page.config(cursor="")


            for label in self.popup_menu_label:
                self.popup_menu.entryconfig(f"{label}", state="normal")

            for label_x in self.dosya_menu_label:
                self.dosya.entryconfig(f"{label_x}", state="normal")

    def text_entry(self):
        self.m_page.config(cursor="xterm")
        for label in self.popup_menu_label:
            self.popup_menu.entryconfig(f"{label}", state="disabled")
        for label_x in self.dosya_menu_label:
            self.dosya.entryconfig(f"{label_x}", state="disabled")
        for button in self.buttons:
            button.config(state="disabled")

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        self.x, self.y = event.x, event.y

        self.entry_text = Text(self.canvas, wrap='word', font=("Arial", 14))
        self.entry_text.place(x=self.x, y=self.y, width=750, height=150)
        self.entry_text.focus()

        self.entry_text.bind("<Escape>", self.add_text)
        self.canvas.unbind("<Button-1>")

    def text_edit(self, event=None):
        try:
            if self.selected_text_id:
                self.current_text_id = self.selected_text_id
                if self.current_text_id in self.text_ids:
                    for label in self.popup_menu_label:
                        self.popup_menu.entryconfig(f"{label}", state="disabled")
                    for label_x in self.dosya_menu_label:
                        self.dosya.entryconfig(f"{label_x}", state="disabled")
                    for button in self.buttons:
                        button.config(state="disabled")

                    old_text = self.canvas.itemcget(self.current_text_id, "text")

                if not self.edit_entry and not self.cb_font:
                    coords = self.canvas.coords(self.current_text_id)
                    x, y = coords[0], coords[1]

                    self.edit_entry = Text(self.canvas, wrap='word', font=("Arial", 14))
                    self.edit_entry.place(x=x, y=y, width=750, height=150)
                    self.edit_entry.insert("1.0", old_text)
                    self.edit_entry.focus()

                    self.edit_entry.bind("<Escape>", self.edit_entry_destroy)
        except IndexError:
            messagebox.showerror(title="ERROR",message="Lütfen Bir Text Seçiniz !")


    def delete_text(self, event=None):
        if self.selected_text_id in self.text_ids:
            self.canvas.delete(self.selected_text_id)
            self.text_ids.remove(self.selected_text_id)


    def edit_entry_destroy(self, event):
        self.editing_text = self.edit_entry.get("1.0", "end-1c")
        self.canvas.itemconfig(self.current_text_id, text=self.editing_text)

        self.edit_entry.destroy()
        self.canvas.update()
        self.edit_entry = None

        for label in self.popup_menu_label:
            self.popup_menu.entryconfig(f"{label}", state="normal")
        for label_x in self.dosya_menu_label:
            self.dosya.entryconfig(f"{label_x}", state="normal")
        for button in self.buttons:
            button.config(state="normal")

    def renk_sec(self):
        if self.selected_text_id:
            self.current_text_color = self.selected_text_id
            if self.current_text_color in self.text_ids:
                self.renk = colorchooser.askcolor(title="Renk seç")
                if self.renk[1]:
                    self.canvas.itemconfig(self.selected_text_id, fill=self.renk[1])


    def font_degistir(self):
        self.secilen_font = self.fontlar_var.get()
        self.yeni_font = tkFont.Font(family=self.secilen_font)

        font_name = self.secilen_font
        font_size = self.font_dict[self.current_font_id][1]
        font = (font_name, font_size)
        self.font_dict[self.current_font_id] = font

        self.canvas.itemconfig(self.current_font_id, font=font)
        if self.yeni_font:
            for label in self.popup_menu_label:
                self.popup_menu.entryconfig(f"{label}", state="normal")
            for label_x in self.dosya_menu_label:
                self.dosya.entryconfig(f"{label_x}", state="normal")
            for button in self.buttons:
                button.config(state="normal")
            self.cb_font.destroy()
            self.cb_font = None

    def font_combobox(self):
        if self.selected_text_id:
            self.current_font_id = self.selected_text_id
            if self.current_font_id in self.text_ids:
                for label in self.popup_menu_label:
                    self.popup_menu.entryconfig(f"{label}", state="disabled")
                for label_x in self.dosya_menu_label:
                    self.dosya.entryconfig(f"{label_x}", state="disabled")
                for button in self.buttons:
                    button.config(state="disabled")
                self.cb_font = Combobox(self.canvas, values=self.fontlar, textvariable=self.fontlar_var)
                self.cb_font.place(x=0, y=0, width=94, height=25)
                self.cb_font.bind("<<ComboboxSelected>>", lambda e: self.font_degistir())

    def font_size_scale(self):
        if self.selected_text_id:
            self.current_font_size_id = self.selected_text_id
            if self.current_font_size_id in self.text_ids:
                self.font_size = Scale(self.canvas, from_=1, to=100, orient=HORIZONTAL, command=self.font_size_change,bg="#d4a443",troughcolor="#000000")
                try:
                    if not self.last_size_dict:
                        self.font_size.set(14)
                    else:
                        self.font_size.set(self.last_size_dict[self.selected_text_id])
                except KeyError:
                    self.font_size.set(14)

                self.font_size.place(x=0, y=0,width=94, height=50)

                for label in self.popup_menu_label:
                    self.popup_menu.entryconfig(f"{label}", state="disabled")
                for label_x in self.dosya_menu_label:
                    self.dosya.entryconfig(f"{label_x}", state="disabled")
                for button in self.buttons:
                    button.config(state="disabled")


    def font_size_change(self, size):
        new_size = size
        old_font = self.font_dict[self.current_font_size_id][0]
        font = (old_font, new_size)
        self.canvas.itemconfig(self.current_font_size_id,font=font)
        self.canvas.update()

        self.font_dict[self.current_font_size_id] = font
        self.font_size.bind("<ButtonRelease-1>", self.font_size_save)

    def font_size_save(self, event):
        last_size = self.font_size.get()
        self.last_size_dict[self.current_font_size_id] = last_size
        self.font_size.destroy()
        for label in self.popup_menu_label:
            self.popup_menu.entryconfig(f"{label}", state="normal")
        for label_x in self.dosya_menu_label:
            self.dosya.entryconfig(f"{label_x}", state="normal")
        for button in self.buttons:
            button.config(state="normal")


    def sag_tiklandi(self, event, text_id):
        self.selected_text_id = text_id
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

