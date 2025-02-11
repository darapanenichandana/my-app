import speech_recognition as sr # type: ignore
from translate import Translator # type: ignore
from monsterapi import client # type: ignore
import requests # type: ignore
from PIL import Image # type: ignore

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjUxMzgyY2VjZWU0ZjI4MzAwMDg3NGM1ZWE1Yjc2YzQ3IiwiY3JlYXRlZF9hdCI6IjIwMjUtMDItMDRUMTU6MTI6NDMuMzE4MDE1In0.qTcB0YFW7Df2bymGhHq4ILK0dTGjdjMB53KiyuM90sQ'  # Replace 'your-api-key' with your actual Monster API key
monster_client = client(api_key)

recognizer = sr.Recognizer()
translator = Translator(from_lang="hi",to_lang="en")

with sr.Microphone() as Source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(Source)
    audio = recognizer.listen(Source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")

        translated_text = translator.translate(text)
        print(translated_text)
    except sr.UnknownValueError:
        print("can't understand")
    except sr.RequestError:
        print("google API Error")

model = 'txt2img'  
input_data = {
'prompt': f'{translated_text}',
'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
'samples': 1,
'steps': 50,
'aspect_ratio': 'square',
'guidance_scale': 7.5,
'seed': 2414,
            }
            
            
print("Generating...")
result = monster_client.generate(model, input_data)

img_url = result['output'][0]

file_name = "image.png"

response = requests.get(img_url)
if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
        print("Image downloaded")

        img = Image.open(file_name)
        img.show()

else:
    print("Failed to download the image") 