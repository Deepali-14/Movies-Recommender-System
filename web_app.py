# import libraries
import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit_lottie import st_lottie



# setting webpage name
st.set_page_config(page_title = "Deepali's Webpage", page_icon = ":confetti_ball:", layout = "wide")



# function returning movie's poster using movie's id as parameter
def fetch_poster(movie_id):

    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=49929770be57a5432e4dffaab8c4d09f&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



# function returning 5 recommended movies with their corresponding posters
def recommend(movie):

    # fetching index of movie's name provided by the user
    movie_index = movies[movies['title'] == movie].index[0]

    # taking similarity of given movie with other movies
    distances = similarity[movie_index]

    # to get 5 most similar movies sorted in descending order of similarity using reverse function and applying
    # enumerate function to distances, converting them to list with 0th column as movie's index and 1st column as distances
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    # iterating through movies_list to fetch movie's poster and corresponding movie's title
    for i in movies_list:

        # getting movie's id from movie's index
        movie_id = movies.iloc[i[0]].movie_id

        # append recommended movie's title to recommended_movies list
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API using movie's id
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters



# function returning animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)



# calling function
local_css("style/style.css")



# calling function with url
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qm8eqzse.json")



# importing dataframes
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))



# heading for website
st.title('CONTENT BASED MOVIE RECOMMENDER SYSTEM')
st_lottie(lottie_coding, height = 300, key = "movie")


# taking input from the user i.e., movie's name
selected_movie_name = st.selectbox('search a movie name...', movies['title'].values)



# if recommend button is hit by the user calling recommend function with given movie name to fetch name and poster of 5 most similar movies
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # for displaying movie's title and their corresponding posters
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.text(names[0])
        st.image(posters[0])

    with c2:
        st.text(names[1])
        st.image(posters[1])

    with c3:
        st.text(names[2])
        st.image(posters[2])

    with c4:
        st.text(names[3])
        st.image(posters[3])

    with c5:
        st.text(names[4])
        st.image(posters[4])



st.sidebar.title("WELCOME :tada:")
st.sidebar.title("RECOMMENDER SYSTEM")
rad = st.sidebar.radio("Table of Content", ["Introduction", "Type", "Movie Recommender System", "Help?", "About Us", "Feedback"])

if rad == "Introduction":
    st.sidebar.info("Recommender System is a system that seeks to predict or filter preferences according to the user's choices.")


if rad == "Type":
    st.sidebar.info("Machine learning algorithms in recommender systems typically fit into two categories:")
    r = st.sidebar.radio("Category", ["Content-Based Systems", "Collaborative Filtering Systems"])

    if r == "Content-Based Systems":
        st.sidebar.info("Content-based methods are based on the similarity of attributes. Like if a user watches one movie, similar movies are recommended. For example, if a user watches a comedy movie starring Adam Sandler, the system will recommend them movies in the same genre or starring the same actor, or both.")

    if r == "Collaborative Filtering Systems":
        st.sidebar.info("With collaborative filtering, the system is based on past interactions between users and movies. The input for a collaborative filtering system is made up of past data of user interactions with the movies they watch. For example, if user A watches M1, M2, and M3, and user B watches M1, M3, M4, we recommend M1 and M3 to a similar user C.")

if rad == "Movie Recommender System":
    st.sidebar.info("A movie recommendation system is a fancy way to describe a process that tries to predict your preferred items based on your viewed content or people similar to you and many other ways. Here our movie recommender system takes a movie input from the user and then tries to find 5 most similar movie's title and corresponding poster based on content of the movie.")

if rad == "Help?":
    st.sidebar.info("Hi! I am Deepali :wave:")
    st.sidebar.info("A B.Tech. Information Technology Student from Banasthali Vidyapith, Jaipur. Lemme help you!")
    st.sidebar.info("Type or select a movie to search and click the recommend button and here you go with five most similar movies based on similarity in content.")

if rad == "About Us":
    st.sidebar.info("For more information contact deepalisingh141101@gmail.com or deepalis1401@gmail.com")

if rad == "Feedback":
        st.sidebar.info("Get In Touch With Me! :point_down:")
        contact_form = """
        <form action="https://formsubmit.co/deepalisingh141101@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="feedback" placeholder="Your feedback" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.sidebar.markdown(contact_form, unsafe_allow_html=True)

