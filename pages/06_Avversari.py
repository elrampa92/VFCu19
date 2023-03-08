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

			avvCremo, difesaCremo = st.columns(2)

			with avvCremo:
				op_avvCremo = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Brescia, index = ind_avv)
			
			with difesaCremo:
				op_difCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	list_corner_difesa_Brescia, index = ind_dif)

			if(op_avvCremo == 'Tutti'and op_difCremo  == 'Tutti'):
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo == 'Tutti'and op_difCremo  != 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['DIFESA'] == op_difCremo]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo != 'Tutti'and op_difCremo  == 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['SQUADRA'] == op_avvCremo]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvCremo != 'Tutti'and op_difCremo  != 'Tutti'):
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['SQUADRA'] == op_avvCremo]
				df_corner_Brescia = df_corner_Brescia.loc[df_corner_Brescia['DIFESA'] == op_difCremo]
				st.write(df_corner_Brescia.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:
			
			ind_avv = len(list_corner_vsBrescia)-1
			ind_dif = len(list_corner_difesa_vsBrescia)-1

			avv_vsCremo, difesa_vsCremo = st.columns(2)

			with avv_vsCremo:
				op_avv_vsCremo = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsBrescia, index = ind_avv)

			with difesa_vsCremo:
				op_dif_vsCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra} :',
			      	list_corner_difesa_vsBrescia, index = ind_dif)

			if(op_avv_vsCremo == 'Tutti'and op_dif_vsCremo  == 'Tutti'):
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo == 'Tutti'and op_dif_vsCremo  != 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['DIFESA'] == op_dif_vsCremo]
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_dif_vsCremo  == 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['SQUADRA'] == op_avv_vsCremo]
				st.write(df_corner_vsBrescia.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_dif_vsCremo  != 'Tutti'):
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['SQUADRA'] == op_avv_vsCremo]
				df_corner_vsBrescia = df_corner_vsBrescia.loc[df_corner_vsBrescia['DIFESA'] == op_dif_vsCremo]
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
			ind_dif = len(list_corner_difesa_vsCremonese)-1

			avv_vsCremo, difesa_vsCremo = st.columns(2)

			with avv_vsCremo:
				op_avv_vsCremo = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsCremonese, index = ind_avv)

			with difesa_vsCremo:
				op_dif_vsCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra} :',
			      	list_corner_difesa_vsCremonese, index = ind_dif)

			if(op_avv_vsCremo == 'Tutti'and op_dif_vsCremo  == 'Tutti'):
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo == 'Tutti'and op_dif_vsCremo  != 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['DIFESA'] == op_dif_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_dif_vsCremo  == 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['SQUADRA'] == op_avv_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsCremo != 'Tutti'and op_dif_vsCremo  != 'Tutti'):
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['SQUADRA'] == op_avv_vsCremo]
				df_corner_vsCremonese = df_corner_vsCremonese.loc[df_corner_vsCremonese['DIFESA'] == op_dif_vsCremo]
				st.write(df_corner_vsCremonese.to_html(escape=False, index=False), unsafe_allow_html=True)
			
