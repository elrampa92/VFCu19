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
st.title("Avversari")


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

Albinoleffe, Alessandria, Brescia, Cittadella, Como, Cremonese, Feralpisalò, Genoa, LRVicenza, Monza, Padova, Parma, Pordenone, Reggiana, Spal = st.tabs(
	["Albinoleffe","Alessandria","Brescia","Cittadella","Como","Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Padova", "Parma", "Pordenone", "Reggiana", "Spal"])

with Brescia:
	
	
	squadra = "Brescia"

	df_corner_Brescia = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Brescia['LINK'] = df_corner_Brescia['LINK'].apply(make_clickable)
	df_corner_Brescia = df_corner_Brescia.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Brescia = df_corner_Brescia.drop(columns = ['ATTACCA'])
	
	list_corner_Brescia = df_corner_Brescia['SQUADRA'].tolist()
	list_corner_Brescia = [*set(list_corner_Brescia)]
	list_corner_Brescia.sort()
	list_corner_Brescia.append('Tutti')

	list_corner_difesa_Brescia = df_corner_Brescia['DIFESA'].tolist()
	list_corner_difesa_Brescia = [*set(list_corner_difesa_Brescia)]
	list_corner_difesa_Brescia.sort()
	list_corner_difesa_Brescia.append('Tutti')
	
	df_corner_vsBrescia = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsBrescia['LINK'] = df_corner_vsBrescia['LINK'].apply(make_clickable)
	df_corner_vsBrescia = df_corner_vsBrescia.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsBrescia = df_corner_vsBrescia.drop(columns = ['DIFENDE'])
	
	list_corner_vsBrescia = df_corner_vsBrescia['SQUADRA'].tolist()
	list_corner_vsBrescia = [*set(list_corner_vsBrescia)]
	list_corner_vsBrescia.sort()
	list_corner_vsBrescia.append('Tutti')

	list_corner_difesa_vsBrescia = df_corner_vsBrescia['DIFESA'].tolist()
	list_corner_difesa_vsBrescia = [*set(list_corner_difesa_vsBrescia)]
	list_corner_difesa_vsBrescia.sort()
	list_corner_difesa_vsBrescia.append('Tutti')
	
	list_corner_avvbatt_vsBrescia = df_corner_vsBrescia['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsBrescia = [*set(list_corner_avvbatt_vsBrescia)]
	list_corner_avvbatt_vsBrescia.sort()
	list_corner_avvbatt_vsBrescia.append('Tutti')


	
	df_golfatti_Brescia = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Brescia = df_golfatti_Brescia.drop(columns = ['ATTACCA'])
	df_golfatti_Brescia['LINK'] = df_golfatti_Brescia['LINK'].apply(make_clickable)
	df_golfatti_Brescia = df_golfatti_Brescia.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Brescia = df_golfatti_Brescia['SQUADRA'].tolist()
	list_golfatti_Brescia = [*set(list_golfatti_Brescia)]
	list_golfatti_Brescia.sort()
	list_golfatti_Brescia.append('Tutti')
	
	list_marcatori_Brescia = df_golfatti_Brescia['GIOCATORE'].tolist()
	list_marcatori_Brescia = [*set(list_marcatori_Brescia)]
	list_marcatori_Brescia.sort()
	list_marcatori_Brescia.append('Tutti')
	
	
	df_golsubiti_Brescia = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Brescia = df_golsubiti_Brescia.drop(columns = ['DIFENDE'])
	df_golsubiti_Brescia['LINK'] = df_golsubiti_Brescia['LINK'].apply(make_clickable)
	df_golsubiti_Brescia = df_golsubiti_Brescia.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Brescia = df_golsubiti_Brescia['SQUADRA'].tolist()
	list_golsubiti_Brescia = [*set(list_golsubiti_Brescia)]
	list_golsubiti_Brescia.sort()
	list_golsubiti_Brescia.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Brescia.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Brescia.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Brescia['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Brescia['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Brescia['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Brescia['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Brescia['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Brescia['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Brescia['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Brescia)-1
				golf_Brescia_giocatore, golf_Brescia_tempo, golf_Brescia_posizione = st.columns(3)

				with golf_Brescia_giocatore:
				
					optggfBrescia = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:', list_marcatori_Brescia, index = ind)
			
				
				with golf_Brescia_tempo:
				
					optgfBrescia = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Brescia_posizione:
				
					oppgfBrescia = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfBrescia == 'Tutti' and optgfBrescia  == 'ENTRAMBI' and oppgfBrescia == 'TUTTE' ):
						st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia != 'Tutti'and optgfBrescia  == 'ENTRAMBI' and oppgfBrescia == 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['GIOCATORE'] == optggfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia == 'Tutti'and optgfBrescia  != 'ENTRAMBI' and oppgfBrescia == 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['TEMPO'] == optgfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia == 'Tutti'and optgfBrescia  == 'ENTRAMBI' and oppgfBrescia != 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['POSIZIONE'] == oppgfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia != 'Tutti'and optgfBrescia  != 'ENTRAMBI' and oppgfBrescia == 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['GIOCATORE'] == optggfBrescia]
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['TEMPO'] == optgfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia == 'Tutti'and optgfBrescia  != 'ENTRAMBI' and oppgfBrescia != 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['POSIZIONE'] == oppgfBrescia]
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['TEMPO'] == optgfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia != 'Tutti'and optgfBrescia  == 'ENTRAMBI' and oppgfBrescia != 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['POSIZIONE'] == oppgfBrescia]
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['GIOCATORE'] == optggfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfBrescia != 'Tutti'and optgfBrescia  != 'ENTRAMBI' and oppgfBrescia != 'TUTTE' ):
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['POSIZIONE'] == oppgfBrescia]
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['GIOCATORE'] == optggfBrescia]
					df_golfatti_Brescia = df_golfatti_Brescia.loc[df_golfatti_Brescia['TEMPO'] == optgfBrescia]
					st.write(df_golfatti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Brescia.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Brescia.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Brescia['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Brescia['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Brescia['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Brescia['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Brescia['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Brescia['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Brescia['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Brescia)-1
				gols_Brescia_giocatore, gols_Brescia_tempo, gols_Brescia_posizione = st.columns(3)

				with gols_Brescia_giocatore:
				
					optggsBrescia = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Brescia, index = ind)
			
				
				with gols_Brescia_tempo:
				
					optgsBrescia = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Brescia_posizione:
				
					oppgsBrescia = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsBrescia == 'Tutte' and optgsBrescia  == 'ENTRAMBI' and oppgsBrescia == 'TUTTE' ):
						st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia != 'Tutte'and optgsBrescia  == 'ENTRAMBI' and oppgsBrescia == 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['SQUADRA'] == optggsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia == 'Tutte'and optgsBrescia  != 'ENTRAMBI' and oppgsBrescia == 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['TEMPO'] == optgsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia == 'Tutte'and optgsBrescia  == 'ENTRAMBI' and oppgsBrescia != 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['POSIZIONE'] == oppgsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia != 'Tutte'and optgsBrescia  != 'ENTRAMBI' and oppgsBrescia == 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['SQUADRA'] == optggsBrescia]
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['TEMPO'] == optgsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia == 'Tutte'and optgsBrescia  != 'ENTRAMBI' and oppgsBrescia != 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['POSIZIONE'] == oppgsBrescia]
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['TEMPO'] == optgsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia != 'Tutte'and optgsBrescia  == 'ENTRAMBI' and oppgsBrescia != 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['POSIZIONE'] == oppgsBrescia]
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['SQUADRA'] == optggsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsBrescia != 'Tutte'and optgsBrescia  != 'ENTRAMBI' and oppgsBrescia != 'TUTTE' ):
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['POSIZIONE'] == oppgsBrescia]
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['SQUADRA'] == optggsBrescia]
					df_golsubiti_Brescia = df_golsubiti_Brescia.loc[df_golsubiti_Brescia['TEMPO'] == optgsBrescia]
					st.write(df_golsubiti_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Brescia)-1
			ind_dif = len(list_corner_difesa_Brescia)-1

			avvBrescia, difesaBrescia = st.columns(2)

			with avvBrescia:
				op_avvBrescia = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Brescia, index = ind_avv)
			
			with difesaBrescia:
				op_difBrescia = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Brescia, index = ind_dif)

			if(op_avvBrescia == 'Tutti'and op_difBrescia  == 'Tutti'):
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvBrescia == 'Tutti'and op_difBrescia  != 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['DIFESA'] == op_difBrescia]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvBrescia != 'Tutti'and op_difBrescia  == 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['SQUADRA'] == op_avvBrescia]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvBrescia != 'Tutti'and op_difBrescia  != 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['SQUADRA'] == op_avvBrescia]
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['DIFESA'] == op_difBrescia]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsBrescia)-1
			ind_avvbatt = len(list_corner_avvbatt_vsBrescia)-1

			avv_vsBrescia, difesa_vsBrescia = st.columns(2)

			with avv_vsBrescia:
				op_avv_vsBrescia = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsBrescia, index = ind_avv)

			with difesa_vsBrescia:
				op_avvbatt_vsBrescia = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:',
			      	list_corner_avvbatt_vsBrescia, index = ind_avvbatt)

			if(op_avv_vsBrescia == 'Tutti'and op_avvbatt_vsBrescia  == 'Tutti'):
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsBrescia == 'Tutti'and op_avvbatt_vsBrescia  != 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['GIOC_SULLA_PALLA'] == op_avvbatt_vsBrescia]
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsBrescia != 'Tutti'and op_avvbatt_vsBrescia  == 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['SQUADRA'] == op_avv_vsBrescia]
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsBrescia != 'Tutti'and op_avvbatt_vsBrescia  != 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['SQUADRA'] == op_avv_vsBrescia]
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['GIOC_SULLA_PALLA'] == op_avvbatt_vsBrescia]
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

