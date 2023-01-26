import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
import matplotlib.pyplot as plt
from pprint import pprint

st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Presenze 22/23")
st.header("Campionato Primavera 2 A")


st.sidebar.success(f"In questa pagina sarà possibile visualizzare i minutaggi di ogni singolo giocatore, da titolare e da subentrato.\nNella sezione Titolare / Subentrato si potrà visualizzare il riepilogo di quante volte un giocatore è partito titolare, entrato dalla panchina, infortunato ecc.")

### LEGGO DATAFRAME CON MINUTAGGI
url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

url_min = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.xlsx" # Make sure the url is the raw version of the file on GitHub
df_min = pd.read_excel(url_min, usecols = "A,B,AN")
df_min_status = pd.read_excel(url_min, usecols = "A,B,AL:AN")
df_status = pd.read_excel(url_min, usecols = "A,B,AC:AJ")

### CREO DATAFRAME PER DIVIDERE IL CSV INIZIALE
tmp_minutaggi = pd.read_csv(url)
tmp_stati= pd.read_csv(url)

### NR DI COLONNE DEL DF
cols = len(tmp_minutaggi.axes[1])

### CREO LISTA CON INTESTAZIONI
fr_tmp = tmp_minutaggi.columns.tolist()
fr_tmp.remove('GIOCATORE')
fr_tmp.remove('RUOLO')

### ELIMINO VALORI CHE NON SERVONO X MINUTAGGI
first_row_m = tmp_minutaggi.columns.tolist()
first_row_m.remove('GIOCATORE')
first_row_m.remove('RUOLO')
for i in range (0, len(first_row_m),2):
  first_row_m.remove(fr_tmp[i])


### ELIMINO VALORI CHE NON SERVONO X STATI
first_row_s = tmp_minutaggi.columns.tolist()
first_row_s.remove('GIOCATORE')
first_row_s.remove('RUOLO')
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

###################################################################################

#DA SISTEMARE SECONDO GRAFICO CON MINUTAGGI TITOLARI E SUBENTRATI

Minutaggi, Status= st.tabs(["Minutaggi", "Titolare / Subentrato"])

with Minutaggi:

  #st.dataframe(df_minutaggi,use_container_width=True, height = 1000)
  st.write(df_minutaggi.to_html(escape=False, index=False), unsafe_allow_html=True)

  option = st.selectbox(
      'Mostra i minutaggi per ruolo:',
      ('PT', 'DIF', 'CEN','ATT','TUTTI'), index = 4)

  df_sum_minuti_giocati = pd.DataFrame({'GIOCATORE':[],'RUOLO':[],'MINUTI GIOCATI':[]})
  df_sum_minuti_giocati['GIOCATORE'] = df_minutaggi['GIOCATORE']
  df_sum_minuti_giocati['RUOLO'] = df_minutaggi['RUOLO']
  df_sum_minuti_giocati['MINUTI GIOCATI'] = df_minutaggi.sum(axis=1)

  if(option!='TUTTI'):
    st.dataframe(df_min_status.loc[df_min_status['RUOLO'] == option] ,use_container_width=False)
    bar_chart = alt.Chart(df_min_status.loc[df_min_status['RUOLO'] == option]).mark_bar().encode(
      x = 'GIOCATORE', y = 'MINUTI TOTALI',tooltip=['GIOCATORE', 'MINUTI TOTALI'])
    st.altair_chart(bar_chart,use_container_width=True)

    tmp_min_status = df_min_status.loc[df_min_status['RUOLO'] == option]
    tmp_min_status = tmp_min_status.set_index('GIOCATORE')
    tmp_min_status = tmp_min_status.drop(columns = ['RUOLO','MINUTI TOTALI'])

    st.bar_chart(tmp_min_status, use_container_width=True)



  else:
    st.dataframe(df_min_status, use_container_width=False)
    bar_chart = alt.Chart(df_min_status).mark_bar().encode(
      x = 'GIOCATORE', y = 'MINUTI TOTALI', tooltip=['GIOCATORE',  'MINUTI TOTALI'])
    st.altair_chart(bar_chart,use_container_width=True)

    tmp_min_status = df_min_status.set_index('GIOCATORE')
    tmp_min_status = tmp_min_status.drop(columns = ['RUOLO','MINUTI TOTALI'])


    st.bar_chart(tmp_min_status, use_container_width=True)


    #fig, ax = plt.subplots()
    #df_min_status.plot.bar(x = 'GIOCATORE', y = ['TITOLARE', 'SUBENTRATO'], ax = ax)
    #st.pyplot(fig)
  
  st.caption("Mattia Rampazzo - Vfc u19")

with Status:

  st.dataframe(df_stati,use_container_width=True)

  tmp_df_stati = df_status.set_index('GIOCATORE')
  tmp_df_stati = tmp_df_stati.drop(columns = ['RUOLO'])
  st.caption("T = TITOLARE - S = SUBENTRATO - NE = NON ENTRATO - NC = NON CONVOCATO - 1SQ = IN PRIMA SQUADRA")
  st.caption("SQL = SQUALIFICATO - INF = INFORTUNATO - NAZ = IN NAZIONALE")

  st.bar_chart(tmp_df_stati, use_container_width=True)


  st.dataframe(df_status,use_container_width=True)





  st.caption("Mattia Rampazzo - Vfc u19")