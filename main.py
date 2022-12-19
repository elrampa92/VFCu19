import streamlit as st
import pandas as pd
import numpy as np
import requests


st.write("provissima!")

url = "https://raw.githubusercontent.com/elrampa92/VFCu19_Dashboard/main/MINUTAGGI/MINUTAGGI.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content


df_minutaggi = pd.read_csv(url)

st.write(df_minutaggi)

