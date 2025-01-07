import pandas as pd
import matplotlib.pyplot as plt
# import streamlit as st
# st.write('hello')
print('Hello1')

data = {
"rollno" : [1,2,3,4,5,6],
"marks" : [23,32,12,43,53,23]
}

df = pd.DataFrame(data)

print("/n DataFrame: "  , df.dtypes)