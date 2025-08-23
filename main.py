import numpy as np
import pandas as pd
from data_load import get_movies
from build_retriever import retriever
from generate_response import search_movies, get_response
import streamlit as st
import json
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

import warnings
warnings.filterwarnings("ignore")

# get_movies()

with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

df = pd.DataFrame(movies)

model, index = retriever(df)
# query = input("search for a movie: ")
# top_movies = search_movies(df, model, index, query, k=5)
# response = get_response(top_movies, query)
# print(response)
query = st.text_input("Search for a movie")
if query:
    top_movies = search_movies(df, model, index, query, k=5)
    response = get_response(top_movies, query)
    # st.write(response)
    for movie in top_movies:
        st.subheader(f"{movie['title']} ({movie['rating']})")
        st.write(f"Genres: {', '.join(movie['genre'])}")
        st.write(movie['overview'])
        st.image(movie["poster_url"], caption=movie["title"], width=150)


