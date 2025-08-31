<h1>Movie Search Engine</h1> 
An interactive movie search engine that helps users discover movies from 2000 to 2025 based on the search query. Built with Python and deployed on Streamlit Cloud for seamless access.

<h2>Live Demo</h2>
Try the app here: [Streamlit App Link](https://movies-search-engine-nhm6kbag7wtb8ljrdboe7p.streamlit.app/)

<h2>Video Demo</h2>
[Gif demo](search-movies.gif)

<h2>Images</h2>
[img1](img1.png)

<h2>Features</h2>
* Search for movies by title, genre, or keyword
* Retrieves the most relevant results from a dataset of around 3000 movies
* Fast similarity search using vector embeddings
* Simple and intuitive interface with Streamlit

<h2>Technologies Used</h2>
* Python - Core language for data processing and search logic
* Streamlit - For interactive UI and deployment
* FAISS / Vector Databases - For efficient similarity search
* JSON - For managing and processing the dataset
* Text Embedding Model - For better search relevance

<h2>Installation (Run Locally)</h2>
<pre>
# Clone the repository
git clone https://github.com/Munfa/movies-search-engine.git
cd movies-search-engine

# Install dependencies
pip install -r requirements.txt

# Run the application
Streamlit run app.py
</pre>

<h2>Dataset</h2>
* Collected movies from [TMDB API](https://developer.themoviedb.org/docs/getting-started)
* Movies from 2000 to 2025 stored in movies.json
* Includes Title, Genres, Release Date, Overview, and Poster Link

<h2>How it works</h2>
1. Enter a search query in the Streamlit App
2. The query is converted into vector embeddings
3. FAISS finds the closest matches from the database
4. The top results are displayed with details such as Title, Genres, Release Date, Overview, and Poster
 
<h2>Future Enhancements</h2>
* Add filtering options (genre, year, rating)
* Use advanced NLP models for improved search accuracy
 
<h2>License</h2>
This project is licensed under the MIT License.





