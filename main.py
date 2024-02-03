import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from Utils import misc
from streamlit_player import st_player 

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
    st.title('MoodUp - Emotional Text Classifier and Suggestions')

    user_input = st.text_input('Enter your text here:')
    if user_input:
        emotion = classify_emotion(user_input)

        st.write(f'Emotional Classification: {emotion}')

        st.subheader('Suggestions:')
        if emotion == 'Positive':

            st.write("Which of the following describes you the best right now ? ")
            st.button("Happy! :smile:", key="happy", on_click=happy_suggestions)

        elif emotion == 'Negative':
            st.write("Which of the following describes you the best right now ? ")
            st.button("Sad! :sweat:", key="sad", on_click=sad_suggestions)
            st.button("Angry! :angry:", key="angry", on_click=angry_suggestions)
            st.button("Anxiety! :grimacing:", key="anxiety", on_click=anxiety_suggestions)
            st.button("Sad! :persevere:", key="stress", on_click=stress_suggestions)
            st.write('- Take a deep breath and try to relax.')
            st.write('- Journal about your feelings to process them.')
            st.write('- Consider reaching out to a mental health professional.')
        else:
            neutral_suggestions()
            st.write('- Take a moment to reflect and find your inner peace.')
            st.write('- Practice mindfulness and meditation.')
            st.write('- Spend time in nature to recharge.')


def happy_suggestions():
    st.title("Here is things to elevate you mood even more : ")
    st_player("http://www.youtube.com/watch?v=I35paFqFOPk")
    st_player("http://www.youtube.com/watch?v=jfs1Y4b-hO0")
    
    st.write("Want Funny videos? , here are some !")
    st_player("http://www.youtube.com/watch?v=268scEdtxYw")
    st_player("http://www.youtube.com/watch?v=tCz8VoCF0uE")
    #st.write('- Think positive thoughts!')
    #st.write('- Reach out to friends and loved ones.')
    #st.write('- Engage in activities that bring you joy.')



if __name__ == '__main__':
    misc.initiate_senti_analyzer()
    main()
