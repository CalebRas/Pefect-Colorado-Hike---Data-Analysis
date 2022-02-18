# Overview

The Perfect Colorado Hike program analyzes and performs various actions on a dataset containing information on mountains in Colorado over fourteen thousand feet. The object of the program is to add to and sort the data to determine what, in my opinion, would be the perfect fourteener in Colorado to hike. The program displays and filters through the dataset until only one mountain is left, which is then displayed. The dataset used can be found on Kaggle at: 

[Colorado Fourteeners Dataset](https://www.kaggle.com/mikeshout/14erpeaks)

This program was created to broaden my software engineering skillset to include data science. In an effort to learn more on the subject, I analyzed a dataset using Pandas and Matplotlib. Having never used either library before, this project taught me how to filter, sort, aggregate, and convert data to answer my questions about Colorado mountaineering. I also learned data visualization equines through the use of graphs, linear regression, and HTTP requests. Please click on the video below to see a demonstration of the code and project. 

[Perfect Colorado Hike - Data Analysis Demonstration](https://youtu.be/LjnfUrLOlDU)

# Data Analysis Results

As a My perfect mountain is determined by answering the following questions: 
1. Does the mountain follow the prominence rule?
* Out of the 57 mountains in the dataset five do not, which are filtered out of the dataset. 

2. Is the mountain challenging to climb? 
*  The remaining 52 mountains each have 1 of 4 different difficulty classes. In the most technical class, "Class 4", there are five mountains. 

3. Which mountain, on average, is the least visited?
* Of the five "Class 4" mountains, 4 have similar traffic averages, so only one mountain is eliminated. 

4. Which mountain offers the best view?
* The last four mountains are sorted based on how far away they are from other peaks. The furthest is the perfect mountain, Mountain Wilson.

# Development Environment

* Visual Stuido Code 
* Python 3.9.7 64-bit
* Pandas 1.4.0
* MatPlotLib

# Useful Websites

* [Pandas Tutorial Geeks for Geeks](https://www.geeksforgeeks.org/pandas-tutorial/)
* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Data Analysis with Python and pandas using Jupyter Notebook](https://dev.socrata.com/blog/2016/02/01/pandas-and-jupyter-notebook.html)

# Future Work

* Add functionality to work with other mountain datasets
* Optimize code for performance 
* Display dataset while analyzing with Markdown 