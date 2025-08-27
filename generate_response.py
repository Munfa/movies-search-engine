from transformers import pipeline
import os
from dotenv import load_dotenv
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

def search_movies(df, model, index, query, k=5):
    query_vec = model.encode([query], convert_to_numpy=True)
    _, indices = index.search(query_vec, k)
    results = []
    for i in indices[0]:
        results.append({
            "title": df.iloc[i]["title"],
            "genre": df.iloc[i]["genre"],
            "rating": df.iloc[i]["rating"],
            "overview": df.iloc[i]["overview"],
            "poster_url": df.iloc[i].get("poster_url")
        })

    return results

def get_response(results, query):
    generator = pipeline("text2text-generation",
                         model="google/flan-t5-base",
                        token=hf_token
                    )
    
    context = "\n".join([f"{r['title']} {r['genre']} ({r['rating']}) {r['overview']}" for r in results])
    prompt = f"""You are a helpful movie assistant.
    User wants to see: {query}
    Here are some relevant movies: {context}
    Suggest the best and most relevant matches in a nice and friendly way. Highlight top 2 choices.
    """

    response = generator(prompt)
    return response[0]['generated_text']
    