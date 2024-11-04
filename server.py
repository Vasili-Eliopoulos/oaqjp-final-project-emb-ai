"""
Emotion Detection App using Flask.

This APP accepts a text input and returns the detected emotions.
"""

from flask import Flask, request, render_template, send_from_directory
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    """
    Serve static files.

    Args:
        path (str): Path to the static file.

    Returns:
        send_from_directory: The static file.
    """
    return send_from_directory('static', path)

@app.route('/', methods=['GET'])
def home():
    """
    Render the home page.

    Returns:
        render_template: The rendered home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    """
    Detect emotions from the given text.

    Returns:
        str: The detected emotions.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    if not text_to_analyse:
        return 'Invalid text! Please try again!'

    emotions = emotion_detector(text_to_analyse)
    if emotions['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    response_string = '''
    For the given statement, the system response is:
    'anger': {anger},
    'disgust': {disgust},
    'fear': {fear},
    'joy': {joy} and
    'sadness': {sadness}.
    The dominant emotion is {dominant_emotion}.
    '''
    response = response_string.format(
        anger=emotions['anger'],
        disgust=emotions['disgust'],
        fear=emotions['fear'],
        joy=emotions['joy'],
        sadness=emotions['sadness'],
        dominant_emotion=emotions['dominant_emotion']
    )
    return response

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
