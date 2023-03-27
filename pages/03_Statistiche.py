import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
from pprint import pprint
from IPython.core.display import display, HTML
import plotly.express as px
from gsheetsdb import connect

st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Statistiche stagionali")

# Create a connection object.
conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl = 60)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

gol_gsheets_url = st.secrets["gol_gsheets_url"]
rows_gol = run_query(f'SELECT * FROM "{gol_gsheets_url}"')
df_gol = pd.DataFrame(rows_gol)
df_gol = df_gol.drop(columns = ['CT'])

corner_gsheets_url = st.secrets["corner_gsheets_url"]
rows_corner = run_query(f'SELECT * FROM "{corner_gsheets_url}"')
df_corner = pd.DataFrame(rows_corner)

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link

    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{"video"}</a>'



url_corner = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/CORNER.xlsx" # Make sure the url is the raw version of the file on GitHub
#df_corner = pd.read_excel(url_corner, usecols = "A:I")

url_gol = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/GOL.xlsx"
#df_gol = pd.read_excel(url_gol, usecols = "A:I")





squadra = "Venezia"

df_corner_Venezia = df_corner.loc[df_corner['ATTACCA'] == squadra]
df_corner_Venezia['LINK'] = df_corner_Venezia['LINK'].apply(make_clickable)
df_corner_Venezia = df_corner_Venezia.rename(columns =  {'DIFENDE' : 'SQUADRA'})
df_corner_Venezia = df_corner_Venezia.drop(columns = ['ATTACCA'])

list_corner_Venezia = df_corner_Venezia['SQUADRA'].tolist()
list_corner_Venezia = [*set(list_corner_Venezia)]
list_corner_Venezia.sort()
list_corner_Venezia.append('Tutti')

list_corner_difesa_Venezia = df_corner_Venezia['DIFESA'].tolist()
list_corner_difesa_Venezia = [*set(list_corner_difesa_Venezia)]
list_corner_difesa_Venezia.sort()
list_corner_difesa_Venezia.append('Tutti')

df_corner_vsVenezia = df_corner.loc[df_corner['DIFENDE'] == squadra]
df_corner_vsVenezia['LINK'] = df_corner_vsVenezia['LINK'].apply(make_clickable)
df_corner_vsVenezia = df_corner_vsVenezia.rename(columns =  {'ATTACCA' : 'SQUADRA'})
df_corner_vsVenezia = df_corner_vsVenezia.drop(columns = ['DIFENDE'])

list_corner_vsVenezia = df_corner_vsVenezia['SQUADRA'].tolist()
list_corner_vsVenezia = [*set(list_corner_vsVenezia)]
list_corner_vsVenezia.sort()
list_corner_vsVenezia.append('Tutti')

list_corner_difesa_vsVenezia = df_corner_vsVenezia['DIFESA'].tolist()
list_corner_difesa_vsVenezia = [*set(list_corner_difesa_vsVenezia)]
list_corner_difesa_vsVenezia.sort()
list_corner_difesa_vsVenezia.append('Tutti')

list_corner_avvbatt_vsVenezia = df_corner_vsVenezia['GIOC_SULLA_PALLA'].tolist()
list_corner_avvbatt_vsVenezia = [*set(list_corner_avvbatt_vsVenezia)]
list_corner_avvbatt_vsVenezia.sort()
list_corner_avvbatt_vsVenezia.append('Tutti')



df_golfatti_Venezia = df_gol.loc[df_gol['ATTACCA'] == squadra]
df_golfatti_Venezia = df_golfatti_Venezia.drop(columns = ['ATTACCA'])
df_golfatti_Venezia['LINK'] = df_golfatti_Venezia['LINK'].apply(make_clickable)
df_golfatti_Venezia = df_golfatti_Venezia.rename(columns =  {'DIFENDE' : 'SQUADRA'})

list_golfatti_Venezia = df_golfatti_Venezia['SQUADRA'].tolist()
list_golfatti_Venezia = [*set(list_golfatti_Venezia)]
list_golfatti_Venezia.sort()
list_golfatti_Venezia.append('Tutti')

