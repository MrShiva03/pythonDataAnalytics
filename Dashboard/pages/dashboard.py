import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.title("Movie Rating Analysis")

df = pd.read_csv("dataset.csv")
st.dataframe(df)

# st.plotly_chart(fig)

#1.....

years = df["Year"].unique()
years.sort()

colors = sns.color_palette("Purples", len(years))

color_mapping = {year: colors[i] for i, year in enumerate(years)}

bar_colors = df["Year"].map(color_mapping)

Freq = df["Year"].value_counts().sort_index().plot(
    kind="bar", 
    title="Distribution of Movies Released per Year", 
    figsize=(16, 8), 
    color=bar_colors
)

Freq.set_xlabel("Year")
Freq.set_ylabel("Frequency")
plt.grid(True, axis='y')
st.plt.show()
