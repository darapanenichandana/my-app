from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

# Updated HTML Template with Bootstrap
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sentiment Analysis Tool</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        .container { max-width: 600px; margin: auto; }
        .result-positive { background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; }
        .result-negative { background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; }
        .result-neutral { background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>

    <div class="container">
        <h1 class="mb-4">Sentiment Analysis Tool</h1>
        <form method="POST">
            <textarea name="text" rows="4" class="form-control mb-3" placeholder="Enter your text here..."></textarea>
            <button type="submit" class="btn btn-primary">Analyze Sentiment</button>
        </form>

        {% if sentiment %}
            <div class="mt-4">
                <h4>Analyzed Text:</h4>
                <p><em>{{ text }}</em></p>
                
                <div class="{% if polarity > 0 %} result-positive {% elif polarity < 0 %} result-negative {% else %} result-neutral {% endif %}">
                    <h3>Sentiment: {{ sentiment }}</h3>
                    <p><strong>Polarity:</strong> {{ polarity }}</p>
                    <p><strong>Subjectivity:</strong> {{ subjectivity }}</p>
                </div>
            </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = polarity = subjectivity = text = None
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

    return render_template_string(html, sentiment=sentiment, polarity=polarity, subjectivity=subjectivity, text=text)

if __name__ == '__main__':
    app.run(debug=True)
