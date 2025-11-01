import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import config

class ReportGenerator:
    def __init__(self):
        # Rapor klasörünü oluştur
        if not os.path.exists(config.REPORT_FOLDER):
            os.makedirs(config.REPORT_FOLDER)
    
    def generate_hashtag_report(self, hashtag_data):
        """Hashtag raporu oluştur"""
        if not hashtag_data:
            print("⚠️ Rapor için veri yok")
            return None
        
        # DataFrame oluştur
        df = pd.DataFrame(hashtag_data)
        
        # Excel dosyası oluştur
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{config.REPORT_FOLDER}/hashtag_analysis_{timestamp}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Hashtag Analysis', index=False)
            
            # Özet sayfa ekle
            summary = {
                'Metric': ['Toplam Hashtag', 'Toplam Post', 'Ortalama Like', 'Ortalama Yorum'],
                'Value': [
                    len(df),
                    df['total_posts'].sum(),
                    df['avg_likes'].mean(),
                    df['avg_comments'].mean()
                ]
            }
            pd.DataFrame(summary).to_excel(writer, sheet_name='Summary', index=False)
        
        print(f"✅ Hashtag raporu oluşturuldu: {filename}")
        
        # Grafik oluştur
        self._create_hashtag_chart(df, timestamp)
        
        return filename
    
    def generate_competitor_report(self, competitor_data):
        """Rakip analiz raporu"""
        if not competitor_data:
            print("⚠️ Rapor için veri yok")
            return None
        
        df = pd.DataFrame(competitor_data)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{config.REPORT_FOLDER}/competitor_analysis_{timestamp}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Competitors', index=False)
            
            # Sıralamalar ekle
            rankings = df.sort_values('followers', ascending=False)[['username', 'followers', 'engagement_rate']]
            rankings.to_excel(writer, sheet_name='Rankings', index=False)
        
        print(f"✅ Rakip raporu oluşturuldu: {filename}")
        
        # Grafik oluştur
        self._create_competitor_chart(df, timestamp)
        
        return filename
    
    def _create_hashtag_chart(self, df, timestamp):
        """Hashtag karşılaştırma grafiği"""
        try:
            plt.figure(figsize=(12, 6))
            
            # Engagement rate grafiği
            plt.subplot(1, 2, 1)
            plt.bar(df['hashtag'], df['engagement_rate'], color='steelblue')
            plt.xlabel('Hashtag')
            plt.ylabel('Engagement Rate')
            plt.title('Hashtag Engagement Comparison')
            plt.xticks(rotation=45, ha='right')
            
            # Average likes grafiği
            plt.subplot(1, 2, 2)
            plt.bar(df['hashtag'], df['avg_likes'], color='coral')
            plt.xlabel('Hashtag')
            plt.ylabel('Average Likes')
            plt.title('Hashtag Average Likes')
            plt.xticks(rotation=45, ha='right')
            
            plt.tight_layout()
            chart_file = f"{config.REPORT_FOLDER}/hashtag_chart_{timestamp}.png"
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Grafik oluşturuldu: {chart_file}")
            
        except Exception as e:
            print(f"⚠️ Grafik oluşturulamadı: {e}")
    
    def _create_competitor_chart(self, df, timestamp):
        """Rakip karşılaştırma grafiği"""
        try:
            plt.figure(figsize=(14, 6))
            
            # Takipçi karşılaştırması
            plt.subplot(1, 3, 1)
            plt.barh(df['username'], df['followers'], color='green')
            plt.xlabel('Followers')
            plt.title('Follower Comparison')
            
            # Engagement rate
            plt.subplot(1, 3, 2)
            plt.barh(df['username'], df['engagement_rate'], color='purple')
            plt.xlabel('Engagement Rate (%)')
            plt.title('Engagement Rate Comparison')
            
            # Average likes
            plt.subplot(1, 3, 3)
            plt.barh(df['username'], df['avg_likes'], color='orange')
            plt.xlabel('Average Likes')
            plt.title('Average Likes Comparison')
            
            plt.tight_layout()
            chart_file = f"{config.REPORT_FOLDER}/competitor_chart_{timestamp}.png"
            plt.savefig(chart_file, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Grafik oluşturuldu: {chart_file}")
            
        except Exception as e:
            print(f"⚠️ Grafik oluşturulamadı: {e}")

if __name__ == '__main__':
    # Test
    reporter = ReportGenerator()
    
    test_data = [
        {'hashtag': '#test1', 'total_posts': 100, 'avg_likes': 500, 'avg_comments': 50, 'engagement_rate': 5.5},
        {'hashtag': '#test2', 'total_posts': 200, 'avg_likes': 700, 'avg_comments': 70, 'engagement_rate': 7.7}
    ]
    
    reporter.generate_hashtag_report(test_data)
    print("✅ Test tamamlandı")