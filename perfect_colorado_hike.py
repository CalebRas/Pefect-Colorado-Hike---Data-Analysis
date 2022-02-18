# Author:
#   Caleb Rasmussen
# File:
#   perfect_colorado_hike.py
# Contains:
#   import_csv()
#   add_info()
#   find_perfect_mountain()
#   display_image()
#   display_mountain()
#   main()
# Description:
#   This program anaylizes data from a Colorado mountain dataset to
#   find the perfect hiking mountain.


# Data Anyalsis
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Images
import urllib.request
from PIL import Image


# Import data from a csv file into a dataframe
def import_csv(file_name):

    # Read csv file into data frame
    dataframe = pd.read_csv(file_name, encoding= 'unicode_escape')

    # Check for missing values 
    if dataframe.isnull().values.any():
        print("Error: missing data")
    else:
        return dataframe


# Adds columns and populates them with info 
def add_info(dataframe):

    # Rename columns to be arround same length
    dataframe.rename(columns={"ID": "Column ID", "Lat": "Latitude", "Long": "Longitude", "Elevation Gain_ft": "Elev Gain_ft"}, 
                                inplace=True)

    # Averarage Traffic: replace low and high traffic columns with an average
    traffic_average = dataframe[['Traffic Low', 'Traffic High']].mean(axis=1)     # averages low and high traffic columns
    dataframe.insert(13, 'Traffic Avg', traffic_average)                          # add column to data frame
    dataframe = dataframe.astype({"Traffic Avg": int})                            # convert column type to int

    dataframe = dataframe.drop(['Traffic Low', 'Traffic High'], axis=1)           # drop low and high

    # Meters: convert feet in meters
    dataframe.insert(4, 'Elevation_m', dataframe['Elevation_ft'])
    dataframe['Elevation_m'] = dataframe['Elevation_m'].apply(lambda x: int(x/3.281))

    # Elevation Gain per mile
    dataframe.insert(13, 'Elev per mi_ft', (dataframe["Elev Gain_ft"] / dataframe["Distance_mi"]))
    dataframe = dataframe.astype({"Elev per mi_ft": int})  

    return dataframe


# Finds the perfect mountain though anaylizing the data
def find_perfect_mountain(df_orginal):

    # Fourteener Data
    figure, graph = plt.subplots(figsize=(5, 5))
    graph.set_title('Does the Mountain follow \nthe Prominence Rule?', fontsize=18)

    pie_labels = ["Yes", "No"]
    pie_colors = ['green', 'gray']

    fourteener_count = df_orginal['fourteener'].value_counts(dropna=True)
    fourteener_values = lambda x: '{}'.format(int(x * fourteener_count.sum() / 100))        # computes mountain values

    # Pie chart
    graph.pie(fourteener_count, labels=pie_labels,  
        autopct= fourteener_values, textprops={'size': 'x-large'},       # mountain values
        explode=(0, 0.1), colors = pie_colors)
    plt.tight_layout()

    # Remove none fourteeners
    df_new = df_orginal.loc[df_orginal["fourteener"] != "N"]  
    df_new = df_new.drop('fourteener', axis=1)              # drop fourteener column


    # Elevation and Traffic Data 
    figure, graph = plt.subplots(nrows=1,ncols=2, figsize=(12, 4))
    graph[0].plot(df_new['Elevation_ft'])
    graph[0].set_title('Elevation', fontsize=18)

    elevation_mean = int(df_new['Elevation_ft'].mean())
    graph[0].set_xlabel(f'Average Height: {elevation_mean} ft')
 

    # Elvation vs Traffic regression graph
    graph[1].set_title('Elevation vs Traffic', fontsize=18)
    graph[1].set_xlabel('Elevation m')
    graph[1].set_ylabel('Estimated Visits (2017)')

    x = df_new['Elevation_m'].values
    y = df_new['Traffic Avg'].values
    
    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)

    regr = LinearRegression()
    regr.fit(x, y)
    regr_pred = regr.predict(x)

    # Regression scatter plot
    graph[1].scatter(x, y)                          # data plots
    graph[1].plot(x, regr_pred, color='red')        # regression line
    plt.tight_layout()


    # Difficulty Data
    df_new.rename({'Difficulty': 'Difficulty Cls'}, axis=1, inplace=True)     # rename Difficulty column

    # Change Difficult values to ints based on the Yosemite Decimal System
    df_new['Difficulty Cls'].replace(['Class 1', 'Class 2', 'Hard Class 2', 'Easy Class 3', 'Class 3', 'Hard Class 3', 'Class 4'], 
                                [1, 2, 2, 3, 3, 3, 4], inplace=True)

    # Difficulty classes graph
    figure, graph = plt.subplots(figsize=(5, 5))
    graph.set_title('Difficulty Classes', fontsize=18)

    pie_labels = ["Class 1", "Class 2", "Class 3", "Class 4"]
    pie_colors = ['forestgreen', 'steelblue', 'darkorange', 'firebrick']

    difficulty_count = df_new['Difficulty Cls'].value_counts().sort_index()
    difficulty_values = lambda x: '{}'.format(int(x * difficulty_count.sum() / 100))        # computes mountain values

    #Pie chart
    graph.pie(difficulty_count, labels=pie_labels,  
        autopct= difficulty_values, textprops={'size': 'x-large'}, 
        colors = pie_colors, startangle=45, explode=(0, 0, 0, 0.1))
    plt.tight_layout()


    # Hardest hikes with low traffic
    df_class_4 = df_new.loc[df_new['Difficulty Cls'] == 4] 

    min_traffic = df_class_4['Traffic Avg'].min()
    df_low_traffic = df_class_4.loc[df_new['Traffic Avg'] <=  min_traffic] 

    perfect_mountain = df_low_traffic.sort_values('Isolation_mi', ascending = False).head(1)

    plt.show()      # Displays graphs
    return perfect_mountain


# Displays a mountain formated on the screen
def display_image(url):
    urllib.request.urlretrieve(url, "mountain.png")
  
    img = Image.open("mountain.png")
    img.show()


# Displays a mountain formated on the screen
def display_mountain(mountain):

    print("Perfect Mountain:")

    # Displays column with data
    i = 0
    for column in mountain:
        print(f"\t{column}:\t{mountain.iat[0, i]}")
        i += 1

    # Display image
    image_url = mountain.iat[0, 15]
    display_image(image_url)


# Runs the program 
def main():
    file_name = "14er.csv"
    df_orginal = import_csv(file_name) 

    print(pd.__version__)
    print(df_orginal.info())


    df_mountains = add_info(df_orginal)
    perfect_mountain = find_perfect_mountain(df_mountains)

    display_mountain(perfect_mountain)

 
# Starts program
main()     