list_marcatori_Venezia = df_golfatti_Venezia['GIOCATORE'].tolist()
list_marcatori_Venezia = [*set(list_marcatori_Venezia)]
list_marcatori_Venezia.sort()
list_marcatori_Venezia.append('Tutti')


df_golsubiti_Venezia = df_gol.loc[df_gol['DIFENDE'] == squadra]
df_golsubiti_Venezia = df_golsubiti_Venezia.drop(columns = ['DIFENDE'])
df_golsubiti_Venezia['LINK'] = df_golsubiti_Venezia['LINK'].apply(make_clickable)
df_golsubiti_Venezia = df_golsubiti_Venezia.rename(columns =  {'ATTACCA' : 'SQUADRA'})

list_golsubiti_Venezia = df_golsubiti_Venezia['SQUADRA'].tolist()
list_golsubiti_Venezia = [*set(list_golsubiti_Venezia)]
list_golsubiti_Venezia.sort()
list_golsubiti_Venezia.append('Tutte')


#Gol, Corner   = st.tabs(["Gol","Corner"])
Gol = st.tabs(["Gol"])

with Gol:

  Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])

  with Golfatti:

    Stats, Link = st.tabs(["Statistiche","Link"])

    with Stats:

      st.subheader(f'Tabella gol fatti :blue[{squadra}]')
      st.dataframe(df_golfatti_Venezia.drop(columns = ['LINK']), use_container_width=True)

      st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
      col1, col2, col3, col4 = st.columns(4)
      with col1:
        tmp_df_gfsqd = df_golfatti_Venezia.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
        tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
        #tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
        #tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

        st.bar_chart(tmp_df_gfsqd, use_container_width=True)
        st.dataframe(df_golfatti_Venezia['GIOCATORE'].value_counts().head(3), use_container_width=True)

      with col2:
        st.bar_chart(df_golfatti_Venezia['TEMPO'].value_counts(), use_container_width=True)
        st.dataframe(df_golfatti_Venezia['TEMPO'].value_counts(), use_container_width=True)	


      with col3:
        st.bar_chart(df_golfatti_Venezia['POSIZIONE'].value_counts(), use_container_width=True)
        st.dataframe(df_golfatti_Venezia['POSIZIONE'].value_counts(), use_container_width=True)				


      with col4:
        st.bar_chart(df_golfatti_Venezia['TIPO'].value_counts(), use_container_width=True)
        st.dataframe(df_golfatti_Venezia['TIPO'].value_counts(), use_container_width=True)				


    with Link:

      ind = len(list_marcatori_Venezia)-1
      golf_Venezia_giocatore, golf_Venezia_tempo, golf_Venezia_posizione = st.columns(3)

      with golf_Venezia_giocatore:

        optggfVenezia = st.selectbox(
                f'Seleziona marcatore della {squadra}:', list_marcatori_Venezia, index = ind)


      with golf_Venezia_tempo:

        optgfVenezia = st.selectbox(
                f'Seleziona tempo di gioco dei gol della {squadra}:',
                ("1T","2T",'ENTRAMBI'), index = 2)

      with golf_Venezia_posizione:

        oppgfVenezia = st.selectbox(
              f'Seleziona la posizione dei gol della {squadra}:',
              ("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)


      if(optggfVenezia == 'Tutti' and optgfVenezia  == 'ENTRAMBI' and oppgfVenezia == 'TUTTE' ):
          st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia != 'Tutti'and optgfVenezia  == 'ENTRAMBI' and oppgfVenezia == 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['GIOCATORE'] == optggfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia == 'Tutti'and optgfVenezia  != 'ENTRAMBI' and oppgfVenezia == 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['TEMPO'] == optgfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia == 'Tutti'and optgfVenezia  == 'ENTRAMBI' and oppgfVenezia != 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['POSIZIONE'] == oppgfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia != 'Tutti'and optgfVenezia  != 'ENTRAMBI' and oppgfVenezia == 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['GIOCATORE'] == optggfVenezia]
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['TEMPO'] == optgfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia == 'Tutti'and optgfVenezia  != 'ENTRAMBI' and oppgfVenezia != 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['POSIZIONE'] == oppgfVenezia]
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['TEMPO'] == optgfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia != 'Tutti'and optgfVenezia  == 'ENTRAMBI' and oppgfVenezia != 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['POSIZIONE'] == oppgfVenezia]
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['GIOCATORE'] == optggfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggfVenezia != 'Tutti'and optgfVenezia  != 'ENTRAMBI' and oppgfVenezia != 'TUTTE' ):
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['POSIZIONE'] == oppgfVenezia]
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['GIOCATORE'] == optggfVenezia]
        df_golfatti_Venezia = df_golfatti_Venezia.loc[df_golfatti_Venezia['TEMPO'] == optgfVenezia]
        st.write(df_golfatti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)




  with Golsubiti:

    Stats, Link = st.tabs(["Statistiche","Link"])

    with Stats:


      st.subheader(f'Tabella gol subiti :blue[{squadra}]')
      st.dataframe(df_golsubiti_Venezia.drop(columns = ['LINK']), use_container_width=True)

      st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


      col1, col2, col3, col4 = st.columns(4)
      with col1:

        tmp_df_gssqd = df_golsubiti_Venezia.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
        tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
        #tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
        #tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

        st.bar_chart(tmp_df_gssqd, use_container_width=True)
        st.dataframe(df_golsubiti_Venezia['SQUADRA'].value_counts().head(3), use_container_width=True)


      with col2:

        st.bar_chart(df_golsubiti_Venezia['TEMPO'].value_counts(), use_container_width=True)
        st.dataframe(df_golsubiti_Venezia['TEMPO'].value_counts(), use_container_width=True)				


      with col3:

        st.bar_chart(df_golsubiti_Venezia['POSIZIONE'].value_counts(), use_container_width=True)
        st.dataframe(df_golsubiti_Venezia['POSIZIONE'].value_counts(), use_container_width=True)				


      with col4:

        st.bar_chart(df_golsubiti_Venezia['TIPO'].value_counts(), use_container_width=True)
        st.dataframe(df_golsubiti_Venezia['TIPO'].value_counts(), use_container_width=True)				


    with Link:

      ind = len(list_golsubiti_Venezia)-1
      gols_Venezia_giocatore, gols_Venezia_tempo, gols_Venezia_posizione = st.columns(3)

      with gols_Venezia_giocatore:

        optggsVenezia = st.selectbox(
                f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Venezia, index = ind)


      with gols_Venezia_tempo:

        optgsVenezia = st.selectbox(
                f'Seleziona tempo di gioco dei gol alla {squadra}:',
                ("1T","2T",'ENTRAMBI'), index = 2)

      with gols_Venezia_posizione:

        oppgsVenezia = st.selectbox(
              f'Seleziona la posizione dei gol alla {squadra}:',
              ("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)


      if(optggsVenezia == 'Tutte' and optgsVenezia  == 'ENTRAMBI' and oppgsVenezia == 'TUTTE' ):
          st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia != 'Tutte'and optgsVenezia  == 'ENTRAMBI' and oppgsVenezia == 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['SQUADRA'] == optggsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia == 'Tutte'and optgsVenezia  != 'ENTRAMBI' and oppgsVenezia == 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['TEMPO'] == optgsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia == 'Tutte'and optgsVenezia  == 'ENTRAMBI' and oppgsVenezia != 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['POSIZIONE'] == oppgsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia != 'Tutte'and optgsVenezia  != 'ENTRAMBI' and oppgsVenezia == 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['SQUADRA'] == optggsVenezia]
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['TEMPO'] == optgsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia == 'Tutte'and optgsVenezia  != 'ENTRAMBI' and oppgsVenezia != 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['POSIZIONE'] == oppgsVenezia]
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['TEMPO'] == optgsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia != 'Tutte'and optgsVenezia  == 'ENTRAMBI' and oppgsVenezia != 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['POSIZIONE'] == oppgsVenezia]
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['SQUADRA'] == optggsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

      elif(optggsVenezia != 'Tutte'and optgsVenezia  != 'ENTRAMBI' and oppgsVenezia != 'TUTTE' ):
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['POSIZIONE'] == oppgsVenezia]
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['SQUADRA'] == optggsVenezia]
        df_golsubiti_Venezia = df_golsubiti_Venezia.loc[df_golsubiti_Venezia['TEMPO'] == optgsVenezia]
        st.write(df_golsubiti_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)


