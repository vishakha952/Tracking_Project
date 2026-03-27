import streamlit as st

st.title("Multi-Object Tracking Project")

st.write("This project uses YOLOv8 for object detection and tracking.")

st.subheader("Demo Output Video")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.subheader("Project Details")
st.write("""
- Model: YOLOv8
- Task: Multi-object detection & tracking
- Framework: OpenCV + Python
""")