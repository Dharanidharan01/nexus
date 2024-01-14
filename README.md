# AI Storyteller

## Presentation link
[Canva](https://www.canva.com/design/DAF5yqG6E0E/Fd2btwoMmynC9iqwdPWQMw/edit?utm_content=DAF5yqG6E0E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## Overview

AI Storyteller is a web application that uses OpenAI's GPT-3.5-turbo-instruct engine to generate stories based on user prompts and selected emotions. The application also integrates HumeStreamClient for capturing facial emotions using a webcam and DALL·E for generating images related to the generated story.

## Features

- **Capture Emotion:** Utilizes HumeStreamClient to capture facial emotion through a webcam.
- **Generate Story:** Takes user input prompts, modifies them based on selected emotions, and generates stories using OpenAI's GPT-3.5-turbo-instruct engine.
- **Generate Images:** Uses DALL·E to generate images corresponding to different sections of the generated story.
- **Text-to-Speech:** Utilizes OpenAI TTS to convert the generated story into audio for playback.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-storyteller.git
2. Install the required dependencies:
   pip install -r requirements.txt
   
3. Obtain API keys:
    OpenAI API key: OpenAI API
HumeStream API key: Obtain from HumeStream (replace the placeholder in face.py)

## Usage
Run the application:
streamlit run storyteller.py

## Dependencies
Streamlit
OpenAI
Hume
OpenCV
asyncio
numpy

## Configuration

Update API keys in storyteller.py and face.py.
Customize the list of emotions in emotion_options in storyteller.py.

## 
