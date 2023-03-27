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
#url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
#download = requests.get(url).content

url_min = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/VENEZIA.xlsx" # Make sure the url is the raw version of the file on GitHub
df_min = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,D:V") #dataframe con minutaggi pp

df_min_ts = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,AH:AJ") #dataframe con minuti giocati + titolare e subentrato

df_status = pd.read_excel(url_min, sheet_name='stati', usecols = "A,C,AH:AO") #dataframe con stati pp

df_gol_fatti = pd.read_excel(url_min, sheet_name='gol', usecols = "A,C,AH") #dataframe con gol fatti

col1, col2 = st.columns(2)

with col1:
   st.subheader("Top 5 per minuti giocati")
   tmp_df = df_min_ts.drop(columns = ['TITOLARE','SUBENTRATO'])
   tmp_df = tmp_df.sort_values(by = ['MINUTI TOTALI'], ascending=False)
   tmp_df = tmp_df.head(5)
   st.dataframe(tmp_df, use_container_width=True)
   #st.write(tmp_df.to_html(escape=False, index=False), unsafe_allow_html=True)

with col2:
   st.subheader("Top 5 marcatori")
   tmp_df_gf = df_gol_fatti.sort_values(by = ['GOL FATTI'], ascending=False)
   tmp_df_gf = tmp_df_gf.head(5)
   st.dataframe(tmp_df_gf, use_container_width=True)










st.caption("Mattia Rampazzo - Vfc u19")
