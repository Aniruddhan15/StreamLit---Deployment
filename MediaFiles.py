import streamlit as st 
from PIL import Image

#Image
st.title('Image Data')
img = Image.open("C:\StreamLit\WIN_20240117_00_01_50_Pro.jpg")
st.image(img)

#Video
st.title('Video')
video = open('')
st.video(video,start_time=23)

#Audio
st.title('Audio Data')
audio = open('')
st.audio(audio)