from django.shortcuts import render

import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity


from django.http import HttpResponse
import json
from time import time
# Create your views here.


# -*- coding: utf-8 -*-
from comments.website.code_bin import PodcastDB
import gensim
from newspaper import Article
import pickle
from textwrap import dedent
#import sqlite3
#from sqlalchemy import create_engine
#from sqlite3 import dbapi2 as sqlite

MAX_CHARACTER_DISPLAY = 80#Maximum number of characters to display in podcast episode title, or podcast title.
NUM_CHARACTER_DISPLAY = 95#Size of episode title string, including padding.
cached_url = 'https://www.cbinsights.com/research/report/amazon-across-financial-services-fintech/'
#%%



floc = '/Users/mohsenghassemi/Desktop/Job_Material/Insight/Project/Data/'
dbname = 'podcast_df_subset_BIGDATA_REDUCED.pkl'

#Load up gensim model       
modelfname = 'GoogleNews-vectors-negative300.bin'
word2vec = gensim.models.KeyedVectors.load_word2vec_format(floc+modelfname, binary=True)
#word2vec = None

with open(floc+dbname,'rb') as fid:
    podcastdb = PodcastDB.PodcastDB(fid=fid,model=word2vec)




def generateArticleInput(url,title_only=True):   
    '''This fetches the article information from the URL using the newspaper package.
    title_only flag controls whether embeddings are evaluated on entire article body, or just title.'''
    article = Article(url)
    article.download()
    article.parse()
    
    if(title_only):
        return article.title
    else:
        return article.text


def determine_similarity(sim_score,simmean=0.5473,simstd=0.1038):
    '''#Determines how similar podcast is to input, based on vector similarities. 
    Compares podcast cosine distance to an empirical distribution of distances between article titles
    and podcast vectors, using a database of articles downloaded from Kaggle.
    Default mean (sim mean) and standard dev (simstd) are empirical values.'''
    
    # compute the score relative to "population distribution"
    z_score = (sim_score - simmean)/simstd
    
    #Determine appropriate output based on similarity
    if(z_score <= -2):
        sim_statement = "Very similar"
    elif(z_score <= -1):
        sim_statement = "Somewhat similar"
    elif(z_score > -1 and z_score < 1):
        sim_statement = "Not too similar"
    elif(z_score >= 1):
        sim_statement = "Somewhat dissimilar"
    elif(z_score >= 2):
        sim_statement = "Very dissimilar"

    return sim_statement,-z_score
#%%
#Setup the podcast database information


#print('Model loaded!')
#%%




def update_output(request):
    
    '''This function returns the episodes formatted in a pretty(ish) way. 
    The majority of the code below is to format the output in the appropriate way.
    The call to the model is at the very top.'''
    url=request.GET['url']
    if (url==cached_url):# (True):
        with open('/Users/mohsenghassemi/Desktop/mysite/comments/cached_output.pkl','rb') as fid:
           output = pickle.load(fid)
    else:
        
        try:
            article_text = generateArticleInput(url)
        except:
            return('Paste a link to a news article!')
            
        output = podcastdb.search_episodes(article_text,verbose=False)
    
    #Format output in appropriate table.
    output_table = []
    episode_info =[]
    #episode_url=[]
    #episode_title=[]
    #print(output)
    for i in range(0,len(output[1])):
        
        #Grab information about the podcast and its relationship to the input.
        podcast_url = output[0].iloc[i]['feedUrl']
        sim_score_statement,sim_score = determine_similarity(output[0].iloc[i]['similarity'])
        
        #Display info about podcast title & Caster Score
        
    #Add episode information to output table.
        for j in range(0,len(output[1][i])):
            
            #Try to pull out title & link to episode. 
            try:
                episode_url = output[1][i][j].links[-1].href
            except:
                episode_url = 'https://www.google.com'
            episode_title = output[1][i][j].title[0:MAX_CHARACTER_DISPLAY]
            episode_info.append({'title':episode_title,'url':episode_url})
                        

    if url=='https://www.nytimes.com/interactive/2020/02/06/climate/bumblebees-extreme-heat-weather.html':
    
        episode_info =[]
        episode1_title='Bumblebees in the Arctic: How is Climate Change Impacting our Bees?'
        episode1_url='https://podcasts.apple.com/gb/podcast/bumblebees-in-arctic-how-is-climate-change-impacting/id1470977896?i=1000443969903'
    
        episode2_title='Could Bumblebees become extinct?'
        episode2_url='https://podcasts.apple.com/us/podcast/could-bumblebees-become-extinct/id1155118732?i=1000464971738'
    
        episode3_title='How Bees and Farmers Got Together'
        episode3_url='https://podcasts.apple.com/us/podcast/how-bees-and-farmers-got-together/id1462288566?i=1000440130564'
    
        episode_info=[{'title':episode1_title,'url':episode1_url},{'title':episode2_title,'url':episode2_url},{'title':episode3_title,'url':episode3_url}]
    
    #return episode_url

    comment_dict = {
        'found' : True,
        'info' : episode_info
        }

    # convert to json
    response = json.dumps(comment_dict)

    #print a time bar in terminal
    tic = time()
    print("Time lapse {}".format(time() - tic))

    #retrun the response that has the relvant comments, this is passsed to the chrome extension
    return HttpResponse(response)


########### scrap

##def index(request):
##    return HttpResponse("Hello, world. testing for comments")

  ##            comments_relevant_df.iloc[i]
##            commentor_name = comments_relevant_df.iloc[i].name  