with Cremonese:
	
	
	squadra = "Cremonese"

	df_corner_Cremonese = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Cremonese['LINK'] = df_corner_Cremonese['LINK'].apply(make_clickable)
	df_corner_Cremonese = df_corner_Cremonese.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Cremonese = df_corner_Cremonese.drop(columns = ['ATTACCA'])
	
	list_corner_Cremonese = df_corner_Cremonese['SQUADRA'].tolist()
	list_corner_Cremonese = [*set(list_corner_Cremonese)]
	list_corner_Cremonese.sort()
	list_corner_Cremonese.append('Tutti')

	list_corner_difesa_Cremonese = df_corner_Cremonese['DIFESA'].tolist()
	list_corner_difesa_Cremonese = [*set(list_corner_difesa_Cremonese)]
	list_corner_difesa_Cremonese.sort()
	list_corner_difesa_Cremonese.append('Tutti')
	
	df_corner_vsCremonese = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsCremonese['LINK'] = df_corner_vsCremonese['LINK'].apply(make_clickable)
	df_corner_vsCremonese = df_corner_vsCremonese.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsCremonese = df_corner_vsCremonese.drop(columns = ['DIFENDE'])
	
	list_corner_vsCremonese = df_corner_vsCremonese['SQUADRA'].tolist()
	list_corner_vsCremonese = [*set(list_corner_vsCremonese)]
	list_corner_vsCremonese.sort()
	list_corner_vsCremonese.append('Tutti')

	list_corner_difesa_vsCremonese = df_corner_vsCremonese['DIFESA'].tolist()
	list_corner_difesa_vsCremonese = [*set(list_corner_difesa_vsCremonese)]
	list_corner_difesa_vsCremonese.sort()
	list_corner_difesa_vsCremonese.append('Tutti')
	
	list_corner_avvbatt_vsCremonese = df_corner_vsCremonese['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsCremonese = [*set(list_corner_avvbatt_vsCremonese)]
	list_corner_avvbatt_vsCremonese.sort()
	list_corner_avvbatt_vsCremonese.append('Tutti')


	
	df_golfatti_Cremonese = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Cremonese = df_golfatti_Cremonese.drop(columns = ['ATTACCA'])
	df_golfatti_Cremonese['LINK'] = df_golfatti_Cremonese['LINK'].apply(make_clickable)
	df_golfatti_Cremonese = df_golfatti_Cremonese.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Cremonese = df_golfatti_Cremonese['SQUADRA'].tolist()
	list_golfatti_Cremonese = [*set(list_golfatti_Cremonese)]
	list_golfatti_Cremonese.sort()
	list_golfatti_Cremonese.append('Tutti')
	
	list_marcatori_Cremonese = df_golfatti_Cremonese['GIOCATORE'].tolist()
	list_marcatori_Cremonese = [*set(list_marcatori_Cremonese)]
	list_marcatori_Cremonese.sort()
	list_marcatori_Cremonese.append('Tutti')
	
	
	df_golsubiti_Cremonese = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Cremonese = df_golsubiti_Cremonese.drop(columns = ['DIFENDE'])
	df_golsubiti_Cremonese['LINK'] = df_golsubiti_Cremonese['LINK'].apply(make_clickable)
	df_golsubiti_Cremonese = df_golsubiti_Cremonese.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Cremonese = df_golsubiti_Cremonese['SQUADRA'].tolist()
	list_golsubiti_Cremonese = [*set(list_golsubiti_Cremonese)]
	list_golsubiti_Cremonese.sort()
	list_golsubiti_Cremonese.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Cremonese.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Cremonese.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Cremonese['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Cremonese['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Cremonese['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Cremonese['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Cremonese['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Cremonese['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Cremonese['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Cremonese)-1
				golf_Cremonese_giocatore, golf_Cremonese_tempo, golf_Cremonese_posizione = st.columns(3)

				with golf_Cremonese_giocatore:
				
					optggfCremonese = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:', list_marcatori_Cremonese, index = ind)
			
				
				with golf_Cremonese_tempo:
				
					optgfCremonese = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Cremonese_posizione:
				
					oppgfCremonese = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfCremonese == 'Tutti' and optgfCremonese  == 'ENTRAMBI' and oppgfCremonese == 'TUTTE' ):
						st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese != 'Tutti'and optgfCremonese  == 'ENTRAMBI' and oppgfCremonese == 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese == 'Tutti'and optgfCremonese  != 'ENTRAMBI' and oppgfCremonese == 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['TEMPO'] == optgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese == 'Tutti'and optgfCremonese  == 'ENTRAMBI' and oppgfCremonese != 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['POSIZIONE'] == oppgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese != 'Tutti'and optgfCremonese  != 'ENTRAMBI' and oppgfCremonese == 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['TEMPO'] == optgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese == 'Tutti'and optgfCremonese  != 'ENTRAMBI' and oppgfCremonese != 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['POSIZIONE'] == oppgfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['TEMPO'] == optgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese != 'Tutti'and optgfCremonese  == 'ENTRAMBI' and oppgfCremonese != 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['POSIZIONE'] == oppgfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfCremonese != 'Tutti'and optgfCremonese  != 'ENTRAMBI' and oppgfCremonese != 'TUTTE' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['POSIZIONE'] == oppgfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['TEMPO'] == optgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Cremonese.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Cremonese.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Cremonese['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Cremonese['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Cremonese['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Cremonese['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Cremonese['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Cremonese['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Cremonese['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Cremonese)-1
				gols_Cremonese_giocatore, gols_Cremonese_tempo, gols_Cremonese_posizione = st.columns(3)

				with gols_Cremonese_giocatore:
				
					optggsCremonese = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Cremonese, index = ind)
			
				
				with gols_Cremonese_tempo:
				
					optgsCremonese = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Cremonese_posizione:
				
					oppgsCremonese = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsCremonese == 'Tutte' and optgsCremonese  == 'ENTRAMBI' and oppgsCremonese == 'TUTTE' ):
						st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese != 'Tutte'and optgsCremonese  == 'ENTRAMBI' and oppgsCremonese == 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['SQUADRA'] == optggsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese == 'Tutte'and optgsCremonese  != 'ENTRAMBI' and oppgsCremonese == 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['TEMPO'] == optgsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese == 'Tutte'and optgsCremonese  == 'ENTRAMBI' and oppgsCremonese != 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['POSIZIONE'] == oppgsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese != 'Tutte'and optgsCremonese  != 'ENTRAMBI' and oppgsCremonese == 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['SQUADRA'] == optggsCremonese]
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['TEMPO'] == optgsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese == 'Tutte'and optgsCremonese  != 'ENTRAMBI' and oppgsCremonese != 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['POSIZIONE'] == oppgsCremonese]
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['TEMPO'] == optgsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese != 'Tutte'and optgsCremonese  == 'ENTRAMBI' and oppgsCremonese != 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['POSIZIONE'] == oppgsCremonese]
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['SQUADRA'] == optggsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsCremonese != 'Tutte'and optgsCremonese  != 'ENTRAMBI' and oppgsCremonese != 'TUTTE' ):
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['POSIZIONE'] == oppgsCremonese]
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['SQUADRA'] == optggsCremonese]
					df_golsubiti_Cremonese = df_golsubiti_Cremonese.loc[df_golsubiti_Cremonese['TEMPO'] == optgsCremonese]
					st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Cremonese)-1
			ind_dif = len(list_corner_difesa_Cremonese)-1

			avvCremo, difesaCremo = st.columns(2)

			with avvCremo:
				op_avvCremo = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Cremonese, index = ind_avv)
			
			with difesaCremo:
				op_difCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Cremonese, index = ind_dif)

			if(op_avvCremo == 'Tutti'and op_difCremo  == 'Tutti'):
				st.write(df_corner_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo == 'Tutti'and op_difCremo  != 'Tutti'):
				df_corner_Cremonese = df_corner_Cremonese.loc[df_corner_Cremonese['DIFESA'] == op_difCremo]
				st.write(df_corner_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo != 'Tutti'and op_difCremo  == 'Tutti'):
				df_corner_Cremonese = df_corner_Cremonese.loc[df_corner_Cremonese['SQUADRA'] == op_avvCremo]
				st.write(df_corner_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo != 'Tutti'and op_difCremo  != 'Tutti'):
				df_corner_Cremonese = df_corner_Cremonese.loc[df_corner_Cremonese['SQUADRA'] == op_avvCremo]
				df_corner_Cremonese = df_corner_Cremonese.loc[df_corner_Cremonese['DIFESA'] == op_difCremo]
				st.write(df_corner_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsCremonese)-1
			ind_avvbatt = len(list_corner_avvbatt_vsCremonese)-1

			avv_vsCremo, difesa_vsCremo = st.columns(2)

			with avv_vsCremo:
				op_avv_vsCremo = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsCremonese, index = ind_avv)

			with difesa_vsCremo:
				op_avvbatt_vsCremo = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta: ',
			      	list_corner_avvbatt_vsCremonese, index = ind_avvbatt)

			if(op_avv_vsCremo == 'Tutti'and op_avvbatt_vsCremo  == 'Tutti'):
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo == 'Tutti'and op_avvbatt_vsCremo  != 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['GIOC_SULLA_PALLA'] == op_avvbatt_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_avvbatt_vsCremo  == 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['SQUADRA'] == op_avv_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_avvbatt_vsCremo  != 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['SQUADRA'] == op_avv_vsCremo]
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['GIOC_SULLA_PALLA'] == op_avvbatt_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				
with Parma:
	
	
	squadra = "Parma"

	df_corner_Parma = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Parma['LINK'] = df_corner_Parma['LINK'].apply(make_clickable)
	df_corner_Parma = df_corner_Parma.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Parma = df_corner_Parma.drop(columns = ['ATTACCA'])
	
	list_corner_Parma = df_corner_Parma['SQUADRA'].tolist()
	list_corner_Parma = [*set(list_corner_Parma)]
	list_corner_Parma.sort()
	list_corner_Parma.append('Tutti')

	list_corner_difesa_Parma = df_corner_Parma['DIFESA'].tolist()
	list_corner_difesa_Parma = [*set(list_corner_difesa_Parma)]
	list_corner_difesa_Parma.sort()
	list_corner_difesa_Parma.append('Tutti')
	
	df_corner_vsParma = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsParma['LINK'] = df_corner_vsParma['LINK'].apply(make_clickable)
	df_corner_vsParma = df_corner_vsParma.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsParma = df_corner_vsParma.drop(columns = ['DIFENDE'])
	
	list_corner_vsParma = df_corner_vsParma['SQUADRA'].tolist()
	list_corner_vsParma = [*set(list_corner_vsParma)]
	list_corner_vsParma.sort()
	list_corner_vsParma.append('Tutti')

	list_corner_difesa_vsParma = df_corner_vsParma['DIFESA'].tolist()
	list_corner_difesa_vsParma = [*set(list_corner_difesa_vsParma)]
	list_corner_difesa_vsParma.sort()
	list_corner_difesa_vsParma.append('Tutti')
	
	list_corner_avvbatt_vsParma = df_corner_vsParma['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsParma = [*set(list_corner_avvbatt_vsParma)]
	list_corner_avvbatt_vsParma.sort()
	list_corner_avvbatt_vsParma.append('Tutti')


	
	df_golfatti_Parma = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Parma = df_golfatti_Parma.drop(columns = ['ATTACCA'])
	df_golfatti_Parma['LINK'] = df_golfatti_Parma['LINK'].apply(make_clickable)
	df_golfatti_Parma = df_golfatti_Parma.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Parma = df_golfatti_Parma['SQUADRA'].tolist()
	list_golfatti_Parma = [*set(list_golfatti_Parma)]
	list_golfatti_Parma.sort()
	list_golfatti_Parma.append('Tutti')
	
	list_marcatori_Parma = df_golfatti_Parma['GIOCATORE'].tolist()
	list_marcatori_Parma = [*set(list_marcatori_Parma)]
	list_marcatori_Parma.sort()
	list_marcatori_Parma.append('Tutti')
	
	
	df_golsubiti_Parma = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Parma = df_golsubiti_Parma.drop(columns = ['DIFENDE'])
	df_golsubiti_Parma['LINK'] = df_golsubiti_Parma['LINK'].apply(make_clickable)
	df_golsubiti_Parma = df_golsubiti_Parma.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Parma = df_golsubiti_Parma['SQUADRA'].tolist()
	list_golsubiti_Parma = [*set(list_golsubiti_Parma)]
	list_golsubiti_Parma.sort()
	list_golsubiti_Parma.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Parma.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Parma.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Parma['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Parma['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Parma['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Parma['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Parma['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Parma['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Parma['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Parma)-1
				golf_Parma_giocatore, golf_Parma_tempo, golf_Parma_posizione = st.columns(3)

				with golf_Parma_giocatore:
				
					optggfParma = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:', list_marcatori_Parma, index = ind)
			
				
				with golf_Parma_tempo:
				
					optgfParma = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Parma_posizione:
				
					oppgfParma = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfParma == 'Tutti' and optgfParma  == 'ENTRAMBI' and oppgfParma == 'TUTTE' ):
						st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma != 'Tutti'and optgfParma  == 'ENTRAMBI' and oppgfParma == 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['GIOCATORE'] == optggfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma == 'Tutti'and optgfParma  != 'ENTRAMBI' and oppgfParma == 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['TEMPO'] == optgfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma == 'Tutti'and optgfParma  == 'ENTRAMBI' and oppgfParma != 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['POSIZIONE'] == oppgfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma != 'Tutti'and optgfParma  != 'ENTRAMBI' and oppgfParma == 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['GIOCATORE'] == optggfParma]
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['TEMPO'] == optgfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma == 'Tutti'and optgfParma  != 'ENTRAMBI' and oppgfParma != 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['POSIZIONE'] == oppgfParma]
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['TEMPO'] == optgfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma != 'Tutti'and optgfParma  == 'ENTRAMBI' and oppgfParma != 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['POSIZIONE'] == oppgfParma]
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['GIOCATORE'] == optggfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfParma != 'Tutti'and optgfParma  != 'ENTRAMBI' and oppgfParma != 'TUTTE' ):
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['POSIZIONE'] == oppgfParma]
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['GIOCATORE'] == optggfParma]
					df_golfatti_Parma = df_golfatti_Parma.loc[df_golfatti_Parma['TEMPO'] == optgfParma]
					st.write(df_golfatti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Parma.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Parma.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Parma['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Parma['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Parma['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Parma['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Parma['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Parma['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Parma['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Parma)-1
				gols_Parma_giocatore, gols_Parma_tempo, gols_Parma_posizione = st.columns(3)

				with gols_Parma_giocatore:
				
					optggsParma = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Parma, index = ind)
			
				
				with gols_Parma_tempo:
				
					optgsParma = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Parma_posizione:
				
					oppgsParma = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsParma == 'Tutte' and optgsParma  == 'ENTRAMBI' and oppgsParma == 'TUTTE' ):
						st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma != 'Tutte'and optgsParma  == 'ENTRAMBI' and oppgsParma == 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['SQUADRA'] == optggsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma == 'Tutte'and optgsParma  != 'ENTRAMBI' and oppgsParma == 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['TEMPO'] == optgsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma == 'Tutte'and optgsParma  == 'ENTRAMBI' and oppgsParma != 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['POSIZIONE'] == oppgsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma != 'Tutte'and optgsParma  != 'ENTRAMBI' and oppgsParma == 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['SQUADRA'] == optggsParma]
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['TEMPO'] == optgsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma == 'Tutte'and optgsParma  != 'ENTRAMBI' and oppgsParma != 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['POSIZIONE'] == oppgsParma]
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['TEMPO'] == optgsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma != 'Tutte'and optgsParma  == 'ENTRAMBI' and oppgsParma != 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['POSIZIONE'] == oppgsParma]
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['SQUADRA'] == optggsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsParma != 'Tutte'and optgsParma  != 'ENTRAMBI' and oppgsParma != 'TUTTE' ):
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['POSIZIONE'] == oppgsParma]
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['SQUADRA'] == optggsParma]
					df_golsubiti_Parma = df_golsubiti_Parma.loc[df_golsubiti_Parma['TEMPO'] == optgsParma]
					st.write(df_golsubiti_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Parma)-1
			ind_dif = len(list_corner_difesa_Parma)-1

			avvParma, difesaParma = st.columns(2)

			with avvParma:
				op_avvParma = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Parma, index = ind_avv)
			
			with difesaParma:
				op_difParma = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Parma, index = ind_dif)

			if(op_avvParma == 'Tutti'and op_difParma  == 'Tutti'):
				st.write(df_corner_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvParma == 'Tutti'and op_difParma  != 'Tutti'):
				df_corner_Parma = df_corner_Parma.loc[df_corner_Parma['DIFESA'] == op_difParma]
				st.write(df_corner_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvParma != 'Tutti'and op_difParma  == 'Tutti'):
				df_corner_Parma = df_corner_Parma.loc[df_corner_Parma['SQUADRA'] == op_avvParma]
				st.write(df_corner_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvParma != 'Tutti'and op_difParma  != 'Tutti'):
				df_corner_Parma = df_corner_Parma.loc[df_corner_Parma['SQUADRA'] == op_avvParma]
				df_corner_Parma = df_corner_Parma.loc[df_corner_Parma['DIFESA'] == op_difParma]
				st.write(df_corner_Parma.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsParma)-1
			ind_avvbatt = len(list_corner_avvbatt_vsParma)-1

			avv_vsParma, difesa_vsParma = st.columns(2)

			with avv_vsParma:
				op_avv_vsParma = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsParma, index = ind_avv)

			with difesa_vsParma:
				op_avvbatt_vsParma = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:  ',
			      	list_corner_avvbatt_vsParma, index = ind_avvbatt)

			if(op_avv_vsParma == 'Tutti'and op_avvbatt_vsParma  == 'Tutti'):
				st.write(df_corner_vsParma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsParma == 'Tutti'and op_avvbatt_vsParma  != 'Tutti'):
				df_corner_vsParma = df_corner_vsParma.loc[df_corner_vsParma['GIOC_SULLA_PALLA'] == op_avvbatt_vsParma]
				st.write(df_corner_vsParma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsParma != 'Tutti'and op_avvbatt_vsParma  == 'Tutti'):
				df_corner_vsParma = df_corner_vsParma.loc[df_corner_vsParma['SQUADRA'] == op_avv_vsParma]
				st.write(df_corner_vsParma.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsParma != 'Tutti'and op_avvbatt_vsParma  != 'Tutti'):
				df_corner_vsParma = df_corner_vsParma.loc[df_corner_vsParma['SQUADRA'] == op_avv_vsParma]
				df_corner_vsParma = df_corner_vsParma.loc[df_corner_vsParma['GIOC_SULLA_PALLA'] == op_avvbatt_vsParma]
				st.write(df_corner_vsParma.to_html(escape=False, index=False), unsafe_allow_html=True)

