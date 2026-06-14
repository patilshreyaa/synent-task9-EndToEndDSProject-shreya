# import pickle
# import streamlit as st
# import requests
import streamlit as pd
import requests
import pickle
import streamlit as st

st.set_page_config(page_title="CineMatch", page_icon="🎬", layout="wide")

# Custom CSS with fixed selectbox padding and interactive feedback fixes
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght=700&family=DM+Sans:wght=300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0f;
    color: #e8e8e8;
}

.stApp {
    background: #0a0a0f;
}

.hero {
    text-align: center;
    padding: 3rem 0 2rem;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 1rem;
    color: #888;
    font-weight: 300;
    letter-spacing: 0.05em;
}

.accent {
    color: #e2b04a;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e2e;
    margin: 0.5 rem 0;
}

/* Fixed Selectbox styling - removed destructive inner padding */
div[data-baseweb="select"] {
    background: #13131f !important;
    border-radius: 12px !important;
}   

div[data-baseweb="select"] > div {
    background: #13131f !important;
    border: 1px solid #2a2a3e !important;
    border-radius: 12px !important;
    color: #e8e8e8 !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Button */
div.stButton > button {
    background: #e2b04a;
    color: #0a0a0f;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 2.5rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 1rem;
    letter-spacing: 0.03em;
    cursor: pointer;
    transition: all 0.2s ease;
    width: 100%;
}

div.stButton > button:hover {
    background: #f0c76a;
    transform: translateY(-1px);
}

/* Movie cards */
.movie-card {
    background: #13131f;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #1e1e2e;
    transition: transform 0.2s ease, border-color 0.2s ease;
    height: 100%;
}

.movie-card:hover {
    transform: translateY(-4px);
    border-color: #e2b04a55;
}

.movie-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    color: #e8e8e8;
    padding: 0.65rem 0.75rem 0.75rem;
    text-align: center;
    line-height: 1.4;
}

.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    color: #e2b04a;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 1.25rem;
    text-align: center;
}

/* Hide default streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stImage img {
    border-radius: 0px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# FIX 1: Cache the API calls so they load instantly after the first fetch
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url, timeout=5)
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception:
        pass
    # Fallback placeholder image if API fails or poster is missing
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters


# Load data assets safely
@st.cache_resource
def load_data():
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

st.markdown("""
<div class="hero">
    <h1>Cine<span class="accent">Match</span></h1>
    <p>Discover movies you'll love, powered by content-based intelligence</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Select a Movie to Search", movie_list, index=0, label_visibility="collapsed")
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    show = st.button("Find Similar Movies")

st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

if show:
    # FIX 2: Added visual spinner UI indicator so the user knows the app is working
    with st.spinner("Analyzing data to find matches..."):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    st.markdown('<p class="section-label">Top 5 Recommendations</p>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class="movie-card">
                <img src="{recommended_movie_posters[i]}" style="width:100%; display:block;" />
                <div class="movie-title">{recommended_movie_names[i]}</div>
            </div>
            """, unsafe_allow_html=True)