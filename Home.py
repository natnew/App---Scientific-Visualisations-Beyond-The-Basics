# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:44:54 2023

@author: NatashaNewbold


"""
#####################################


import plotly.express as px
import streamlit as st

#####################################

st.title('Scientific Visualisations: Beyond The Basics')

st.subheader('A gallary of data visualisations using Python.')

######################################

import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

fig.update_layout(title_text='Life Expectancy vs. GDP')

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
    
##########################

st.caption('An interactive graph taken from the Streamlit library. This bubble graph shows the correlation between GDP per capita and life expectancy across five continents. This information was taken from the [Our World](https://ourworldindata.org/charts) webpage. (Updated 2023).')

st.subheader("Choosing The Right Graph")
st.markdown("Several online tools and resources assist you with selecting the right tool. [CHARTI](https://chartio.com/learn/charts/essential-chart-types-for-data-visualization/) provides a blog post describing the different chart types. Yan Holtz has a detailed website called The Python Graph Library, where graphs have been categorised based on their function. CodeAcademy has a blog containing a diagram that you can use to assist you when selecting a graph. You may also explore [Visual Vocabulary](http://ft-interactive.github.io/visual-vocabulary/), an interactive web app that makes chart selection much easier.")

st.subheader("What Can Space Tell Us About Life On Earth?")
st.markdown("The data visualisations in this app aim to give you an insight into how space can improve life on Earth. We will use the interactive [Plotly Library](https://plotly.com/python/) due to its seamless integration with many applications and beautiful visualisations. ")
st.markdown("Note: This is a proof-of-concept app. Use at your own discretion.")
st.markdown("Reach out to me on [LinkedIn](https://www.linkedin.com/in/natasha-newbold/)")
