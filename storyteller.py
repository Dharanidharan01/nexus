import streamlit as st
import openai

openai.api_key = "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"  #zorodium api key

# Set page title and favicon
st.set_page_config(page_title="AI Storyteller", page_icon="📖")

# Add a header and description
st.title("AI Storyteller")
st.markdown("This AI storyteller generates creative stories based on your prompts. Enter a prompt and click 'Generate Story'.")

# User input for prompt
user_input = st.text_area("Write a prompt for the AI storyteller:")

# Button to generate the story
if st.button("Generate Story"):
    if user_input:
        try:
            # Generate story using OpenAI GPT-3.5-turbo-instruct engine
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct", 
                prompt=user_input,
                max_tokens=500
            )

            # Display the generated story
            st.subheader("Generated Story:")
            st.write(response.choices[0].text)
        except Exception as e:
            st.error("An error occurred:")
            st.write(str(e)) 
    else:
        st.warning("Please enter a prompt for the AI storyteller.")

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
