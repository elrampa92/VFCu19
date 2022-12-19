import streamlit as st
import pandas as pd
import numpy as np
import requests
from pprint import pprint

st.write("provissima!")

### LEGGO DATAFRAME CON MINUTAGGI
url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content
tmp_minutaggi = pd.read_csv(url)

### NR DI COLONNE DEL DF
cols = len(tmp_minutaggi.axes[1])

### CREO LISTA CON INTESTAZIONI ED ELIMINO VALORI CHE NON SERVONO
fr_tmp = tmp_minutaggi.columns.tolist()
first_row = tmp_minutaggi.columns.tolist()
first_row.remove('PLAYER')
fr_tmp.remove('PLAYER')
for i in range (0, len(first_row),2):
  first_row.remove(fr_tmp[i])

### CREO DF DEI MINUTAGGI CHE ANDRO' A PULIRE DALLE COLONNE CHE NON SERVONO
df_minutaggi = pd.DataFrame()
df_minutaggi = df_minutaggi.append(tmp_minutaggi.iloc[:,[0]])
for i in range(len(first_row)):
  tmp_minutaggi.drop(first_row[i], inplace=True, axis=1)


st.write(df_minutaggi)
