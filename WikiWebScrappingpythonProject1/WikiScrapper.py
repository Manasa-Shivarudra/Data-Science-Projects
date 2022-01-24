import pywhatkit as kt
import requests
import validators
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import re
import nltk
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import db
from db import client, user_collection, db
from flask import Flask, render_template, request
import base64

nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)
@app.route('/')
def flask_mongodb_atlas():
    return render_template("Index.html")#return "flask mongodb atlas!"

@app.route('/summary', methods=['GET', 'POST'])
def summary():
    search = request.form["search"]
    URL = "https://en.wikipedia.org/w/index.php?search=" + search

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find all the text in the paragraph tag
    paras = soup.find_all('p')

    # Create a string which will hold the formatted text from the wikipedia page
    article_text = ""

    # Iterate the paragraph tag and add the data to the new string article_text
    for p in paras:
        article_text += p.text

    # Format the string using regular expression by removing the occurrance of numbers within [] and white spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    sentence_list = nltk.sent_tokenize(article_text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    # Extract all the reference links from the wiki page
    references = soup.find(id="bodyContent")
    #ref_list = references.find_all("div", class_="reflist")
    findreferences = references.find_all('ol')
    href = BeautifulSoup(str(findreferences), "html.parser")
    links = [a["href"] for a in href.find_all("a", href=True)]

    result_links = []

    for link in links:
        if link.startswith('http'):
            result_links.append(link)
        else:
            pass

    result_links

    # Extract all the images from wikipage and store them as base64 string in the db
    modified_link = []

    # Extract all the images and store it in the list
    for a in soup.findAll('img'):
        if 'src' in a.attrs:
            url = "https:" + a.get('src')
            modified_link.append(url)
        else:
            pass
        modified_link

    # Converting all the image URL to base64 strings
    base64ImageList = []
    for link in modified_link:
        validate = validators.url(link)
        if validate:
            str_base64 = base64.b64encode(requests.get(link).content)
            base64ImageList.append(str_base64)
        else:
            pass
        base64ImageList

    my_dict = {"Topic": search, "Summary": summary, "References": result_links, "Base64_Image_String": base64ImageList}
    db['Wiki_Scrapper'].insert_one(my_dict)

    rows = user_collection.find()
    reviews = [i for i in rows]
    #return "Connected to the data base!"
    return render_template('results.html', rows=reviews)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
