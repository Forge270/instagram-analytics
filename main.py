from instagram_scraper import InstagramScraper
from report_generator import ReportGenerator
import config
import time

def main():
    print("="*60)
    print("📊 INSTAGRAM ANALYTICS TOOL")
    print("="*60)
    
    # Scraper'ı başlat
    scraper = InstagramScraper()
    
    # Giriş yap
    if not scraper.login():
        print("❌ Instagram'a giriş yapılamadı. Lütfen config.py'deki bilgileri kontrol et.")
        return
    
    print("\n" + "="*60)
    print("Hangi analizi yapmak istersiniz?")
    print("="*60)
    print("1. Hashtag Analizi")
    print("2. Rakip/Kullanıcı Analizi")
    print("3. İkisini de yap")
    print("="*60)
    
    choice = input("\nSeçiminiz (1/2/3): ").strip()
    
    reporter = ReportGenerator()
    
    if choice in ['1', '3']:
        # Hashtag analizi
        print("\n" + "="*60)
        print("📈 HASHTAG ANALİZİ BAŞLIYOR")
        print("="*60)
        
        hashtag_results = []
        for hashtag in config.HASHTAGS_TO_ANALYZE:
            result = scraper.analyze_hashtag(hashtag)
            if result:
                hashtag_results.append(result)
            time.sleep(2)  # Rate limiting
        
        if hashtag_results:
            reporter.generate_hashtag_report(hashtag_results)
        else:
            print("⚠️ Hashtag verisi alınamadı")
    
    if choice in ['2', '3']:
        # Rakip analizi
        print("\n" + "="*60)
        print("👥 RAKİP ANALİZİ BAŞLIYOR")
        print("="*60)
        
        competitor_results = []
        for username in config.COMPETITORS_TO_TRACK:
            result = scraper.analyze_user(username)
            if result:
                competitor_results.append(result)
            time.sleep(2)  # Rate limiting
        
        if competitor_results:
            reporter.generate_competitor_report(competitor_results)
        else:
            print("⚠️ Rakip verisi alınamadı")
    
    print("\n" + "="*60)
    print("✅ ANALIZ TAMAMLANDI!")
    print(f"📁 Raporlar '{config.REPORT_FOLDER}' klasöründe")
    print("="*60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Program kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Beklenmeyen hata: {e}")
        import traceback
        traceback.print_exc()