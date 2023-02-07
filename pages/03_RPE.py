import streamlit as st
import pandas as pd
import numpy as np
import requests
import altair as alt
import matplotlib.pyplot as plt
from pprint import pprint
from datetime import date
from PIL import Image

#image = Image.open('https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/LOGHI/VFC_LOGO.png')
st.image(image, width=130)

today = date.today()
# dd/mm/YY
t_date = today.strftime("%d/%m/%Y")

st.set_page_config(page_title="VFC u19 Dashboard", layout="wide")
st.title("Dati RPE")

url_rpe = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/RPE/rpe_10.csv" # Make sure the url is the raw version of the file on GitHub
download_rpe = requests.get(url_rpe).content
df_rpe_ottobre = pd.read_csv(url_rpe)

from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl = 60)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
df = pd.DataFrame(rows)

Inserimento, Agosto, Settembre, Ottobre, Novembre, Dicembre, Gennaio, Febbraio, Marzo, Aprile, Maggio = st.tabs(
	["Inserimento", "Agosto","Settembre","Ottobre","Novembre","Dicembre","Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio"])

with Inserimento:
	st.text("Insert your RPE value")

	sel_player = st.selectbox(
		"Who are you?",
		('BADOUIN NOAH','BORECKI KRYSTIAN','BOUDRI AMIN','BUSATO LORENZO','CAMBER DAVID','CAMOLESE NICOLA',
		 'DA POZZO LORENZO','ENEM JAY','IVARSSON ISAK','JONSSON KRISTOFER','KARAGIANNIDIS GEORGIOS',
		 'KYVIK LEO', 'MAGNUSSON ARON','MAKADJI MORRE','MIKAELSSON HILMIR','MOZZO FILIPPO','OKORO ALVIN OBINHA',
		 'REMY MELVIN','RODRIGUES ALVES JAMES','SALVADOR TOMMASO','SANDBERG GABRIEL','SLOWIKOWSKI ERIK',
		 'SPERANDIO TOMMASO','VELCEA VALENTIN')
	)
	sel_date = st.date_input(
		"Training session date",)
	sel_session = st.radio(
		"Select the session",
		options=["Morning", "Afternoon"],
	)
	st.write("Today is: ",t_date)


	rpe = st.selectbox(
		'Rate effort of the session',
		(0, 0.3, 0.5, 0.7, 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10, 11), index = 8)
	#    rpe = st.slider('Rate effort of the session', 0, 10, 3)
	#    st.write("RPE value",rpe)
	b_confirm = st.button(label ='Confirm!')
	if b_confirm:
	    #st.write(sel_player,"- RPE:", rpe,"during ",sel_session," session on", sel_date)
	    new_row = {'Player':sel_player, 'Data':f'{sel_date} - {sel_session}', 'RPE':rpe}
	    st.write(new_row)

with Agosto:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Settembre:
	#st.subheader("RPE - Settembre")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

########NON SERVE + FARE QUESTO MA LEGGERE LE COLONNE INTERESSATE DEL FILE EXCEL!!!

with Ottobre:
	#st.subheader("RPE - Ottobre")
	df_rpe_week5 = pd.DataFrame({'GIOCATORE':[],'03p-Min':[],'03p-RPE':[],'03p-TL':[],'04/10m-Min':[],'04/10m-RPE':[],'04/10m-TL':[],'04/10p-Min':[],'04/10p-RPE':[],'04p/10-TL':[]
		,'05/10m-Min':[],'05/10m-RPE':[],'05/10m-TL':[],'05/10p-Min':[],'05/10p-RPE':[],'05/10p-TL':[],'06/10p-Min':[],'06/10p-RPE':[],'06/10p-TL':[],'07/10p-Min':[],'07/10p-RPE':[],'07/10p-TL':[]
		,'08/10p-Min':[],'08/10p-RPE':[],'08/10p-TL':[],'09/10m-Min':[],'09/10m-RPE':[],'09/10m-TL':[]})


	tabS, tabM, = st.tabs(["Settimanale","Mensile"])
	with tabS:
		opt_week = st.selectbox(
      'Seleziona la settimana:',
      ('WEEK 5', 'WEEK 6', 'WEEK 7','WEEK 8'), index = 0)
		if(opt_week == 'WEEK 5'):
			st.dataframe(df_rpe_week5)

with Novembre:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Dicembre:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Gennaio:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

	with tabS:
		opt_weekG = st.selectbox(
	  'Seleziona la settimana:',
	  ('WEEK 17', 'WEEK 18', 'WEEK 19','WEEK 20'), index = 0)
		if(opt_weekG == 'WEEK 17'):
			url_rpe_week17 = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/RPE/rpe_week17.xlsx" # Make sure the url is the raw version of the file on GitHub
			df_rpe_week17 = pd.read_excel(url_rpe_week17, usecols = "A:AF")
			st.dataframe(df_rpe_week17, use_container_width=True, height = 700)

			


with Febbraio:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Marzo:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Aprile:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

with Maggio:
	#st.subheader("RPE - Agosto")
	tabS, tabM, = st.tabs(["Settimanale","Mensile"])

