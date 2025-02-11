from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

# HTML Template
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis App</title>
</head>
<body style="font-family: Arial; text-align: center; padding: 50px;">
    <h1>Sentiment Analysis Tool</h1>
    <form method="POST">
        <textarea name="text" rows="5" cols="50" placeholder="Enter your text here..."></textarea><br><br>
        <input type="submit" value="Analyze Sentiment">
    </form>
    {% if sentiment %}
        <h2>Sentiment: {{ sentiment }}</h2>
        <p><strong>Polarity:</strong> {{ polarity }}</p>
        <p><strong>Subjectivity:</strong> {{ subjectivity }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = polarity = subjectivity = None
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render_template_string(html, sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True)
