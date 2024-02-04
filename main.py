import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from Utils import misc
from streamlit_player import st_player 
from streamlit_lottie import st_lottie
import json
import requests
import base64
from PIL import Image

from joblib import load 

model = load("Data/model.pkl")

sid = SentimentIntensityAnalyzer()
st.set_page_config(page_title = "MoodUp" ,page_icon = ":relieved_face:",layout = "wide")
def load_lottiefile(filepath : str):
    with open(filepath,"r") as f:
        return json.load(f)
    
lottie_coding = load_lottiefile("C:/Users/Navneeth/Desktop/Me/Hackathons/HackStreet_2.0/HackStreet2.0/mindful.json")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("C:/Users/Navneeth/Desktop/Me/Hackathons/HackStreet_2.0/HackStreet2.0/background.jpg");
    background-size: cover;

}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar]{}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)


def classify_emotion(text):
    score = sid.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'Positive'
    elif score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
st.title('MoodUp - your comfort place to elevate your mood')

def main():
    global emotion
    global user_input
    user_input = st.text_input("",placeholder="How are you feeling right now ? ")
    if user_input:
        emotion = model.predict([user_input])
        st.write(f'Emotional Classification: {emotion}')

        
        

        
def sentiment():
    if user_input:
        st.header("What is your feeling in response to the above event ?")
        col1 , col2, col3 = st.columns(3)
        with col1:
            st.button("Positive :smile:",key="positive")
        with col2:
            st.button("Negative :worried:",key="negative")
        with col3:
            st.button("Neutral :no_mouth:",key="neutral")

        
        if st.session_state.get("positive"):
            positive()

        elif st.session_state.get("negative"):
            negative()

            st.write('- Take a deep breath and try to relax.')
            st.write('- Journal about your feelings to process them.')
            st.write('- Consider reaching out to a mental health professional.')
    
        elif st.session_state.get("neutral"):
            neutral()

        #neutral_suggestions()
        st.write('- Take a moment to reflect and find your inner peace.')
        st.write('- Practice mindfulness and meditation.')
        st.write('- Spend time in nature to recharge.')
        
        final_evaluation()

