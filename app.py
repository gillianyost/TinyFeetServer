from server import app
from flask import render_template, request
from server import db
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

# Resources
@app.route('/resources')
def resources():
    return render_template('mainPages/resources.html')

# Recommendations
@app.route('/feedback')
def feedback():
    return render_template('mainPages/feedback.html')

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

