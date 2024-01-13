import streamlit as st
import openai


openai.api_key = "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"  #zorodium api key

st.title("AI Storyteller")

user_input = st.text_input("Write a prompt for the AI storyteller:")

if st.button("Generate Story"):
    if user_input:
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct", 
                prompt=user_input,
                max_tokens=500
            )

            st.subheader("Generated Story:")
            st.write(response.choices[0].text)
        except Exception as e:
            st.error("An error occurred:")
            st.write(str(e)) 
    else:
        st.warning("Please enter a prompt for the AI storyteller.")