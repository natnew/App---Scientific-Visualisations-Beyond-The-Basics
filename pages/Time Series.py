# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:29:06 2023

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
def get_chart_78288066():
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = px.line(df, x='Date', y='AAPL.High', title='Time Series with Range Slider and Selectors')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    
    fig.update_layout(title_text='Solar Exploration: Earth Days')
    
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        
get_chart_78288066()        
#########################################  

import datetime
import streamlit as st

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Your spaceship alarm is set for', t)


######################################### 

@st.experimental_memo
def get_chart_86765810():
    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["2021-01-01", "2021-04-01", "2021-07-01", "2021-10-01"],
        y=[1000, 1500, 1700, 2000],
        xperiod="M3",
        xperiodalignment="middle",
        xhoverformat="Q%q",
        hovertemplate="%{y}%{_xother}"
    ))

    fig.add_trace(go.Scatter(
        x=["2021-01-01", "2021-02-01", "2021-03-01",
          "2021-04-01", "2021-05-01", "2021-06-01",
          "2021-07-01", "2021-08-01", "2021-09-01",
          "2021-10-01", "2021-11-01", "2021-12-01"],
        y=[1100,1050,1200,1300,1400,1700,1500,1400,1600, 1700, 1800, 2000],
        xperiod="M1",
        xperiodalignment="middle",
        hovertemplate="%{y}%{_xother}"
    ))

    fig.update_layout(hovermode="x unified")

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)


get_chart_86765810()


######################################### 


st.subheader('Bar Chart with Plotly')
st.markdown('**Function:** Show change over time.')
st.markdown('**Function:** Understand relationships.')
st.markdown('**Charts in the same category:** Scatterplot, Line-Column, Scatterplot Connected, XY-Heatmap')
st.markdown('**Example:** Elements vs Life Expectancy')
    