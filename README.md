# ArtiCast

Articast is a similarity-based podcast recommendation system based on the contents of articles using natural-language processing. Specifically, articles and podcast episode descriptions (and titles) are transformed using GloVe, and for each article, the most similar podcast episodes are found by comparing the cosine simi

The code in this repository falls into three categories: scraping  and semantic embedding tools to build the podcast database, Google Chrome Extension codes, and analytical tools to validate the approach used to recommend podcasts.

====================SCRAPING and SEMANTIC EMBEDDING

All scraping tools in this repository are Jupyter notebooks. The scrape starts with combing iTunes website for the titles and RSS feed URLs of every popular podcast in their library. Then, the RSS feeds of each podcast are scraped to obtain episode descriptions and titles.  Then, text documents are cleaned and preprocessed. The scraping/cleaning codes are in Data_preparation.ipynb. Finally, the code for obtaining representation of the podcast episodes can be found in Validation_Similariteies.ipynb.

====================CHROME EXTENSION TOOLS

The overall format of this chrome extension is based on [this repository](https://github.com/jiananarthurli/insight_chrome_extension). 

 INSTALLATION:
* Download or clone this repo to your personal machine
* Install and launch Google Chrome
* Click the the three vertical dots in the top right of Chrome, then click More tools, then click Extensions (see Extension support for more info)
* Click the Load unpacked button in the upper left corner, navigate to wherever you downloaded this repo (most likely Downloads) and and select the chrome__ext folder located inside the foodTalk directory If the installation was successful you will see this logo grayLogo to the right of search bar. Navigate to a recipe you want to try for example, and click on the icon to begin!

====================ANALYTICAL TOOLS

The  file for analytics is Validation_Similariteies.ipynb. This file contains a number of analyses aimed at demonstrating that the GloVe representations of podcasts are a valid way of representing what a podcast is about, and that the system makes sensible recommendations.
