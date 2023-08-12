from flask import Flask, render_template, request
from stories import story, Story

app = Flask(__name__)


@app.route('/')
def madlib_form():
    prompts = story.prompts
    return render_template('home.html', questions=prompts)


@app.route('/story')
def madlib_story():
    answers = request.args
    print(answers)
    return render_template('story.html', story = story.generate(answers))