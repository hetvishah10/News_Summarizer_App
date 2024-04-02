#!/usr/bin/env python
# coding: utf-8

# #### Name: Hetvi Shah
# #### Student ID: 041137738

# ## Project: Milestone - 2
# ## Title: "News Article Summarization App" 
# ## Aim: To create an app that summerizes text related to news using Text Summarization which falls under NLP i.e. Natural Language Processing 

# ## In this project I have tried to summarize a news article published by Wtop News 
# ### url: "https://wtop.com/sports/2024/03/robots-replicate-reality-high-tech-pitching-machine-mimics-every-pitcher/"

# ### Installing necessary libraries for summerization 
# 
# #### I have used 2 methods for summerizing news articles 
# 1. Sumy 
# 2. Summa
# 
# #### Used streamlit to deploy my model

# In[1]:


#!pip install streamlit
#!pip install sumy
#!pip install summa


# ### Importing necessary libraries

# In[2]:


import streamlit as st
import time
import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from summa.summarizer import summarize as summa_summarize


# ### Creating function to scrape text from a URL

# In[3]:


def scrape_text(url):
    req = requests.get(url)
    soup_library = BeautifulSoup(req.content, 'html.parser')
    paragraphs = soup_library.find_all('p')
    text = ' '.join([p.text for p in paragraphs])
    return text


# ### Creating function to summarize text using Sumy

# In[4]:


def summarize_text_sumy(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    start_time = time.time()
    summary = summarizer(parser.document, sentences_count)
    end_time = time.time()
    summarized_text = ' '.join(str(sentence) for sentence in summary)
    return summarized_text, end_time - start_time


# ### Creating function to summarize text using Summa

# In[5]:


def summarize_text_summa(text, ratio=0.2):
    start_time = time.time()
    summarized_text = summa_summarize(text, ratio=ratio)
    end_time = time.time()
    return summarized_text, end_time - start_time


# ### Creating main function to print summarized output for both Sumy and Summa libraries

# In[6]:


def print_summarized_output(url):
    text = scrape_text(url)
    
    # Summarizing text using Sumy
    print("Summarized Text (Sumy):")
    summary_sumy, time_sumy = summarize_text_sumy(text)
    print(summary_sumy)
    print(f"Time taken (Sumy): {time_sumy} seconds\n")
    
    # Summarizing text using Summa
    print("Summarized Text (Summa):")
    summary_summa, time_summa = summarize_text_summa(text)
    print(summary_summa)
    print(f"Time taken (Summa): {time_summa} seconds\n")


# ### Adding URL for testing

# In[7]:


url = "https://wtop.com/sports/2024/03/robots-replicate-reality-high-tech-pitching-machine-mimics-every-pitcher/"


# ### Printing Summarized output for both Sumy and Summa libraries

# In[8]:


print_summarized_output(url)


# ###  Creating main function for Streamlit app

# #### Following are the steps which I have performed to create Main function for streamlit app
#     1. Setting title for the app
#     2. Adding field to enter URL
#     3. Scrape text from the provided URL
#     4. Summarizing text using Sumy
#     5. Summarizing text using Summa

# In[9]:


def main():
    
    #Setting title for the app
    st.title("News Article Summarization App")
    
    #Adding field to enter URL
    get_url = st.text_input("Enter the URL of the news article:")
    
    if get_url:
        text = scrape_text(get_url)

        # Summarizing text using Sumy
        st.subheader("Summarized Text (Sumy):")
        summary_sumy, time_sumy = summarize_text_sumy(text)
        st.write(summary_sumy)
        st.write(f"Time taken: {time_sumy} seconds")

        # Summarizing text using Summa
        st.subheader("Summarized Text (Summa):")
        summary_summa, time_summa = summarize_text_summa(text)
        st.write(summary_summa)
        st.write(f"Time taken: {time_summa} seconds")


# ### Running the main function

# In[10]:


if __name__ == "__main__":
    main()


# In[ ]:




