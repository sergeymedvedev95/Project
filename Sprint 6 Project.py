#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:00:29 2023

@author: sergeymedvedev
"""

import streamlit as st
import pandas as pd 
import plotly_express as px

st.write("""
### Sergey Medvedev Sprint 6 Project
""")

st.write("""
#### Table of data
""")

df = pd.read_csv('/Users/sergeymedvedev/Downloads/vehicles_us.csv')

columns_to_replace = ['model_year', 'cylinders' , 'odometer', 'paint_color', 'is_4wd']
for column in columns_to_replace:
    print(column)
    df[column] = df[column].fillna('unknown')
    print('missing values in ', column, 'are replaced')
st.table(df.head())


df.insert(0, 'id', range(0, 0 + len(df)))

st.write("""
### Proportion of different types of vehicles
""")
grouped_cars = df.groupby('type')['id'].nunique().reset_index()
st.table(grouped_cars)

st.write("""
### Histogram of various consition of vehicles
""")

hist = px.histogram(df, x='condition', color = 'type')
st.plotly_chart(hist)


st.write("""
### Pie chart of the representation of different types of vehicles
""")

pie = px.pie(grouped_cars, values=grouped_cars.id, names=grouped_cars.type)
st.plotly_chart(pie)

st.write("""
### Scatterplot of a price againt model year of vehicles, represented by different types of cars 
""")

fig = px.scatter(df, x='model_year', y='price', color='type')
st.plotly_chart(fig)

st.write("""
### Scatterplot of a price againt model year of vehicles, represented by different conditions of cars 
""")

fig_1 = px.scatter(df, x='model_year', y='price', color='condition')
st.plotly_chart(fig_1)


st.write("""
## Block with Filtered Data 
""")

rest_type = df['type'].unique()
make_choice = st.sidebar.selectbox('Select type of vehicle:', rest_type)
filtered_type = df[df.type==make_choice]

st.write("""
### Scatterplot with filtered data
""")

fig_2 = px.scatter(filtered_type, x='model_year', y='price', color='condition')
st.plotly_chart(fig_2)

st.write("""
### Histogram with filtered data
""")
hist_filt = px.histogram(filtered_type, x='condition')
st.plotly_chart(hist_filt)

