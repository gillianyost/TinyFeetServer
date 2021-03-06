from server import app
from flask import render_template, request
from server import db
from server.survey.forms import RecForm
from server.models import Solutions
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
            # query = Solutions.query(Solutions.solution_description, \
            # Solutions.section, \
            # Solutions.subsection, \
            # Solutions.ghg_reduction_potential) # Cannot get to work TO DO

            # columnNames = Solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = Solutions.query.all()
        else: 
            # query = Solutions.query(Solutions.solution_description, \
            # Solutions.section, \
            # Solutions.subsection, \
            # Solutions.ghg_reduction_potential)\
            # .filter((Solutions.equity & form.equity.data) | \
            # (Solutions.economic_sustainability & form.econSus.data) | \
            # (Solutions.local_environmental_quality & form.envQuality.data) | \
            # (Solutions.enhances_public_safety & form.healthSafety.data) | \
            # (Solutions.builds_resilience & form.resilience.data)) # Cannot get to work TO DO

            # columnNames = Solutions.__tablename__.columns.keys()  # Cannot get to work TO DO
            query = Solutions.query.filter((Solutions.equity & form.equity.data) | \
            (Solutions.economic_sustainability & form.econSus.data) | \
            (Solutions.local_environmental_quality & form.envQuality.data) | \
            (Solutions.enhances_public_safety & form.healthSafety.data) | \
            (Solutions.builds_resilience & form.resilience.data))

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


















    