# 🎨 Image Editor - Görsel Düzenleme Aracı

Modern ve kullanıcı dostu arayüzü ile görsellerinizi kolayca düzenleyin! Tkinter ve PIL kullanılarak geliştirilmiş bir görsel düzenleme uygulaması.

## ✨ Özellikler

### 🖼️ Görsel Yönetimi
- **750x750 Sabit Boyut** görsel ekleme
- **100x100 Sabit Boyut** logo ekleme (taşınabilir)
- PNG, JPG, JPEG format desteği
- Yüksek kalitede görsel kaydetme

### 📝 Metin Düzenleme
- Çok satırlı metin ekleme
- **Font değiştirme** (JSON veri tabanlı)
- **Font boyutu ayarlama** (1-100 arası)
- **Renk seçimi** (renk paleti ile)
- Sürükle-bırak ile metin taşıma

### 🎯 Kullanıcı Arayüzü
- **Buton tabanlı** kullanım
- **Sağ tık menüsü** ile hızlı erişim
- **Menü sistemi** ile dosya işlemleri
- Modern ve temiz tasarım

## 🚀 Kurulum

### Gereksinimler
```bash
pip install tkinter pillow
```

### Çalıştırma
```bash
python main.py
```

### EXE Versiyonu
**Releases kısmından indirin veya dahil edilen çalıştırılabilir dosyayı kullanın:**
- `editor.exe` - Tek dosya halinde çalıştırılabilir uygulama
- Kurulum gerekmez, sadece exe dosyasını çalıştırın

## 📖 Kullanım Kılavuzu

### 1. Görsel Ekleme
- **File > Add Image** menüsünden görsel yükleyin
- **File > Add Logo** menüsünden logo ekleyin

### 2. Metin Ekleme
- **Text Ekle** butonuna tıklayın
- Canvas üzerinde istediğiniz yere tıklayın
- Metninizi yazın ve **Escape** tuşuna basın

### 3. Metin Düzenleme
- Metne **sağ tıklayın**
- **Edit** - Metni düzenleyin
- **Font** - Font değiştirin
- **Font Size** - Boyut ayarlayın
- **Color** - Renk seçin
- **Delete** - Metni silin

### 4. Kaydetme
- **File > Save Image** menüsünden kaydedin
- PNG veya JPG formatında çıktı alın

## 🛠️ Teknik Özellikler

### Mimari
- **Modüler yapı** - Clean code prensipleri
- **Separation of concerns** - Her sınıf kendi sorumluluğu
- **Error handling** - Güvenli hata yönetimi

### Font Sistemi
- **JSON tabanlı** font yönetimi
- **Cross-platform** font desteği
- **Dinamik font** yükleme
- **Font state** yönetimi

### Görsel İşleme
- **PIL/Pillow** entegrasyonu
- **DPI düzeltme** (72/96 oranı)
- **Layer yönetimi** (Logo > Text > Image)
- **Yüksek kalite** çıktı

## 🎯 Katman Sıralaması

1. **Logo** (En üstte)
2. **Metin** (Ortada)
3. **Görsel** (En altta)

Bu sıralama ile baskıda doğru katman düzeni sağlanır.

## ⚠️ Önemli Notlar

- Metin ekleme sırasında diğer butonlar devre dışı kalır
- Düzenleme modunda tüm UI senkronize çalışır
- Silinen metinler listeden otomatik kaldırılır
- Font değiştirirken boyut korunur, boyut değiştirirken font korunur

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📄 Lisans

Copyright (c) 2024 WATSONSK14

Bu yazılım ücretsizdir ancak:
- Kaynak gösterilmelidir
- GitHub'da star atılması zorunludur
- Ticari kullanım için izin alınmalıdır
- Buton tasarımları özeldir

## ⭐ Star

Bu projeyi beğendiyseniz star atmayı unutmayın!

---

**Geliştirici:** WATSONSK14  
**Versiyon:** 1.0  
**Son Güncelleme:** 2024
