# import liberaries 
import streamlit as st # for web app, front end
import plotly.express as px # for ploting, graphing
import pandas as pd # for data manipulation, data analysis
# Importing the dataset
st.title("Gapminder Data Visualization")
df=px.data.gapminder() # to load the data
# show top 10 countries with highest population uniquely
df=df.sort_values(by="pop",ascending=False) # sort the data by population
df=df.drop_duplicates(subset="country",keep="first") # drop duplicate countries
# show the data
st.dataframe(df.head(10)) # show the data in table format
# summary statistics
st.write(df.describe())
# data management
year_option=df["year"].unique().tolist() # get the unique years
# year=st.selectbox("Select Year",year_option,0) # create a drop down menu
# filter the data
# df=df[df["year"]==year] # filter the data by year
fig=px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",
               hover_name="continent",log_x=True,size_max=55
               ,range_x=[100,100000],range_y=[20,90]
                ,animation_frame="year",animation_group="country",
                labels=dict(pop="Population",gdpPercap="GDP Per Capita",lifeExp="Life Expectancy")
                ,title="Gapminder Data Visualization",template="plotly_dark"
                ,color_continuous_scale=px.colors.sequential.Viridis
                ,hover_data=["continent"]) # create the plot
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"]=3000 # set the animation speed
fig.update_layout(width=800,height=600) # set the width and height of the plot
st.plotly_chart(fig) # show the plot
