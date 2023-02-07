import streamlit as st
from PIL import Image

def gen_app():
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>New incentives rates</b></p>', unsafe_allow_html=True)
    st.write("What Incentive are given?")
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Why are they given?</b></p>', unsafe_allow_html=True)
    image = Image.open('../Data/resources/taxi_incentivization.png')
    st.image(image, caption='57 charging stations')
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>How you are going to get it?</b></p>', unsafe_allow_html=True)
    st.write("How you are going to get it?")
    
    