# Building a Sentiment Analysis Web App
# What is Sentiment Analysis? >>> the process of computationally idnetifying and categorizing opinions expressed in a piece of text
# in short, sentiment analysis determines whether the writer's attitude is positive/negative/neutral

from flask import Flask, render_template, request, url_for
from textblob import TextBlob

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] #needed to establish connection w database
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #disables SQLALCHEMY tracking feature to minimize performance impacts (so it does not emit signals for various events)

@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    #Retrieve text input from user
    text = request.form['text']

    #Perform the sentiment analysis w/Textblob()
    sentiment_analysis = TextBlob(text)

    #Get the polarity score to determine if it's positive/negative/neutral (1, 0, -1)
    # subjectivity_score = sentiment_analysis.sentiment.subjectivity # this determines if it is an opionion
    polarity_score = sentiment_analysis.sentiment.polarity

    if polarity_score > 0:
        sentiment_result = "Positive 😀"
    elif polarity_score < 0:
        sentiment_result = "Negative 😞"
    else:
        sentiment_result = "Neutral 😐"

    return render_template(template_name_or_list="results.html", text=text, sentiment=sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)
