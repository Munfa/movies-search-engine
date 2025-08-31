from sentence_transformers import SentenceTransformer
import faiss
import pickle
from huggingface_hub import login
import numpy as np
import json
import os
from dotenv import load_dotenv
load_dotenv()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def create_faiss(movies):
    texts_to_embed = []
    metadata = []

    for movie in movies:
        genres = ", ".join(movie["genre"])
        text = f"Title: {movie['title']} | Genres: {genres} | Release Date: {movie['release_date']} | Overview: {movie['overview']} | Rating: {movie['rating']}"
        texts_to_embed.append(text)

    embedding_dim = 384
    index = faiss.IndexFlatL2(embedding_dim)
    batch_size = 200
    for i in range(0, len(texts_to_embed), batch_size):
        batch = texts_to_embed[i : i+batch_size]
        batch_embeddings = model.encode(batch, show_progress_bar=True)
        index.add(np.array(batch_embeddings, dtype=np.float32))

        metadata.extend(movies[i:i+batch_size])

    faiss.write_index(index, "movie_index.faiss")
    with open("movie_metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)
    print("successful!!!")

def load_models():
    index = faiss.read_index("movie_index.faiss")
    with open("movie_metadata.pkl", "rb") as f:
        metadata = pickle.load(f)
    return model, index, metadata
