import nltk 

def initiate_senti_analyzer():
    nltk.download('vader_lexicon')
    nltk.download("stopwords")


def map_new_emotion(row):
    emotion = row['Emotion']
    analyzer_output = row['Analyzer_Output']

    if emotion == 'neutral':
        if analyzer_output == 'Positive':
            return 'Contentment'
        elif analyzer_output == 'Negative':
            return 'Disappointment'
        else:
            return 'Calm'
    elif emotion == 'joy':
        if analyzer_output == 'Positive':
            return 'Elation'
        elif analyzer_output == 'Negative':
            return 'Discontentment'
        else:
            return 'Happiness'
    elif emotion == 'sadness':
        if analyzer_output == 'Positive':
            return 'Hopefulness'
        elif analyzer_output == 'Negative':
            return 'Despair'
        else:
            return 'Sadness'
    elif emotion == 'anger':
        if analyzer_output == 'Positive':
            return 'Determination'
        elif analyzer_output == 'Negative':
            return 'Resentment'
        else:
            return 'Anger'
    elif emotion == 'fear':
        if analyzer_output == 'Positive':
            return 'Courage'
        elif analyzer_output == 'Negative':
            return 'Anxiety'
        else:
            return 'Fear'
    elif emotion == 'love':
        if analyzer_output == 'Positive':
            return 'Passion'
        elif analyzer_output == 'Negative':
            return 'Heartbreak'
        else:
            return 'Love'
    elif emotion == 'surprise':
        if analyzer_output == 'Positive':
            return 'Excitement'
        elif analyzer_output == 'Negative':
            return 'Dismay'
        else:
            return 'Surprise'
    else:
        return 'Neutral'
