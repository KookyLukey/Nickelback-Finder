from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searchPhrase = StringField('Search Phrase', validators=[DataRequired()])
    submit = SubmitField('Search')
