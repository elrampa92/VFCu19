import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
from pprint import pprint
from IPython.core.display import display, HTML
import plotly.express as px
#from streamlit_extras.stoggle import stoggle



def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link

    text = link.split('=')[0]
    return f'<a target="_blank" href="{link}">{"video"}</a>'

st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Avversari")

url_corner = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/CORNER.xlsx" # Make sure the url is the raw version of the file on GitHub
df_corner = pd.read_excel(url_corner, usecols = "A:I")

url_gol = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/DATABASE/GOL.xlsx"
df_gol = pd.read_excel(url_gol, usecols = "A:I")

Albinoleffe, Alessandria, Brescia, Cittadella, Como, Cremonese, Feralpisalò, Genoa, LRVicenza, Monza, Padova, Parma, Pordenone, Reggiana, Spal = st.tabs(
	["Albinoleffe","Alessandria","Brescia","Cittadella","Como","Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Padova", "Parma", "Pordenone", "Reggiana", "Spal"])

with Cittadella:
	
	squadra = "Cittadella"

	df_corner_Cittadella = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_vsCittadella = df_corner.loc[df_corner['DIFENDE'] == squadra]

	df_corner_Cittadella['LINK'] = df_corner_Cittadella['LINK'].apply(make_clickable)
	df_corner_vsCittadella['LINK'] = df_corner_vsCittadella['LINK'].apply(make_clickable)

	df_golfatti_Cittadella = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Cittadella = df_golfatti_Cittadella.drop(columns = ['ATTACCA'])
	#df_golfatti_Padova = df_golfatti_Padova.reset_index()

	df_golsubiti_Cittadella = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Cittadella = df_golsubiti_Cittadella.drop(columns = ['DIFENDE'])
	#df_golsubiti_Padova = df_golsubiti_Padova.reset_index()

	df_golfatti_Cittadella['LINK'] = df_golfatti_Cittadella['LINK'].apply(make_clickable)
	df_golsubiti_Cittadella['LINK'] = df_golsubiti_Cittadella['LINK'].apply(make_clickable)
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			st.write(df_golfatti_Cittadella.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Golsubiti:

			st.write(df_golsubiti_Cittadella.to_html(escape=False, index=False), unsafe_allow_html=True)
			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:

			st.write(df_corner_Cittadella.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:

			st.write(df_corner_vsCittadella.to_html(escape=False, index=False), unsafe_allow_html=True)



with Como:

	squadra = "Como"

	df_corner_Como = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_vsComo = df_corner.loc[df_corner['DIFENDE'] == squadra]

	df_corner_Como['LINK'] = df_corner_Como['LINK'].apply(make_clickable)
	df_corner_vsComo['LINK'] = df_corner_vsComo['LINK'].apply(make_clickable)

	df_golfatti_Como = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Como = df_golfatti_Como.drop(columns = ['ATTACCA'])
	#df_golfatti_Padova = df_golfatti_Padova.reset_index()

	df_golsubiti_Como = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Como = df_golsubiti_Como.drop(columns = ['DIFENDE'])
	#df_golsubiti_Padova = df_golsubiti_Padova.reset_index()

	
	df_golfatti_Como['LINK'] = df_golfatti_Como['LINK'].apply(make_clickable)
	df_golsubiti_Como['LINK'] = df_golsubiti_Como['LINK'].apply(make_clickable)

	Presenze, Gol, Iniziogioco, PInattive   = st.tabs(["Presenze","Gol","Inizio gioco","Palle Inattive"])

	with Presenze:

		st.write("Ciao")

	with Gol:
		Fatti, Subiti = st.tabs(["Fatti", "Subiti"])

		with Fatti:

			st.write(df_golfatti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Subiti:

			st.write(df_golsubiti_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

	with PInattive:
		Cornerf, Cornerc, Punizionif, Punizionic, Rigorif, Rigoric = st.tabs(["Corner a favore",
			"Corner contro", "Punizioni a favore", "Punizioni contro", "Rigori a favore", "Rigori contro"])

		with Cornerf:
			avvComo, difesaComo = st.columns(2)

			with avvComo:
				op_avvComo = st.selectbox(
			      	'Seleziona avversario:',
			      	("Albinoleffe","Alessandria","Brescia","Cittadella","Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Padova", "Parma", "Pordenone", "Reggiana", "Spal",'Tutti'), index = 14)
			with difesaComo:
				op_difComo = st.selectbox(
			      	'Seleziona tipo difesa:',
			      	("Uomo", "Zona", 'Mista', 'Tutti'), index = 3)

			if(op_avvComo == 'Tutti'and op_difComo  == 'Tutti'):
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo == 'Tutti'and op_difComo  != 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFESA'] == op_difComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo != 'Tutti'and op_difComo  == 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFENDE'] == op_avvComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avvComo != 'Tutti'and op_difComo  != 'Tutti'):
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFENDE'] == op_avvComo]
				df_corner_Como = df_corner_Como.loc[df_corner_Como['DIFESA'] == op_difComo]
				st.write(df_corner_Como.to_html(escape=False, index=False), unsafe_allow_html=True)
			#st.dataframe(df_corner_como, use_container_width=True, height = 600)

		with Cornerc:
			avvvsComo, tipovsComo = st.columns(2)

			with avvvsComo:
				op_avv_vsComo = st.selectbox(
			      	'Seleziona avversario: ',
			      	("Albinoleffe","Alessandria","Brescia","Cittadella","Cremonese", "Feralpisalò", "Genoa", "LRVicenza", "Monza", "Padova", "Parma", "Pordenone", "Reggiana", "Spal",'Tutti'), index = 14)
			with tipovsComo:
				op_tipo_vsComo = st.selectbox(
			      	'Seleziona tipo:',
			      	("Lungo", "Corto", 'Tutti'), index = 2)
			if(op_avv_vsComo == 'Tutti'and op_tipo_vsComo  == 'Tutti'):
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo == 'Tutti'and op_tipo_vsComo != 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['TIPO'] == op_tipo_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo != 'Tutti'and op_tipo_vsComo  == 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['ATTACCA'] == op_avv_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)

			elif(op_avv_vsComo != 'Tutti'and op_tipo_vsComo  != 'Tutti'):
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['DIFENDE'] == op_avv_vsComo]
				df_corner_vsComo = df_corner_vsComo.loc[df_corner_vsComo['TIPO'] == op_tipo_vsComo]
				st.write(df_corner_vsComo.to_html(escape=False, index=False), unsafe_allow_html=True)
			#st.dataframe(df_corner_como, use_container_width=True, height = 600)


