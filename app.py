from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/advanced_search')
def advanced_search():
    return render_template('advanced_search.html')

@app.route('/image_search')
def image_search():
    return render_template('image_search.html')

if __name__ == '__main__':
    app.run(debug=True)
