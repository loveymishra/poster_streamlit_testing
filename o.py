import streamlit as st
import pandas as pd
import  numpy as np
import hydralit_components as hc

a=pd.read_csv("C:\\Users\\PC\\Desktop\\Datasets\\poster_links.csv")
img=a['links']
ttl=a['id']





for i in range(0,len(img)):
    st.image(img[i],ttl[i])


# url="https://2.bp.blogspot.com/-2O82E16W6tQ/T1tkTXaTdRI/AAAAAAAANZY/OFiSWeruBvc/s1600/Pagani_Huayra_Side_Profile.jpg"
# vid="https://d2ox13tjqpxop5.cloudfront.net/BUGATTI-2023/Bugatti-Models/Super-Sport/chiron-super-sport-intro-desktop.mp4"
# aud="https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/few_off/sian-fkp-37/feel_the_engine/sian_rds_8D.m4a"
# vid2="https://www.youtube.com/watch?v=puc_FEFmxxY"
# st.image(url,"Pagani huayra")
# st.audio(aud)
# st.video(vid2)

#
# st.balloons()
# st.snow()
# st.write("[![Follow](<https://img.shields.io/twitter/follow/><username>?style=social)](<https://www.twitter.com/><username>)")
# st.toast('Mr Stay-Puft')
# st.error('Error message')
# st.warning('Warning message')
# st.info('Info message')
# st.success('Success message')
# st.exception("loj")