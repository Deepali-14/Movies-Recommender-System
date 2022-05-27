# Movie Recommendation System
# Content-Based Movie Recommendation System -
This type of recommendation engine works on the concept that if a user liked a particular movie, he/she might like a movie similar to it based on attributes such as genre, director, actors etc.

Check out the project here : https://deepali-movies-recommender.herokuapp.com/ 

For this initially the datasets were selected from https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

The movies posters were fetched from https://www.themoviedb.org/

The frontend contains a mixture of animations from https://lottiefiles.com/tools/json-editor?gclid=CjwKCAjw7cGUBhA9EiwArBAvorhnUz_8Xltfagq9azJ3dPit7iTLgYWemaLEdxU4MpovIFg0KnnCwRoC1yIQAvD_BwE and emojis from https://www.webfx.com/tools/emoji-cheat-sheet/#

# How to get the API key?
Create an account on https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

# How to run the project?
1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
4. Replace YOUR_API_KEY in both the places (line no. 15 and 29) of static/recommend.js file and hit save.
5. Open your terminal/command prompt from your project directory and run the file main.py by executing the command python main.py.
6. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
7. Hurray! That's it.