with LRVicenza:

	

	

	squadra = "LRVicenza"



	df_corner_LRVicenza = df_corner.loc[df_corner['ATTACCA'] == squadra]

	df_corner_LRVicenza['LINK'] = df_corner_LRVicenza['LINK'].apply(make_clickable)

	df_corner_LRVicenza = df_corner_LRVicenza.rename(columns =  {'DIFENDE' : 'SQUADRA'})

	df_corner_LRVicenza = df_corner_LRVicenza.drop(columns = ['ATTACCA'])

	

	list_corner_LRVicenza = df_corner_LRVicenza['SQUADRA'].tolist()

	list_corner_LRVicenza = [*set(list_corner_LRVicenza)]

	list_corner_LRVicenza.sort()

	list_corner_LRVicenza.append('Tutti')



	list_corner_difesa_LRVicenza = df_corner_LRVicenza['DIFESA'].tolist()

	list_corner_difesa_LRVicenza = [*set(list_corner_difesa_LRVicenza)]

	list_corner_difesa_LRVicenza.sort()

	list_corner_difesa_LRVicenza.append('Tutti')

	

	df_corner_vsLRVicenza = df_corner.loc[df_corner['DIFENDE'] == squadra]

	df_corner_vsLRVicenza['LINK'] = df_corner_vsLRVicenza['LINK'].apply(make_clickable)

	df_corner_vsLRVicenza = df_corner_vsLRVicenza.rename(columns =  {'ATTACCA' : 'SQUADRA'})

	df_corner_vsLRVicenza = df_corner_vsLRVicenza.drop(columns = ['DIFENDE'])

	

	list_corner_vsLRVicenza = df_corner_vsLRVicenza['SQUADRA'].tolist()

	list_corner_vsLRVicenza = [*set(list_corner_vsLRVicenza)]

	list_corner_vsLRVicenza.sort()

	list_corner_vsLRVicenza.append('Tutti')



	list_corner_difesa_vsLRVicenza = df_corner_vsLRVicenza['DIFESA'].tolist()

	list_corner_difesa_vsLRVicenza = [*set(list_corner_difesa_vsLRVicenza)]

	list_corner_difesa_vsLRVicenza.sort()

	list_corner_difesa_vsLRVicenza.append('Tutti')

	

	list_corner_avvbatt_vsLRVicenza = df_corner_vsLRVicenza['GIOC_SULLA_PALLA'].tolist()

	list_corner_avvbatt_vsLRVicenza = [*set(list_corner_avvbatt_vsLRVicenza)]

	list_corner_avvbatt_vsLRVicenza.sort()

	list_corner_avvbatt_vsLRVicenza.append('Tutti')





	

	df_golfatti_LRVicenza = df_gol.loc[df_gol['ATTACCA'] == squadra]

	df_golfatti_LRVicenza = df_golfatti_LRVicenza.drop(columns = ['ATTACCA'])

	df_golfatti_LRVicenza['LINK'] = df_golfatti_LRVicenza['LINK'].apply(make_clickable)

	df_golfatti_LRVicenza = df_golfatti_LRVicenza.rename(columns =  {'DIFENDE' : 'SQUADRA'})

	

	list_golfatti_LRVicenza = df_golfatti_LRVicenza['SQUADRA'].tolist()

	list_golfatti_LRVicenza = [*set(list_golfatti_LRVicenza)]

	list_golfatti_LRVicenza.sort()

	list_golfatti_LRVicenza.append('Tutti')

	

	list_marcatori_LRVicenza = df_golfatti_LRVicenza['GIOCATORE'].tolist()

	list_marcatori_LRVicenza = [*set(list_marcatori_LRVicenza)]

	list_marcatori_LRVicenza.sort()

	list_marcatori_LRVicenza.append('Tutti')

	

	

	df_golsubiti_LRVicenza = df_gol.loc[df_gol['DIFENDE'] == squadra]

	df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.drop(columns = ['DIFENDE'])

	df_golsubiti_LRVicenza['LINK'] = df_golsubiti_LRVicenza['LINK'].apply(make_clickable)

	df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.rename(columns =  {'ATTACCA' : 'SQUADRA'})

	

	list_golsubiti_LRVicenza = df_golsubiti_LRVicenza['SQUADRA'].tolist()

	list_golsubiti_LRVicenza = [*set(list_golsubiti_LRVicenza)]

	list_golsubiti_LRVicenza.sort()

	list_golsubiti_LRVicenza.append('Tutte')

	



	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])

	

	with Gol:

		

		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])

		

		with Golfatti:



			Stats, Link = st.tabs(["Statistiche","Link"])



			with Stats:



				st.subheader(f'Tabella gol fatti :blue[{squadra}]')

				st.dataframe(df_golfatti_LRVicenza.drop(columns = ['LINK']), use_container_width=True)



				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')

				col1, col2, col3, col4 = st.columns(4)

				with col1:

					tmp_df_gfsqd = df_golfatti_LRVicenza.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')

					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')

					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})

					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})



					st.bar_chart(tmp_df_gfsqd, use_container_width=True)

					st.dataframe(df_golfatti_LRVicenza['GIOCATORE'].value_counts().head(3), use_container_width=True)



				with col2:

					st.bar_chart(df_golfatti_LRVicenza['TEMPO'].value_counts(), use_container_width=True)

					st.dataframe(df_golfatti_LRVicenza['TEMPO'].value_counts(), use_container_width=True)	

					



				with col3:

					st.bar_chart(df_golfatti_LRVicenza['POSIZIONE'].value_counts(), use_container_width=True)

					st.dataframe(df_golfatti_LRVicenza['POSIZIONE'].value_counts(), use_container_width=True)				

					



				with col4:

					st.bar_chart(df_golfatti_LRVicenza['TIPO'].value_counts(), use_container_width=True)

					st.dataframe(df_golfatti_LRVicenza['TIPO'].value_counts(), use_container_width=True)				

					



			with Link:

				

				ind = len(list_marcatori_LRVicenza)-1

				golf_LRVicenza_giocatore, golf_LRVicenza_tempo, golf_LRVicenza_posizione = st.columns(3)



				with golf_LRVicenza_giocatore:

				

					optggfLRVicenza = st.selectbox(

			      			f'Seleziona marcatore della {squadra}:', list_marcatori_LRVicenza, index = ind)

			

				

				with golf_LRVicenza_tempo:

				

					optgfLRVicenza = st.selectbox(

			      			f'Seleziona tempo di gioco dei gol della {squadra}:',

			      			("1T","2T",'ENTRAMBI'), index = 2)

			

				with golf_LRVicenza_posizione:

				

					oppgfLRVicenza = st.selectbox(

			      		f'Seleziona la posizione dei gol della {squadra}:',

			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)

			

				

				if(optggfLRVicenza == 'Tutti' and optgfLRVicenza  == 'ENTRAMBI' and oppgfLRVicenza == 'TUTTE' ):

						st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza != 'Tutti'and optgfLRVicenza  == 'ENTRAMBI' and oppgfLRVicenza == 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['GIOCATORE'] == optggfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza == 'Tutti'and optgfLRVicenza  != 'ENTRAMBI' and oppgfLRVicenza == 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['TEMPO'] == optgfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza == 'Tutti'and optgfLRVicenza  == 'ENTRAMBI' and oppgfLRVicenza != 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['POSIZIONE'] == oppgfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza != 'Tutti'and optgfLRVicenza  != 'ENTRAMBI' and oppgfLRVicenza == 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['GIOCATORE'] == optggfLRVicenza]

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['TEMPO'] == optgfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza == 'Tutti'and optgfLRVicenza  != 'ENTRAMBI' and oppgfLRVicenza != 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['POSIZIONE'] == oppgfLRVicenza]

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['TEMPO'] == optgfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza != 'Tutti'and optgfLRVicenza  == 'ENTRAMBI' and oppgfLRVicenza != 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['POSIZIONE'] == oppgfLRVicenza]

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['GIOCATORE'] == optggfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggfLRVicenza != 'Tutti'and optgfLRVicenza  != 'ENTRAMBI' and oppgfLRVicenza != 'TUTTE' ):

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['POSIZIONE'] == oppgfLRVicenza]

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['GIOCATORE'] == optggfLRVicenza]

					df_golfatti_LRVicenza = df_golfatti_LRVicenza.loc[df_golfatti_LRVicenza['TEMPO'] == optgfLRVicenza]

					st.write(df_golfatti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)









		with Golsubiti:

			

			Stats, Link = st.tabs(["Statistiche","Link"])



			with Stats:



			

				st.subheader(f'Tabella gol subiti :blue[{squadra}]')

				st.dataframe(df_golsubiti_LRVicenza.drop(columns = ['LINK']), use_container_width=True)



				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')





				col1, col2, col3, col4 = st.columns(4)

				with col1:



					tmp_df_gssqd = df_golsubiti_LRVicenza.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')

					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')

					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})

					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})



					st.bar_chart(tmp_df_gssqd, use_container_width=True)

					st.dataframe(df_golsubiti_LRVicenza['SQUADRA'].value_counts().head(3), use_container_width=True)

					



				with col2:



					st.bar_chart(df_golsubiti_LRVicenza['TEMPO'].value_counts(), use_container_width=True)

					st.dataframe(df_golsubiti_LRVicenza['TEMPO'].value_counts(), use_container_width=True)				

					



				with col3:



					st.bar_chart(df_golsubiti_LRVicenza['POSIZIONE'].value_counts(), use_container_width=True)

					st.dataframe(df_golsubiti_LRVicenza['POSIZIONE'].value_counts(), use_container_width=True)				

					



				with col4:



					st.bar_chart(df_golsubiti_LRVicenza['TIPO'].value_counts(), use_container_width=True)

					st.dataframe(df_golsubiti_LRVicenza['TIPO'].value_counts(), use_container_width=True)				

					



			with Link:



				ind = len(list_golsubiti_LRVicenza)-1

				gols_LRVicenza_giocatore, gols_LRVicenza_tempo, gols_LRVicenza_posizione = st.columns(3)



				with gols_LRVicenza_giocatore:

				

					optggsLRVicenza = st.selectbox(

			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_LRVicenza, index = ind)

			

				

				with gols_LRVicenza_tempo:

				

					optgsLRVicenza = st.selectbox(

			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',

			      			("1T","2T",'ENTRAMBI'), index = 2)

			

				with gols_LRVicenza_posizione:

				

					oppgsLRVicenza = st.selectbox(

			      		f'Seleziona la posizione dei gol alla {squadra}:',

			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)

			

				

				if(optggsLRVicenza == 'Tutte' and optgsLRVicenza  == 'ENTRAMBI' and oppgsLRVicenza == 'TUTTE' ):

						st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza != 'Tutte'and optgsLRVicenza  == 'ENTRAMBI' and oppgsLRVicenza == 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['SQUADRA'] == optggsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza == 'Tutte'and optgsLRVicenza  != 'ENTRAMBI' and oppgsLRVicenza == 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['TEMPO'] == optgsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza == 'Tutte'and optgsLRVicenza  == 'ENTRAMBI' and oppgsLRVicenza != 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['POSIZIONE'] == oppgsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza != 'Tutte'and optgsLRVicenza  != 'ENTRAMBI' and oppgsLRVicenza == 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['SQUADRA'] == optggsLRVicenza]

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['TEMPO'] == optgsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza == 'Tutte'and optgsLRVicenza  != 'ENTRAMBI' and oppgsLRVicenza != 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['POSIZIONE'] == oppgsLRVicenza]

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['TEMPO'] == optgsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza != 'Tutte'and optgsLRVicenza  == 'ENTRAMBI' and oppgsLRVicenza != 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['POSIZIONE'] == oppgsLRVicenza]

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['SQUADRA'] == optggsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



				elif(optggsLRVicenza != 'Tutte'and optgsLRVicenza  != 'ENTRAMBI' and oppgsLRVicenza != 'TUTTE' ):

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['POSIZIONE'] == oppgsLRVicenza]

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['SQUADRA'] == optggsLRVicenza]

					df_golsubiti_LRVicenza = df_golsubiti_LRVicenza.loc[df_golsubiti_LRVicenza['TEMPO'] == optgsLRVicenza]

					st.write(df_golsubiti_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			

	with Corner:

		

		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])

		

		with Favore:

			

			ind_avv = len(list_corner_LRVicenza)-1

			ind_dif = len(list_corner_difesa_LRVicenza)-1



			avvLRVicenza, difesaLRVicenza = st.columns(2)



			with avvLRVicenza:

				op_avvLRVicenza = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_LRVicenza, index = ind_avv)

			

			with difesaLRVicenza:

				op_difLRVicenza = st.selectbox(

			      	f'Seleziona tipo difesa avversario della {squadra}:',

			      	list_corner_difesa_LRVicenza, index = ind_dif)



			if(op_avvLRVicenza == 'Tutti'and op_difLRVicenza  == 'Tutti'):

				st.write(df_corner_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avvLRVicenza == 'Tutti'and op_difLRVicenza  != 'Tutti'):

				df_corner_LRVicenza = df_corner_LRVicenza.loc[df_corner_LRVicenza['DIFESA'] == op_difLRVicenza]

				st.write(df_corner_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avvLRVicenza != 'Tutti'and op_difLRVicenza  == 'Tutti'):

				df_corner_LRVicenza = df_corner_LRVicenza.loc[df_corner_LRVicenza['SQUADRA'] == op_avvLRVicenza]

				st.write(df_corner_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avvLRVicenza != 'Tutti'and op_difLRVicenza  != 'Tutti'):

				df_corner_LRVicenza = df_corner_LRVicenza.loc[df_corner_LRVicenza['SQUADRA'] == op_avvLRVicenza]

				df_corner_LRVicenza = df_corner_LRVicenza.loc[df_corner_LRVicenza['DIFESA'] == op_difLRVicenza]

				st.write(df_corner_LRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



		with Contro:

			

			ind_avv = len(list_corner_vsLRVicenza)-1

			ind_avvbatt = len(list_corner_avvbatt_vsLRVicenza)-1



			avv_vsLRVicenza, difesa_vsLRVicenza = st.columns(2)



			with avv_vsLRVicenza:

				op_avv_vsLRVicenza = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsLRVicenza, index = ind_avv)



			with difesa_vsLRVicenza:

				op_avvbatt_vsLRVicenza = st.selectbox(

			      	f'Seleziona quanti giocatori avversari presenti in battuta:    ',

			      	list_corner_avvbatt_vsLRVicenza, index = ind_avvbatt)



			if(op_avv_vsLRVicenza == 'Tutti'and op_avvbatt_vsLRVicenza  == 'Tutti'):

				st.write(df_corner_vsLRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avv_vsLRVicenza == 'Tutti'and op_avvbatt_vsLRVicenza  != 'Tutti'):

				df_corner_vsLRVicenza = df_corner_vsLRVicenza.loc[df_corner_vsLRVicenza['GIOC_SULLA_PALLA'] == op_avvbatt_vsLRVicenza]

				st.write(df_corner_vsLRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avv_vsLRVicenza != 'Tutti'and op_avvbatt_vsLRVicenza  == 'Tutti'):

				df_corner_vsLRVicenza = df_corner_vsLRVicenza.loc[df_corner_vsLRVicenza['SQUADRA'] == op_avv_vsLRVicenza]

				st.write(df_corner_vsLRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)



			elif(op_avv_vsLRVicenza != 'Tutti'and op_avvbatt_vsLRVicenza  != 'Tutti'):

				df_corner_vsLRVicenza = df_corner_vsLRVicenza.loc[df_corner_vsLRVicenza['SQUADRA'] == op_avv_vsLRVicenza]

				df_corner_vsLRVicenza = df_corner_vsLRVicenza.loc[df_corner_vsLRVicenza['GIOC_SULLA_PALLA'] == op_avvbatt_vsLRVicenza]

				st.write(df_corner_vsLRVicenza.to_html(escape=False, index=False), unsafe_allow_html=True)				

