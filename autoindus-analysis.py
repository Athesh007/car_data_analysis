import matplotlib
import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from matplotlib.pyplot import figure
from streamlit_option_menu import option_menu
import time

#change the webpage to wide screen.
st.set_page_config(layout="wide")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# create progress bar
my_bar = st.progress(0)
# progress bar continues to complete from 0 to 100
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)


#side--navbar
with st.sidebar:
        selected = option_menu(
                menu_title="Main Menu",
                options=["Home","Data Cleaning","Brandwise Data","Car Body Types","Engine Fuels","Displacement and price","3D Graph"],
        )
#csv  data file
df = pd.read_csv("cars_engage_2022.csv")

#selection for table
if selected == "Home":
        st.title('Automotive Industry Data Analysis')
        st.subheader('The below table is represent the csv file details')
        st.write("This table shows report analysis for the given data")
        st.write(df)
        st.image("https://www.mcrsafety.com/~/media/mcrsafety/industry/categories/automotive/automotive_herou.png?h=550&la=en&mw=1900&w=1300&hash=57167CDBCE15375389FF6F18B71F28E2")

#cleaning of data
if selected == "Data Cleaning":
        st.header("It about the mean, median, mode, and much more about the numeric data value of the dataset")
        st.write(df.describe())
        df[df.isnull()].count()
        df[df.duplicated()].count()
        df=df.fillna('')
        df=df.replace(' ','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace(',','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace('Rs.','',regex=False)
        df['Displacement']=df['Displacement'].str.replace('cc','')
        df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']] = df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']].apply(pd.to_numeric)
        f,ax = plt.subplots(figsize=(14,10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", ax=ax)
        st.subheader("""Correlation""")
        st.pyplot(f)
        st.text("""Ex-Showroom price is positively correlated to Displacement.
Ex-Showroom Price is Positively Correlated to the number of Cylinders. 
This means, more the number of cylinders, more the ex-showroom price.
The more the number of cylinders in a car, the more will be its displacement. 
Generally speaking, the higher an engine’s displacement the more power it can create""")

#brandwise data
if selected =="Brandwise Data":
        st.header("Display the all Hyundai model cars")
        st.write(df[df.Make =='Hyundai'])
        fig = plt.figure(figsize = (10,10))
        ax = fig.subplots()
        df.Make.value_counts().plot(ax=ax, kind='pie')
        ax.set_ylabel("")
        ax.set_title("Top Car Making Companies")
        st.header("Companies")
        st.pyplot(fig)
        st.title("Comparison")
        st.text("""Maruti Suzuki has more car variants than any other company.
The Top 5 companies with more than car variants are Maruti Suzuki, Hyundai, Mahindra, Tata, and Toyota.
Sports car variants are very low""")

#Car body types in various companies
if selected =="Car Body Types":
        st.header("Car by car body types")
        plt.figure(figsize=(16,7))
        sns.countplot(data=df, y='Body_Type',alpha=.6,color='blue')
        plt.title('Car / car body type',fontsize=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel('')
        plt.ylabel('')
        st.pyplot(plt)

#Car types in ascending order
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace(',','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace('Rs.','',regex=False)
        df['Displacement']=df['Displacement'].str.replace('cc','')
        df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']] = df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']].apply(pd.to_numeric)
        PriceByType = df.groupby('Body_Type').sum().sort_values('Ex-Showroom_Price', ascending=False)
        PriceByType = PriceByType.reset_index()
        PriceByType=px.bar(x='Body_Type', y ="Ex-Showroom_Price", data_frame=PriceByType)
        st.header("Car prices prediction")
        st.plotly_chart(PriceByType,use_container_width=True,use_container_height=True)
        st.text("""If we some up all the SUVs Ex-Showroom price present in the Dataset then it will be nearly 2B INR
Sports cars a minimal spike in the graph""")

#Car Engine fuels
if selected == "Engine Fuels":
        st.header("Engine Fuel Types")
        fig = plt.figure(figsize = (10,10))
        ax = fig.subplots()
        df.Fuel_Type.value_counts().plot(ax=ax, kind='pie')
        ax.set_ylabel("")
        ax.set_title("Cars Count by Engine Fuel Type")
        st.pyplot(fig)
        st.text("""Almost 90 percent of cars run on Petrol or Diesel.
This data is going to change because electric vehicles have arrived.""")

#displacement and price
if selected == "Displacement and price":
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace(',','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace('Rs.','',regex=False)
        df['Displacement']=df['Displacement'].str.replace('cc','')
        df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']] = df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']].apply(pd.to_numeric)
        PriceByType = df.groupby('Body_Type').sum().sort_values('Ex-Showroom_Price', ascending=False)
        PriceByType = PriceByType.reset_index()
        PriceByType=px.bar(x='Body_Type', y ="Ex-Showroom_Price", data_frame=PriceByType)
        plt.figure(figsize=(10,8))
        st.header("Displacement and Price")
        sns.scatterplot(data=df, x='Displacement', y='Ex-Showroom_Price',hue='Body_Type',palette='viridis',alpha=.89, s=120 );
        plt.xticks(fontsize=13);
        plt.yticks(fontsize=13)
        plt.xlabel('power',fontsize=14)
        plt.ylabel('price',fontsize=14)
        plt.title('Relation between Displacement and price',fontsize=20);
        st.pyplot(plt)

#displacement and price in separate chart
        fig = sns.pairplot(df,vars=[ 'Displacement', 'Ex-Showroom_Price'], hue= 'Fuel_Type', palette=sns.color_palette('magma'),diag_kind='kde',height=2, aspect=1.8);
        st.header("Displacement and Price in seperate graph")
        st.pyplot(fig)
        st.text("This data is self-explanatory. The price and power of the sports car are the highest.")

if selected == "3D Graph":
        
        st.header("3D Graph Representation")
        df=df.fillna('')
        df=df.replace(' ','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace(',','')
        df['Ex-Showroom_Price']=df['Ex-Showroom_Price'].str.replace('Rs.','',regex=False)
        df['Displacement']=df['Displacement'].str.replace('cc','')
        df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']] = df[['Cylinders', 'Valves_Per_Cylinder', 'Doors', 'Seating_Capacity', 'Number_of_Airbags', 'Ex-Showroom_Price', 'Displacement']].apply(pd.to_numeric)
        f,ax = plt.subplots(figsize=(14,10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", ax=ax)
        fig = px.scatter_3d(df, x='Displacement', z='Ex-Showroom_Price', y='Fuel_Type',color='Make')
        fig.update_layout(showlegend=True)
        st.plotly_chart(fig)