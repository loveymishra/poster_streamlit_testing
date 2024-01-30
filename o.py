import streamlit as st
import pandas as pd

a=pd.read_csv("poster_links.csv")
img=a['links']
ttl=a['id']





for i in range(0,len(img)):
    st.image(img[i],ttl[i])


