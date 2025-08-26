#!/usr/bin/env python3
import os
from pathlib import Path

template_path = Path('/workspace/templates/game-template.html')
base_dir = Path('/workspace')
subjects = {
	'fen-bilgisi': [
		'Canlı-Cansız Sınıflandırma', 'Besin Zinciri Oluşturma', 'Maddenin Halleri Quiz', 'Güneş Sistemi Gezegenleri', 'Basit Makineler Eşleştirme', 'Hava Olayları Tahmin', 'Bitki Büyüme Döngüsü', 'Elektrik Devresi Kurma', 'Hayvan Sesleri Eşleştirme', 'Geri Dönüşüm Kutuları', 'Vücudumuzun Sistemleri Puzzle', 'Işık ve Gölge Deneyi', 'Su Döngüsü Tamamlama', 'Mikroskop Altında Hücreler', 'Kuvvet ve Hareket Quiz', 'Doğal Afetler ve Korunma', 'Vitamin ve Mineraller', 'Ses Dalgaları Simülasyonu', 'Ekosistem Dengesi', 'Bilimsel Yöntem Adımları'
	],
	'turkce': [
		'Kelime Avı', 'Eş Anlamlı Kelimeler', 'Noktalama İşaretleri', 'Hece Ayırma Yarışı', 'Deyimler ve Anlamları', 'Büyük-Küçük Harf Kullanımı', 'Cümle Kurma', 'Zıt Anlamlı Kelimeler', 'Yazım Yanlışlarını Bul', 'Atasözleri Tamamlama', 'Fiil Çekimleri Quiz', 'Sözcük Türleri Sınıflandırma', 'Ses Olayları Tanıma', 'Metin Anlama Soruları', 'Kelime Türetme Atölyesi', 'Özel İsim-Cins İsim', 'Bulmaca Çözme', 'Hikaye Sıralama', 'Ses Bilgisi Eşleştirme', 'Dilbilgisi Maratonu'
	],
	'fizik': [
		'Newton\'un Yasaları Quiz', 'Basit Sarkaç Simülasyonu', 'Elektrik Devre Elemanları', 'Işık Kırılması Deneyi', 'Kuvvet Vektörleri Toplama', 'Serbest Düşme Hesaplayıcı', 'Mıknatıslar ve Kutuplar', 'Basınç Kavramı', 'Isı ve Sıcaklık Farkı', 'Ses Dalgaları Frekansı', 'Enerji Dönüşümleri', 'Paralel-Seri Devreler', 'Hız-Zaman Grafikleri', 'Optik Aletler Quiz', 'Basit Makineler Verimi', 'Dalga Boyu Hesaplama', 'Elektrik Alan Çizgileri', 'Momentum Korunumu', 'Yansıma Yasaları', 'Fizik Formülleri Eşleştirme'
	],
	'kimya': [
		'Periyodik Tablo Puzzle', 'Element Sembolleri Quiz', 'Asit-Baz pH Ölçümü', 'Molekül Yapısı Oluşturma', 'Kimyasal Denklem Dengeleme', 'Madde Sınıflandırması', 'Atom Modelleri Tarihi', 'İyon Yüklerini Eşleştirme', 'Çözünürlük Deneyi', 'Kimyasal Bağlar', 'Mol Hesaplamaları', 'Organik Bileşikler', 'Redoks Reaksiyonları', 'Gaz Yasaları Simülasyonu', 'Elektron Dizilimi', 'Kimyasal Değişimler', 'Karışımları Ayırma', 'Endotermik-Ekzotermik', 'Lewis Yapıları Çizimi', 'Laboratuvar Güvenliği Quiz'
	],
	'biyoloji': [
		'Hücre Organelleri Eşleştirme', 'DNA Sarmal Yapısı', 'Sindirim Sistemi Yolculuğu', 'Kan Grupları Quiz', 'Fotosentez Süreci', 'Mikroorganizmalar Sınıflandırma', 'Kalıtım Problemleri', 'Besin Piramidi Oluşturma', 'Solunum Sistemi Puzzle', 'Bitki-Hayvan Hücresi Farkları', 'Evrim Ağacı', 'Hormonlar ve Görevleri', 'Ekosistem İlişkileri', 'Mitoz-Mayoz Karşılaştırma', 'Virüs ve Bakteri Farkları', 'Boşaltım Sistemi Quiz', 'Biyolojik Çeşitlilik', 'Protein Sentezi', 'Duyu Organları Eşleştirme', 'Biyoteknoloji Uygulamaları'
	],
	'cografya': [
		'Türkiye İlleri Haritası', 'Dünya Başkentleri Quiz', 'İklim Tipleri Eşleştirme', 'Yön Bulma Pusulası', 'Coğrafi Şekiller Tanıma', 'Nüfus Piramidi Analizi', 'Doğal Kaynaklar Haritası', 'Kıtalar ve Okyanuslar', 'Türkiye\'nin Bölgeleri', 'Harita Sembolleri', 'Nehirler ve Göller', 'Dağlar ve Ovalar', 'Ekonomik Faaliyetler', 'Ulaşım Yolları Planlama', 'Zaman Dilimleri', 'Göç ve Nedenleri', 'Turistik Yerler Quiz', 'İhracat-İthalat Eşleştirme', 'Deprem Kuşakları', 'Şehir Planlama Simülasyonu'
	],
}


