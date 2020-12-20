from flask import Flask, request, render_template

from recommend import Lens

app = Flask(__name__)
app.debug = True

lens = Lens()


@app.route('/', methods=['GET', 'POST'])
def index():
    most_popular = lens.recommend_most_popular()
    highly_rated = lens.highly_rated()
    return render_template('index.html', most_popular=most_popular, highly_rated=highly_rated)


if __name__ == '__main__':
    app.run()
