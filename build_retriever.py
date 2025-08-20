from sentence_transformers import SentenceTransformer
import faiss
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Preparing text for embedding
def movie_text(row):
    genres = ",".join(row["genre"])
    text = f"Title:{row['title']} | Genres:{genres} | Overview:{row['overview']} | Rating:{row['rating']}"
    return text

def retriever(df):
    docs = df.apply(movie_text, axis=1).tolist()

    model = SentenceTransformer("all-MiniLM-L6-v2")
    # generate embeddings for the sentences
    embeddings = model.encode(docs, convert_to_numpy=True)
    
    d = embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(embeddings)
    print(f"Total movies indexed: {index.ntotal}")