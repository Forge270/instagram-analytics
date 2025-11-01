import os
from dotenv import load_dotenv

load_dotenv()

# Instagram hesap bilgileri
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', 'nisaa_logg')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD', 'goktug1994.')

# Analiz ayarları
HASHTAGS_TO_ANALYZE = [
    '#marketing',
    '#dijitalpazarlama',
    '#sosyalmedya',
    '#istanbul',
    '#entrepreneur'
]

COMPETITORS_TO_TRACK = [
    'instagram',  # Örnek hesaplar
    'nike',
    'adidas'
]

# Rapor ayarları
REPORT_FOLDER = 'reports'
MAX_POSTS_TO_ANALYZE = 50

# Session ayarları
SESSION_FILE = 'instagram_session.json'