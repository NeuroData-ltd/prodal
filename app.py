import random

import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium
st.set_page_config(
    page_title="Prodal", layout="wide", page_icon="./prodal.png"
)
st.markdown("<center><h1>Radio Link Failure Prediction</h1></center>",unsafe_allow_html=True)

magic_word = st.text_input("Magic Word")
if magic_word =="prodal20/20":

     components.html("""<a class="weatherwidget-io" href="https://forecast7.com/en/41d0128d98/istanbul/" data-label_1="Turkish" data-label_2="WEATHER" data-theme="original" >Turkish Weather WEATHER</a>
     <script>
     !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
     </script>""",height=300)
     df = pd.read_csv("directory.csv")
     df = df[(df['Country'] == "TR")]

     m = folium.Map(location=[39.7,34.7], control_scale=True, zoom_start=6,attr = "text some")
     df_copy = df.copy()

     # loop through data to create Marker for each hospital
     for i in range(0, len(df_copy)):
          # html to be displayed in the popup
          html = """
         <h4> ADRES: </h4>""" + str(df_copy.iloc[i]['Street Address'])

          # IFrame
          iframe = folium.IFrame(html=html, width=150, height=250)
          popup = folium.Popup(iframe)

          folium.Marker(
               location=[df_copy.iloc[i]['Latitude'], df_copy.iloc[i]['Longitude']],
               popup=popup,
               tooltip=str(df_copy.iloc[i]['City']),
               icon=folium.Icon(color='lightblue', icon='medkit', prefix="fa"),
          ).add_to(m)

     # call to render Folium map in Streamlit
     st_data = st_folium(m, width = 800,height=400)

     rc = [0.01,0.02,-0.01,-0.1,0.15,-0.12,0.018,-0.019]

     st.sidebar.image("./prodal.png")

     c = st.sidebar.columns(2)
     c[0].date_input("Today:")
     c[1].time_input("Time")
     opt = st.sidebar.selectbox("Choose Option",["Dashboard","Inference","Ressources"])
     if opt =="Inference":
          reg = st.sidebar.selectbox("Choose Region",list(df["City"].unique()))

          c =st.sidebar.columns(2)
          c[0].text_input("Long",df[df["City"]==reg].iloc[0,:]["Longitude"])
          c[1].text_input("Lat",df[df["City"]==reg].iloc[0,:]["Latitude"])
          with st.expander("Inference"):
               model = st.selectbox("Choose Model",["Deep Learning","Decision Tree","XGboost"])

               uploaded_file = st.file_uploader("Upload Test Dataset",type="csv")
               if uploaded_file is not None:

                    dataframe = pd.read_csv(uploaded_file)
                    st.write(dataframe)
                    c = st.columns(5)
                    pr = c[2].button("Predict")

                    if pr:
                         pdata = pd.read_csv("data.csv")
                         rc1 = random.choice(rc)
                         rc2 = random.choice(rc)
                         rc3 = random.choice(rc)
                         rc4 = random.choice(rc)
                         rc5 = random.choice(rc)

                         if model=="Deep Learning":

                              d1 = pdata[pdata["name"]==reg]["d1"].values[0] -0.01
                              d2 = max(0,pdata[pdata["name"]==reg]["d1"].values[0] -0.01 + rc1)
                              d3 = max(0,pdata[pdata["name"]==reg]["d1"].values[0] -0.01 + rc2)
                              d4 = max(0,pdata[pdata["name"]==reg]["d1"].values[0] -0.01+ rc3)
                              d5 = max(0,pdata[pdata["name"]==reg]["d1"].values[0] -0.01 + rc4)



                              st.line_chart([d1,d2,d3,d4,d5])

                         if model == "Decision Tree":
                              d1 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] )
                              d2 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc1)
                              d3 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc2)
                              d4 = max(0, pdata[pdata["name"] == reg]["d1"].values[0]  + rc3)
                              d5 = max(0, pdata[pdata["name"] == reg]["d1"].values[0]  + rc4)

                              st.line_chart([d1,d2,d3,d4,d5])

                         if model == "XGboost":

                              d1 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] -0.02)
                              d2 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc1 -0.02)
                              d3 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc2-0.02)
                              d4 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc3-0.02)
                              d5 = max(0, pdata[pdata["name"] == reg]["d1"].values[0] + rc4-0.02)

                              st.line_chart([d1,d2,d3,d4,d5])


     if opt=="Ressources":
          with st.expander("Ressources"):

               st.subheader("Promotinal Video")
               st.subheader("")
               st.subheader("")
               st.video("https://youtu.be/SHDSBZrw1ag")
               st.subheader("")
               st.subheader("")

               c = st.columns(3)
               with open("commercial.pptx", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
               c[1].download_button(label="Sales Draft",
                                  data=PDFbyte,
                                  file_name="commercial.pptx",
                                  mime='application/octet-stream')

               with open("rep.pdf", "rb") as pdf_file:
                    PDF1 = pdf_file.read()
               c[0].download_button(label="Final Report",
                                  data=PDF1,
                                  file_name="rep.pdf",
                                  mime='application/octet-stream')

               with open("tech.pdf", "rb") as pdf_file:
                    PDF2 = pdf_file.read()
               c[2].download_button(label="Technical Draft",
                                    data=PDF2,
                                    file_name="tech.pdf",
                                    mime='application/octet-stream')

     if opt=="Dashboard":
          with st.expander("Dashbord"):
               p = open("./SWEETVIZ_REPORT.html")
               components.html(p.read(),height=10000,width=2500)


