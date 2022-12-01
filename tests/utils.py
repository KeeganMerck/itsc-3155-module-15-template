from src.models import Movie, db

def refresh_db():
    Movie.query.delete()
    db.session.commit()

def create_movie(title='Harry Potter', director='JK', rating=5):
    test_movie = Movie(title='Harry Potter', director='JK', rating=5)
    db.session.add(test_movie)
    db.session.commit()
    return test_movie