from server import app
from flask import render_template

# -------------------------------- Page Routes ------------------------------- #
# INDEX
@app.route('/')
def index():
    return render_template('index.html')


# Page Not Found
@app.errorhandler(404)
def err404(err):
    return render_template('err.html', err=err)


#Internal Server Error
@app.errorhandler(500)
def err404(err):
    return render_template('err.html', err=err)


if __name__ == '__main__':
    app.run(debug=True)


















    