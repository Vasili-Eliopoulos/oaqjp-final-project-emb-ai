import requests as rq 

def emotion_detector(text_to_analyse: str) -> str:
    """
    Arguments: text_to_analyse string
    Response: json string containing sentiment analsis predictions for the input string
    """
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = {
        "raw_document": {
            "text": text_to_analyse 
        }
    }
    response = rq.post(url=URL, headers=HEADERS, json=json)
    response_dict = response.json()

    emotion_dict = response_dict['emotionPredictions'][0]['emotion']
    dominant_emotion = sorted(emotion_dict.items(), key=lambda item: item[1], reverse=True)[0][0]
    emotion_dict['domination_emotion'] = dominant_emotion
    
    return emotion_dict