with Albinoleffe:
	
	
	squadra = "Albinoleffe"

	df_corner_Albinoleffe = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Albinoleffe['LINK'] = df_corner_Albinoleffe['LINK'].apply(make_clickable)
	df_corner_Albinoleffe = df_corner_Albinoleffe.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Albinoleffe = df_corner_Albinoleffe.drop(columns = ['ATTACCA'])
	
	list_corner_Albinoleffe = df_corner_Albinoleffe['SQUADRA'].tolist()
	list_corner_Albinoleffe = [*set(list_corner_Albinoleffe)]
	list_corner_Albinoleffe.sort()
	list_corner_Albinoleffe.append('Tutti')

	list_corner_difesa_Albinoleffe = df_corner_Albinoleffe['DIFESA'].tolist()
	list_corner_difesa_Albinoleffe = [*set(list_corner_difesa_Albinoleffe)]
	list_corner_difesa_Albinoleffe.sort()
	list_corner_difesa_Albinoleffe.append('Tutti')
	
	df_corner_vsAlbinoleffe = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsAlbinoleffe['LINK'] = df_corner_vsAlbinoleffe['LINK'].apply(make_clickable)
	df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.drop(columns = ['DIFENDE'])
	
	list_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe['SQUADRA'].tolist()
	list_corner_vsAlbinoleffe = [*set(list_corner_vsAlbinoleffe)]
	list_corner_vsAlbinoleffe.sort()
	list_corner_vsAlbinoleffe.append('Tutti')

	list_corner_difesa_vsAlbinoleffe = df_corner_vsAlbinoleffe['DIFESA'].tolist()
	list_corner_difesa_vsAlbinoleffe = [*set(list_corner_difesa_vsAlbinoleffe)]
	list_corner_difesa_vsAlbinoleffe.sort()
	list_corner_difesa_vsAlbinoleffe.append('Tutti')
	
	list_corner_avvbatt_vsAlbinoleffe = df_corner_vsAlbinoleffe['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsAlbinoleffe = [*set(list_corner_avvbatt_vsAlbinoleffe)]
	list_corner_avvbatt_vsAlbinoleffe.sort()
	list_corner_avvbatt_vsAlbinoleffe.append('Tutti')


	
	df_golfatti_Albinoleffe = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.drop(columns = ['ATTACCA'])
	df_golfatti_Albinoleffe['LINK'] = df_golfatti_Albinoleffe['LINK'].apply(make_clickable)
	df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Albinoleffe = df_golfatti_Albinoleffe['SQUADRA'].tolist()
	list_golfatti_Albinoleffe = [*set(list_golfatti_Albinoleffe)]
	list_golfatti_Albinoleffe.sort()
	list_golfatti_Albinoleffe.append('Tutti')
	
	list_marcatori_Albinoleffe = df_golfatti_Albinoleffe['GIOCATORE'].tolist()
	list_marcatori_Albinoleffe = [*set(list_marcatori_Albinoleffe)]
	list_marcatori_Albinoleffe.sort()
	list_marcatori_Albinoleffe.append('Tutti')
	
	
	df_golsubiti_Albinoleffe = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.drop(columns = ['DIFENDE'])
	df_golsubiti_Albinoleffe['LINK'] = df_golsubiti_Albinoleffe['LINK'].apply(make_clickable)
	df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe['SQUADRA'].tolist()
	list_golsubiti_Albinoleffe = [*set(list_golsubiti_Albinoleffe)]
	list_golsubiti_Albinoleffe.sort()
	list_golsubiti_Albinoleffe.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Albinoleffe.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Albinoleffe.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Albinoleffe['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Albinoleffe['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Albinoleffe['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Albinoleffe['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Albinoleffe['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Albinoleffe['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Albinoleffe['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Albinoleffe)-1
				golf_Albinoleffe_giocatore, golf_Albinoleffe_tempo, golf_Albinoleffe_posizione = st.columns(3)

				with golf_Albinoleffe_giocatore:
				
					optggfAlbinoleffe = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:  ', list_marcatori_Albinoleffe, index = ind)
			
				
				with golf_Albinoleffe_tempo:
				
					optgfAlbinoleffe = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}: ',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Albinoleffe_posizione:
				
					oppgfAlbinoleffe = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfAlbinoleffe == 'Tutti' and optgfAlbinoleffe  == 'ENTRAMBI' and oppgfAlbinoleffe == 'TUTTE' ):
						st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe != 'Tutti'and optgfAlbinoleffe  == 'ENTRAMBI' and oppgfAlbinoleffe == 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['GIOCATORE'] == optggfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe == 'Tutti'and optgfAlbinoleffe  != 'ENTRAMBI' and oppgfAlbinoleffe == 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['TEMPO'] == optgfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe == 'Tutti'and optgfAlbinoleffe  == 'ENTRAMBI' and oppgfAlbinoleffe != 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['POSIZIONE'] == oppgfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe != 'Tutti'and optgfAlbinoleffe  != 'ENTRAMBI' and oppgfAlbinoleffe == 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['GIOCATORE'] == optggfAlbinoleffe]
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['TEMPO'] == optgfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe == 'Tutti'and optgfAlbinoleffe  != 'ENTRAMBI' and oppgfAlbinoleffe != 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['POSIZIONE'] == oppgfAlbinoleffe]
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['TEMPO'] == optgfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe != 'Tutti'and optgfAlbinoleffe  == 'ENTRAMBI' and oppgfAlbinoleffe != 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['POSIZIONE'] == oppgfAlbinoleffe]
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['GIOCATORE'] == optggfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfAlbinoleffe != 'Tutti'and optgfAlbinoleffe  != 'ENTRAMBI' and oppgfAlbinoleffe != 'TUTTE' ):
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['POSIZIONE'] == oppgfAlbinoleffe]
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['GIOCATORE'] == optggfAlbinoleffe]
					df_golfatti_Albinoleffe = df_golfatti_Albinoleffe.loc[df_golfatti_Albinoleffe['TEMPO'] == optgfAlbinoleffe]
					st.write(df_golfatti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Albinoleffe.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Albinoleffe.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Albinoleffe['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Albinoleffe['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Albinoleffe['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Albinoleffe['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Albinoleffe['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Albinoleffe['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Albinoleffe['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Albinoleffe)-1
				gols_Albinoleffe_giocatore, gols_Albinoleffe_tempo, gols_Albinoleffe_posizione = st.columns(3)

				with gols_Albinoleffe_giocatore:
				
					optggsAlbinoleffe = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Albinoleffe, index = ind)
			
				
				with gols_Albinoleffe_tempo:
				
					optgsAlbinoleffe = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Albinoleffe_posizione:
				
					oppgsAlbinoleffe = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsAlbinoleffe == 'Tutte' and optgsAlbinoleffe  == 'ENTRAMBI' and oppgsAlbinoleffe == 'TUTTE' ):
						st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe != 'Tutte'and optgsAlbinoleffe  == 'ENTRAMBI' and oppgsAlbinoleffe == 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['SQUADRA'] == optggsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe == 'Tutte'and optgsAlbinoleffe  != 'ENTRAMBI' and oppgsAlbinoleffe == 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['TEMPO'] == optgsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe == 'Tutte'and optgsAlbinoleffe  == 'ENTRAMBI' and oppgsAlbinoleffe != 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['POSIZIONE'] == oppgsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe != 'Tutte'and optgsAlbinoleffe  != 'ENTRAMBI' and oppgsAlbinoleffe == 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['SQUADRA'] == optggsAlbinoleffe]
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['TEMPO'] == optgsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe == 'Tutte'and optgsAlbinoleffe  != 'ENTRAMBI' and oppgsAlbinoleffe != 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['POSIZIONE'] == oppgsAlbinoleffe]
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['TEMPO'] == optgsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe != 'Tutte'and optgsAlbinoleffe  == 'ENTRAMBI' and oppgsAlbinoleffe != 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['POSIZIONE'] == oppgsAlbinoleffe]
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['SQUADRA'] == optggsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsAlbinoleffe != 'Tutte'and optgsAlbinoleffe  != 'ENTRAMBI' and oppgsAlbinoleffe != 'TUTTE' ):
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['POSIZIONE'] == oppgsAlbinoleffe]
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['SQUADRA'] == optggsAlbinoleffe]
					df_golsubiti_Albinoleffe = df_golsubiti_Albinoleffe.loc[df_golsubiti_Albinoleffe['TEMPO'] == optgsAlbinoleffe]
					st.write(df_golsubiti_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Albinoleffe)-1
			ind_dif = len(list_corner_difesa_Albinoleffe)-1

			avvAlbinoleffe, difesaAlbinoleffe = st.columns(2)

			with avvAlbinoleffe:
				op_avvAlbinoleffe = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Albinoleffe, index = ind_avv)
			
			with difesaAlbinoleffe:
				op_difAlbinoleffe = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Albinoleffe, index = ind_dif)

			if(op_avvAlbinoleffe == 'Tutti'and op_difAlbinoleffe  == 'Tutti'):
				st.write(df_corner_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvAlbinoleffe == 'Tutti'and op_difAlbinoleffe  != 'Tutti'):
				df_corner_Albinoleffe = df_corner_Albinoleffe.loc[df_corner_Albinoleffe['DIFESA'] == op_difAlbinoleffe]
				st.write(df_corner_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvAlbinoleffe != 'Tutti'and op_difAlbinoleffe  == 'Tutti'):
				df_corner_Albinoleffe = df_corner_Albinoleffe.loc[df_corner_Albinoleffe['SQUADRA'] == op_avvAlbinoleffe]
				st.write(df_corner_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvAlbinoleffe != 'Tutti'and op_difAlbinoleffe  != 'Tutti'):
				df_corner_Albinoleffe = df_corner_Albinoleffe.loc[df_corner_Albinoleffe['SQUADRA'] == op_avvAlbinoleffe]
				df_corner_Albinoleffe = df_corner_Albinoleffe.loc[df_corner_Albinoleffe['DIFESA'] == op_difAlbinoleffe]
				st.write(df_corner_Albinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsAlbinoleffe)-1
			ind_avvbatt = len(list_corner_avvbatt_vsAlbinoleffe)-1

			avv_vsAlbinoleffe, difesa_vsAlbinoleffe = st.columns(2)

			with avv_vsAlbinoleffe:
				op_avv_vsAlbinoleffe = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsAlbinoleffe, index = ind_avv)

			with difesa_vsAlbinoleffe:
				op_avvbatt_vsAlbinoleffe = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:      ',
			      	list_corner_avvbatt_vsAlbinoleffe, index = ind_avvbatt)

			if(op_avv_vsAlbinoleffe == 'Tutti'and op_avvbatt_vsAlbinoleffe  == 'Tutti'):
				st.write(df_corner_vsAlbinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsAlbinoleffe == 'Tutti'and op_avvbatt_vsAlbinoleffe  != 'Tutti'):
				df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.loc[df_corner_vsAlbinoleffe['GIOC_SULLA_PALLA'] == op_avvbatt_vsAlbinoleffe]
				st.write(df_corner_vsAlbinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsAlbinoleffe != 'Tutti'and op_avvbatt_vsAlbinoleffe  == 'Tutti'):
				df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.loc[df_corner_vsAlbinoleffe['SQUADRA'] == op_avv_vsAlbinoleffe]
				st.write(df_corner_vsAlbinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsAlbinoleffe != 'Tutti'and op_avvbatt_vsAlbinoleffe  != 'Tutti'):
				df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.loc[df_corner_vsAlbinoleffe['SQUADRA'] == op_avv_vsAlbinoleffe]
				df_corner_vsAlbinoleffe = df_corner_vsAlbinoleffe.loc[df_corner_vsAlbinoleffe['GIOC_SULLA_PALLA'] == op_avvbatt_vsAlbinoleffe]
				st.write(df_corner_vsAlbinoleffe.to_html(escape=False, index=False), unsafe_allow_html=True)
