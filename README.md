# Movie Search Engine
An interactive movie search engine that helps users discover movies from 2000 to 2025 based on the search query. Built with Python and deployed on Streamlit Cloud for seamless access.

## Live Demo
Try the app here: [Streamlit App Link](https://movies-search-engine-nhm6kbag7wtb8ljrdboe7p.streamlit.app/)

## Video Demo
[Gif demo](search-movies.gif)

## Features
* Search for movies by title, genre, or keyword
* Retrieves the most relevant results from a dataset of around 3000 movies
* Fast similarity search using vector embeddings
* Simple and intuitive interface with Streamlit

## Technologies Used
* Python - Core language for data processing and search logic
* Streamlit - For interactive UI and deployment
* FAISS / Vector Databases - For efficient similarity search
* JSON - For managing and processing the dataset
* Text Embedding Model - For better search relevance

## Installation (Run Locally)
```
# Clone the repository
git clone https://github.com/Munfa/movies-search-engine.git
cd movies-search-engine

# Install dependencies
pip install -r requirements.txt

# Run the application
Streamlit run app.py
```

## Dataset
* Collected movies from [TMDB API](https://developer.themoviedb.org/docs/getting-started)
* Movies from 2000 to 2025 stored in movies.json
* Includes Title, Genres, Release Date, Overview, and Poster Link

## How it works
1. Enter a search query in the Streamlit App
2. The query is converted into vector embeddings
3. FAISS finds the closest matches from the database
4. The top results are displayed with details such as Title, Genres, Release Date, Overview, and Poster
 
## Future Enhancements
* Add filtering options (genre, year, rating)
* Use advanced NLP models for improved search accuracy
 
## License
This project is licensed under the MIT License.





