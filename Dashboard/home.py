import streamlit as st 
import pandas as pd 
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go 

st.markdown("<h1 style='color:white; font-weight:bolder; background-color:red; border:4px solid white; text-align:center;'>Movie Rating Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='color:black; text-align:center; margin-top:20px;'>This project is for Analyizing the movie rating according the year </h5>", unsafe_allow_html=True)
# st.image(use_column_width=True)

st.markdown("<h3 style='color:black; text-align:center; '>About Detaset</h3>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'> The dataset, which includes manually recorded data on movie ratings in India , has been processed meticulously to remove sensitive information, through careful encoding. The final dataset comprises 32 attributes across 12,316 recorded of flop movie. Preprocessing has prepared the data for analyzing key causes of flop mmovies, with plans to use a range of machine learning classification algorithms for analysis. </p>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'> India experiences one of the world’s highest rates movie, with over 150,000 cr. annually. To understand and categorize movies in India, we can examine multiple factors like causes, wrong actor, bad story, and backgroud editing details. </p>", unsafe_allow_html=True)


st.markdown("<h5 style='color:black; margin-top:20px;'>Causes:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'>The main contributors of flop movies is in India included not a highlevel VFX and good story salso a big actors not work on main content.</p>", unsafe_allow_html=True)

st.markdown("<h5 style='color:black; margin-top:20px;'>Types of Accidents:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'>The common flop movies in India include head-on collisions, rear-end collisions, side-impact of badactors, and bad story.</p>", unsafe_allow_html=True)

st.markdown("<h5 style='color:black; margin-top:20px;'>Classification:</h5>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'>flop  movies in India can be categorized into several main types. bad story and not a good director work for passion it work only on money, such as director, bad actors, bad story, and normal souting of movies likes without VFX. </p>", unsafe_allow_html=True)
st.markdown("<p style='color:black;'>By examining and categorizing movies based on these factors, we can identify primaryreason and implement effective prevention strategies. These may include infrastructure improvements, enhancing directors awareness of VFX regulations, and enforcing stricter penalties for actors. </p>", unsafe_allow_html=True)