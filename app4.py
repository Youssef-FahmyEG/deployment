import streamlit as st
import pandas as pd
import plotly.express as px

tips = px.data.tips()

def page1() :
    st.button("Pages")
    st.text_input("Email")
def page2() :
    st.date_input("DOB")
    st.plotly_chart(px.histogram(data_frame = tips , x = "total_bill" , nbins = 50 , color = "sex" , color_discrete_sequence =["blue" , "black"] , facet_col = "day" , marginal = "violin"))

pages = {"First_page" : page1 ,
"second_page" : page2}

select_page = st.sidebar.selectbox("Select Page" , pages.keys())
pages[select_page]()
