# Instagram Analytics Tool | Instagram Analiz Aracı

[English](#english) | [Türkçe](#turkish)

---

<a name="english"></a>
## 🇬🇧 English

Automated Instagram analytics and competitor tracking system.

### Features

- 📊 Hashtag performance analysis
- 👥 Competitor account monitoring
- 📈 Engagement rate tracking
- ⏰ Best posting time analysis
- 📑 Excel report generation with charts

### Tech Stack

- Python 3.10+
- Instagrapi (Instagram API wrapper)
- Pandas (data processing)
- Matplotlib (visualizations)
- OpenPyXL (Excel reports)

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Edit `config.py`:

```python
INSTAGRAM_USERNAME = 'your_username'
INSTAGRAM_PASSWORD = 'your_password'

HASHTAGS_TO_ANALYZE = ['#marketing', '#socialmedia']
COMPETITORS_TO_TRACK = ['competitor1', 'competitor2']
```

### Usage

```bash
python main.py
```

Select analysis type:
1. Hashtag Analysis
2. Competitor Analysis
3. Both

Reports are saved to `reports/` folder.

### Sample Output

- `hashtag_analysis_TIMESTAMP.xlsx` - Hashtag performance data
- `competitor_analysis_TIMESTAMP.xlsx` - Competitor metrics
- Chart visualizations (PNG format)

### Use Cases

- Marketing agencies tracking campaign performance
- Influencers optimizing content strategy
- Businesses monitoring competitor activity
- Social media managers analyzing trends

### License

MIT

---

<a name="turkish"></a>
## 🇹🇷 Türkçe

Otomatik Instagram analiz ve rakip takip sistemi.

### Özellikler

- 📊 Hashtag performans analizi
- 👥 Rakip hesap takibi
- 📈 Etkileşim oranı izleme
- ⏰ En iyi paylaşım zamanı analizi
- 📑 Grafikli Excel rapor oluşturma

### Teknolojiler

- Python 3.10+
- Instagrapi (Instagram API)
- Pandas (veri işleme)
- Matplotlib (görselleştirme)
- OpenPyXL (Excel raporlar)

### Kurulum

```bash
pip install -r requirements.txt
```

### Yapılandırma

`config.py` dosyasını düzenleyin:

```python
INSTAGRAM_USERNAME = 'kullanici_adiniz'
INSTAGRAM_PASSWORD = 'sifreniz'

HASHTAGS_TO_ANALYZE = ['#pazarlama', '#sosyalmedya']
COMPETITORS_TO_TRACK = ['rakip1', 'rakip2']
```

### Kullanım

```bash
python main.py
```

Analiz tipini seçin:
1. Hashtag Analizi
2. Rakip Analizi
3. İkisi de

Raporlar `reports/` klasörüne kaydedilir.

### Örnek Çıktılar

- `hashtag_analysis_ZAMAN.xlsx` - Hashtag performans verileri
- `competitor_analysis_ZAMAN.xlsx` - Rakip metrikleri
- Grafik görselleri (PNG formatında)

### Kullanım Alanları

- Pazarlama ajansları kampanya takibi
- Influencer'lar içerik stratejisi optimizasyonu
- İşletmeler rakip aktivite izleme
- Sosyal medya yöneticileri trend analizi

### Lisans

MIT

---

Built with ⚡ by [Forge270](https://github.com/Forge270)
