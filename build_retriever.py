from sentence_transformers import SentenceTransformer
import faiss
from huggingface_hub import login
import os
from dotenv import load_dotenv
load_dotenv()

# Preparing text for embedding
def movie_text(row):
    genres = ",".join(row["genre"])
    text = f"Title:{row['title']} | Genres:{genres} | Overview:{row['overview']} | Rating:{row['rating']}"
    return text

def retriever(df):
    docs = df.apply(movie_text, axis=1).tolist()

    login(token=os.getenv("HF_TOKEN"))
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    # generate embeddings for the sentences
    embeddings = model.encode(docs, convert_to_numpy=True)
    
    # using FAISS for storing and search
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(embeddings)

    return model, index
