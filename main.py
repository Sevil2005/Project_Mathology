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
@app.route('/AnaSəhifə')
def home():
    return render_template('home.html')


@app.route('/haqqımızda')
def about():
    return render_template('about.html', title="Haqqımızda")

@app.route('/rfo')
def rfo():
    return render_template('advice.html', title="RFO")

@app.route('/BeynəlxalqOlimpiadalar')
def IO():
    return render_template('advice.html', title="BeynəlxalqOlimpiadalar")

@app.route('/məsləhətlər')
def advice():
    return render_template('advice.html', posts=posts, title="Məsləhətlər")

@app.route('/müzakirə')
def disc():
    return render_template('discussion.html', title="Müzakirə")

if __name__ == '__main__':
    app.run(debug = True)
