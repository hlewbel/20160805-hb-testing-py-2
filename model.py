from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example game (data) for the test database and add to the db."""
    #FIXME: write a function that creates a game and adds it to the database.
    
    #create sample game data

    game = Game(name="Sample", description="this is the sample game data")
    db.session.add(game)
    db.session.commit()    



if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."