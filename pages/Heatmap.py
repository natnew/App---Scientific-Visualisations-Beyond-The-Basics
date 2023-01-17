# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:28:25 2023

@author: NatashaNewbold
"""

########################

import plotly.express as px
import streamlit as st


########################
st.title('Scientific Visualisations: Beyond The Basics')

st.subheader('A gallary of data visualisations using Python.')

######################################

@st.experimental_memo
def get_chart_37340223():
    import plotly.graph_objects as go

    fig = go.Figure(data=go.Heatmap(
                       z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                       x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                       y=['Morning', 'Afternoon', 'Evening'],
                       hoverongaps = False, colorscale = 'Blues'))

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    fig.update_layout(title_text='Solar Exploration: Earth Days')
    
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
get_chart_37340223()        
        
#########################################  

import streamlit as st

title = st.text_input('Name your own planet', 'Venus')
st.write('Your planet is called', title)

st.caption("This [heatmap](https://en.wikipedia.org/wiki/Heat_map) shows each planet's atmospheric composition during different times of the day and week. The planets listed are Mercury, Venus, Earth, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023)")

##########################################

@st.experimental_memo
def get_chart_54456624():
    import plotly.graph_objects as go
    import datetime
    import numpy as np
    np.random.seed(1)

    programmers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    base = datetime.datetime.today()
    dates = base - np.arange(180) * datetime.timedelta(days=1)
    z = np.random.poisson(size=(len(programmers), len(dates)))

    fig = go.Figure(data=go.Heatmap(
            z=z,
            x=dates,
            y=programmers,
            colorscale='Blues'))

    fig.update_layout(
        title='Solar Exploration: Earth Days',
        xaxis_nticks=36)


    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
get_chart_54456624()

st.caption("This [heatmap](https://en.wikipedia.org/wiki/Heat_map) shows each planet's atmospheric composition during different times of the day, week and year. The planets listed are Mercury, Venus, Earth, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023)")

#########################################      


st.subheader('Bar Chart with Plotly')
st.markdown('**Function:** Showing hierarchy or correlation.')
st.markdown('**Function:** Understand relationships.')
st.markdown('**Charts in the same category:** Scatterplot, Line-Column, Scatterplot Connected, Bubble Chart, XY-Heatmap')
st.markdown('**Example:** Elements & Life Expectancy')
