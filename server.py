"""Flask server for the Emotion Detection web application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyse the text received via query parameter and return emotion scores.

    Query Parameters:
        textToAnalyze (str): The text submitted by the user for analysis.

    Returns:
        str: A formatted string with individual emotion scores and the
             dominant emotion, or an error message for blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