def build_game_html(template: str, subject_key: str, title: str) -> str:
	subject_label = {
		'fen-bilgisi': 'Fen Bilgisi',
		'turkce': 'Türkçe',
		'fizik': 'Fizik',
		'kimya': 'Kimya',
		'biyoloji': 'Biyoloji',
		'cografya': 'Coğrafya',
	}[subject_key]
	html = template.replace('{{TITLE}}', f'{title} - {subject_label}')
	html = html.replace('{{SUBJECT}}', subject_label)
	return html


def ensure_dirs():
	(base_dir / 'games').mkdir(parents=True, exist_ok=True)
	(base_dir / 'assets').mkdir(parents=True, exist_ok=True)
	for key in subjects.keys():
		(base_dir / 'games' / key).mkdir(parents=True, exist_ok=True)


def write_index(index_items: list[tuple[str, str, str]]):
	# index_items: (subject_label, title, rel_path)
	lines = []
	lines.append('<!doctype html>')
	lines.append('<html lang="tr"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><title>Eğitici Oyunlar</title><link rel="stylesheet" href="/assets/base.css" /></head><body>')
	lines.append('<div class="container"><h1>Eğitici Oyun Platformu</h1>')
	# Group by subject
	from collections import defaultdict
	grp = defaultdict(list)
	for subj, title, path in index_items:
		grp[subj].append((title, path))
	for subj in ['Fen Bilgisi','Türkçe','Fizik','Kimya','Biyoloji','Coğrafya']:
		if subj not in grp: continue
		lines.append(f'<h2>{subj}</h2>')
		lines.append('<div class="grid grid-4">')
		for title, path in grp[subj]:
			lines.append(f'<a class="card" href="{path}"><h3>{title}</h3></a>')
		lines.append('</div>')
	lines.append('</div></body></html>')
	(base_dir / 'index.html').write_text('\n'.join(lines), encoding='utf-8')


def main():
	ensure_dirs()
	template = template_path.read_text(encoding='utf-8')
	index_entries = []
	for subject_key, titles in subjects.items():
		subject_label = {
			'fen-bilgisi': 'Fen Bilgisi',
			'turkce': 'Türkçe',
			'fizik': 'Fizik',
			'kimya': 'Kimya',
			'biyoloji': 'Biyoloji',
			'cografya': 'Coğrafya',
		}[subject_key]
		for i, title in enumerate(titles, start=1):
			filename = f'oyun-{i:02d}.html'
			out_path = base_dir / 'games' / subject_key / filename
			html = build_game_html(template, subject_key, title)
			out_path.write_text(html, encoding='utf-8')
			rel = f'/games/{subject_key}/{filename}'
			index_entries.append((subject_label, title, rel))
	write_index(index_entries)
	print(f'Generated {len(index_entries)} games and index.html')

if __name__ == '__main__':
	main()