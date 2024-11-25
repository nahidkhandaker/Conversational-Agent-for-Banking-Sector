from gtts import gTTS
import os

def text_to_speech(text, output_audio_path="static/audio/output.wav"):
    try:
        if not os.path.exists(output_audio_path):
            myobj = gTTS(text=text, lang='bn', slow=False)
            myobj.save(output_audio_path)
        os.system("mpg123 " + output_audio_path)
    except Exception as e:
        print("Text-to-Speech Error:", e)
