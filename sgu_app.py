# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(
    page_title="SGU underwater video/photo interpretation app",
    page_icon='./assets/sgu-logotype-blue-eng-489.png'
)

# Fix style issues
hide_streamlit_style = """
           <style>
            footer {

	visibility: hidden;

	}
footer:after {
	content:'Be GeoSpatial powered by Streamlit';
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
            .sidebar .sidebar-content {
    background-color: #f0f2f6;
    background-image: linear-gradient(
180deg
,#f0f2f6,#fafafa);
    background-attachment: fixed;
    box-sizing: border-box;
    flex-shrink: 0;
    height: 100vh;
    overflow: auto;
    padding: 0rem 1rem;
    position: relative;
    transition: margin-left .3s,box-shadow .3s;
    width: 21rem;
    z-index: 100;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



st.sidebar.title("Tasks")

st.markdown(
    """
    # Geological Survey of Sweden (SGU)  
    """
)