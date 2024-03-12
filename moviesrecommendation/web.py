import streamlit as st
import pickle as pk
import requests

def fetch_poster (movies_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=97e4da295a0edb878b497549bcb0edde".format(movies_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path


movies=pk.load(open("movie_list.pkl", 'rb'))
similarity=pk.load(open("sim.pkl", 'rb'))
movies_list = movies['title'].values

st.header("MOVIES RECOMMENDATION")


selected_movie = st.selectbox('Select a movie', movies_list)

import streamlit.components.v1 as components

def recommend (movie):
    index = movies [movies['title'] == movie].index[0]
    distance=sorted(list (enumerate(similarity [index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    recommend_post=[]
    for i in distance[0:10]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_post.append(fetch_poster(movies_id))
    return recommend_movie,recommend_post

if st.button("show Recommended  Movies"):
    rec_movies,rec_posts=recommend(selected_movie)
    c1,c2,c3,c4,c5,c6=st.columns(6)
    with c1:
        st.text(rec_movies[0])
        st.image(rec_posts[0])
    with c2:
        st.text(rec_movies[1])
        st.image(rec_posts[1])
    with c3:
        st.text(rec_movies[2])
        st.image(rec_posts[2])
    with c4:
        st.text(rec_movies[3])
        st.image(rec_posts[3])
    with c5:
        st.text(rec_movies[4])
        st.image(rec_posts[4])
    with c6:
        st.text(rec_movies[5])
        st.image(rec_posts[5]) 