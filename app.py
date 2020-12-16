import joblib
import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='wP4xQ8huljJ5oI1c'
bootstrap = Bootstrap(app)

class InputForm(FlaskForm):
    alcohol = FloatField('Alcohol:', validators=[DataRequired()])
    malic_acid = FloatField('Malic Acid:', validators=[DataRequired()])
    ash = FloatField('Ash:', validators=[DataRequired()])
    alcalinity_of_ash = FloatField('Alcalinity of ash:', validators=[DataRequired()])
    magnesium = FloatField('Magnesium:', validators=[DataRequired()])
    total_phenols = FloatField('Total phenols:', validators=[DataRequired()])
    flavanoids = FloatField('Flavanoids:', validators=[DataRequired()])
    nonflavanoid_phenols = FloatField('Nonflavanoid phenols:', validators=[DataRequired()])
    proanthocyanins = FloatField('Proanthocyanins:', validators=[DataRequired()])
    color_intensity = FloatField('Color intensity:', validators=[DataRequired()])
    hue = FloatField('Hue:', validators=[DataRequired()])
    diluted_wines = FloatField('OD280/OD315 of diluted wines:', validators=[DataRequired()])
    proline = FloatField('Proline:', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    wine = 'No-image'

    if form.validate_on_submit():
        x = [[form.alcohol.data, form.malic_acid.data, form.ash.data, form.alcalinity_of_ash.data, form.magnesium.data, form.total_phenols.data, form.flavanoids.data, 
        form.nonflavanoid_phenols.data, form.proanthocyanins.data, form.color_intensity.data, form.hue.data, form.diluted_wines.data, form.proline.data]]
        wine = make_prediction(x)
        if wine == 1:
            wine = 'Classe-1'
        elif wine == 2:
            wine = 'Classe-2'
        elif wine == 3:
            wine = 'Classe-3'    

    return render_template('index.html', form=form, wine=wine)

def make_prediction(x):
    filename = os.path.join('model', 'finalized_model.sav')
    model = joblib.load(filename)
    return model.predict(x)[0]