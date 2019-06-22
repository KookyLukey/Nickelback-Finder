from flask import render_template, flash, redirect, url_for, request, session
from app import app
from app.forms import SearchForm
import nickelbackfinder

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        flash('Searching {}'.format(form.searchPhrase.data))
        session['input_search'] = form.searchPhrase.data
        nickelbackfinder.get_all_songs(form.searchPhrase.data)
        return redirect(url_for('results'))
    return render_template('index.html', title='Search', form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    str_search = session.get('input_search', None)
    return render_template('results.html', title='Results', testval=str_search)
