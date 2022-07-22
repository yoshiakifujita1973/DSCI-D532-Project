from flask import Flask
from flask import request
from flask import render_template

#app = Flask(__name__)
app = Flask(__name__, static_folder='./templates/static')

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route("/hello")
def hello():
    return "Hello, Welcome to GeeksForGeeks"

@app.route("/index")
def index_name():
    return render_template('index.html', title='Welcome')

@app.route("/dass")
def index_dass():
    return render_template('index_dass.html', title='dass')

@app.route("/visualization")
def visualization():
    import sqlvisualize
    
    fname = sqlvisualize.visualize_sql()
    
    return render_template('visualization.html', title='personality visualization', fname=fname)

@app.route("/visualizationDS")
def dass_visualizationDS():
    import sqlvisualize
    dass_type = "DS"
    sqlvisualize.dass_visualize_sql(dass_type)

    return render_template('dass_visualization.html', title='personality visualization')

@app.route("/visualizationAS")
def dass_visualizationAS():
    import sqlvisualize
    dass_type = "AS"
    sqlvisualize.dass_visualize_sql(dass_type)

    return render_template('dass_visualization.html', title='personality visualization')

@app.route("/visualizationAD")
def dass_visualizationAD():
    import sqlvisualize
    dass_type = "AD"
    sqlvisualize.dass_visualize_sql(dass_type)

    return render_template('dass_visualization.html', title='personality visualization')

@app.route("/action", methods=['GET', 'POST'])
def action():
    
    import sqlvisualize
    
    if request.method == 'POST':
        
        gender = request.form['Gender']
        race = request.form['Race']
        age_min = request.form['Age_min']
        age_max = request.form['Age_max'] 
        depression = request.form['Depression']
        anxiety = request.form['Anxiety']
        stress = request.form['Stress']
        
        #s = gender + ' ' + race + ' ' + age_min + ' ' + age_max + ' ' + depression + ' ' + anxiety + ' ' + stress
        
    elif request.method == 'GET':
        return request.form['Gender']
    
    fname = sqlvisualize.peasonal_visualize_filter(gender, race, age_min, age_max, depression, anxiety, stress)
    
    return render_template('visualization.html', title='personality visualization', fname=fname)
    
if __name__ == '__main__':
    app.run()