import streamlit as st
import yt_dlp
import os

# ==========================================
# ១. ការកំណត់ទម្រង់ពណ៌ និងស្ទីល (Custom CSS)
# ==========================================
st.set_page_config(page_title="ULTIMATE VIDEO REUP ENGINE PRO", page_icon="🚀", layout="centered")

# បន្ថែម CSS ដើម្បីដំឡើងពណ៌ Dark Theme ស៊ីវីល័យ និងប៊ូតុងពណ៌បៃតងខ្ចី
st.markdown("""
    <style>
        .stApp { background-color: #0d0d0d; color: #ffffff; }
        h1 { color: #ff66b2 !important; font-family: 'Courier New', sans-serif; font-weight: bold; }
        .stButton>button {
            background-color: #2ecc71 !important;
            color: black !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            width: 100% !important;
            height: 50px !important;
            border: none !important;
        }
        .stButton>button:hover { background-color: #27ae60 !important; }
        div[data-testid="stBlock"] { background-color: #1a1a1a; padding: 20px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 ULTIMATE VIDEO REUP ENGINE PRO")
st.write("ប្រព័ន្ធទាញយកសាច់វីដេអូ ព្រមទាំងចាប់យកចំណងជើង និងហាស់ថេកសម្រាប់ Reup ស្វ័យប្រវត្ត")

# ប្រអប់បញ្ចូល Link
url = st.text_input("🔗 សូមទម្លាក់ Link វីដេអូនៅទីនេះ៖", placeholder="ទម្លាក់លីង YouTube, FB, TikTok...")

if url:
    with st.spinner("⏳ កំពុងទម្លុះប្រព័ន្ធសុវត្ថិភាព និងវិភាគទិន្នន័យវីដេអូ..."):
        
        # ការកំណត់កម្រិតខ្ពស់ដើម្បី Bypass / ដោះស្រាយ HTTP Error 403
       ydl_opts = {
            'format': 'bestvideo+bestaudio/best' if "tiktok.com" not in url else 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'quiet': True,
            'no_warnings': True,
            
            # 🔗 បន្ថែម Proxy នៅទីនេះ (អ្នកអាចប្រើប្រាស់ Free proxy ឬ Proxy ផ្ទាល់ខ្លួនរបស់អ្នក)
            # ឧទាហរណ៍៖ 'proxy': 'http://username:password@openproxy.com:port'
            # ឬប្រើប្រាស់ទម្រង់សាមញ្ញ៖ 'proxy': 'http://IP_Address:Port'
            
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            }
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', 'Video')
                description = info.get('description', '')
                tags = info.get('tags', [])
                
                # ដំណើរការទាញយកហាស់ថេក
                hashtags = [f"#{tag}" for tag in tags] if tags else []
                if description:
                    hashtags.extend([w for w in description.split() if w.startswith("#")])
                hashtags_str = " ".join(list(set(hashtags))) if hashtags else "#reels #foryou #viral"
                
                # បង្ហាញព័ត៌មានលទ្ធផលនៅលើផ្ទះកម្មវិធី
                st.markdown("---")
                st.subheader(f"📌 {video_title}")
                st.markdown(f"**🔥 ហាស់ថេក (Hashtags):** `{hashtags_str}`")
                
                # បង្ហាញផ្ទាំង Player មើលវីដេអូ
                st.video(url)
                
                # ប៊ូតុងទាញយកធំពណ៌បៃតង
                if st.button("EXECUTE ULTIMATE BYPASS RENDER"):
                    with st.spinner("📥 កំពុងរក្សាទុកវីដេអូទៅកាន់ Server..."):
                        ydl.download([url])
                    st.success("🎉 ដំណើរការទាញយក និង Bypass ត្រូវបានបញ្ចប់ជាស្ថាពរ!")
                    
        except Exception as e:
            st.error(f"❌ បរាជ័យ៖ {str(e).splitlines()[0]}")
            st.info("💡 គន្លឹះ៖ ប្រសិនបើនៅតែជួប Error 403 នេះនៅលើ Hosting (Streamlit) ដដែល នោះមកពី IP របស់ Server នោះត្រូវបានគេប្លុកទាំងស្រុង។ អ្នកអាចរត់កូដនេះនៅលើម៉ាស៊ីនកុំព្យូទ័រផ្ទាល់ខ្លួនវិញ (Localhost) វានឹងដំណើរការបានយ៉ាងរលូន។")
