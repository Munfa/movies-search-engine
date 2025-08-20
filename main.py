import numpy as np
import pandas as pd
from data_load import get_movies
from build_retriever import retriever
import json
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import warnings
warnings.filterwarnings("ignore")

get_movies()

with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

df = pd.DataFrame(movies)

# retriever(df)


