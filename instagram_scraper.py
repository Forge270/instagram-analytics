from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import json
import os
import time
import config

class InstagramScraper:
    def __init__(self):
        self.client = Client()
        self.session_file = config.SESSION_FILE
        
    def login(self):
        """Instagram'a giriş yap"""
        
        # Önceki session var mı kontrol et
        if os.path.exists(self.session_file):
            try:
                print("📱 Önceki session yükleniyor...")
                self.client.load_settings(self.session_file)
                self.client.login(config.INSTAGRAM_USERNAME, config.INSTAGRAM_PASSWORD)
                
                # Session geçerli mi kontrol et
                self.client.get_timeline_feed()
                print("✅ Session geçerli, giriş başarılı!")
                return True
            except Exception as e:
                print(f"⚠️ Session geçersiz: {e}")
                print("🔄 Yeni giriş yapılıyor...")
        
        # Yeni giriş yap
        try:
            print("🔐 Instagram'a giriş yapılıyor...")
            self.client.login(config.INSTAGRAM_USERNAME, config.INSTAGRAM_PASSWORD)
            
            # Session'ı kaydet
            self.client.dump_settings(self.session_file)
            print("✅ Giriş başarılı! Session kaydedildi.")
            return True
            
        except LoginRequired:
            print("❌ Giriş başarısız: 2FA gerekli olabilir")
            return False
        except Exception as e:
            print(f"❌ Giriş hatası: {e}")
            return False
    
    def analyze_hashtag(self, hashtag):
        """Hashtag analizi yap"""
        print(f"\n🔍 Hashtag analizi: {hashtag}")
        
        try:
            # Hashtag'i temizle
            hashtag_clean = hashtag.replace('#', '')
            
            # Hashtag bilgilerini al
            medias = self.client.hashtag_medias_recent(hashtag_clean, amount=config.MAX_POSTS_TO_ANALYZE)
            
            if not medias:
                print(f"⚠️ {hashtag} için post bulunamadı")
                return None
            
            total_likes = sum(media.like_count for media in medias)
            total_comments = sum(media.comment_count for media in medias)
            avg_likes = total_likes / len(medias) if medias else 0
            avg_comments = total_comments / len(medias) if medias else 0
            
            result = {
                'hashtag': hashtag,
                'total_posts': len(medias),
                'total_likes': total_likes,
                'total_comments': total_comments,
                'avg_likes': round(avg_likes, 2),
                'avg_comments': round(avg_comments, 2),
                'engagement_rate': round((avg_likes + avg_comments) / 1000, 2)  # Basitleştirilmiş
            }
            
            print(f"✅ {hashtag}: {len(medias)} post, {avg_likes:.0f} avg likes")
            return result
            
        except Exception as e:
            print(f"❌ {hashtag} analiz hatası: {e}")
            return None
    
    def analyze_user(self, username):
        """Kullanıcı/rakip analizi"""
        print(f"\n👤 Kullanıcı analizi: @{username}")
        
        try:
            user_id = self.client.user_id_from_username(username)
            user_info = self.client.user_info(user_id)
            
            # Son postları al
            medias = self.client.user_medias(user_id, amount=config.MAX_POSTS_TO_ANALYZE)
            
            total_likes = sum(media.like_count for media in medias)
            total_comments = sum(media.comment_count for media in medias)
            avg_likes = total_likes / len(medias) if medias else 0
            avg_comments = total_comments / len(medias) if medias else 0
            
            result = {
                'username': username,
                'full_name': user_info.full_name,
                'followers': user_info.follower_count,
                'following': user_info.following_count,
                'total_posts': user_info.media_count,
                'avg_likes': round(avg_likes, 2),
                'avg_comments': round(avg_comments, 2),
                'engagement_rate': round((avg_likes + avg_comments) / user_info.follower_count * 100, 2) if user_info.follower_count > 0 else 0
            }
            
            print(f"✅ @{username}: {user_info.follower_count:,} takipçi, {avg_likes:.0f} avg likes")
            return result
            
        except Exception as e:
            print(f"❌ @{username} analiz hatası: {e}")
            return None
    
    def get_best_posting_times(self, username):
        """En iyi post zamanlarını analiz et"""
        print(f"\n⏰ En iyi post zamanları analizi: @{username}")
        
        try:
            user_id = self.client.user_id_from_username(username)
            medias = self.client.user_medias(user_id, amount=config.MAX_POSTS_TO_ANALYZE)
            
            hour_performance = {}
            
            for media in medias:
                hour = media.taken_at.hour
                engagement = media.like_count + media.comment_count
                
                if hour not in hour_performance:
                    hour_performance[hour] = []
                hour_performance[hour].append(engagement)
            
            # Ortalama engagement'i hesapla
            hour_avg = {
                hour: sum(engs) / len(engs) 
                for hour, engs in hour_performance.items()
            }
            
            # En iyi 3 saati bul
            best_hours = sorted(hour_avg.items(), key=lambda x: x[1], reverse=True)[:3]
            
            result = {
                'best_hours': [f"{hour:02d}:00 - Avg: {eng:.0f}" for hour, eng in best_hours],
                'hour_performance': hour_avg
            }
            
            print(f"✅ En iyi saatler: {', '.join([f'{h:02d}:00' for h, _ in best_hours])}")
            return result
            
        except Exception as e:
            print(f"❌ Zaman analizi hatası: {e}")
            return None

if __name__ == '__main__':
    scraper = InstagramScraper()
    if scraper.login():
        # Test
        result = scraper.analyze_hashtag('#marketing')
        if result:
            print(f"\n📊 Sonuç: {result}")
    else:
        print("❌ Giriş yapılamadı")