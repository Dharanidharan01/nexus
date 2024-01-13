import streamlit as st
from openai import OpenAI

# Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
client = OpenAI(api_key="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")

# Set page title and favicon
st.set_page_config(page_title="AI Storyteller", page_icon="📖")

# Add a header and description
st.title("AI Storyteller")
st.markdown("Enter a prompt and select the emotion you want the story to convey. Click 'Generate Story' to see the magic!")

# User input for prompt and story title
user_input_prompt = st.text_area("Write a prompt for the AI storyteller:")
user_input_title = st.text_input("Enter a title for the story:")

# Dropdown for selecting emotion
emotion_options = ["Happy", "Sad", "Excited", "Mysterious", "Surprised"]
selected_emotion = st.selectbox("Select the emotion for the story:", emotion_options)

# Variable to store generated story
if "generated_story" not in st.session_state:
    st.session_state.generated_story = None

# Button to generate the story and play audio
if st.button("Generate Story"):
    if user_input_prompt:
        try:
            # Modify the prompt based on the selected emotion
            prompt_with_emotion = f"Write a {selected_emotion.lower()} story: {user_input_prompt}"

            # Generate story using OpenAI GPT-3.5-turbo-instruct engine
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt_with_emotion,
                max_tokens=500
            )

            # Store the generated story in session state
            st.session_state.generated_story = response.choices[0].text

            # Display the generated story with title
            st.subheader(f"**{user_input_title}**")
            st.write(st.session_state.generated_story)

        except Exception as e:
            st.error(f"An error occurred while generating the story: {str(e)}")
    else:
        st.warning("Please enter a prompt for the AI storyteller.")

# Button to play audio
if st.button("Play Audio") and st.session_state.generated_story:
    try:
        # Use OpenAI TTS for text-to-speech
        speech_response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=st.session_state.generated_story
        )

        # Play the generated speech within the website itself
        st.audio(speech_response.content, format="audio/mp3", start_time=0)

    except Exception as e:
        st.error(f"An error occurred during text-to-speech: {str(e)}")

# Add a footer with attribution and link to OpenAI
st.markdown("---")
st.markdown("Built with ❤️ by Nexus")

# Add some styling to the app
st.markdown(
    """
    <style>
        body {
            color: #394240;
            background-color: #f5f5f5;
        }
        .st-bd {
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
