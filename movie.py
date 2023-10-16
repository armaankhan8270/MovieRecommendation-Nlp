from PIL import Image
import pickle
import streamlit as st
import pandas as pd
import requests


def recomed(movie):
    index = df[(df['title'] == movie) | (
        df['title'] == movie.title())].index[0]

    distance = similarity[index]
    movie_index = sorted(
        list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:7]
    inedxes = []
    for l in movie_index:
        movid = M_id[l[0]]
        inedxes.append(movid)

    lists = []
    for m in movie_index:
        lists.append(df.iloc[m[0]].title)
    ti = []
    for m in movie_index:
        ti.append(df.iloc[m[0]].title)

    return movie_index, inedxes, ti


movies = pickle.load(open('./movies_list.pkl', 'rb'))
M_id = pickle.load(open('./id.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))
df = pd.DataFrame(list(movies.items()), columns=['Index', 'title'])

st.title("Movie Recommendations")

option = st.selectbox("Pick a movie", df['title'])

selected_index = df[df['title'] == option]['Index'].values[0]

selected_movie_details = movies[selected_index]

recommedn_movies, id_s, t = recomed(option)
st.subheader("Selected Movie Details:")
st.write("Title:", option)
for movie in t:
    st.write("Recommedn Movies : ", movie)

if st.button("Click me"):
    recomed(option)


def getposter(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=fc85b8aebcdd175a81c9ce4e23df26bf&language=en-US'.format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path1 = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path1
    return full_path


rows = [id_s[0:1], id_s[1:2], id_s[2:3], id_s[3:4], id_s[4:5]]

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    for i in rows[0]:
        Image = getposter(i)
        st.image(Image)

# Display images in the second column (row 2)
with col2:

    for i in rows[1]:
        Image = getposter(i)
        st.image(Image)
with col3:

    for i in rows[2]:
        Image = getposter(i)
        st.image(Image)
with col4:

    for i in rows[3]:
        Image = getposter(i)
        st.image(Image)

with col5:

    for i in rows[4]:
        Image = getposter(i)
        st.image(Image)
