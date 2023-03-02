import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
import matplotlib.pyplot as plt
from pprint import pprint


st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Homepage")
st.sidebar.success("Seleziona una pagina")

### LEGGO DATAFRAME CON MINUTAGGI
url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

url_min = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/VENEZIA.xlsx" # Make sure the url is the raw version of the file on GitHub
df_min = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,D:V") #dataframe con minutaggi pp

df_min_ts = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,AH:AJ") #dataframe con minuti giocati + titolare e subentrato

df_status = pd.read_excel(url_min, sheet_name='stati', usecols = "A,C,AH:AO") #dataframe con stati pp

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Top 10 Minuti giocati")
   tmp_df = df_min_ts.drop(columns = ['TITOLARE','SUBENTRATO'])
   tmp_df = tmp_df.sort_values(by = ['MINUTI TOTALI'], ascending=False)
   tmp_df = tmp_df.head(10)
   st.dataframe(tmp_df, use_container_width=True)
   #st.write(tmp_df.to_html(escape=False, index=False), unsafe_allow_html=True)

with col2:
   st.subheader("Top 10 marcatori")

with col3:
   st.subheader("prova")










st.caption("Mattia Rampazzo - Vfc u19")
