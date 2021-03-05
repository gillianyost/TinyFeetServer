from server import app
from flask import render_template, request
from server import db
from server.survey.forms import RecForm
from server.models import solutions
from sqlalchemy import distinct, inspect
from server.sectors.views import object_as_dict
import collections

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
    columnNames = []
    tableData = []
    if request.method == 'POST':
       
        if form.allSol.data:
            # query = solutions.query(solutions.solution_description, \
            # solutions.section, \
            # solutions.subsection, \
            # solutions.ghg_reduction_potential) # Cannot get to work TO DO

            # columnNames = solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = solutions.query.all()
        else: 
            # query = solutions.query(solutions.solution_description, \
            # solutions.section, \
            # solutions.subsection, \
            # solutions.ghg_reduction_potential)\
            # .filter((solutions.equity & form.equity.data) | \
            # (solutions.economic_sustainability & form.econSus.data) | \
            # (solutions.local_environmental_quality & form.envQuality.data) | \
            # (solutions.enhances_public_safety & form.healthSafety.data) | \
            # (solutions.builds_resilience & form.resilience.data)) # Cannot get to work TO DO

            # columnNames = solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = solutions.query.filter((solutions.equity & form.equity.data) | \
            (solutions.economic_sustainability & form.econSus.data) | \
            (solutions.local_environmental_quality & form.envQuality.data) | \
            (solutions.enhances_public_safety & form.healthSafety.data) | \
            (solutions.builds_resilience & form.resilience.data))

        for row in query:
            d = object_as_dict(row)
            tableData.append(d.values())
    
    # if request.method == 'POST':
    #     if form.equity.data:
    #         columnNames = recommendations.__table__.columns.keys()
    #         query = recommendations.all()
    
    # tableData = []
    # d = object_as_dict(row)
    # tableData.append(d.values())

    return render_template('/mainPages/recommendations.html', form=form, columnNames=columnNames, tableData=tableData)


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


















    