with Reggiana:
	
	
	squadra = "Reggiana"

	df_corner_Reggiana = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Reggiana['LINK'] = df_corner_Reggiana['LINK'].apply(make_clickable)
	df_corner_Reggiana = df_corner_Reggiana.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Reggiana = df_corner_Reggiana.drop(columns = ['ATTACCA'])
	
	list_corner_Reggiana = df_corner_Reggiana['SQUADRA'].tolist()
	list_corner_Reggiana = [*set(list_corner_Reggiana)]
	list_corner_Reggiana.sort()
	list_corner_Reggiana.append('Tutti')

	list_corner_difesa_Reggiana = df_corner_Reggiana['DIFESA'].tolist()
	list_corner_difesa_Reggiana = [*set(list_corner_difesa_Reggiana)]
	list_corner_difesa_Reggiana.sort()
	list_corner_difesa_Reggiana.append('Tutti')
	
	df_corner_vsReggiana = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsReggiana['LINK'] = df_corner_vsReggiana['LINK'].apply(make_clickable)
	df_corner_vsReggiana = df_corner_vsReggiana.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsReggiana = df_corner_vsReggiana.drop(columns = ['DIFENDE'])
	
	list_corner_vsReggiana = df_corner_vsReggiana['SQUADRA'].tolist()
	list_corner_vsReggiana = [*set(list_corner_vsReggiana)]
	list_corner_vsReggiana.sort()
	list_corner_vsReggiana.append('Tutti')

	list_corner_difesa_vsReggiana = df_corner_vsReggiana['DIFESA'].tolist()
	list_corner_difesa_vsReggiana = [*set(list_corner_difesa_vsReggiana)]
	list_corner_difesa_vsReggiana.sort()
	list_corner_difesa_vsReggiana.append('Tutti')
	
	list_corner_avvbatt_vsReggiana = df_corner_vsReggiana['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsReggiana = [*set(list_corner_avvbatt_vsReggiana)]
	list_corner_avvbatt_vsReggiana.sort()
	list_corner_avvbatt_vsReggiana.append('Tutti')


	
	df_golfatti_Reggiana = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Reggiana = df_golfatti_Reggiana.drop(columns = ['ATTACCA'])
	df_golfatti_Reggiana['LINK'] = df_golfatti_Reggiana['LINK'].apply(make_clickable)
	df_golfatti_Reggiana = df_golfatti_Reggiana.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Reggiana = df_golfatti_Reggiana['SQUADRA'].tolist()
	list_golfatti_Reggiana = [*set(list_golfatti_Reggiana)]
	list_golfatti_Reggiana.sort()
	list_golfatti_Reggiana.append('Tutti')
	
	list_marcatori_Reggiana = df_golfatti_Reggiana['GIOCATORE'].tolist()
	list_marcatori_Reggiana = [*set(list_marcatori_Reggiana)]
	list_marcatori_Reggiana.sort()
	list_marcatori_Reggiana.append('Tutti')
	
	
	df_golsubiti_Reggiana = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Reggiana = df_golsubiti_Reggiana.drop(columns = ['DIFENDE'])
	df_golsubiti_Reggiana['LINK'] = df_golsubiti_Reggiana['LINK'].apply(make_clickable)
	df_golsubiti_Reggiana = df_golsubiti_Reggiana.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Reggiana = df_golsubiti_Reggiana['SQUADRA'].tolist()
	list_golsubiti_Reggiana = [*set(list_golsubiti_Reggiana)]
	list_golsubiti_Reggiana.sort()
	list_golsubiti_Reggiana.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Reggiana.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Reggiana.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Reggiana['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Reggiana['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Reggiana['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Reggiana['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Reggiana['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Reggiana['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Reggiana['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Reggiana)-1
				golf_Reggiana_giocatore, golf_Reggiana_tempo, golf_Reggiana_posizione = st.columns(3)

				with golf_Reggiana_giocatore:
				
					optggfReggiana = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:  ', list_marcatori_Reggiana, index = ind)
			
				
				with golf_Reggiana_tempo:
				
					optgfReggiana = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}: ',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Reggiana_posizione:
				
					oppgfReggiana = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfReggiana == 'Tutti' and optgfReggiana  == 'ENTRAMBI' and oppgfReggiana == 'TUTTE' ):
						st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana != 'Tutti'and optgfReggiana  == 'ENTRAMBI' and oppgfReggiana == 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['GIOCATORE'] == optggfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana == 'Tutti'and optgfReggiana  != 'ENTRAMBI' and oppgfReggiana == 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['TEMPO'] == optgfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana == 'Tutti'and optgfReggiana  == 'ENTRAMBI' and oppgfReggiana != 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['POSIZIONE'] == oppgfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana != 'Tutti'and optgfReggiana  != 'ENTRAMBI' and oppgfReggiana == 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['GIOCATORE'] == optggfReggiana]
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['TEMPO'] == optgfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana == 'Tutti'and optgfReggiana  != 'ENTRAMBI' and oppgfReggiana != 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['POSIZIONE'] == oppgfReggiana]
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['TEMPO'] == optgfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana != 'Tutti'and optgfReggiana  == 'ENTRAMBI' and oppgfReggiana != 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['POSIZIONE'] == oppgfReggiana]
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['GIOCATORE'] == optggfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfReggiana != 'Tutti'and optgfReggiana  != 'ENTRAMBI' and oppgfReggiana != 'TUTTE' ):
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['POSIZIONE'] == oppgfReggiana]
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['GIOCATORE'] == optggfReggiana]
					df_golfatti_Reggiana = df_golfatti_Reggiana.loc[df_golfatti_Reggiana['TEMPO'] == optgfReggiana]
					st.write(df_golfatti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Reggiana.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Reggiana.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Reggiana['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Reggiana['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Reggiana['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Reggiana['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Reggiana['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Reggiana['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Reggiana['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Reggiana)-1
				gols_Reggiana_giocatore, gols_Reggiana_tempo, gols_Reggiana_posizione = st.columns(3)

				with gols_Reggiana_giocatore:
				
					optggsReggiana = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Reggiana, index = ind)
			
				
				with gols_Reggiana_tempo:
				
					optgsReggiana = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Reggiana_posizione:
				
					oppgsReggiana = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsReggiana == 'Tutte' and optgsReggiana  == 'ENTRAMBI' and oppgsReggiana == 'TUTTE' ):
						st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana != 'Tutte'and optgsReggiana  == 'ENTRAMBI' and oppgsReggiana == 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['SQUADRA'] == optggsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana == 'Tutte'and optgsReggiana  != 'ENTRAMBI' and oppgsReggiana == 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['TEMPO'] == optgsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana == 'Tutte'and optgsReggiana  == 'ENTRAMBI' and oppgsReggiana != 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['POSIZIONE'] == oppgsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana != 'Tutte'and optgsReggiana  != 'ENTRAMBI' and oppgsReggiana == 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['SQUADRA'] == optggsReggiana]
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['TEMPO'] == optgsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana == 'Tutte'and optgsReggiana  != 'ENTRAMBI' and oppgsReggiana != 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['POSIZIONE'] == oppgsReggiana]
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['TEMPO'] == optgsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana != 'Tutte'and optgsReggiana  == 'ENTRAMBI' and oppgsReggiana != 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['POSIZIONE'] == oppgsReggiana]
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['SQUADRA'] == optggsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsReggiana != 'Tutte'and optgsReggiana  != 'ENTRAMBI' and oppgsReggiana != 'TUTTE' ):
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['POSIZIONE'] == oppgsReggiana]
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['SQUADRA'] == optggsReggiana]
					df_golsubiti_Reggiana = df_golsubiti_Reggiana.loc[df_golsubiti_Reggiana['TEMPO'] == optgsReggiana]
					st.write(df_golsubiti_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Reggiana)-1
			ind_dif = len(list_corner_difesa_Reggiana)-1

			avvReggiana, difesaReggiana = st.columns(2)

			with avvReggiana:
				op_avvReggiana = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Reggiana, index = ind_avv)
			
			with difesaReggiana:
				op_difReggiana = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Reggiana, index = ind_dif)

			if(op_avvReggiana == 'Tutti'and op_difReggiana  == 'Tutti'):
				st.write(df_corner_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvReggiana == 'Tutti'and op_difReggiana  != 'Tutti'):
				df_corner_Reggiana = df_corner_Reggiana.loc[df_corner_Reggiana['DIFESA'] == op_difReggiana]
				st.write(df_corner_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvReggiana != 'Tutti'and op_difReggiana  == 'Tutti'):
				df_corner_Reggiana = df_corner_Reggiana.loc[df_corner_Reggiana['SQUADRA'] == op_avvReggiana]
				st.write(df_corner_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvReggiana != 'Tutti'and op_difReggiana  != 'Tutti'):
				df_corner_Reggiana = df_corner_Reggiana.loc[df_corner_Reggiana['SQUADRA'] == op_avvReggiana]
				df_corner_Reggiana = df_corner_Reggiana.loc[df_corner_Reggiana['DIFESA'] == op_difReggiana]
				st.write(df_corner_Reggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsReggiana)-1
			ind_avvbatt = len(list_corner_avvbatt_vsReggiana)-1

			avv_vsReggiana, difesa_vsReggiana = st.columns(2)

			with avv_vsReggiana:
				op_avv_vsReggiana = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsReggiana, index = ind_avv)

			with difesa_vsReggiana:
				op_avvbatt_vsReggiana = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:          ',
			      	list_corner_avvbatt_vsReggiana, index = ind_avvbatt)

			if(op_avv_vsReggiana == 'Tutti'and op_avvbatt_vsReggiana  == 'Tutti'):
				st.write(df_corner_vsReggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsReggiana == 'Tutti'and op_avvbatt_vsReggiana  != 'Tutti'):
				df_corner_vsReggiana = df_corner_vsReggiana.loc[df_corner_vsReggiana['GIOC_SULLA_PALLA'] == op_avvbatt_vsReggiana]
				st.write(df_corner_vsReggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsReggiana != 'Tutti'and op_avvbatt_vsReggiana  == 'Tutti'):
				df_corner_vsReggiana = df_corner_vsReggiana.loc[df_corner_vsReggiana['SQUADRA'] == op_avv_vsReggiana]
				st.write(df_corner_vsReggiana.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsReggiana != 'Tutti'and op_avvbatt_vsReggiana  != 'Tutti'):
				df_corner_vsReggiana = df_corner_vsReggiana.loc[df_corner_vsReggiana['SQUADRA'] == op_avv_vsReggiana]
				df_corner_vsReggiana = df_corner_vsReggiana.loc[df_corner_vsReggiana['GIOC_SULLA_PALLA'] == op_avvbatt_vsReggiana]
				st.write(df_corner_vsReggiana.to_html(escape=False, index=False), unsafe_allow_html=True)
				

