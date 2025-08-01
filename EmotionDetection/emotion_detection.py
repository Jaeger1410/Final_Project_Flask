import requests
import json

def emotion_detector(text_to_analyze):
    # Request response from API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    # Format response into json
    formatted_response = json.loads(response.text) 
    # Create empty list to store emotion scores
    emotions_score = []
    # If response is OK
    if response.status_code == 200:
        # Extract emotions and emotions scores
        for emotion in formatted_response['emotionPredictions'][0]['emotion']:
            emotions_score.append(formatted_response['emotionPredictions'][0]['emotion'][emotion])
        # Emotions scores
        anger_score = emotions_score[0]
        disgust_score = emotions_score[1]
        fear_score = emotions_score[2]
        joy_score = emotions_score[3]
        sadness_score = emotions_score[4]
        # Find dominant emotion
        dominant_emotion = ''
        dominant_emotion_score = max(emotions_score)
        for emotion in formatted_response['emotionPredictions'][0]['emotion']:
            if dominant_emotion_score == formatted_response['emotionPredictions'][0]['emotion'][emotion]:
                dominant_emotion = emotion
    # If response outputs an error, make result dictionary None
    elif response.status_code == 400:
        for i in range(0,5):
            emotions_score.append(None)
        anger_score = emotions_score[0]
        disgust_score = emotions_score[1]
        fear_score = emotions_score[2]
        joy_score = emotions_score[3]
        sadness_score = emotions_score[4]
        dominant_emotion = None
    # Save result as dictionary
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return result
