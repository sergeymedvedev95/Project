#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:00:29 2023

@author: sergeymedvedev
"""

import streamlit as st
import pandas as pd 
import plotly_express as px

st.header('Sergey Medvedev Sprint 6 Project')

df = pd.read_csv('vehicles_us.csv')

df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'))

columns_to_replace = ['cylinders' , 'odometer', 'is_4wd']
for column in columns_to_replace:
    print(column)
    df[column] = df[column].fillna(0)
    print('missing values in ', column, 'are replaced')
    
another_column_to_replace = ['paint_color']
for column in another_column_to_replace:
    print(column)
    df[column] = df[column].fillna('unknown')
    print('missing values in ', column, 'are replaced')

st.header('Table of Data')

show_table = st.checkbox('Show data table slice')
if show_table :
    st.write("""
    ### Data table slice
    """)
    st.table(df.head())

df.insert(0, 'id', range(0, 0 + len(df)))
grouped_cars = df.groupby(['type'])['model'].nunique().reset_index()
grouped_cars_sorted = grouped_cars.sort_values(by = 'model',ascending=False)

st.write("""
### Number of models per vehicle type shown in a descending order
""")
show_table = st.checkbox('Show table')
if show_table : 
    st.write("""
    ### Table of number of different models per type of vehicle
    """)
    grouped_cars = df.groupby(['type'])['model'].nunique().reset_index()
    grouped_cars_sorted = grouped_cars.sort_values(by = 'model',ascending=False)
    st.table(grouped_cars_sorted)

st.write("""
### Histogram of popularity of different types of vehicles
""")

histogram = px.bar(grouped_cars_sorted, x=grouped_cars_sorted.type, y=grouped_cars_sorted.model)
histogram.update_layout(title="<b> Popularity of the bodystyle")
st.plotly_chart(histogram)


st.write("""
### Scatterplot of various models of vehicles against their prices, represented by different types of cars 
""")


# Scatter plot
fig = px.scatter(df, x='model', y='price', color='type',
                  labels={
                     'model' : 'Model',
                     'price' : 'Price',
                     'type' : 'Type'
                 })
st.plotly_chart(fig)

st.write("""
### Scatterplot of years of vehicles against their price, represented by different conditions of vehicles 
""")

fig_1 = px.scatter(df, x='model_year', y='price', color='condition',
                 labels={
                     'model_year' : 'Year',
                     'price' : 'Price',
                     'condition' : 'Condition'
                 })
st.plotly_chart(fig_1)

st.write("""
## Block with Filtered Data - Filters will work on the graphs below
""")

price_range = st.slider(
     "What is your price range?",
     value=(0, 375000))

actual_range=list(range(price_range[0],price_range[1]+1))

option = st.checkbox(
    'Only high performance vehicles')

if option:
    filtered_data=df[df.price.isin(actual_range)]
    filtered_data=filtered_data[df.cylinders>=8]
else:
    filtered_data=df[df.price.isin(actual_range)]

st.write("""
### Scatterplot with filtered data
""")

fig_2 = px.scatter(filtered_data, x='model_year', y='price', color='type',
                  labels={
                     'model_year' : 'Model',
                     'price' : 'Price',
                     'type' : 'Type'
                 })
st.plotly_chart(fig_2)

st.write("""
### Histogram with filtered data
""")
hist_filt = px.bar(filtered_data, x=filtered_data.price, y=filtered_data.type, color= 'condition').update_xaxes(categoryorder = 'total descending')
st.plotly_chart(hist_filt)
