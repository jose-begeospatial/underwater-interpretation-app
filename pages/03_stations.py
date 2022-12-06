# -*- coding: utf-8 -*-
import streamlit as st
import cv2
from PIL import Image 

st.set_page_config(
    page_title="Station", 
    layout='wide')

stations_list = ['station_01', 'station_02', 'statin_03']

st.sidebar.header("Select station for interpretation")
selected_station = st.sidebar.selectbox(
    label = 'Select station',
    options  = stations_list
)

selected_platform = st.sidebar.radio(
    label='method', 
    options=[
        'Underwater video',
        'Lander camera']
    )

video_url = ''
upload_image = None

if selected_platform == 'Lander camera':
    upload_image = st.sidebar.file_uploader("Choose video", type=["png"])
else:
    video_url = st.sidebar.text_input(
    'video URL',
    value="")


 


col1, col2 = st.columns([3,1], gap="medium") 

with col1:
    #

    if video_url is not "":
        st.video(video_url)

    if upload_image is not None:
        st.image(upload_image)

 
 
with col2:

    st.header(selected_platform)
        
    current_frame = st.selectbox(
        label='Frames',
        options=[1,2,3,4,5,6,7,8,9,10] )

    biota_expander = st.expander("Biota", expanded=True)
    with biota_expander:
        st.multiselect(
            label='select',
            options={
                'species1':'species 01', 
                'species2': 'species 02',
                'species3': 'species 03'}
        )
    substrates_expander = st.expander("Substrates", expanded=True)
    with substrates_expander:
        st.selectbox(
            label='select',
            options={
                'substrate1':'substrate 01',
                'substrate2': 'substrate 02',
                'substrate3': 'substrate 03',            }
            )

