from server import app
from flask import render_template, request, send_from_directory
from server import db
from server.models import Solutions
from sqlalchemy import distinct, inspect


# -------------------------------- Page Routes ------------------------------- #
# INDEX
@app.route('/')
def index():
    return render_template('mainPages/index.html')

# Emissions
@app.route('/emissions')
def emissions():
    return render_template('mainPages/emissions.html')

# Recommendations route moved to survey folder to use survey blueprint

# News
@app.route('/news')
def news():
    return render_template('mainPages/news.html')

# Page Not Found
@app.errorhandler(404)
def err404(err):
    return render_template('helpers/err.html', err=err)

#Internal Server Error
@app.errorhandler(500)
def err404(err):
    return render_template('helpers/err.html', err=err)


if __name__ == '__main__':
    app.run(debug=True)


















    