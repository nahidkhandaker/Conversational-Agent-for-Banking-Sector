import pandas as pd
from joblib import load
from chatbot import chatbot_ans  # Import your chatbot logic

def validate_chatbot(model_path="data/chatbot_model.joblib", embedding_path="data/sentence_embeddings", data_path="data/transcript.csv"):
    # Load the dataset and models
    dataframe = pd.read_csv(data_path)
    loaded_model = load(model_path)
    sentence_embeddings = load(embedding_path)
    
    correct_responses = 0
    total_questions = len(dataframe)
    
    for index, row in dataframe.iterrows():
        question = row['Question']  # Adjust column names based on your CSV structure
        expected_answer = row['Answer']  # Adjust column names
        
        # Get chatbot response
        chatbot_response, _ = chatbot_ans(loaded_model, sentence_embeddings, question, dataframe)
        
        # Compare chatbot response with expected answer
        if chatbot_response.strip() == expected_answer.strip():
            correct_responses += 1
        
        # Optional: Print comparison for debugging
        print(f"Q: {question}")
        print(f"Expected: {expected_answer}")
        print(f"Chatbot: {chatbot_response}")
        print("-" * 50)
    
    # Calculate accuracy
    accuracy = (correct_responses / total_questions) * 100
    print(f"\nAccuracy: {accuracy:.2f}%")
    print(f"Correct Answers: {correct_responses}/{total_questions}")

# Run validation
if __name__ == "__main__":
    validate_chatbot()
