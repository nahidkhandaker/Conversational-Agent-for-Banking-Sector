from speech_to_text import speech_to_text
from chatbot import chatbot_ans
from joblib import load
from pandas import read_csv
from text_to_speech import text_to_speech

# Load resources once at startup
loaded_model = load('data/chatbot_model.joblib')
sentence_embeddings = load('data/sentence_embeddings')
dataframe = read_csv("data/transcript.csv")

def interactive_agent():
    user_question_text = speech_to_text()

    if user_question_text.startswith("আপনার বক্তব্য পরিষ্কারভাবে শোনা যায়নি"):
        text_to_speech(user_question_text)
        return
    
    db_ans, similarity_score = chatbot_ans(loaded_model, sentence_embeddings, user_question_text, dataframe)
    print(f"Similarity Score: {similarity_score:.2f}")
    
    text_to_speech(text=db_ans)
