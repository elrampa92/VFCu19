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
sheet_url = st.secrets["gol_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
df_gol = pd.DataFrame(rows)
df_gol = df_gol.drop(columns = ['CT'])


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link

    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{"video"}</a>'



url_corner = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/CORNER.xlsx" # Make sure the url is the raw version of the file on GitHub
df_corner = pd.read_excel(url_corner, usecols = "A:I")

url_gol = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/GOL.xlsx"
#df_gol = pd.read_excel(url_gol, usecols = "A:I")

Albinoleffe, Alessandria, Brescia, Cittadella, Como, Cremonese, Feralpisalò, Genoa, LRVicenza, Monza, Padova, Parma, Pordenone, Reggiana, Spal = st.tabs(
	["Albinoleffe","Alessandria","Brescia","Cittadella","Como","Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Padova", "Parma", "Pordenone", "Reggiana", "Spal"])

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
	
	df_corner_vsCremonese = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsCremonese['LINK'] = df_corner_vsCremonese['LINK'].apply(make_clickable)
	df_corner_vsCremonese = df_corner_vsCremonese.rename(columns =  {'ATTACCA' : 'SQUADRA'})
	df_corner_vsCremonese = df_corner_vsCremonese.drop(columns = ['DIFENDE'])
	
	list_corner_vsCremonese = df_corner_vsCremonese['SQUADRA'].tolist()
	list_corner_vsCremonese = [*set(list_corner_vsCremonese)]
	list_corner_vsCremonese.sort()
	list_corner_vsCremonese.append('Tutti')

	
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
	list_golsubiti_Cremonese.append('Tutti')
	

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
			
				
				if(optgfCremonese == 'ENTRAMBI' and oppgfCremonese  == 'TUTTE' and optggfCremonese == 'Tutti' ):
						st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optgfCremonese == 'ENTRAMBI'and oppgfCremonese  == 'TUTTE' and optggfCremonese != 'Tutti' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)
					
				elif(optgfCremonese == 'ENTRAMBI'and oppgfCremonese  != 'TUTTE' and optggfCremonese != 'Tutti' ):
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['GIOCATORE'] == optggfCremonese]
					df_golfatti_Cremonese = df_golfatti_Cremonese.loc[df_golfatti_Cremonese['POSIZIONE'] == oppgfCremonese]
					st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)
					
				elif(optgfCremonese != 'ENTRAMBI'and oppgfCremonese  == 'TUTTE' and optggfCremonese == 'Tutti' ):
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

				st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:
			
			ind = len(list_corner_Cremonese)-1
			avvCremo, difesaCremo = st.columns(2)

			with avvCremo:
				op_avvCremo = st.selectbox(f'Seleziona avversario della {squadra} :', list_corner_Cremonese, index = ind)
			
			with difesaCremo:
				op_difCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra}:',
			      	("Uomo", "Zona", 'Mista', 'Tutti'), index = 3)

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
			
			ind = len(list_corner_vsCremonese)-1
			avv_vsCremo, difesa_vsCremo = st.columns(2)

			with avv_vsCremo:
				op_avv_vsCremo = st.selectbox(f'Seleziona avversario della {squadra} che batte:', list_corner_vsCremonese, index = ind)

			with difesa_vsCremo:
				op_dif_vsCremo = st.selectbox(
			      	f'Seleziona tipo difesa avversario della {squadra} :',
			      	("Uomo", "Zona", 'Mista', 'Tutti'), index = 3)

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
			

