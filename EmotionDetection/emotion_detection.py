import requests
import json



def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    JSON={ "raw_document": { "text": text_to_analyze }}
    response = requests.post(url=URL,headers=HEADERS,json=JSON)
    if response.status_code == 400:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None}


    req_dict = json.loads(response.text)
    final_dict = req_dict["emotionPredictions"][0]["emotion"]


    #lis to be created
    anger_score = final_dict['anger']
    disgust_score = final_dict['disgust']
    fear_score = final_dict['fear']
    joy_score = final_dict['joy']
    sadness_score = final_dict['sadness']

   # getting the max value
    dominant_emotion = max(final_dict, key=final_dict.get)


    # returning
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

