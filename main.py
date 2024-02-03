import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from Utils import misc

sid = SentimentIntensityAnalyzer()



def classify_emotion(text):
    score = sid.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'



def main():
    st.title('Emotional Text Classifier and Suggestions')

    user_input = st.text_input('Enter your text here:')
    if user_input:
        emotion = classify_emotion(user_input)

        st.write(f'Emotional Classification: {emotion}')

        st.subheader('Suggestions:')
        if emotion == 'Positive':
            st.write('- Think positive thoughts!')
            st.write('- Reach out to friends and loved ones.')
            st.write('- Engage in activities that bring you joy.')
        elif emotion == 'Negative':
            st.write('- Take a deep breath and try to relax.')
            st.write('- Journal about your feelings to process them.')
            st.write('- Consider reaching out to a mental health professional.')
        else:
            st.write('- Take a moment to reflect and find your inner peace.')
            st.write('- Practice mindfulness and meditation.')
            st.write('- Spend time in nature to recharge.')


if __name__ == '__main__':
    misc.initiate_senti_analyzer()
    main()
