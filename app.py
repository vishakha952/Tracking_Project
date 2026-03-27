import streamlit as st

# Page config
st.set_page_config(page_title="Multi-Object Tracking", layout="centered")

# Title
st.title("🚀 Multi-Object Tracking Project")

# Description
st.write("This project uses YOLOv8 for real-time object detection and tracking.")

# Video Section
st.subheader("🎥 Demo Output Video")

st.video("https://raw.githubusercontent.com/vishakha952/Tracking_Project/main/output_video.mp4")

# Project Details
st.subheader("📌 Project Details")

st.write("""
- 🔍 Model: YOLOv8  
- 🎯 Task: Multi-object detection & tracking  
- 🛠 Framework: OpenCV + Python  
- 📊 Type: Computer Vision Project  
""")

# Footer
st.markdown("---")
st.write("✅ Project by Vishakha")
