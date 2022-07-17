import json

from flask import Flask, render_template, request
import flask_sqlalchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite4'# <--- add this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db = flask_sqlalchemy.SQLAlchemy(app)

class cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    tshirtNo = db.Column(db.Integer)
    size = db.Column(db.String(10))

    def __init__(self, name, tshirtNo, size):
        self.name = name
        self.tshirtNo = tshirtNo
        self.size = size

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    userDetails = {}
    if request.method == 'POST':
        name = request.form['name']
        tshirtNo = request.form['tshirt_number']
        size = request.form['size']
        userDetails['name'] = name
        userDetails['tshirtNo'] = tshirtNo
        userDetails['size'] = size
        # print(customer, dealer, rating, comments)
        if name is None or tshirtNo is None:
            return render_template('index.html', message='Please enter required fields')
        data = cart(name, tshirtNo, size)
        db.create_all()
        db.session.add(data)
        db.session.commit()
        return json.dumps(userDetails)
	    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)
