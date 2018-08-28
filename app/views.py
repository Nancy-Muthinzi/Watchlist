from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    '''

    #getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = 'Home - Welcome to The Best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

    
# @app.route('/movie/<int:movie_id>')
# def movie(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data    
#     '''

#     return render_template('movie.html', title = title)