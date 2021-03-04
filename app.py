from server import app
from flask import render_template, request
from server.survey.forms import RecForm

# -------------------------------- Page Routes ------------------------------- #
# INDEX
@app.route('/')
def index():
    return render_template('mainPages/index.html')

# Emissions
@app.route('/emissions')
def emissions():
    return render_template('mainPages/emissions.html')




# Actions
@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    form = RecForm()
    count = 0
    if request.method == 'POST':
        count = 0
        if form.equity.data:
            count += 1
        if form.envQuality.data:
            count += 1
        if form.healthSafety.data:
            count += 1
        if form.resilience.data:
            count += 1
        if form.cementMan.data:
            count += 1
        if form.waste.data:
            count += 1
        if form.electricity.data:
            count += 1
        if form.naturalGas.data:
            count += 1
        if form.transportation.data:
            count += 1
        
    return render_template('/mainPages/recommendations.html', form=form, count=count)




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


















    