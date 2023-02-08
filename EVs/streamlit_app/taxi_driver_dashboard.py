import streamlit as st
from PIL import Image

def gen_app():
    image = Image.open('../Data/resources/taxi_driver_poster.jpg')
    st.image(image)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 30px;"><b>Welcome: Mark</b></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Account number: </b> 0379812</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Vehicle type: </b> Electric Hackney Cab</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Operated under a business fleet?: </b> yes</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Business fleet name: </b> IoW cabs ltd</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Registered cab driver since: </b> 07 June 2015</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Last electric meter reading: </b> 00036751.08</p>', unsafe_allow_html=True)

    st.markdown('''&nbsp;&nbsp;&nbsp;<p style="font-family:sans-serif; color:Black; font-size: 18px;">We are excited to announce new incentives designed to reward and support your hard work. Our goal is to help you earn more and provide a better experience for your passengers. 
    We are committed to supporting our taxi drivers and helping you succeed. We hope these new incentives will make your job easier and more enjoyable.</p>''', unsafe_allow_html=True)

    st.markdown('''&nbsp;&nbsp;&nbsp;<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Following are new winter peek and off-peak hours and charges for different charging types.</b></p>''', unsafe_allow_html=True)
    col1, col2, col4 = st.columns(3)
    with col1:
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Charging at home</b></p>', unsafe_allow_html=True)
        image = Image.open('../Data/resources/taxi_home.jpg')
        st.image(image)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak hours: </b>7AM to 9AM, 5PM to 7PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak prices: </b>£0.17 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>7PM to 7AM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.04 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>9AM to 5PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.10 per Kw</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Charging on the go</b></p>', unsafe_allow_html=True)
        image = Image.open('../Data/resources/taxi_public.jpg')
        st.image(image)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak hours: </b>8AM to 10AM, 3PM to 6PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak prices: </b>£0.28 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>6PM to 8AM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.03 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>10AM to 3PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.12 per Kw</p>', unsafe_allow_html=True)
    with col4:
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Charging on the fleet chargers</b></p>', unsafe_allow_html=True)
        image = Image.open('../Data/resources/taxi_business.jpg')
        st.image(image)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak hours: </b>8AM to 10AM, 3PM to 6PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Peak prices: </b>£0.26 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>6PM to 8AM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.04 per Kw</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>10AM to 3PM</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans-serif; color:Black; font-size: 18px;"><b>Winter Off-Peak hours: </b>£0.11 per Kw</p>', unsafe_allow_html=True)
    
    