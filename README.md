# 🎬 Movie Recommendation System

# 📌 Problem Statement

With thousands of movies available across streaming platforms, users often struggle to discover movies that match their interests. Traditional searching requires users to know exactly what they want to watch, making content discovery challenging.

The objective of this project is to build a Content-Based Movie Recommendation System that recommends movies similar to a selected movie by analyzing its content features such as genres, keywords, cast, and movie overview.

# 🚀 Project Overview

This project leverages Natural Language Processing (NLP) techniques to create a movie recommendation engine using the TMDB Movie Dataset.

The system combines multiple movie attributes into a single textual representation, applies Bag of Words (BoW) vectorization, and calculates movie similarity using Cosine Similarity. When a user selects a movie, the system recommends the most similar movies based on their content characteristics.

An interactive Streamlit web application allows users to easily search and receive movie recommendations in real time.

# 🎯 Objectives
1) Recommend movies based on content similarity.
2) Improve movie discovery experience for users.
3) Apply NLP techniques on movie metadata.
4) Build and deploy an interactive recommendation system.

# 🛠️ Tech Stack
Programming Language :
Python

Libraries & Frameworks:
Pandas
NumPy
Scikit-learn
NLTK
Pickle
Streamlit

Machine Learning Techniques:
Content-Based Filtering
Bag of Words (BoW)
Cosine Similarity

Dataset:
TMDB 5000 Movies Dataset

# 📊 Key Insights
Content Similarity Works Effectively

Movies sharing similar genres, themes, cast members, or plot descriptions tend to cluster together and generate relevant recommendations.

Importance of Feature Combination

Using only genres provides limited recommendations. Combining:

Genres
Keywords
Cast
Director
Overview

significantly improves recommendation quality.

NLP Enhances Matching

Text preprocessing and stemming help identify semantically related movies by reducing variations of similar words.

Fast Recommendation Retrieval

Precomputing the similarity matrix enables near real-time recommendations during user interaction.

# 📈 Outcome

✅ Built a fully functional Content-Based Movie Recommendation System.

✅ Implemented NLP preprocessing and Bag of Words vectorization.

✅ Used cosine similarity to generate accurate movie recommendations.

✅ Developed an interactive Streamlit UI for real-time recommendations.

✅ Integrated TMDB API to display movie posters dynamically.

✅ Created an end-to-end deployable machine learning application.
