# 🎨 Image Editor - Image Editing Tool

Easily edit your images with a modern and user-friendly interface! An image editing application developed using Tkinter and PIL.

## ✨ Features

###️ Image Management
- **750x750 Fixed Size** image adding
- **100x100 Fixed Size** logo adding (draggable)
- PNG, JPG, JPEG format support
- High-quality image saving

### 📝 Text Editing
- Multi-line text adding
- **Font changing** (JSON database)
- **Font size adjustment** (1-100 range)
- **Color selection** (color palette)
- Drag & drop text movement

### User Interface
- **Button-based** usage
- **Right-click menu** for quick access
- **Menu system** for file operations
- Modern and clean design

## 🚀 Installation

### Requirements
```bash
pip install tkinter pillow
```

### Running
```bash
python main.py
```

### EXE Version
**Download from releases or use the included executable:**
- `editor.exe` - Single file executable application
- No installation required, just run the exe file

## User Guide

### 1. Adding Images
- Load images from **File > Add Image** menu
- Add logos from **File > Add Logo** menu

### 2. Adding Text
- Click **Text Ekle** button
- Click anywhere on the canvas
- Type your text and press **Escape**

### 3. Editing Text
- **Right-click** on text
- **Edit** - Edit text
- **Font** - Change font
- **Font Size** - Adjust size
- **Color** - Select color
- **Delete** - Delete text

### 4. Saving
- Save from **File > Save Image** menu
- Export in PNG or JPG format

## 🛠️ Technical Features

### Architecture
- **Modular structure** - Clean code principles
- **Separation of concerns** - Each class has its own responsibility
- **Error handling** - Safe error management

### Font System
- **JSON-based** font management
- **Cross-platform** font support
- **Dynamic font** loading
- **Font state** management

### Image Processing
- **PIL/Pillow** integration
- **DPI correction** (72/96 ratio)
- **Layer management** (Logo > Text > Image)
- **High quality** output

## 🎯 Layer Order

1. **Logo** (Top layer)
2. **Text** (Middle layer)
3. **Image** (Bottom layer)

This order ensures correct layer arrangement in printing.

## ⚠️ Important Notes

- Other buttons are disabled during text adding
- UI works synchronized during editing mode
- Deleted texts are automatically removed from list
- Font size is preserved when changing font, font is preserved when changing size

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

Copyright (c) 2024 WATSONSK14

This software is free but subject to the following conditions:
- Source must be credited
- Star on GitHub is mandatory
- Commercial use requires permission
- Button designs are proprietary

## ⭐ Star

If you liked this project, don't forget to give it a star!

---

**Developer:** WATSONSK14  
**Version:** 1.0  
**Last Update:** 2024
