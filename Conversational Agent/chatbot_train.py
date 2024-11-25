from joblib import dump
from sentence_transformers import SentenceTransformer
import pandas as pd

def chatbot_train(data, model_path="data/", embedding_path="data/"):
    # Validate dataset
    if data.empty or data.shape[1] < 2:
        print("Invalid dataset. Ensure it contains at least two columns (queries and responses).")
        return
    
    # Extract sentences efficiently
    sentences = data.iloc[:, -2].dropna().tolist()  # Assumes questions are in the second-last column

    # Load the model once
    model = SentenceTransformer('paraphrase-mpnet-base-v2')
    
    try:
        # Generate embeddings with progress tracking
        print("Generating sentence embeddings...")
        sentence_embeddings = model.encode(sentences, show_progress_bar=True)
        
        # Save the model and embeddings
        dump(model, f"{model_path}chatbot_model.joblib")
        dump(sentence_embeddings, f"{embedding_path}sentence_embeddings")
        print("Training complete. Model and embeddings saved successfully.")

    except Exception as e:
        print(f"Error during training: {e}")
