

import streamlit as st
import pandas as pd
import numpy as np

info = st.container()
dataset = st.container()

with info:
    st.markdown('**Sale con fritas**')

with dataset:
    data = pd.read_csv('/Users/javi/Documents/APP/prueba_2/data/customers.csv',delimiter=",", decimal=".")
    st.write(data.head(20))        