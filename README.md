# Movie Recommendation System
# Content-Based Movie Recommendation System -
This type of recommendation engine works on the concept that if a user liked a particular movie, he/she might like a movie similar to it based on attributes such as genre, director, actors etc.

Check out the project here : https://deepali-movies-recommender.herokuapp.com/ 

For this initially the datasets were selected from https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

The movies posters were fetched from https://www.themoviedb.org/

The frontend contains a mixture of animations from https://lottiefiles.com/tools/json-editor?gclid=CjwKCAjw7cGUBhA9EiwArBAvorhnUz_8Xltfagq9azJ3dPit7iTLgYWemaLEdxU4MpovIFg0KnnCwRoC1yIQAvD_BwE and emojis from https://www.webfx.com/tools/emoji-cheat-sheet/#

For more information on streamlit visit https://docs.streamlit.io/library/api-reference

# How to get the API key?
Create an account on https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

# How to run the project?
1. Clone or download this repository to your local machine.
2. Run the movie-recommender-system.ipynb python file on your Jupyter Notebook by installing all the required libraries.
3. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt in PyCharm. 
4. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
5. Replace YOUR_API_KEY in (line no. 18) of web_app.py file and hit save.
6. Open your terminal/command prompt from your project directory and run the file web_app.py by executing the command streamlit run web_app.py.
7. And Hurray! That's it. Your Recommendation Engine is ready!

# Similarity Score -
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges which between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
