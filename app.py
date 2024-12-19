from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Gemini Pro API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get a response
def get_gemini_response(image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([image[0], prompt])
    return response.text

# Function to get text response from Google Gemini Pro
def get_text_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt])
    return response.text

# Function to set up input image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="K-Drama Recommender and Analyzer", layout="wide")
st.header("🎬 K-Drama Companion 📺")

# Tabs for different functionalities
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Character Recognition", "Personalized Recommendations", "K-Drama Trends", "Trivia and Quizzes", "Fan Community"])

with tab1:
    st.subheader("🕵️ Character Recognition and Information")
    uploaded_file = st.file_uploader("Upload a screenshot or photo of a K-drama character...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_container_width=True)
        submit = st.button("IDENTIFY CHARACTER")
        input_prompt = """
        ### K-Drama Character Information 🎭

        You are an expert in K-dramas. Provide detailed information about the character in this image:

        - **Character Name**: The name of the character.
        - **Actor Name**: The actor who plays this character.
        - **Biography**: A brief biography of the actor.
        - **Other Roles**: Other notable roles played by the actor.
        - **Character Backstory**: The backstory of the character in the K-drama.
        """
        if submit:
            try:
                image_data = input_image_setup(uploaded_file)
                response = get_gemini_response(image_data, input_prompt)
                st.subheader("Character Information")
                st.write(response)
            except FileNotFoundError as e:
                st.error(str(e))

with tab2:
    st.subheader("📚 Personalized K-Drama Recommendations")
    mood = st.selectbox("Select your current mood or preference", ["None", "Currently trending", "High ratings and positive reviews","Action", "Comedy", "Drama", "Strong female characters", "Heartwarming friendships and strong bonds between characters", "Family dynamics"])
    get_recommendations = st.button("Get Recommendations")
    if get_recommendations:
        recommendations_prompt = f"""
        ### K-Drama Recommendations 📺

        Based on the user's mood or preference for {mood} dramas, recommend some K-dramas: 

        -1. **Title**: The title of the K-drama.
        - **Synopsis**: A brief synopsis of the K-drama.
        - **Why Watch**: Reasons why this K-drama fits the {mood} mood or preference.

        -2. **Title**: The title of the K-drama.
        - **Synopsis**: A brief synopsis of the K-drama.
        - **Why Watch**: Reasons why this K-drama fits the {mood} mood or preference.
        .
        .
        .
        -10. **Title**: The title of the K-drama.
        - **Synopsis**: A brief synopsis of the K-drama.
        - **Why Watch**: Reasons why this K-drama fits the {mood} mood or preference.

        """
        try:
            recommendations_response = get_text_response(recommendations_prompt)
            st.subheader("Recommended K-Dramas")
            st.write(recommendations_response)
        except Exception as e:
            st.error(str(e))

with tab3:
    st.subheader("📈 K-Drama Trends and Analytics")
    st.text("Analyzing trends...")
    trends_prompt = """
    ### K-Drama Trends 📊

    Analyze current trends in K-dramas based on viewing data and social media mentions. Provide insights on:

    - **Most Popular K-Dramas**: Current most popular K-dramas.
    - **Trending Genres**: Genres that are currently trending.
    - **Viewer Demographics**: Insights on the demographics of K-drama viewers.

    I don't want and overview please provide the names. Here are some effective methods to discover the latest popular Korean dramas:

    Streaming platforms (Netflix, Viki)
    Entertainment Websites (Marie Claire)
    Online Communities and Forums (Reddit)
    Social Media Platforms (Instagram and Twitter)
    YouTube channels
    Official Broadcasting Channels (tvN)
    """
    try:
        trends_response = get_text_response(trends_prompt)
        st.subheader("K-Drama Trends")
        st.write(trends_response)
    except Exception as e:
        st.error(str(e))

with tab4:
    st.subheader("🧠 Trivia and Quizzes")
    trivia_quiz_type = st.selectbox("Select type", ["Trivia", "Personality Quiz"])
    if trivia_quiz_type == "Trivia":
        trivia_prompt = """
        ### K-Drama Trivia ❓

        Generate some trivia questions based on K-drama plots, characters, and behind-the-scenes information.
        """
        try:
            trivia_response = get_text_response(trivia_prompt)
            st.subheader("K-Drama Trivia Questions")
            st.write(trivia_response)
        except Exception as e:
            st.error(str(e))

    elif trivia_quiz_type == "Personality Quiz":
        personality_quiz_prompt = """
        ### K-Drama Personality Quiz 🤔

        Create a personality quiz to match users with K-drama characters or determine which K-drama fits their personality.
        """
        try:
            personality_quiz_response = get_text_response(personality_quiz_prompt)
            st.subheader("K-Drama Personality Quiz")
            st.write(personality_quiz_response)
        except Exception as e:
            st.error(str(e))

with tab5:
    st.subheader("💬 Fan Community Discussions")
    discussion_input=st.text_area("Share your thoughts, theories, and favorite moments from K-dramas...")
    post_discussion=st.button("Post Discussion")
    if post_discussion and discussion_input:
        st.success("Discussion posted!")
    
    discussions_prompt = """
    ### Fan Community Discussions 💭

    List recent fan discussions on various K-dramas including theories, favorite moments, and general thoughts.
    """
    try:
        discussions_response = get_text_response(discussions_prompt)
        st.subheader("Recent Discussions")
        st.write(discussions_response)
    except Exception as e:
        st.error(str(e))
