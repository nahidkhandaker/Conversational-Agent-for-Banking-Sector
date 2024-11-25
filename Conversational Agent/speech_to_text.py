import speech_recognition as sr

def speech_to_text(path_to_save_ASR_audio="static/audio/", path_to_save_ASR_text="static/text/"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Calibrating microphone... Please wait.")
            r.adjust_for_ambient_noise(source, duration=2)  # Adjust for ambient noise
            print("Please say your query...")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            
            # Retry mechanism for better accuracy
            for attempt in range(3):  
                try:
                    text = r.recognize_google(audio, language='bn-BD')
                    break  # Break loop if successful
                except sr.UnknownValueError:
                    if attempt == 2:
                        text = "আপনার বক্তব্য পরিষ্কারভাবে শোনা যায়নি। দয়া করে আবার বলুন।"
                        print("Recognition failed after multiple attempts.")
            
            # Save audio and text
            with open(path_to_save_ASR_audio + "input.wav", "wb") as f:
                f.write(audio.get_wav_data())
            with open(path_to_save_ASR_text + "input.txt", "w", encoding='utf-8') as f:
                f.write(text)
            
            return text

        except Exception as e:
            print("Error:", e)
            return "কিছু সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।"
