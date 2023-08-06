## Data pipelines project-Earthquake scraper

The Earthquake scraper is a web scraper built in Python. Its purpose is to collect data on earthquakes registered by the United States Geological Survey. The data collected follow the format:
  * Magnitude
  * Place
  * Datetime
  * Depth

The purpose of this dataset is its possible use in an ML algorithm in order to predict features of earthquakes.

## Necessary libraries and packages

In order to make use of this scrapers, the following libraries are required:
  * selenium
  * os
  * time
  * pandas

In order to connect to an Amazon S3 bucket, boto3 is also needed. For Selenium, chromedriver or geckodriver are also needed depending on the browser you are using (Google Chrome and Firefox Mozilla accordingly).

## Repository content

In this repo you can find the code for the earthquake scraper in a python file (Earthquake scraper.py). In this intuitive python script you can see the process from beginning to end: from visiting the main page all the way to the saving and export of the dataset. You can also find a block of code which is used to upload the collected data to an Amazon S3 bucket (link to the AWS S3 bucket: https://earthquakescraper.s3.amazonaws.com/df.csv) . There will also be a .csv file with the initial collection of data. 


## Step-by-step data collection using the Earthquake scraper

Visit the webpage:

![Καταγραφή](https://user-images.githubusercontent.com/83223559/127509970-b84ee137-f88d-4797-ac5b-5e5bbc97d588.PNG)

Set the desired start date and time (YYYY-MM-DD HH:MM:SS):

![asas](https://user-images.githubusercontent.com/83223559/127510690-425dd38c-0d0d-46dc-91e3-8cb429b85146.PNG)

Get and save the results:

![Καταγραφfffή](https://user-images.githubusercontent.com/83223559/127511023-18b225a2-8d39-47b5-b5f9-c80833caa7f8.PNG)
