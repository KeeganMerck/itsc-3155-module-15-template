from flask.testing import FlaskClient
from tests.utils import create_movie, refresh_db

def test_get_all_movies(test_app: FlaskClient):
    #Setup
    refresh_db()
    test_movie = create_movie()
    #Run action
    res = test_app.get('/movies')
    page_data = res.data.decode()

    assert res.status_code == 200
    assert f'<td><a href="/movies/{ test_movie.movie_id }">Harry Potter</a></td>' in page_data
    assert f'<td>JK</td>' in page_data
    assert f'<td>5</td>' in page_data

def test_get_all_movies_empty(test_app: FlaskClient):
    #Setup
    refresh_db()
    #Run action
    res = test_app.get('/movies')
    page_data = res.data.decode()

    assert res.status_code == 200
    assert f'<td>' not in page_data

def test_get_single_movie(test_app: FlaskClient):
    #Setup
    refresh_db()
    test_movie = create_movie()
    #Run action
    res = test_app.get(f'/movies/{test_movie.movie_id}')
    page_data = res.data.decode()

    assert res.status_code == 200
    assert f'<h1>Harry Potter - 5</h1>' in page_data
    assert f'<h2>JK</h2>' in page_data

def test_get_single_movie_404(test_app: FlaskClient):
    #Setup
    refresh_db()
    #Run action
    res = test_app.get('/movies/1')
    page_data = res.data.decode()

    assert res.status_code == 404

def test_create_movie(test_app: FlaskClient):
    #Setup
    refresh_db()
    #Run action
    res = test_app.post('/movies', data={
        'title': "Harry Potter",
        'director': 'JK',
        'rating': 5
    }, follow_redirects=True)
    page_data = res.data.decode()

    assert res.status_code == 200
    assert f'<h1>Harry Potter - 5</h1>' in page_data
    assert f'<h2>JK</h2>' in page_data

def test_create_movie_400(test_app: FlaskClient):
    #Setup
    refresh_db()
    #Run action
    res = test_app.post('/movies', data={
        'title': "Harry Potter",
        'director': 'JK'
    }, follow_redirects=True)
    page_data = res.data.decode()

    assert res.status_code == 400