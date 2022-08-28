from xmlrpc.client import boolean
from flask import Flask, request, render_template
from form import PatientInfo
import pickle

def create_app():
    model = None
    with open('model.pkl','rb') as pickle_file:
        model = pickle.load(pickle_file)

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'i dont know why i have to choose this'

    @app.route('/', methods=['GET','POST'])
    def index():
        form = PatientInfo()
        if form.validate_on_submit():
            Name = form.Name.data
            Age = form.Age.data
            Gender = int(request.form['Gender'])
            Scholarship = int(request.form['Scholarship'])
            Hipertension = int(request.form['Hipertension'])
            Diabetes = int(request.form['Diabetes'])
            Alcholism = int(request.form['Alcholism'])
            Handcap = int(request.form['Handcap'])
            SMS_received = int(request.form['SMS_received'])
            
            Patient = [Gender, Age, Scholarship, Hipertension, Diabetes, Alcholism, Handcap, SMS_received]
            res = model.predict([Patient])
            if res == 1:
                return render_template('result1.html', Name=Name)
            else:
                return render_template('result2.html', Name=Name)
        return render_template('index.html', form=form)

