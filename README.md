Karınca Kolonisi Algoritması ile Uşak Elektrik Arıza Rota Optimizasyonu

Bu proje, Uşak ilinde 15 farklı mahallede aynı anda gelen elektrik arızalarına giden tek bir teknik ekibin toplam yolunu minimize eden rotayı bulmak amacıyla geliştirilmiştir.
Rota optimizasyonu, Karınca Kolonisi Algoritması (Ant Colony Optimization — ACO) kullanılarak gerçekleştirilmiştir.

Adreslerin koordinatları Google Maps Geocoding API ile alınmış, mesafe hesaplamaları Haversine formülü ile yapılmıştır.
Uygulama, kullanıcıya web tabanlı bir arayüz sunmak için Streamlit kullanılarak geliştirilmiştir.

*Projenin Amacı

Arıza noktalarının en kısa toplam mesafe ile gezilmesini sağlamak
Teknik ekibe optimum rota önermek
ACO meta-sezgisel algoritmasının gerçek bir problem üzerinde uygulanmasını göstermek
Google Maps API entegrasyonu ile gerçek dünya verileri kullanmak

Kullanılan Teknolojiler
Python	
Google Maps Geocoding API	Adres 
Haversine Formülü	Kuş uçuşu mesafe hesabı
Ant Colony Optimization (ACO)	Rota optimizasyon algoritması
Streamlit	Etkileşimli uygulama arayüzü
Matplotlib	Rota & yakınsama grafikleri
📁 Proje Klasör Yapısı
aco_usak_elektrik_rutasi/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   ├── addresses.py
│   └── google_maps_utils.py
│
├── core/
│   ├── haversine.py
│   └── ant_algorithm.py
│
├── visual/
│   └── plotting.py
│
├── .streamlit/
│   └── secrets.toml
│
└── README.md
📊 Çıktılar
1️⃣ En iyi rota grafiği

Arıza noktaları sırasına göre çizilmiş rota

2️⃣ ACO yakınsama grafiği

Her iterasyonda gelişen en iyi çözüm mesafesi
<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/c519e2d8-0369-4595-a6db-7d3bd5967eab" />
<img width="1919" height="883" alt="image" src="https://github.com/user-attachments/assets/94935af2-9dce-48db-9328-8dc2fcf48081" />
<img width="1189" height="913" alt="image" src="https://github.com/user-attachments/assets/11bc4b6b-d159-4123-b931-71c9b949809f" />
<img width="1126" height="912" alt="image" src="https://github.com/user-attachments/assets/d85d6d05-7c2a-4ed0-909a-e72843c6baca" />
🧑‍🎓 Öğrenci Bilgileri
Adınız:YEŞİM
Soyadınız:AYMA
Okul Numaranız:2312721002
GitHub Repo Bağlantısı:
https://github.com/kullanici_adi/Proje2KarincaAlgoritmasi




