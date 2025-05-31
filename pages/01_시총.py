import streamlit as st
import plotly.graph_objects as go
import pandas as pd

data = {
    '기업명': ['Apple', 'Microsoft', 'Alphabet'],
    '2022': [2.07, 1.79, 1.15],
    '2023': [2.87, 2.53, 1.92],
    '2024': [3.78, 3.13, 2.32]
}

df = pd.DataFrame(data)

fig = go.Figure()
years = ['2022', '2023', '2024']

for i in range(len(df)):
    fig.add_trace(go.Scatter(
        x=years,
        y=[df.loc[i, year] for year in years],
        mode='lines+markers',
        name=df.loc[i, '기업명']
    ))

st.title("시가총액 변화")
st.plotly_chart(fig, use_container_width=True)
