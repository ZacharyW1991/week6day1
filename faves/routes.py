from faves import faves

from flask import render_template

@faves.route('/')
def index():
    return render_template('index.html')

@faves.route('/fave_list')
def fave_list():
    faves=['Detailed, mechanical sci-fi', 'Faux- and actual Shakespearian dialogue', 'Narrative that challenges', 'Stories about figurative and literal journies into Hell', 'Pretentious music that goes on way too long']
    return render_template('fave_list.html', faves=faves)