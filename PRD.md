# Eğitici Oyun Platformu - Ürün Gereksinimleri Dökümanı (PRD)

## 1. Genel Bakış

### 1.1 Proje Özeti
Türkiye'deki ilkokul ve ortaokul öğrencilerine yönelik, müfredata uygun, eğlenceli ve interaktif HTML5 tabanlı eğitici oyun platformu geliştirilmesi.

### 1.2 Vizyon
Öğrencilerin ders çalışmayı eğlenceli hale getirerek akademik başarılarını artırmak ve öğrenmeye karşı pozitif tutum geliştirmelerini sağlamak.

### 1.3 Hedef Kitle
- **Birincil Hedef:** 7-14 yaş arası ilkokul ve ortaokul öğrencileri
- **İkincil Hedef:** Öğretmenler ve ebeveynler

## 2. Teknik Gereksinimler

### 2.1 Platform Özellikleri
- **Teknoloji:** Pure HTML5, CSS3, JavaScript (framework kullanılmadan)
- **Dosya Yapısı:** Her oyun tek bir HTML dosyası olarak paketlenmiş
- **Responsive Tasarım:** Tüm ekran boyutlarına otomatik uyum
- **Kaydırma:** Dikey veya yatay kaydırma olmadan tam ekran deneyim
- **Tarayıcı Desteği:** Modern tüm tarayıcılarda çalışabilir
- **Offline Çalışma:** İnternet bağlantısı gerektirmeden çalışabilir

### 2.2 Performans Kriterleri
- Yükleme süresi: Maksimum 3 saniye
- FPS: Minimum 30 FPS
- Bellek kullanımı: Maksimum 100MB
- Dosya boyutu: Her oyun maksimum 5MB

## 3. Oyun Kategorileri ve İçerik

### 3.1 Ders Dağılımı (Her ders için 20 oyun)

#### Fen Bilgisi (20 Oyun)
- Canlılar ve yaşam döngüsü
- Madde ve değişim
- Fiziksel olaylar
- Dünya ve evren
- Basit makineler

#### Türkçe (20 Oyun)
- Kelime bilgisi
- Dil bilgisi
- Okuma anlama
- Yazım kuralları
- Noktalama işaretleri

#### Fizik (20 Oyun)
- Hareket ve kuvvet
- Elektrik devreleri
- Işık ve ses
- Basınç
- Enerji dönüşümleri

#### Kimya (20 Oyun)
- Periyodik tablo
- Kimyasal reaksiyonlar
- Asit-baz
- Karışımlar
- Element ve bileşikler

#### Biyoloji (20 Oyun)
- Hücre yapısı
- Sistemler (sindirim, dolaşım, vb.)
- Genetik
- Ekosistem
- Evrim ve adaptasyon

#### Coğrafya (20 Oyun)
- Türkiye coğrafyası
- Dünya haritası
- İklim ve hava olayları
- Nüfus ve yerleşme
- Doğal kaynaklar

### 3.2 Oyun Türleri
- **Eşleştirme Oyunları:** Kavram-tanım, görsel-kelime eşleştirme
- **Sürükle-Bırak:** Sınıflandırma, sıralama aktiviteleri
- **Quiz/Test:** Çoktan seçmeli, doğru-yanlış soruları
- **Bulmaca:** Kelime avı, çapraz bulmaca
- **Simülasyon:** Deney simülasyonları, ekosistem modelleri
- **Hafıza Oyunları:** Kart eşleştirme, sıra hatırlama
- **Zaman Yarışı:** Hızlı cevaplama, reaksiyon oyunları
- **Yapboz:** Görsel tamamlama, parça birleştirme

## 4. Oyun Mekanikleri

### 4.1 Temel Özellikler
- **Puan Sistemi:** Her doğru cevap için puan kazanma
- **Seviye Sistemi:** Kolay, orta, zor seviyeler
- **Geri Bildirim:** Anlık doğru/yanlış bildirimleri
- **İpucu Sistemi:** Sınırlı sayıda ipucu hakkı
- **Zaman Sayacı:** İsteğe bağlı zaman limiti
- **Ses Efektleri:** Etkinleştirilebilir/devre dışı bırakılabilir
- **Görsel Animasyonlar:** Smooth geçişler ve etkileşimler

