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
import random
from joblib import load 

model = load("Data/model.pkl")
word_list = "Data/extreme.txt"
with open(word_list , 'r') as file:
    bad_words = set(file.read().splitlines())
sid = SentimentIntensityAnalyzer()
st.set_page_config(page_title = "MoodUp" ,page_icon = ":relieved_face:",layout = "wide")
def load_lottiefile(filepath : str):
    with open(filepath,"r") as f:
        return json.load(f)
    
lottie_coding = load_lottiefile("mindful.json")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("background.jpg");
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
    st.subheader("How are you feeling right now ? ")
    user_input = st.text_input("", placeholder="Enter here...")
    if user_input:

        emotion = model.predict([user_input])
        st.write(f'Emotional Classification: {emotion[0]}')       

        
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
    
        elif st.session_state.get("neutral"):
            neutral()
        
        if any(word.lower() in bad_words for word in user_input.split()):
            st.write("Your thoughts seem concerning. Please reach out to a helpline for support.")
            st.write("Here's a helpline number: +91 9999 666 555", )

        final_evaluation()
    


def positive():
    if(emotion == "Elation"): 
    
        st.title("Here are things to elevate you mood even more : ")
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            st_player("http://www.youtube.com/watch?v=I35paFqFOPk")
        with c2:
            st_player("http://www.youtube.com/watch?v=jfs1Y4b-hO0")
            
        with c3:
            st_player("http://www.youtube.com/watch?v=268scEdtxYw")
        with c4:
            st_player("http://www.youtube.com/watch?v=tCz8VoCF0uE")

    if(emotion == "Despair"):
        st.title("It is commendable that despite the nature of events you feel positive towards it,Here are things to fix your mood : ")
        st.header("Here is a story to cheer you up ! ")
        with st.container(height=300,border=True):
            st.markdown("""
        <style>
        .big-font {
            font-size: 100px;
        }
    </style>
    <div class="big-font">
        <p>As a man was passing the elephants, he suddenly stopped, confused by the fact that these huge creatures were being held by only a small rope tied to their front leg. No chains, no cages. It was obvious that the elephants could, at any time, break away from their bonds but for some reason, they did not.</p>
        <p>He saw a trainer nearby and asked why these animals just stood there and made no attempt to get away. “Well,” the trainer said, “when they are very young and much smaller we use the same size rope to tie them and, at that age, it’s enough to hold them. As they grow up, they are conditioned to believe they cannot break away. They believe the rope can still hold them, so they never try to break free.”</p>
        <p>The man was amazed. These animals could at any time break free from their bonds but because they believed they couldn’t, they were stuck right where they were.</p>
        <p>Like the elephants, how many of us go through life hanging onto a belief that we cannot do something, simply because we failed at it once before?</p>
        <p>Failure is part of learning; we should never give up the struggle in life.</p>
    </div>
""", unsafe_allow_html=True)
            st.header("That was a good story!")
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
    if(emotion == "Elation"): 
        
        st.title("Despite things going well you seem to be unsatisfied. It's okay to feel so.")

        st.title("Here are things to elevate your mood : ")
        st_player("http://www.youtube.com/watch?v=I35paFqFOPk")
        st_player("http://www.youtube.com/watch?v=jfs1Y4b-hO0")
        
        st.write("Want Funny videos? , here are some !")
        st_player("http://www.youtube.com/watch?v=268scEdtxYw")
        st_player("http://www.youtube.com/watch?v=tCz8VoCF0uE")
    
    if(emotion == "Despair"): 
    
        st.title("It's okay to feel despair, and we're here to support you through this challenging time. We understand that despair can be overwhelming, and reaching out for help is a brave step.")
        st.header("Here is a story to cheer you up ! ")
        with st.container(height=300,border=True):
            st.write("""Think what a remarkable, un-duplicatable, and miraculous thing it is to be you! Of all the people who have come and gone on the earth, since the beginning of time, not ONE of them is like YOU!
No one who has ever lived or is to come has had your combination of abilities, talents, appearance, friends, acquaintances, burdens, sorrows and opportunities.

No, one’s hair grows exactly the way yours does. No one’s finger prints are like yours. No one has the same combination of secret inside jokes and family expressions that you know.

The few people who laugh at all the same things you do, don’t sneeze the way you do. No one prays about exactly the same concerns as you do. No one is loved by the same combination of people that love you — NO ONE!

No one before, no one to come. YOU ARE ABSOLUTELY UNIQUE!

Enjoy that uniqueness. You do not have to pretend in order to seem more like someone else. You weren’t meant to be like someone else. You do not have to lie to conceal the parts of you that are not like what you see in anyone else.

You were meant to be different. Nowhere ever in all of history will the same things be going on in anyone’s mind, soul and spirit as are going on in yours right now.

If you did not exist, there would be a hole in creation, a gap in history, something missing from the plan for humankind.

Treasure your uniqueness. It is a gift given only to you. Enjoy it and share it!

No one can reach out to others in the same way that you can. No one can speak your words. No one can convey your meanings. No one can comfort with your kind of comfort. No one can bring your kind of understanding to another person.

No one can be cheerful and lighthearted and joyous in your way. No one can smile your smile. No one else can bring the whole unique impact of you to another human being.

Share your uniqueness. Let it be free to flow out among your family and friends and people you meet in the rush and clutter of living wherever you are. That gift of yourself was given you to enjoy and share. Give yourself away!

See it! Receive it! Let it tickle you! Let it inform you and nudge you and inspire you! YOU ARE UNIQUE!""")
            st.header("That was a good story!, but remember that reaching out to friends and family in times of distress is great way to provide relief")
            url = "https://medium.com/motivationapp"
            st.write("For more stories check out this [link](%s)" % url)


    if(emotion == "Anxiety"):
        st.title("It is understandable that dealing with anxiety can be challenging, and it's completely okay to feel negative about it. We're here to provide support and helpful suggestions to navigate through these moments.")
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
            st.write(":one: Physical Activities : Recommendation: High-intensity workouts like kickboxing, running, or weightlifting can be effective in releasing pent-up feelings.")
            st.write(":two: Yoga and meditation - Recommendation: Engage in a yoga or meditation session to calm the mind and release tension. Practices focused on deep breathing and mindfulness can be particularly helpful.")
            st.write(":three: Journaling - Write about your feelings, and potential solutions. Journaling can help gain clarity and perspective.")
            st.write(":four: Meditation could be your thing!")
            st_player("http://www.youtube.com/watch?v=ZVcQXX7fmFI")

    if(emotion == "Resentment"):
        st.write(":one: Identify and Understand: Reflect on the source of resentment. Understand the specific actions or events that led to these feelings.")
        st.write(":two: If possible and appropriate, communicate your feelings with the person involved. Choose a calm and constructive setting to express how certain actions affected you.")
        st.write(":three: If resentment is significantly impacting your mental health and relationships, consider seeking the assistance of a mental health professional. Therapy can provide a safe space to explore and address these emotions.")
        st.title("It is commendable that despite the nature of events you have taken a brave step in addressing your feelings : ")
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
    
