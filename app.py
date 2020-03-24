from flask import Flask, render_template, request
# from flask_debug import Debug
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)
# Debug(app)

# ?environment this should connect us 
ENV = 'prod'

# ?dev as developemnt then we use database
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/vertu' #*passwrd auth failed here several times
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dvvnhvdmazdhux:6c3c2185ce00f63101466322f9bebe8ad476a2a6814075a4c88557b1169e35e5@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d5t4jgj5tdi3ir'

# ? adding config value  to track modifications 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# ?env connecntion ends -> we are connected


# !database OBJECT
db = SQLAlchemy(app) #*pass in our app
#!gonna extent the model
class Feedback(db.Model): 
    __tablename__ = 'feedback' #!create a table feedback 
    id =db.Column(db.Integer, primary_key=True )  #!goint to define the fields 
    customer = db.Column(db.String(100), unique = True)
    dealer = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    improve = db.Column(db.String())


    # !sonstructor/initializer / self is like this keyword
    # !takes in self and other fields except the id!
    def __init__(self, customer, dealer, rating, comments, improve):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating 
        self.comments = comments
        self.improve = improve

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')

# !test been succesful!!!
@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        improve = request.form['improve']
        print (customer, dealer, rating, comments, improve)

        # !message back customer:::
        if customer == '' or dealer == '':
            return render_template('index.html', message="Please enter your details!")
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments, improve)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments, improve)
            return render_template('success.html')
        return render_template('success.html', message = "You have already submitted feedback")

if (__name__) == '__main__':
    # app.debug = True
    # Debug(app)
    app.run() 