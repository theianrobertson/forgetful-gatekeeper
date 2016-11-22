from app import db

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass_phrase = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(50))
    create_date = db.Column(db.Date())
    expiry_date = db.Column(db.Date())

    def __repr__(self):
        return '<User %r>' % (self.pass_phrase)

