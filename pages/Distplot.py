# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:27:48 2023

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
def get_chart_66135393():
    import plotly.figure_factory as ff
    import numpy as np

    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]

    group_labels = ['Venus', 'Earth', 'Mars']
    colors = ['rgb(93, 164, 214)', '#A6ACEC', '#63F5EF']

    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, colors=colors,
                             bin_size=.2, show_rug=False)

    # Add title
    fig.update_layout(title_text='Solar Exploration: Earth Days')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
        

get_chart_66135393()        
##########################################  

import streamlit as st

if st.button('Tell me something about the Sun.'):
    st.write('The Sun is nearly 4.5 billion years old.')
else:
    st.write('Our solar system is amazing!')




##########################################

@st.experimental_memo
def get_chart_43764040():
    import plotly.figure_factory as ff
    import numpy as np

    x1 = np.random.randn(200) - 1
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 1

    hist_data = [x1, x2, x3]

    group_labels = ['Venus', 'Earth', 'Mars']
    colors = ['rgb(93, 164, 214)', '#37AA9C', '#94F3E4']

    # Create distplot with curve_type set to 'normal'
    fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

    # Add title
    fig.update_layout(title_text='Solar Exploration: Earth Days')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

get_chart_43764040()
##########################################      


st.subheader('Distplot with Plotly')
st.markdown('**Function:** Compare values.')
st.markdown('**Function:** Understand relationships.')
st.markdown('**Charts in the same category:** Histogram, Boxplot, Violin, Dot Plot, Barcode, Cumulative Curvep')
st.markdown('**Example:** Elements distribution')
