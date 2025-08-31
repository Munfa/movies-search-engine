from transformers import pipeline
from sentence_transformers import CrossEncoder
import os
from dotenv import load_dotenv
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

def search_movies(query, model, index, metadata, k):
    query_vec = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        if i<len(metadata):
            results.append({
                "title": metadata[i].get("title"),
                "genre": metadata[i].get("genre"),
                "release_date": metadata[i].get("release_date"),
                "rating": metadata[i].get("rating"),
                "overview": metadata[i].get("overview"),
                "poster_url": metadata[i].get("poster_url")
            })
    
    results.sort(key=lambda x:x['rating'], reverse=True)
    return results

def get_response(query):
    generator = pipeline("text2text-generation",
                         model="google/flan-t5-base",
                        token=hf_token
                    )
    
    # context = "\n".join([f"{r['title']} {r['genre']} ({r['rating']}) {r['overview']}" for r in results])
    # Here are some relevant movies: {context}
    
    prompt = f"""You are a helpful movie assistant.
    User wants to see: {query}
    Suggest the best and most relevant movies
    """

    response = generator(prompt)
    return response [0]['generated_text']
    