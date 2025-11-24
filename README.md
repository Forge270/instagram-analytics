# Instagram Analytics Tool

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
