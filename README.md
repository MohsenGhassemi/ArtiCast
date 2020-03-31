# ArtiCast

Articast is a similarity-based podcast recommendation system based on the contents of articles using natural-language processing. Specifically, articles and podcast episode descriptions (and titles) are transformed using GloVe, and for each article, the most similar podcast episodes are found by comparing the cosine simi

The code in this repository falls into three categories: scraping  and semantic embedding tools to build the podcast database, Google Chrome Extension codes, and analytical tools to validate the approach used to recommend podcasts.

## ====================SCRAPING and SEMANTIC EMBEDDING

All scraping tools in this repository are Jupyter notebooks. The scrape starts with combing iTunes website for the titles and RSS feed URLs of every popular podcast in their library. Then, the RSS feeds of each podcast are scraped to obtain episode descriptions and titles.  Then, text documents are cleaned and preprocessed. The scraping/cleaning codes are in Data_preparation.ipynb. Finally, the code for obtaining representation of the podcast episodes can be found in Validation_Similariteies.ipynb.

## ====================CHROME EXTENSION TOOLS

The overall format of this chrome extension is based on [this repository](https://github.com/jiananarthurli/insight_chrome_extension). 

## INSTALLATION:
* Download or clone this repo to your personal machine
* Install and launch Google Chrome
* Click the the three vertical dots in the top right of Chrome, then click More tools, then click Extensions (see Extension support for more info)
* Click the Load unpacked button in the upper left corner, navigate to wherever you downloaded this repo (most likely Downloads) and and select the Chrome_extension folder located inside the ArtiCast directory. If the installation was successful you will see the Articast logo to the right of search bar. Now, you can click on the ArtiCast when you find an interesting article and listen  and find related 

## How it works
The algorithm is implemented as an application on an Amazon EC2 instance using the [Django](https://www.djangoproject.com/start/overview/) webframework.
When the user clicks on the "Find podcast episodes" button on the chrome extension (see [/chrome\_ext/src/browswer\_action.html](https://github.com/alxdroR/foodTalk/blob/master/chrome_ext/src/browser_action/browser_action.html) 
for the html code controlling the display in the Chrome pop-up window display), the javascript function _get\_reviews_ located 
in [/chrome\_ext/src/browser\_action.js](https://github.com/MohsenGhassemi/ArtiCast/blob/master/Chrome_extension/src/browser_action/browser_action.js) sends 
the article url to the Amazon server. Then, the related podcast episodes information (packaged into a JSON file) is sent back to the Chrome extension _get\_podcasts_ function in [/chrome\_ext/src/browswer\_action.js](https://github.com/MohsenGhassemi/ArtiCast/blob/master/Chrome_extension/src/browser_action/browser_action.js), 
unpacked and displayed onto the Chrome pop-up.

## ====================ANALYTICAL TOOLS

The  file for analytics is Validation_Similariteies.ipynb. This file contains a number of analyses aimed at demonstrating that the GloVe representations of podcasts are a valid way of representing what a podcast is about, and that the system makes sensible recommendations.
