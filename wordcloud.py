#!/usr/bin/env python
# coding: utf-8

# Word Cloud

# This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like, save this as a .txt file somewhere on your computer.

# Upload your input file here so that your script will be able to process it.  To do the upload, you will need an uploader widget.  Run the following cell to perform all the installs and imports for your word cloud script and uploader widget.  It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest.

# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# To upload your text file, run the following code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# The uploader widget saved the contents of your uploaded file into a string object named *file_contents* that your word cloud script can process. 

# Function that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word. Then use it in the `generate_from_frequencies` function to generate your very own word cloud!

# Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

def calculate_frequencies(file_contents):
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    format_list = []
    new_list = []
    frequencies = {}
    file_contents = file_contents.split()

    for word in file_contents:
        if word not in punctuations and word.isalpha() :
            format_list.append(word.lower())
    
    
    for palabra in format_list:
        if palabra not in uninteresting_words:
            new_list.append(palabra)
       
    
    for x in new_list:
        if x not in frequencies:
            frequencies[x] = 1
        else:
            frequencies[x] += 1        
            
    
        #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# If you have done everything correctly, your word cloud image should appear after running the code below.

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

# If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequency count dictionary into the `generate_from_frequencies` function of `wordcloud`. 