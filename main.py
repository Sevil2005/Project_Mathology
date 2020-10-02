from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': "Sevil Rasulova",
        'title': "Post 1",
        'content': "Post 1 Content",
        'date': "26-Sep"
    },
    {
        'author': "Anar Rzayev",
        'title': "Post 2",
        'content': "Post 2 Content",
        'date': "27-Sep"
    },
    {
        'author': "Zəhra Bayramlı",
        'title': "Post 3",
        'content': "Post 3 Content",
        'date': "28-Sep"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/discussion')
def disc():
    return render_template('discussion.html', title="Discussion")

@app.route('/advice')
def advice():
    return render_template('advice.html', posts=posts, title="Advice")


if __name__ == '__main__':
    app.run(debug = True)