def neutral():
    st.title("It is okay to feel unsure about the event that you encountered, since you are confused - here some suggestions to fix your mood : ")
    st.write(""":one: Explore a new book : Pick up a book in a genre that interests you. Whether it's fiction, non-fiction, or a genre you haven't tried before, reading can be a great way to engage your mind. Here are some : 
	If you enjoy fiction: "The Night Circus" by Erin Morgenstern - A magical and enchanting tale set in a mysterious circus.
    If you prefer non-fiction: "Sapiens: A Brief History of Humankind" by Yuval Noah Harari - A thought-provoking exploration of human history.
    If you like mystery/thriller: "Gone Girl" by Gillian Flynn - A gripping psychological thriller. 

    Visit Goodreads to explore or reach out a library!
""")
    st.write(""":two: Try a new recipe : I fyou enjoy baking , we recommend you to try chocolate chip cookies - classic and comforting :yum:""")    
    st.write(""":three: Go for a walk : Walking is easily one of the most relaxing activities to feel calm and composed""")

def final_evaluation() : 
    st.header("We hope the suggestions helped you out ! Do you feel better now ?")
    st.button("I feel great!", key = "bye")
    st.button("I still don't feel better...", key = "helplines")

    if st.session_state.get("bye"):
        st.balloons()
        st.success("That's the way to go! We are happy that our application was able to solve your situation. Don't hesitate to return for help!")

    elif st.session_state.get("helplines"):
        st.error("Please consider reaching out to the following helplines immediately!") 
        found1, found2, found3 = st.columns(3)

        with found1:
            st.header*("The livelovelaugh foundation")
            st_player("https://youtu.be/rK0ALlJBdMQ?si=ryry2f2ER1ABN5Ik")
            st.link_button("Contact","https://www.thelivelovelaughfoundation.org/")   
        with found2:
            st.header*("Mental Health foundation India")
            st_player("https://youtu.be/YApr7jNxjL4")
            st.link_button("Contact","https://mhfindia.org/")   
        with found3:
            st.header*("Minds Foundation")
            st_player("https://youtu.be/J89L80N45wM")
            st.link_button("Contact","https://www.mindsfoundation.org/") 




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
        
                
        
            

