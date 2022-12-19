import streamlit as st
import pandas as pd
import numpy as np
import requests
from pprint import pprint

st.write("provissima!")

### LEGGO DATAFRAME CON MINUTAGGI
url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

### CREO DATAFRAME PER DIVIDERE IL CSV INIZIALE
tmp_minutaggi = pd.read_csv(url)
tmp_stati= pd.read_csv(url)

### NR DI COLONNE DEL DF
cols = len(tmp_minutaggi.axes[1])

### CREO LISTA CON INTESTAZIONI
fr_tmp = tmp_minutaggi.columns.tolist()
fr_tmp.remove('PLAYER')

### ELIMINO VALORI CHE NON SERVONO X MINUTAGGI
first_row_m = tmp_minutaggi.columns.tolist()
first_row_m.remove('PLAYER')
for i in range (0, len(first_row_m),2):
  first_row_m.remove(fr_tmp[i])


### ELIMINO VALORI CHE NON SERVONO X STATI
first_row_s = tmp_minutaggi.columns.tolist()
first_row_s.remove('PLAYER')
for i in range (1, len(first_row_s),2):
  first_row_s.remove(fr_tmp[i])

### CREO DF DEI MINUTAGGI CHE ANDRO' A PULIRE DALLE COLONNE CHE NON SERVONO
df_minutaggi = tmp_minutaggi
for i in range(len(first_row_m)):
  df_minutaggi.drop(first_row_m[i], inplace=True, axis=1)

### CREO DF DEGLI STATI CHE ANDRO' A PULIRE DALLE COLONNE CHE NON SERVONO
df_stati = tmp_stati
for i in range(len(first_row_s)):
  df_stati.drop(first_row_s[i], inplace=True, axis=1)

st.dataframe(df_minutaggi)

df_sum_minuti_giocati = pd.DataFrame({'PLAYER':[],'MINUTI GIOCATI':[]})
df_sum_minuti_giocati['PLAYER'] = df_minutaggi['PLAYER']
df_sum_minuti_giocati['MINUTI GIOCATI'] = df_minutaggi.sum(axis=1)

st.dataframe(df_sum_minuti_giocati)

bar_chart = alt.Chart(df_sum_minuti_giocati).mark_bar().encode(x = 'PLAYER', y = 'MINUTI GIOCATI')
st.altair_chart(bar_chart)
