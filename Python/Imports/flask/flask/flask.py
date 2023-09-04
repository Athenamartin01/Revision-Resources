import flask as fl
import os

app = fl.Flask(__name__)  #creates a Flask app object
    
app.run(debug=True, host='0.0.0.0') #runs the app (in debug mode) host is usually local by default, by setting to 0.0.0.0 allows for all traffic

@app.route('/Path', methods=['GET','POST']) #sets an endpoint to the app with specific request methods
@app.route('/Path/<int:num>') #used to collect an integer variable out of the URL
def index(num:int): 
    return('Random Name Generator <br> This is a newline') #displays on page, with html elements also!
    
fl.request.method() #used to see which method is being used
fl.request.args.get()
fl.redirect('http://www.google.com') #redirects to a different webpage
fl.url_for("index") #returns a URL inbuilt page based on function name
     
    #type: mysql+pymysql:// 
    #user:pass : root:password
    #location: @localhost:3306
    #exact db: /world
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/world' #databses from mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #in-built databases into the application
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') #private as database is added through console
    #all used to add a databse to the webpage

fl.render_template('index.html', name='John') #used to display html file
