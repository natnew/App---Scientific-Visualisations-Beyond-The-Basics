# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:59:11 2023

@author: NatashaNewbold
"""

########################

import plotly.express as px
import streamlit as st


########################

st.title('Scientific Visualisations: Beyond The Basics')

st.subheader('A gallary of data visualisations using Python.')

######################################




########################################

@st.experimental_memo
def get_chart_81583906():
    import plotly.graph_objects as go

    colors = ['rgb(93, 164, 214)',] * 5
    colors[4] = 'crimson'

    fig = go.Figure(data=[go.Bar(
        x=['Mercury', 'Venus', 'Earth',
           'Mars', 'Jupiter'],
        y=[88 , 225, 365, 686, 4330],
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    
    fig.update_layout(title_text='Solar Exploration: Earth Days Per Planet')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
get_chart_81583906()

###########################

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Mercury", "88d")
col2.metric("Venus", "225d")
col3.metric("Earth", "365d")
col4.metric("Mars", "1.88y")
col5.metric("Jupiter", "11.86y")

st.caption("This [bar chart](https://en.wikipedia.org/wiki/Bar_chart) shows the length of a year for each planet. The planets listed are Mercury, Venus, Earth, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023).")

###########################


#############################

@st.experimental_memo
def get_chart_68279038():
    import plotly.graph_objects as go

    months = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months,
        y=[20, 14, 25, 16, 18],
        name='Primary Element',
        marker_color='crimson'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=[19, 14, 22, 14, 16],
        name='Secondary Element',
        marker_color='rgb(93, 164, 214)'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45, title_text='Solar Exploration: Elements Per Planet')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

get_chart_68279038()

st.caption("This [bar chart](https://en.wikipedia.org/wiki/Bar_chart) shows the two most abundant elements for each planet. The planets listed are Mercury, Venus, Earth, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023).")

##############################################

st.subheader('Bar Chart with Plotly')
st.markdown('**Function:** Compare values or show distribution.')
st.markdown('**Charts in the same category:** Histogram, Boxplot, Violin, Dot Plot, Barcode, Cumulative Curve')
st.markdown('**Example:** Element distribution.')





##############################################

