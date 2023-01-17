# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:26:49 2023

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
def get_chart_98774632():
    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Scatter(
        x=['Mercury', 'Venus',
           'Mars', 'Jupiter'], y=[10, 11, 12, 13],
        mode='markers',
        
        marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(93, 164, 214)',  'rgb(93, 164, 214)', 'rgb(255, 65, 54)'],
        size=[40, 60, 80, 100])
    )])
    
    fig.update_layout(title_text='Solar Exploration: Distance From The Sun')


    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
get_chart_98774632()        
########################################

planet = st.radio(
    "What\'s your favorite planet?",
    ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'))

if planet == 'Mercury':
    st.write('You selected Mercury. Did you know **"Mercury—the smallest planet in our solar system and closest to the Sun—is only slightly larger than Earth\'s Moon. Mercury is the fastest planet, zipping around the Sun every 88 Earth days."** - Nasa, 2022')
elif planet == 'Venus':
        st.write('You selected Venus. Did you know **"Venus spins slowly in the opposite direction from most planets. A thick atmosphere traps heat in a runaway greenhouse effect, making it the hottest planet in our solar system."**- Nasa, 2022')
elif planet == 'Earth':
        st.write('You selected Earth. Did you know **"Earth—our home planet—is the only place we know of so far that’s inhabited by living things. It\'s also the only planet in our solar system with liquid water on the surface."**- Nasa, 2022')
elif planet == 'Mars':
        st.write('You selected Mars. Did you know **"Mars is a dusty, cold, desert world with a very thin atmosphere. There is strong evidence Mars was—billions of years ago—wetter and warmer, with a thicker atmosphere."**- Nasa, 2022')
elif planet == 'Jupiter':
        st.write('You selected Jupiter. Did you know **"Jupiter is more than twice as massive than the other planets of our solar system combined. The giant planet\'s Great Red spot is a centuries-old storm bigger than Earth."**- Nasa, 2022' )
else:
    st.write("You didn\'t select a planet.")
    
st.caption("This [bubble chart](https://en.wikipedia.org/wiki/Bubble_chart) shows the planet's distance from the Sun. The planets listed are Mercury, Venus, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023).")

#######################################

@st.experimental_memo
def get_chart_19077817():
    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Scatter(
        x=['Mercury', 'Venus', 'Earth',
           'Mars', 'Jupiter', ' Saturn'],
        y=[1, 3.2, 5.4, 7.6, 9.8, 12.5],
        mode='markers',
        marker=dict(
            color=[120, 125, 130, 135, 140, 145],
            size=[15, 30, 55, 70, 85, 100],
            showscale=True
            )
    )])
    
#size=[15, 30, 55, 70, 90, 110],
    
    fig.update_layout(title_text='Solar Exploration: Distance From The Sun')


    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
get_chart_19077817()

st.caption("Using a gradient colour scheme, this [bubble chart](https://en.wikipedia.org/wiki/Bubble_chart) shows the planet's distance from the Sun. The planets listed are Mercury, Venus, Mars and Jupiter. This information came from the [NASA](https://solarsystem.nasa.gov/planets/mercury/overview/) solar system webpage. (Updated 2023).")
#######################################


st.subheader('Bubble Chart with Plotly')
st.markdown('**Function:** Understand relationships.')
st.markdown('**Charts in the same category:** Scatterplot, Line-Column, Scatterplot Connected, XY-Heatmap')
st.markdown('**Example:** Elements vs Life Expectancy')
