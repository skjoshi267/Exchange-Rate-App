from Flask_App import database

class Users(database.Model):
    __table_args__ = {'extend_existing':False}
    userid = database.Column(database.Integer,
                         primary_key=True,
                         unique=True,
                         nullable=False)
    username = database.Column(database.String(20),
                         index=True,
                         unique=True,
                         nullable=False)
    email = database.Column(database.String(20),
                      index=True,
                      unique=True,
                      nullable=False)
    password = database.Column(database.String(10),
                      index=False,
                      nullable=False)


def __repr__(self):
    return '<User> {}'.format(self.username)