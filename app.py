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
show_histogram_bodystyle = st.checkbox('Show the histogram of popularity of the bodystyle')
if show_histogram_bodystyle :
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
show_scatter_plot = st.checkbox('Show scatter plot of model of vehicles against price')
if show_scatter_plot :
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
show_scatter_plot1 = st.checkbox('Show scatterplot of prices against year of vehicles')
if show_scatter_plot1 :
    st.plotly_chart(fig_1)

st.write("""
## Block with Filtered Data - Filter on the left side on the screen works only with following two charts
""")

rest_type = df['type'].unique()
make_choice = st.sidebar.selectbox('Select type of vehicle:', rest_type)
filtered_type = df[df.type==make_choice]

st.write("""
### Scatterplot with filtered data
""")

fig_2 = px.scatter(filtered_type, x='model_year', y='price', color='type',
                  labels={
                     'model_year' : 'Model',
                     'price' : 'Price',
                     'type' : 'Type'
                 })
show_scatter_plot2 = st.checkbox('Show scatterplot of prices against year of vehicles filtered by type of vehicle')
if show_scatter_plot2:
    st.plotly_chart(fig_2)

st.write("""
### Histogram with filtered data
""")
hist_filt = px.bar(filtered_type, x=filtered_type.model, y=filtered_type.cylinders, color= 'condition').update_xaxes(categoryorder = 'total descending')
show_histogram = st.checkbox('Show histogram of different models of vehicles based on the amount of cylinders, differentiated by vehicle condition')
if show_histogram:
    st.plotly_chart(hist_filt)
