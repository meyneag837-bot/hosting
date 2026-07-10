import streamlit as st
import yt_dlp
import os

# រៀបចំទម្រង់វេបសាយ (Theme & Title)
st.set_page_config(page_title="MULTI-VIDEO DOWNLOADER PRO", page_icon="⚡", layout="centered")

st.title("⚡ MULTI-VIDEO DOWNLOADER PRO")
st.write("ទាញយកវីដេអូពី YouTube, Facebook, TikTok ព្រមទាំងទាញយក ចំណងជើង និង ហាស់ថេក ស្វ័យប្រវត្តិ")

# ប្រអប់បញ្ចូល Link
url = st.text_input("សូមទម្លាក់ Link វីដេអូនៅទីនេះ៖", placeholder="https://...")

if url:
    with st.spinner("⏳ កំពុងវិភាគព័ត៌មានវីដេអូ..."):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best' if "tiktok.com" not in url else 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'quiet': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', 'Video')
                description = info.get('description', '')
                tags = info.get('tags', [])
                
                # ចាប់យកហាស់ថេក
                hashtags = [f"#{tag}" for tag in tags] if tags else []
                if description:
                    hashtags.extend([w for w in description.split() if w.startswith("#")])
                hashtags_str = " ".join(list(set(hashtags))) if hashtags else "#reels #foryou #viral"
                
                # បង្ហាញព័ត៌មាននៅលើវេបសាយ
                st.subheader(f"📌 {video_title}")
                st.write(f"**ហាស់ថេក៖** {hashtags_str}")
                
                # បង្ហាញវីដេអូឱ្យមើលនៅលើវេបសាយ (Video Player)
                if 'url' in info:
                    st.video(url)
                
                # ប៊ូតុងទាញយក
                if st.button("🚀 ចាប់ផ្តើមទាញយកទៅកាន់ Server"):
                    ydl.download([url])
                    st.success("🎉 រួចរាល់!")
        except Exception as e:
            st.error(f"❌ បរាជ័យ៖ {str(e).splitlines()[0]}")
