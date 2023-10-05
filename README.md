# Project

This is my project for the Sprint 6
The project for this sprint is to make an application, a tool to simulate random events, and the methods and libraries used to implement it.

# URL of my App on Render: 
https://project-hrm2.onrender.com

# Application used:
I was using two application for making the online application - Visual Code in order to create Jupyter Notebook and Spyder through Anaconda Navigator for writing actual code. 

# Librares used: 
Throughout this project, three modules/libraries were used
- pandas
- streamlit
- plotly.express

# Exploratory Data Analysis
The main directory contains a folder called: 'notebooks'. Inside that folder there is a file called 'EDA.ipynb' with exploratory data analysis of a given data:

- Information about dataset
- Checking for empty data
- Fixing empty data
- Checking for duplicates
- Getting an average price for bodytype
- Pie chart 
- Histogram
- 2 scatterplots

# File App.py includes:

- pd.read_csv() - Reads the file
- st.table() - Displays a static table
- st.write() - Displays text
- px.bar(df, x='x', y='y') - Creates a histogram
- st.plotly_chart() - Displays an interactive Plotly chart
- px.scatter(df, x='x', y='y', color='color') - Creates scatter plot
- st.slider() - Allows for choosing a range of values
- st.selectbox - Allows for choosing a specific value 


# Code itself consists of: 

- Importing necessary modules that will be useful in the future
- Several tables
- Histogram
- 2 scatterplots
- 2 filtering options
- Scatterplot that will work with above filters
- Histogram that will work with above filters

# Running a file locally
In order to be able to use it, all you need to do is to run 'app.py' file in any app that can run python code. After that, you will receive the message in the console of that app you chose 'streamlit run /Users/username/Downloads/app.py'
After that, all you need to do is to open the console in your computer, past this code and run it. 