with Spal:
	
	
	squadra = "Spal"

	df_corner_Spal = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Spal['LINK'] = df_corner_Spal['LINK'].apply(make_clickable)
	df_corner_Spal = df_corner_Spal.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Spal = df_corner_Spal.drop(columns = ['ATTACCA'])
	
	list_corner_Spal = df_corner_Spal['SQUADRA'].tolist()
	list_corner_Spal = [*set(list_corner_Spal)]
	list_corner_Spal.sort()
	list_corner_Spal.append('Tutti')

	list_corner_difesa_Spal = df_corner_Spal['DIFESA'].tolist()
	list_corner_difesa_Spal = [*set(list_corner_difesa_Spal)]
	list_corner_difesa_Spal.sort()
	list_corner_difesa_Spal.append('Tutti')
	
	df_corner_vsSpal = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsSpal['LINK'] = df_corner_vsSpal['LINK'].apply(make_clickable)
	df_corner_vsSpal = df_corner_vsSpal.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsSpal = df_corner_vsSpal.drop(columns = ['DIFENDE'])
	
	list_corner_vsSpal = df_corner_vsSpal['SQUADRA'].tolist()
	list_corner_vsSpal = [*set(list_corner_vsSpal)]
	list_corner_vsSpal.sort()
	list_corner_vsSpal.append('Tutti')

	list_corner_difesa_vsSpal = df_corner_vsSpal['DIFESA'].tolist()
	list_corner_difesa_vsSpal = [*set(list_corner_difesa_vsSpal)]
	list_corner_difesa_vsSpal.sort()
	list_corner_difesa_vsSpal.append('Tutti')
	
	list_corner_avvbatt_vsSpal = df_corner_vsSpal['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsSpal = [*set(list_corner_avvbatt_vsSpal)]
	list_corner_avvbatt_vsSpal.sort()
	list_corner_avvbatt_vsSpal.append('Tutti')


	
	df_golfatti_Spal = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Spal = df_golfatti_Spal.drop(columns = ['ATTACCA'])
	df_golfatti_Spal['LINK'] = df_golfatti_Spal['LINK'].apply(make_clickable)
	df_golfatti_Spal = df_golfatti_Spal.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Spal = df_golfatti_Spal['SQUADRA'].tolist()
	list_golfatti_Spal = [*set(list_golfatti_Spal)]
	list_golfatti_Spal.sort()
	list_golfatti_Spal.append('Tutti')
	
	list_marcatori_Spal = df_golfatti_Spal['GIOCATORE'].tolist()
	list_marcatori_Spal = [*set(list_marcatori_Spal)]
	list_marcatori_Spal.sort()
	list_marcatori_Spal.append('Tutti')
	
	
	df_golsubiti_Spal = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Spal = df_golsubiti_Spal.drop(columns = ['DIFENDE'])
	df_golsubiti_Spal['LINK'] = df_golsubiti_Spal['LINK'].apply(make_clickable)
	df_golsubiti_Spal = df_golsubiti_Spal.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Spal = df_golsubiti_Spal['SQUADRA'].tolist()
	list_golsubiti_Spal = [*set(list_golsubiti_Spal)]
	list_golsubiti_Spal.sort()
	list_golsubiti_Spal.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Spal.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Spal.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Spal['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Spal['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Spal['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Spal['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Spal['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Spal['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Spal['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Spal)-1
				golf_Spal_giocatore, golf_Spal_tempo, golf_Spal_posizione = st.columns(3)

				with golf_Spal_giocatore:
				
					optggfSpal = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:  ', list_marcatori_Spal, index = ind)
			
				
				with golf_Spal_tempo:
				
					optgfSpal = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}: ',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Spal_posizione:
				
					oppgfSpal = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfSpal == 'Tutti' and optgfSpal  == 'ENTRAMBI' and oppgfSpal == 'TUTTE' ):
						st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal != 'Tutti'and optgfSpal  == 'ENTRAMBI' and oppgfSpal == 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['GIOCATORE'] == optggfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal == 'Tutti'and optgfSpal  != 'ENTRAMBI' and oppgfSpal == 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['TEMPO'] == optgfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal == 'Tutti'and optgfSpal  == 'ENTRAMBI' and oppgfSpal != 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['POSIZIONE'] == oppgfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal != 'Tutti'and optgfSpal  != 'ENTRAMBI' and oppgfSpal == 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['GIOCATORE'] == optggfSpal]
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['TEMPO'] == optgfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal == 'Tutti'and optgfSpal  != 'ENTRAMBI' and oppgfSpal != 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['POSIZIONE'] == oppgfSpal]
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['TEMPO'] == optgfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal != 'Tutti'and optgfSpal  == 'ENTRAMBI' and oppgfSpal != 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['POSIZIONE'] == oppgfSpal]
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['GIOCATORE'] == optggfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfSpal != 'Tutti'and optgfSpal  != 'ENTRAMBI' and oppgfSpal != 'TUTTE' ):
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['POSIZIONE'] == oppgfSpal]
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['GIOCATORE'] == optggfSpal]
					df_golfatti_Spal = df_golfatti_Spal.loc[df_golfatti_Spal['TEMPO'] == optgfSpal]
					st.write(df_golfatti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Spal.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Spal.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Spal['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Spal['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Spal['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Spal['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Spal['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Spal['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Spal['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Spal)-1
				gols_Spal_giocatore, gols_Spal_tempo, gols_Spal_posizione = st.columns(3)

				with gols_Spal_giocatore:
				
					optggsSpal = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Spal, index = ind)
			
				
				with gols_Spal_tempo:
				
					optgsSpal = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Spal_posizione:
				
					oppgsSpal = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsSpal == 'Tutte' and optgsSpal  == 'ENTRAMBI' and oppgsSpal == 'TUTTE' ):
						st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal != 'Tutte'and optgsSpal  == 'ENTRAMBI' and oppgsSpal == 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['SQUADRA'] == optggsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal == 'Tutte'and optgsSpal  != 'ENTRAMBI' and oppgsSpal == 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['TEMPO'] == optgsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal == 'Tutte'and optgsSpal  == 'ENTRAMBI' and oppgsSpal != 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['POSIZIONE'] == oppgsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal != 'Tutte'and optgsSpal  != 'ENTRAMBI' and oppgsSpal == 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['SQUADRA'] == optggsSpal]
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['TEMPO'] == optgsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal == 'Tutte'and optgsSpal  != 'ENTRAMBI' and oppgsSpal != 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['POSIZIONE'] == oppgsSpal]
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['TEMPO'] == optgsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal != 'Tutte'and optgsSpal  == 'ENTRAMBI' and oppgsSpal != 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['POSIZIONE'] == oppgsSpal]
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['SQUADRA'] == optggsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsSpal != 'Tutte'and optgsSpal  != 'ENTRAMBI' and oppgsSpal != 'TUTTE' ):
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['POSIZIONE'] == oppgsSpal]
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['SQUADRA'] == optggsSpal]
					df_golsubiti_Spal = df_golsubiti_Spal.loc[df_golsubiti_Spal['TEMPO'] == optgsSpal]
					st.write(df_golsubiti_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Spal)-1
			ind_dif = len(list_corner_difesa_Spal)-1

			avvSpal, difesaSpal = st.columns(2)

			with avvSpal:
				op_avvSpal = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Spal, index = ind_avv)
			
			with difesaSpal:
				op_difSpal = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Spal, index = ind_dif)

			if(op_avvSpal == 'Tutti'and op_difSpal  == 'Tutti'):
				st.write(df_corner_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvSpal == 'Tutti'and op_difSpal  != 'Tutti'):
				df_corner_Spal = df_corner_Spal.loc[df_corner_Spal['DIFESA'] == op_difSpal]
				st.write(df_corner_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvSpal != 'Tutti'and op_difSpal  == 'Tutti'):
				df_corner_Spal = df_corner_Spal.loc[df_corner_Spal['SQUADRA'] == op_avvSpal]
				st.write(df_corner_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvSpal != 'Tutti'and op_difSpal  != 'Tutti'):
				df_corner_Spal = df_corner_Spal.loc[df_corner_Spal['SQUADRA'] == op_avvSpal]
				df_corner_Spal = df_corner_Spal.loc[df_corner_Spal['DIFESA'] == op_difSpal]
				st.write(df_corner_Spal.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsSpal)-1
			ind_avvbatt = len(list_corner_avvbatt_vsSpal)-1

			avv_vsSpal, difesa_vsSpal = st.columns(2)

			with avv_vsSpal:
				op_avv_vsSpal = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsSpal, index = ind_avv)

			with difesa_vsSpal:
				op_avvbatt_vsSpal = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:               ',
			      	list_corner_avvbatt_vsSpal, index = ind_avvbatt)

			if(op_avv_vsSpal == 'Tutti'and op_avvbatt_vsSpal  == 'Tutti'):
				st.write(df_corner_vsSpal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsSpal == 'Tutti'and op_avvbatt_vsSpal  != 'Tutti'):
				df_corner_vsSpal = df_corner_vsSpal.loc[df_corner_vsSpal['GIOC_SULLA_PALLA'] == op_avvbatt_vsSpal]
				st.write(df_corner_vsSpal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsSpal != 'Tutti'and op_avvbatt_vsSpal  == 'Tutti'):
				df_corner_vsSpal = df_corner_vsSpal.loc[df_corner_vsSpal['SQUADRA'] == op_avv_vsSpal]
				st.write(df_corner_vsSpal.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsSpal != 'Tutti'and op_avvbatt_vsSpal  != 'Tutti'):
				df_corner_vsSpal = df_corner_vsSpal.loc[df_corner_vsSpal['SQUADRA'] == op_avv_vsSpal]
				df_corner_vsSpal = df_corner_vsSpal.loc[df_corner_vsSpal['GIOC_SULLA_PALLA'] == op_avvbatt_vsSpal]
				st.write(df_corner_vsSpal.to_html(escape=False, index=False), unsafe_allow_html=True)

