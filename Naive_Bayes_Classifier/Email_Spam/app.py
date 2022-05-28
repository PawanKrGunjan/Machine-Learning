import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from flask import Flask, render_template, request
app = Flask(__name__,
            template_folder=r"E:\Machine-Learning-Projects\Naive_Bayes_Classifier\Email_Spam")
model = joblib.load(open('spam_mail.pkl', "rb"))


@app.route('/')
def Model():
    return render_template('Model.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    '''
    For rendering results on HTML GUI
    '''
    prediction = model.predict(Massage)
    return render_template("Label.html", result=result)


if __name__ == '__main__':
    app.run()