with Padova:

	squadra = "Padova"

	df_corner_Padova = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_Padova = df_corner_Padova.drop(columns = ['ATTACCA'])

	df_corner_vsPadova = df_corner.loc[df_corner['DIFENDE'] == squadra]
	df_corner_vsPadova = df_corner_vsPadova.drop(columns = ['DIFENDE'])

	df_corner_Padova['LINK'] = df_corner_Padova['LINK'].apply(make_clickable)
	df_corner_vsPadova['LINK'] = df_corner_vsPadova['LINK'].apply(make_clickable)

	df_golfatti_Padova = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Padova = df_golfatti_Padova.drop(columns = ['ATTACCA'])
	#df_golfatti_Padova = df_golfatti_Padova.reset_index()

	df_golsubiti_Padova = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Padova = df_golsubiti_Padova.drop(columns = ['DIFENDE'])
	#df_golsubiti_Padova = df_golsubiti_Padova.reset_index()

	
	df_golfatti_Padova['LINK'] = df_golfatti_Padova['LINK'].apply(make_clickable)
	df_golsubiti_Padova['LINK'] = df_golsubiti_Padova['LINK'].apply(make_clickable)


	Presenze, Gol, Iniziogioco, PInattive   = st.tabs(["Presenze","Gol","Inizio gioco","Palle Inattive"])

	with Presenze:

		st.write("Ciao")

	with Gol:
		Fatti, Subiti = st.tabs(["Fatti", "Subiti"])

		with Fatti:
			tab_golf_Padova, graf_golf_Padova = st.columns(2)

			with tab_golf_Padova:
				optgfPadova = st.selectbox(
			      	f'Seleziona tempo di gioco del gol del {squadra}:',
			      	("1T","2T",'ENTRAMBI'), index = 2)
				oppgfPadova = st.selectbox(
			      	f'Seleziona la posizione del gol del {squadra}:',
			      	("FUORI AREA", "AREA", 'AREA PICCOLA', 'TUTTE'), index = 3)
				if(optgfPadova == 'ENTRAMBI'and oppgfPadova  == 'TUTTE'):
					#st.dataframe(df_golfatti_Padova)
					st.write(df_golfatti_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optgfPadova == 'ENTRAMBI'and oppgfPadova  != 'TUTTE'):
					df_golfatti_Padova = df_golfatti_Padova.loc[df_golfatti_Padova['POSIZIONE'] == oppgfPadova]
					st.write(df_golfatti_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optgfPadova != 'ENTRAMBI'and oppgfPadova  == 'TUTTE'):
					df_golfatti_Padova = df_golfatti_Padova.loc[df_golfatti_Padova['TEMPO'] == optgfPadova]
					st.write(df_golfatti_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

				elif(optgfPadova != 'Tutti'and oppgfPadova  != 'Tutti'):
					df_golfatti_Padova = df_golfatti_Padova.loc[df_golfatti_Padova['TEMPO'] == optgfPadova]
					df_golfatti_Padova = df_golfatti_Padova.loc[df_golfatti_Padova['POSIZIONE'] == oppgfPadova]
					st.write(df_golfatti_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)
				



		with Subiti:

			st.write(df_golsubiti_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)




	with PInattive:
		Cornerf, Cornerc, Punizionif, Punizionic, Rigorif, Rigoric = st.tabs(["Corner a favore",
			"Corner contro", "Punizioni a favore", "Punizioni contro", "Rigori a favore", "Rigori contro"])

		with Cornerf:
			avvPadova, difesaPadova = st.columns(2)

			with avvPadova:
				op_avvPadova = st.selectbox(
			      	f'Seleziona avversario del {squadra}:',
			      	("Albinoleffe","Alessandria","Brescia","Cittadella", "Como", "Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Parma", "Pordenone", "Reggiana", "Spal",'Tutti'), index = 14)
			with difesaPadova:
				op_difPadova = st.selectbox(
			      	f'Seleziona tipo difesa avversario del {squadra}:',
			      	("Uomo", "Zona", 'Mista', 'Tutti'), index = 3)

			if(op_avvPadova == 'Tutti'and op_difPadova  == 'Tutti'):
				st.write(df_corner_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvPadova == 'Tutti'and op_difPadova  != 'Tutti'):
				df_corner_Padova = df_corner_Padova.loc[df_corner_Padova['DIFESA'] == op_difPadova]
				st.write(df_corner_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvPadova != 'Tutti'and op_difPadova  == 'Tutti'):
				df_corner_Padova = df_corner_Padova.loc[df_corner_Padova['DIFENDE'] == op_avvPadova]
				st.write(df_corner_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvPadova != 'Tutti'and op_difPadova  != 'Tutti'):
				df_corner_Padova = df_corner_Padova.loc[df_corner_Padova['DIFENDE'] == op_avvPadova]
				df_corner_Padova = df_corner_Padova.loc[df_corner_Padova['DIFESA'] == op_difPadova]
				st.write(df_corner_Padova.to_html(escape=False, index=False), unsafe_allow_html=True)
			#st.dataframe(df_corner_como, use_container_width=True, height = 600)

		with Cornerc:
			op_avv_vsPadova = st.selectbox(
			      	f'Seleziona avversario del {squadra} che batte:',
			      	("Albinoleffe","Alessandria","Brescia","Cittadella", "Como", "Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Parma", "Pordenone", "Reggiana", "Spal",'Tutti'), index = 14)
		
			if(op_avv_vsPadova == 'Tutti'):
				st.write(df_corner_vsPadova.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsPadova != 'Tutti'):
				df_corner_vsPadova = df_corner_vsPadova.loc[df_corner_vsPadova['ATTACCA'] == op_avv_vsPadova]
				st.write(df_corner_vsPadova.to_html(escape=False, index=False), unsafe_allow_html=True)