### 4.2 Motivasyon Elementleri
- Başarı rozetleri
- Yıldız toplama sistemi
- Liderlik tablosu (local storage)
- İlerleme çubuğu
- Combo sistemi (art arda doğru cevaplar)

## 5. Kullanıcı Arayüzü (UI) Gereksinimleri

### 5.1 Tasarım Prensipleri
- **Minimalist:** Dikkat dağıtıcı unsurlar olmadan
- **Renkli ve Canlı:** Çocukların ilgisini çekecek renk paleti
- **Büyük ve Okunabilir:** Font boyutu minimum 14px
- **Touch-Friendly:** Mobil cihazlar için optimize edilmiş dokunma alanları (minimum 44x44px)
- **İkonografik:** Metinlerle birlikte açıklayıcı ikonlar

### 5.2 Navigasyon
- Ana menü butonu her zaman görünür
- Oyundan çıkış onayı
- Ses açma/kapama toggle'ı
- Tam ekran modu butonu
- Yardım/nasıl oynanır butonu

### 5.3 Responsive Breakpoints
- Mobil: 320px - 768px
- Tablet: 768px - 1024px
- Desktop: 1024px ve üzeri

## 6. Veri Yönetimi

### 6.1 Local Storage Kullanımı
- Oyuncu skorları
- Seviye ilerlemesi
- Ses tercihleri
- Tamamlanan oyunlar
- En yüksek skorlar

### 6.2 Veri Güvenliği
- Client-side veri şifreleme
- XSS koruması
- Input validasyonu

## 7. Erişilebilirlik

### 7.1 WCAG 2.1 Uyumluluğu
- Klavye navigasyonu desteği
- Screen reader uyumluluğu
- Yüksek kontrast modu
- Font boyutu ayarlama
- Renk körlüğü desteği

### 7.2 Çoklu Dil Desteği
- Türkçe (varsayılan)
- İngilizce (opsiyonel)

## 8. Test Gereksinimleri

### 8.1 Test Türleri
- Fonksiyonel testler
- Performans testleri
- Tarayıcı uyumluluk testleri
- Responsive tasarım testleri
- Kullanılabilirlik testleri

### 8.2 Test Cihazları
- iOS Safari
- Android Chrome
- Windows (Chrome, Firefox, Edge)
- Tablet (iPad, Android Tablet)

## 9. Başarı Metrikleri

### 9.1 Kullanım Metrikleri
- Oyun başına ortalama oynama süresi (hedef: 5+ dakika)
- Tekrar oynama oranı (hedef: %40+)
- Oyun tamamlama oranı (hedef: %70+)
- Günlük aktif kullanıcı sayısı

### 9.2 Öğrenme Metrikleri
- Doğru cevap oranındaki artış
- Seviye ilerleme hızı
- Konu başına harcanan süre

## 10. Geliştirme Aşamaları

### Faz 1: Temel Altyapı (2 hafta)
- HTML/CSS/JS template oluşturma
- Responsive grid sistemi
- Temel oyun motoru

### Faz 2: İlk Oyun Seti (4 hafta)
- Her dersten 5 oyun
- Test ve optimizasyon

### Faz 3: Genişletme (6 hafta)
- Kalan oyunların geliştirilmesi
- Çapraz test

### Faz 4: Polish ve Optimizasyon (2 hafta)
- Bug fixing
- Performans optimizasyonu
- Son kullanıcı testleri

## 11. Riskler ve Azaltma Stratejileri

| Risk | Etki | Olasılık | Azaltma Stratejisi |
|------|------|----------|-------------------|
| Performans sorunları | Yüksek | Orta | Progressive enhancement, lazy loading |
| Tarayıcı uyumsuzlukları | Orta | Düşük | Polyfill kullanımı, feature detection |
| İçerik kalitesi | Yüksek | Orta | Eğitimci desteği, pilot testler |
| Kullanıcı ilgisizliği | Yüksek | Orta | Gamification, ödül sistemi |

## 12. Bakım ve Güncelleme

- Aylık bug fix güncellemeleri
- Çeyrek dönemlik içerik güncellemeleri
- Yıllık müfredat uyum kontrolü
- Kullanıcı geri bildirimlerine göre iyileştirmeler