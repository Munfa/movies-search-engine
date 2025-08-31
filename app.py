import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

import pandas as pd
from data_load import get_movies
from build_retriever import create_faiss, load_models
from query_movies import search_movies, get_response
import streamlit as st
import json

# get_movies()      #load movies from the API

with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

# create_faiss(movies)  # creating the retriever

model, index, metadata = load_models()

st.title("Movie Search Engine")
query = st.text_input("Search for a movie", placeholder="nice family movie with animals")
if query:
    response = get_response(query)
    top_movies = search_movies(response, model, index, metadata, k=5)
    
    for movie in top_movies:
        st.subheader(f"{movie['title']} ({movie['rating']})")
        st.write(f"Genres: {', '.join(movie['genre'])}")
        st.write(f"Release Date: {movie['release_date']}")
        st.write(movie['overview'])
        st.image(movie["poster_url"], caption=movie["title"], width=200)

