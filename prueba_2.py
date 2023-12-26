

import streamlit as st
import pandas as pd
import numpy as np

info = st.container()
dataset = st.container()

with info:
    st.markdown('**Sale con fritas**')

with dataset:
    url = "https://raw.githubusercontent.com/usebien/prueba_3/main/customers.csv"
    data = pd.read_csv(url)
    st.write(data.head(20))        
