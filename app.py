import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium
st.markdown("<center><h1>Radio Link Failure Prediction</h1></center>",unsafe_allow_html=True)
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


st.sidebar.image("./prodal.png")

c = st.sidebar.columns(2)
c[0].date_input("Today:")
c[1].time_input("Time")
opt = st.sidebar.selectbox("Choose Option",["Data Visualisation","Inference"])
if opt =="Inference":
     st.sidebar.selectbox("Choose Region",["Antakia","Galata Saray","Beshktash","Ankara","finer Batsh","Istunbul"])




if opt=="Data Visualisation":
     with st.expander("Dashbord"):
          p = open("./SWEETVIZ_REPORT.html")
          components.html(p.read(),height=10000,width=2500)


