from flask import Flask
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
    
    sqlvisualize.visualize_sql()
    
    return render_template('visualization.html', title='personality visualization')

@app.route("/visualization/<dass_type>")
def dass_visualization(dass_type):
    import sqlvisualize
    
    #sqlvisualize.dass_visualize_sql(dass_type)
    
    sqlvisualize.dass_visualize_sql(dass_type)

    return render_template('dass_visualization.html', title='dass visualization')


if __name__ == '__main__':
    app.run()