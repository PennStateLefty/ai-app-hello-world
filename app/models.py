from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InputText(db.Model):
    __tablename__ = 'input_texts'

    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, id, text):
        self.id = id
        self.text = text

class ResponseText(db.Model):
    __tablename__ = 'response_texts'

    id = db.Column(db.String, primary_key=True)
    input_id = db.Column(db.String, db.ForeignKey('input_texts.id'), nullable=False)
    response = db.Column(db.Text, nullable=False)

    def __init__(self, id, input_id, response):
        self.id = id
        self.input_id = input_id
        self.response = response