with Como:
	
	
	squadra = "Como"

	df_corner_Como = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Como['LINK'] = df_corner_Como['LINK'].apply(make_clickable)
	df_corner_Como = df_corner_Como.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	df_corner_Como = df_corner_Como.drop(columns = ['ATTACCA'])
	
	list_corner_Como = df_corner_Como['SQUADRA'].tolist()
	list_corner_Como = [*set(list_corner_Como)]
	list_corner_Como.sort()
	list_corner_Como.append('Tutti')

	list_corner_difesa_Como = df_corner_Como['DIFESA'].tolist()
	list_corner_difesa_Como = [*set(list_corner_difesa_Como)]
	list_corner_difesa_Como.sort()
	list_corner_difesa_Como.append('Tutti')
	
	df_corner_vsComo = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsComo['LINK'] = df_corner_vsComo['LINK'].apply(make_clickable)
	df_corner_vsComo = df_corner_vsComo.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsComo = df_corner_vsComo.drop(columns = ['DIFENDE'])
	
	list_corner_vsComo = df_corner_vsComo['SQUADRA'].tolist()
	list_corner_vsComo = [*set(list_corner_vsComo)]
	list_corner_vsComo.sort()
	list_corner_vsComo.append('Tutti')

	list_corner_difesa_vsComo = df_corner_vsComo['DIFESA'].tolist()
	list_corner_difesa_vsComo = [*set(list_corner_difesa_vsComo)]
	list_corner_difesa_vsComo.sort()
	list_corner_difesa_vsComo.append('Tutti')
	
	list_corner_avvbatt_vsComo = df_corner_vsComo['GIOC_SULLA_PALLA'].tolist()
	list_corner_avvbatt_vsComo = [*set(list_corner_avvbatt_vsComo)]
	list_corner_avvbatt_vsComo.sort()
	list_corner_avvbatt_vsComo.append('Tutti')


	
	df_golfatti_Como = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Como = df_golfatti_Como.drop(columns = ['ATTACCA'])
	df_golfatti_Como['LINK'] = df_golfatti_Como['LINK'].apply(make_clickable)
	df_golfatti_Como = df_golfatti_Como.rename(columns =  {'DIFENDE' : 'SQUADRA'})
	
	list_golfatti_Como = df_golfatti_Como['SQUADRA'].tolist()
	list_golfatti_Como = [*set(list_golfatti_Como)]
	list_golfatti_Como.sort()
	list_golfatti_Como.append('Tutti')
	
	list_marcatori_Como = df_golfatti_Como['GIOCATORE'].tolist()
	list_marcatori_Como = [*set(list_marcatori_Como)]
	list_marcatori_Como.sort()
	list_marcatori_Como.append('Tutti')
	
	
	df_golsubiti_Como = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Como = df_golsubiti_Como.drop(columns = ['DIFENDE'])
	df_golsubiti_Como['LINK'] = df_golsubiti_Como['LINK'].apply(make_clickable)
	df_golsubiti_Como = df_golsubiti_Como.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	
	list_golsubiti_Como = df_golsubiti_Como['SQUADRA'].tolist()
	list_golsubiti_Como = [*set(list_golsubiti_Como)]
	list_golsubiti_Como.sort()
	list_golsubiti_Como.append('Tutte')
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

				st.subheader(f'Tabella gol fatti :blue[{squadra}]')
				st.dataframe(df_golfatti_Como.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol fatti :blue[{squadra}]')
				col1, col2, col3, col4 = st.columns(4)
				with col1:
					tmp_df_gfsqd = df_golfatti_Como.groupby('GIOCATORE').size().reset_index(name = 'GOL FATTI')
					tmp_df_gfsqd = tmp_df_gfsqd.set_index('GIOCATORE')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gfsqd, use_container_width=True)
					st.dataframe(df_golfatti_Como['GIOCATORE'].value_counts().head(3), use_container_width=True)

				with col2:
					st.bar_chart(df_golfatti_Como['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Como['TEMPO'].value_counts(), use_container_width=True)	
					

				with col3:
					st.bar_chart(df_golfatti_Como['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Como['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:
					st.bar_chart(df_golfatti_Como['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golfatti_Como['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:
				
				ind = len(list_marcatori_Como)-1
				golf_Como_giocatore, golf_Como_tempo, golf_Como_posizione = st.columns(3)

				with golf_Como_giocatore:
				
					optggfComo = st.selectbox(
			      			f'Seleziona marcatore della {squadra}:  ', list_marcatori_Como, index = ind)
			
				
				with golf_Como_tempo:
				
					optgfComo = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol della {squadra}: ',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with golf_Como_posizione:
				
					oppgfComo = st.selectbox(
			      		f'Seleziona la posizione dei gol della {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggfComo == 'Tutti' and optgfComo  == 'ENTRAMBI' and oppgfComo == 'TUTTE' ):
						st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo != 'Tutti'and optgfComo  == 'ENTRAMBI' and oppgfComo == 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['GIOCATORE'] == optggfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo == 'Tutti'and optgfComo  != 'ENTRAMBI' and oppgfComo == 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['TEMPO'] == optgfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo == 'Tutti'and optgfComo  == 'ENTRAMBI' and oppgfComo != 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['POSIZIONE'] == oppgfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo != 'Tutti'and optgfComo  != 'ENTRAMBI' and oppgfComo == 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['GIOCATORE'] == optggfComo]
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['TEMPO'] == optgfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo == 'Tutti'and optgfComo  != 'ENTRAMBI' and oppgfComo != 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['POSIZIONE'] == oppgfComo]
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['TEMPO'] == optgfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo != 'Tutti'and optgfComo  == 'ENTRAMBI' and oppgfComo != 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['POSIZIONE'] == oppgfComo]
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['GIOCATORE'] == optggfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggfComo != 'Tutti'and optgfComo  != 'ENTRAMBI' and oppgfComo != 'TUTTE' ):
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['POSIZIONE'] == oppgfComo]
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['GIOCATORE'] == optggfComo]
					df_golfatti_Como = df_golfatti_Como.loc[df_golfatti_Como['TEMPO'] == optgfComo]
					st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)




		with Golsubiti:
			
			Stats, Link = st.tabs(["Statistiche","Link"])

			with Stats:

			
				st.subheader(f'Tabella gol subiti :blue[{squadra}]')
				st.dataframe(df_golsubiti_Como.drop(columns = ['LINK']), use_container_width=True)

				st.subheader(f'Statistiche sui gol subiti :blue[{squadra}]')


				col1, col2, col3, col4 = st.columns(4)
				with col1:

					tmp_df_gssqd = df_golsubiti_Como.groupby('SQUADRA').size().reset_index(name = 'GOL SUBITI')
					tmp_df_gssqd = tmp_df_gssqd.set_index('SQUADRA')
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'' : 'GIOCATORE'})
					#tmp_df_gssqd = tmp_df_gssqd.rename(columns =  {'SQUADRA' : 'GOL SUBITI'})

					st.bar_chart(tmp_df_gssqd, use_container_width=True)
					st.dataframe(df_golsubiti_Como['SQUADRA'].value_counts().head(3), use_container_width=True)
					

				with col2:

					st.bar_chart(df_golsubiti_Como['TEMPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Como['TEMPO'].value_counts(), use_container_width=True)				
					

				with col3:

					st.bar_chart(df_golsubiti_Como['POSIZIONE'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Como['POSIZIONE'].value_counts(), use_container_width=True)				
					

				with col4:

					st.bar_chart(df_golsubiti_Como['TIPO'].value_counts(), use_container_width=True)
					st.dataframe(df_golsubiti_Como['TIPO'].value_counts(), use_container_width=True)				
					

			with Link:

				ind = len(list_golsubiti_Como)-1
				gols_Como_giocatore, gols_Como_tempo, gols_Como_posizione = st.columns(3)

				with gols_Como_giocatore:
				
					optggsComo = st.selectbox(
			      			f'Seleziona squadra che ha segnato alla {squadra}:', list_golsubiti_Como, index = ind)
			
				
				with gols_Como_tempo:
				
					optgsComo = st.selectbox(
			      			f'Seleziona tempo di gioco dei gol alla {squadra}:',
			      			("1T","2T",'ENTRAMBI'), index = 2)
			
				with gols_Como_posizione:
				
					oppgsComo = st.selectbox(
			      		f'Seleziona la posizione dei gol alla {squadra}:',
			      		("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
			
				
				if(optggsComo == 'Tutte' and optgsComo  == 'ENTRAMBI' and oppgsComo == 'TUTTE' ):
						st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo != 'Tutte'and optgsComo  == 'ENTRAMBI' and oppgsComo == 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['SQUADRA'] == optggsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo == 'Tutte'and optgsComo  != 'ENTRAMBI' and oppgsComo == 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['TEMPO'] == optgsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo == 'Tutte'and optgsComo  == 'ENTRAMBI' and oppgsComo != 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['POSIZIONE'] == oppgsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo != 'Tutte'and optgsComo  != 'ENTRAMBI' and oppgsComo == 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['SQUADRA'] == optggsComo]
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['TEMPO'] == optgsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo == 'Tutte'and optgsComo  != 'ENTRAMBI' and oppgsComo != 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['POSIZIONE'] == oppgsComo]
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['TEMPO'] == optgsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo != 'Tutte'and optgsComo  == 'ENTRAMBI' and oppgsComo != 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['POSIZIONE'] == oppgsComo]
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['SQUADRA'] == optggsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optggsComo != 'Tutte'and optgsComo  != 'ENTRAMBI' and oppgsComo != 'TUTTE' ):
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['POSIZIONE'] == oppgsComo]
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['SQUADRA'] == optggsComo]
					df_golsubiti_Como = df_golsubiti_Como.loc[df_golsubiti_Como['TEMPO'] == optgsComo]
					st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind_avv = len(list_corner_Como)-1
			ind_dif = len(list_corner_difesa_Como)-1

			avvComo, difesaComo = st.columns(2)

			with avvComo:
				op_avvComo = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Como, index = ind_avv)
			
			with difesaComo:
				op_difComo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Como, index = ind_dif)

			if(op_avvComo == 'Tutti'and op_difComo  == 'Tutti'):
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo == 'Tutti'and op_difComo  != 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFESA'] == op_difComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo != 'Tutti'and op_difComo  == 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['SQUADRA'] == op_avvComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo != 'Tutti'and op_difComo  != 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['SQUADRA'] == op_avvComo]
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFESA'] == op_difComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsComo)-1
			ind_avvbatt = len(list_corner_avvbatt_vsComo)-1

			avv_vsComo, difesa_vsComo = st.columns(2)

			with avv_vsComo:
				op_avv_vsComo = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsComo, index = ind_avv)

			with difesa_vsComo:
				op_avvbatt_vsComo = st.selectbox(
			      	f'Seleziona quanti giocatori avversari presenti in battuta:                   ',
			      	list_corner_avvbatt_vsComo, index = ind_avvbatt)

			if(op_avv_vsComo == 'Tutti'and op_avvbatt_vsComo  == 'Tutti'):
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo == 'Tutti'and op_avvbatt_vsComo  != 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['GIOC_SULLA_PALLA'] == op_avvbatt_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo != 'Tutti'and op_avvbatt_vsComo  == 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['SQUADRA'] == op_avv_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo != 'Tutti'and op_avvbatt_vsComo  != 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['SQUADRA'] == op_avv_vsComo]
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['GIOC_SULLA_PALLA'] == op_avvbatt_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)
