# Eğitici Oyun Platformu

Bu depo, ilkokul ve ortaokul öğrencilerine yönelik, müfredata uygun ve tamamen tarayıcıda çalışan HTML5 tabanlı eğitici oyunlar barındırır. Proje; framework kullanmadan, saf HTML/CSS/JS ile geliştirilmiştir ve statik olarak barındırılabilir.

## Özellikler
- Saf HTML5, CSS3 ve JavaScript (ES Modules)
- Tek dosya oyun yapısı: Her oyun tek bir `*.html` dosyasıdır
- Responsive, tam ekran deneyimi; mobil/masaüstü uyumlu
- Basit oyun motoru (`assets/engine.js`): skor, süre, ses efektleri, localStorage
- Offline çalışabilir statik mimari
- Tarayıcı uyumluluğu: modern tarayıcılar (Chrome, Edge, Firefox, Safari)

## Canlı Önizleme / Çalıştırma
ES Modules kullanıldığı için dosyaları doğrudan `file://` ile açmak yerine basit bir statik sunucu ile servis etmeniz gerekir.

Python ile hızlı başlatma (önerilir):

```bash
cd /workspace
python3 -m http.server 8080
```

Ardından tarayıcınızdan şu adresi açın:

- `http://localhost:8080/index.html`

Node.js yüklüyse alternatif:

```bash
npx serve -l 8080 /workspace
```

## Dosya Yapısı
```
/workspace
├─ index.html                 # Ana menü (tüm oyunlara bağlantı)
├─ games/                     # Oyunların oluşturulduğu klasör (otomatik üretilir)
│  ├─ fen-bilgisi/           
│  ├─ turkce/
│  ├─ fizik/
│  ├─ kimya/
│  ├─ biyoloji/
│  └─ cografya/
├─ assets/
│  ├─ base.css               # Ortak stil
│  └─ engine.js              # Basit oyun motoru ve yardımcılar
├─ templates/
│  └─ game-template.html     # Yeni oyunlar için HTML şablonu
├─ scripts/
│  └─ gen_games.py           # Oyun dosyalarını ve index.html'i üreten script
├─ PRD.md                    # Ürün gereksinimleri (vizyon, kapsam, metrikler)
├─ TODO.md                   # Geliştirme yapılacaklar listesi
└─ README.md                 # Bu dosya
```

## Geliştirme Akışı
1) Statik sunucuyu başlatın ve `index.html` üzerinden oyunları açın.
2) Mevcut oyunlar `games/<ders>/oyun-XX.html` yollarında bulunur.
3) Yeni oyunlar üretmek veya tüm seti tekrar oluşturmak için scripti çalıştırın.

### Oyunları Otomatik Üretme
Script, `templates/game-template.html` şablonunu kullanarak 6 derste 20'şer olmak üzere toplam 120 oyunu ve `index.html` dosyasını oluşturur/yeniler.

```bash
# Gereksinim: Python 3
python3 /workspace/scripts/gen_games.py
```

Çıktı:
- `games/<ders>/oyun-01.html` ... `oyun-20.html` dosyaları
- Kategorilere göre gruplandırılmış bağlantılar içeren `index.html`

Notlar:
- Script çalıştığında var olan dosyaların üzerine yazabilir. Kendi oyunlarınızı manuel düzenliyorsanız önce yedekleyin.
- Üretim tamamlandığında terminalde toplam üretilen oyun sayısı yazdırılır.

### Yeni Oyun Eklemek (Manuel)
- `templates/game-template.html` dosyasını kopyalayın ve `games/<ders>/oyun-YY.html` olarak kaydedin.
- `<title>` ve sayfa içindeki içerikleri güncelleyin; oyun panosunu `#board` içine yerleştirin.
- Gerekirse `index.html` dosyasına yeni bağlantı ekleyin (otomatik script bunu kendisi yönetir).

## Oyun Motoru Kısa Rehberi (`assets/engine.js`)
- `GameEngine.init({ onStart, onReset })`: Başlatma ve sıfırlama callback'leri bağlar, global UI event'lerini kurar.
- `GameEngine.addScore(points)`: Skoru artırır; `score:change` event'i yayar ve `localStorage`'a yazar.
- `GameEngine.resetScore()`: Skoru sıfırlar.
- `Timer.start(duration, onTick, onEnd)`: Geri sayımı başlatır.
- `Timer.stop() / Timer.reset()`: Zamanlayıcı kontrolü.
- `AudioFx.play('s-correct'|'s-wrong')`: Sayfada tanımlı `<audio>` elementlerini çalar (sessiz mod `localStorage.muted`).
- `$` ve `$all`: Hızlı DOM yardımcıları.

Şablonda (`templates/game-template.html`) hazır butonlar ve sayaçlar bulunur:
- `data-action="start"` ve `data-action="reset"` butonları
- Skor alanı: `#score`
- Süre alanı: `#time`
- Oyun içeriği alanı: `#board`

## Tarayıcı ve Performans
- Hedef: hızlı yükleme (≤ 3 sn), 30+ FPS, düşük bellek kullanımı.
- Modern tarayıcıların güncel sürümlerinde test edilmesi önerilir.

## Dağıtım
- Proje tamamen statiktir; GitHub Pages, Netlify, Vercel, Cloudflare Pages gibi ortamlara doğrudan dağıtılabilir.
- Gerekli dosyalar: `index.html`, `games/**`, `assets/**` (ve varsa ek varlıklar).

## Katkıda Bulunma
- PR gönderirken oyunların mobil uyumluluğunu ve erişilebilirliğini (klavye navigasyonu, kontrast, font boyutu) göz önünde bulundurun.
- Yeni ders/oyun eklerken şablon ve kategori yapısına sadık kalın.

## Lisans
- Lisans bilgisi eklenmemiştir. Kullanım koşulları netleştirilene kadar özel/kısıtlı kullanım varsayılır.