def positive():
    if(emotion == "Elation"): 
    
        st.title("Here are things to elevate you mood even more : ")
        st_player("http://www.youtube.com/watch?v=I35paFqFOPk")
        st_player("http://www.youtube.com/watch?v=jfs1Y4b-hO0")
        
        st.write("Want Funny videos? , here are some !")
        st_player("http://www.youtube.com/watch?v=268scEdtxYw")
        st_player("http://www.youtube.com/watch?v=tCz8VoCF0uE")

    if(emotion == "Despair"):
        st.title("It is commendable that despite the nature of events you feel positive towards it,Here are things to fix your mood : ")
        st.header("Here is a story to cheer you up ! ")
        with st.container(height=300,border=True):
            st.write("""Imagine there is a bank, which credits your account each morning with Rs 86,400, carries over no balance from day to day, allows you to keep no cash balance, and every evening cancels whatever part of the amount you had failed to use during the day. What would you do? Draw out every pence, of course!
Well, everyone has such a bank. Its name is Time.
Every morning, it credits you with 86,400 seconds. Every night it writes off, as lost, whatever of this you have failed to invest to good purpose. It carries over no balance. It allows no overdraft. Each day it opens a new account for you. Each night it burns the records of the day. If you fail to use the day’s deposits, the loss is yours.
There is no going back. There is no drawing against the “tomorrow.”
Therefore, there is never not enough time or too much time. Time management is decided by us alone and nobody else. It is never the case of us not having enough time to do things, but the case of whether we want to do it.""")
            st.header("That was a good story!, but also remember to reach out to friends and family in times of distress")
            url = "https://medium.com/motivationapp"
            st.write("For more stories check out this [link](%s)" % url)

    if(emotion == "Anxiety"):
        st.title("It is commendable that despite the nature of events you feel positive towards it,Here are things to fix your mood : ")
        st.header("Here is a story to cheer you up ! ")
        with st.container(height=300,border=True):
            st.write("""A man found a cocoon of a butterfly.
                     
One day a small opening appeared. He sat and watched the butterfly for several hours as it struggled to force its body through that little hole.

Until it suddenly stopped making any progress and looked like it was stuck.

So the man decided to help the butterfly. He took a pair of scissors and snipped off the remaining bit of the cocoon. The butterfly then emerged easily, although it had a swollen body and small, shriveled wings.

The man didn’t think anything of it and sat there waiting for the wings to enlarge to support the butterfly. But that didn’t happen. The butterfly spent the rest of its life unable to fly, crawling around with tiny wings and a swollen body.

Despite the kind heart of the man, he didn’t understand that the restricting cocoon and the struggle needed by the butterfly to get itself through the small opening; were God’s way of forcing fluid from the body of the butterfly into its wings. To prepare itself for flying once it was out of the cocoon.

Moral of the story:
Our struggles in life develop our strengths. Without struggles, we never grow and never get stronger, so it’s important for us to tackle challenges on our own, and not be relying on help from others.""")

            st.subheader("Wait up ! Here are some personalized recommendation : ")
            st.write(":one: Physical Activities : Recommendation: High-intensity workouts like kickboxing, running, or weightlifting can be effective in releasing pent-up frustration.")
            st.write(":two: Yoga and meditation - Recommendation: Engage in a yoga or meditation session to calm the mind and release tension. Practices focused on deep breathing and mindfulness can be particularly helpful.")
            st.write(":three: Journaling - Write about the source of frustration, your feelings, and potential solutions. Journaling can help gain clarity and perspective.")
            st.write(":four: Meditation could be your thing!")
            st_player("http://www.youtube.com/watch?v=ZVcQXX7fmFI")

    if(emotion == "Resentment"):
        st.title("It is commendable that despite the nature of events you feel positive towards it,Here are things to fix your mood : ")
        st.header("Here is a story to cheer you up ! ")
        with st.container(height=300,border=True):
            st.write("""As a group of frogs was traveling through the woods, two of them fell into a deep pit. When the other frogs crowded around the pit and saw how deep it was, they told the two frogs that there was no hope left for them.

However, the two frogs decided to ignore what the others were saying and they proceeded to try and jump out of the pit.

Despite their efforts, the group of frogs at the top of the pit were still saying that they should just give up. That they would never make it out.

Eventually, one of the frogs took heed to what the others were saying and he gave up, falling down to his death. The other frog continued to jump as hard as he could. Again, the crowd of frogs yelled at him to stop the pain and just die.

He jumped even harder and finally made it out. When he got out, the other frogs said, “Did you not hear us?”

The frog explained to them that he was deaf. He thought they were encouraging him the entire time.

Moral of the story:
People’s words can have a big effect on other’s lives. Think about what you say before it comes out of your mouth. It might just be the difference between life and death.""")
            st.header("That was a good story!, but also remember no one is perfect it is okay to make mistakes!")
            url = "https://medium.com/motivationapp"
            st.write("For more stories check out this [link](%s)" % url)
    if emotion =="Courage":
         st.title("Bravery is one of the amazing virtues a person can have, and you are no lesser than an amazing person. Wanna hear about one more amazing person ? ")
         st.subheader("Harriet Tubman")
         st.write("""Dubbed as one of America’s most courageous women, Tubman suffered a lot but overcame and fought.

Born into slavery in the 1820s, she was regularly whipped and punished. Two of her sisters were sold to a gang. One day, she was hit with a two-pound weight in the head causing her to have sleeping spells (narcolepsy) for the rest of her life.

But that didn’t stop her. After her slave owner died, she fled north with two of her brothers.

And she repeatedly risked her life, 13 times to be exact, when she traveled back south to free the rest of her family.

She later worked as a Union army nurse, scout, and spy during the Civil War.

In 1863, she became the first woman in American history to plan and lead a military raid, liberating almost 700 enslaved people in South Carolina.

And that’s not all. She raised funds for formerly enslaved persons and helped build schools and a hospital.

And she fought to collect a veteran’s pension, which she was eventually awarded.

Her final words, at age 91, were, “I go away to prepare a place for you.” """)


def negative():
    pass
def neutral():
    pass

def final_evaluation() : 
    st.header("We hope the suggestions helped you out ! Do you feel better now ?")
    st.button("I feel great!", key = "bye")
    st.button("I still don't feel better...", key = "helplines")

    if st.session_state.get("bye"):
        st.header("That's the way to go!")

    elif st.session_state.get("helplines"):
        st.header("Please consider reaching out to the following helplines ! ")



if __name__ == '__main__':
    misc.initiate_senti_analyzer()
    with st.container():
        with st.container():
            left_coloumn, right_coloumn = st.columns(2)
            with left_coloumn:
                main()
            with right_coloumn:
                st_lottie(
                    lottie_coding,speed=1,
                    reverse=True,quality="high",
                    height=None,
                    width="None",key="Be Present",

            )
        
        sentiment()
        
                
        
            

