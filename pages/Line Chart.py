# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:28:51 2023
########################

import plotly.express as px
import streamlit as st


########################
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
def get_chart_51048942():
    import plotly.express as px
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    
    fig.update_layout(title_text='Solar Exploration: Life Expectancy Between 1950 And 2010')
    
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
        
get_chart_51048942()  
        
#########################################    

import streamlit as st

number = st.number_input('Insert a number')
st.write('The current number of moons orbiting your planet is ', number)

st.caption("This [line chart](https://en.wikipedia.org/wiki/Line_chart) shows the increase in life expectancy between 1950 and 2010 across the two countries. The countries are Australia and New Zealand. This information came from the [Our World](https://ourworldindata.org/charts) webpage. (Updated 2023)")

#########################################

@st.experimental_memo
def get_chart_42947925():
    import plotly.graph_objects as go
    import numpy as np

    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 3, 2, 3, 1])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, name="Sun",
                        line_shape='linear'))
    fig.add_trace(go.Scatter(x=x, y=y + 5, name="Jupiter",
                        text=["tweak line smoothness<br>with 'smoothing' in line object"],
                        hoverinfo='text+name',
                        line_shape='spline'))
    fig.add_trace(go.Scatter(x=x, y=y + 10, name="Mercury",
                        line_shape='vhv'))
    fig.add_trace(go.Scatter(x=x, y=y + 15, name="Venus",
                        line_shape='hvh'))
    fig.add_trace(go.Scatter(x=x, y=y + 20, name="Earth",
                        line_shape='vh'))
    fig.add_trace(go.Scatter(x=x, y=y + 25, name="Mars",
                        line_shape='hv'))

    fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    fig.update_layout(title_text='Solar Exploration: Magnetic Field ')


    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

get_chart_42947925()

st.caption("This [line chart](https://en.wikipedia.org/wiki/Line_chart) shows each planet's magnetic field relative to the planet's equator across the last four centuries. The planets listed are Mercury, Venus, Earth, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023)")

######################################### 






#########################################


st.subheader('Bar Chart with Plotly')
st.markdown('**Function:** Show change over time.')
st.markdown('**Function:** Understand relationships.')
st.markdown('**Charts in the same category:** Line, Column-Timeline, Area, Fan, Seismogram')
st.markdown('**Example:** Orbit movement')
   

