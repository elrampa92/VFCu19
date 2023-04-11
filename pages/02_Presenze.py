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

url_min = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/VENEZIA.xlsx" # Make sure the url is the raw version of the file on GitHub
df_min = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,D:AB") #dataframe con minutaggi pp

df_min_ts = pd.read_excel(url_min, sheet_name='minuti', usecols = "A,C,AH:AJ") #dataframe con minuti giocati + titolare e subentrato

df_status = pd.read_excel(url_min, sheet_name='stati', usecols = "A,C,AH:AO") #dataframe con stati pp





Minutaggi, Status= st.tabs(["Minutaggi", "Titolare / Subentrato"])

with Minutaggi:

  st.dataframe(df_min,use_container_width=True)
  #st.write(df_minutaggi.to_html(escape=False, index=False), unsafe_allow_html=True)
  bar_chart = alt.Chart(df_min_ts).mark_bar().encode(
      x = 'Giocatore', y = 'MINUTI TOTALI', tooltip=['Giocatore',  'MINUTI TOTALI'])
  st.altair_chart(bar_chart,use_container_width=True)
  option = st.selectbox(
        'Mostra i minutaggi per ruolo:',
        ('PT', 'DIF', 'CEN','ATT','TUTTI'), index = 4)


  col1, col2 = st.columns(2)



  with col1:


    if(option!='TUTTI'):
      st.dataframe(df_min_ts.loc[df_min_ts['Ruolo'] == option] ,use_container_width=False)

    else:
      st.dataframe(df_min_ts, use_container_width=False)



      #fig, ax = plt.subplots()
      #df_min_status.plot.bar(x = 'GIOCATORE', y = ['TITOLARE', 'SUBENTRATO'], ax = ax)
      #st.pyplot(fig)
    
  with col2:
    if(option!='TUTTI'):

      tmp_min_tot = df_min_ts.loc[df_min_ts['Ruolo'] == option]
      tmp_min_tot = tmp_min_tot.set_index('Giocatore')
      tmp_min_tot = tmp_min_tot.drop(columns = ['Ruolo','MINUTI TOTALI'])

      st.bar_chart(tmp_min_tot, use_container_width=True)

    else:
      

      tmp_min_status = df_min_ts.set_index('Giocatore')
      tmp_min_status = tmp_min_status.drop(columns = ['Ruolo','MINUTI TOTALI'])


      st.bar_chart(tmp_min_status, use_container_width=True)



    
  st.caption("Mattia Rampazzo - Vfc u19")

with Status:

  st.dataframe(df_status,use_container_width=True)

  tmp_df_stati = df_status.set_index('Giocatore')
  tmp_df_stati = tmp_df_stati.drop(columns = ['Ruolo'])
  st.caption("T = TITOLARE - S = SUBENTRATO - NE = NON ENTRATO - NC = NON CONVOCATO - 1SQ = IN PRIMA SQUADRA")
  st.caption("SQL = SQUALIFICATO - INF = INFORTUNATO - NAZ = IN NAZIONALE")

  st.bar_chart(tmp_df_stati, use_container_width=True)








  st.caption("Mattia Rampazzo - Vfc u19")
