# Moonbucks

## Introduction

Moonbucks is a coffee chain that has stores located all over the world. The company is constantly looking at running better logistics as well as expansion to open more stores at strategic locations. You and your team have been hired to do analysis and provide insights to the management for making business decisions.
<br/><br/>
You have been given a sample dataset that contains the location of Moonbucks stores all over the world. Please use this list to determine the country in Problem 1 and location of store in Problem 2.

## Setup

Setting up the local virtual environment:

1. Create virtual environment.  
`python -m venv venv`

2. Activate the venv.
`Set-ExecutionPolicy Unrestricted -Scope Process`
`venv/Scripts/activate`

3. Installed required dependencies.
`pip install -r requirements.txt`

4. Install other dependencies. (same as using `pip`)
`pip install <package>`

5. Update the dependencies list.
`pip freeze > requirements.txt`

Install the following packages:

1. Install nltk
   1. (Windows) using pip:
      > $ pip install nltk

   2. Mac Os/LINX Installation
      > $ sudo pip install -U nltk

   3. See more: [https://www.nltk.org/install.html](https://www.nltk.org/install.html)

2. Install Plotly
   1. using pip:
      > $ pip install plotly==5.7.0

   2. or conda:
      > $ conda install -c plotly plotly=5.7.0

   3. See more: [https://plotly.com/python/getting-started/](https://plotly.com/python/getting-started/)

3. Install Beautifulsoup
   1. using pip: 
      > pip install beautifulsoup4

4. Install extra nltk modules through Python console
   > import nltk
   > nltk.download('wordnet')
   > nltk.download('punkt')
   > nltk.download('omw-1.4')
   > nltk.download('averaged_perceptron_tagger')

## Some Useful Links

   1. [NLTK](https://www.nltk.org/)
   2. [Plotly](https://plotly.com/)
   3. [Google Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/intro)
   4. [Python Web Scraping Practical Introduction](https://realpython.com/python-web-scraping-practical-introduction/)
   5. [Beautifulsoup](https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm)
   6. [Matching Country Information in Python](https://towardsdatascience.com/matching-country-information-in-python-7e1928583644)
