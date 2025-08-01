''' This module runs the server using Flask,
    with error handling for blank inputs.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def em_detector():
    ''' This method handles the emotion_detector function.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    emotions = list(response.keys())
    values = list(response.values())
    # If dominant emotion is None, return error message
    if values[-1] is None:
        return "Invalid text! Please try again!"
    # If response is OK, return formatted response
    return f"For the given statement, the system response is \
            '{emotions[0]}': {response['anger']}, '{emotions[1]}': {response['disgust']}, \
            '{emotions[2]}': {response['fear']}, '{emotions[3]}': {response['joy']} \
            and '{emotions[4]}': {response['sadness']}. \
            The dominant emotions is {str(response['dominant_emotion'])}."

@app.route('/')
def render_index_page():
    ''' This function renders the index page where the user interacts with the app.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
