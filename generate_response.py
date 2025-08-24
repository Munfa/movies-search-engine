from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from huggingface_hub import InferenceApi
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

def search_movies(df, model, index, query, k=5):
    # query = "funny family movie with cooking"
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
                        token="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"
                    )
    
    context = "\n".join([f"{r['title']} {r['genre']} ({r['rating']}) {r['overview']}" for r in results])
    prompt = f"""You are a helpful movie assistant.
    User wants to see: {query}
    Here are some relevant movies: {context}
    Suggest the best and most relevant matches in a nice and friendly way. Highlight top 2 choices.
    """

    # response = text_gen(prompt)[0]["generated_text"]
    response = generator(prompt)
    return response[0]['generated_text']
    