'''with Corner:

  Favore, Contro = st.tabs(["Corner a favore","Corner contro"])

  with Favore:

    ind_avv = len(list_corner_Venezia)-1
    ind_dif = len(list_corner_difesa_Venezia)-1

    avvVenezia, difesaVenezia = st.columns(2)

    with avvVenezia:
      op_avvVenezia = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Venezia, index = ind_avv)

    with difesaVenezia:
      op_difVenezia = st.selectbox(
            f'Seleziona tipo difesa avversario della {squadra}:',
            list_corner_difesa_Venezia, index = ind_dif)

    if(op_avvVenezia == 'Tutti'and op_difVenezia  == 'Tutti'):
      st.write(df_corner_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avvVenezia == 'Tutti'and op_difVenezia  != 'Tutti'):
      df_corner_Venezia = df_corner_Venezia.loc[df_corner_Venezia['DIFESA'] == op_difVenezia]
      st.write(df_corner_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avvVenezia != 'Tutti'and op_difVenezia  == 'Tutti'):
      df_corner_Venezia = df_corner_Venezia.loc[df_corner_Venezia['SQUADRA'] == op_avvVenezia]
      st.write(df_corner_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avvVenezia != 'Tutti'and op_difVenezia  != 'Tutti'):
      df_corner_Venezia = df_corner_Venezia.loc[df_corner_Venezia['SQUADRA'] == op_avvVenezia]
      df_corner_Venezia = df_corner_Venezia.loc[df_corner_Venezia['DIFESA'] == op_difVenezia]
      st.write(df_corner_Venezia.to_html(escape=False, index=False), unsafe_allow_html=True)

  with Contro:

    ind_avv = len(list_corner_vsVenezia)-1
    ind_avvbatt = len(list_corner_avvbatt_vsVenezia)-1

    avv_vsVenezia, difesa_vsVenezia = st.columns(2)

    with avv_vsVenezia:
      op_avv_vsVenezia = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsVenezia, index = ind_avv)

    with difesa_vsVenezia:
      op_avvbatt_vsVenezia = st.selectbox(
            f'Seleziona quanti giocatori avversari presenti in battuta:',
            list_corner_avvbatt_vsVenezia, index = ind_avvbatt)

    if(op_avv_vsVenezia == 'Tutti'and op_avvbatt_vsVenezia  == 'Tutti'):
      st.write(df_corner_vsVenezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avv_vsVenezia == 'Tutti'and op_avvbatt_vsVenezia  != 'Tutti'):
      df_corner_vsVenezia = df_corner_vsVenezia.loc[df_corner_vsVenezia['GIOC_SULLA_PALLA'] == op_avvbatt_vsVenezia]
      st.write(df_corner_vsVenezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avv_vsVenezia != 'Tutti'and op_avvbatt_vsVenezia  == 'Tutti'):
      df_corner_vsVenezia = df_corner_vsVenezia.loc[df_corner_vsVenezia['SQUADRA'] == op_avv_vsVenezia]
      st.write(df_corner_vsVenezia.to_html(escape=False, index=False), unsafe_allow_html=True)

    elif(op_avv_vsVenezia != 'Tutti'and op_avvbatt_vsVenezia  != 'Tutti'):
      df_corner_vsVenezia = df_corner_vsVenezia.loc[df_corner_vsVenezia['SQUADRA'] == op_avv_vsVenezia]
      df_corner_vsVenezia = df_corner_vsVenezia.loc[df_corner_vsVenezia['GIOC_SULLA_PALLA'] == op_avvbatt_vsVenezia]
      st.write(df_corner_vsVenezia.to_html(escape=False, index=False), unsafe_allow_html=True)
'''