with Cremonese:
	
	#st.dataframe(df)
	
	squadra = "Cremonese"

	df_corner_Cremonese = df_corner.loc[df_corner['ATTACCA'] == squadra]
	df_corner_vsCremonese = df_corner.loc[df_corner['DIFENDE'] == squadra]

	df_corner_Cremonese['LINK'] = df_corner_Cremonese['LINK'].apply(make_clickable)
	df_corner_vsCremonese['LINK'] = df_corner_vsCremonese['LINK'].apply(make_clickable)

	df_golfatti_Cremonese = df_gol.loc[df_gol['ATTACCA'] == squadra]
	df_golfatti_Cremonese = df_golfatti_Cremonese.drop(columns = ['ATTACCA'])
	#df_golfatti_Padova = df_golfatti_Padova.reset_index()

	df_golsubiti_Cremonese = df_gol.loc[df_gol['DIFENDE'] == squadra]
	df_golsubiti_Cremonese = df_golsubiti_Cremonese.drop(columns = ['DIFENDE'])
	#df_golsubiti_Padova = df_golsubiti_Padova.reset_index()

	df_golfatti_Cremonese['LINK'] = df_golfatti_Cremonese['LINK'].apply(make_clickable)
	df_golsubiti_Cremonese['LINK'] = df_golsubiti_Cremonese['LINK'].apply(make_clickable)
	

	Gol, Corner, Punizioni   = st.tabs(["Gol","Corner","Punizioni"])
	
	with Gol:
		
		Golfatti, Golsubiti = st.tabs(["Gol fatti","Gol subiti"])
		
		with Golfatti:

			st.write(df_golfatti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Golsubiti:

			st.write(df_golsubiti_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)
			
	with Corner:
		
		Favore, Contro = st.tabs(["Corner a favore","Corner contro"])
		
		with Favore:

			st.write(df_corner_Cremonese.to_html(escape=False, index=False), unsafe_allow_html=True)

		with Contro:

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

				with graf_golf_Padova:
					tmpgraf = df_golfatti_Padova['TEMPO'].value_counts()
					st.bar_chart(tmpgraf)
					#fig = px.bar(tmpgraf)
				



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

