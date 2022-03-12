#APP FLASK (commande : flask run)
# Partie formulaire non utilisée (uniquement appel à l'API)

from flask import Flask, jsonify
#from flask_wtf import Form
#from wtforms.fields import StringField,BooleanField, PasswordField, TextAreaField
#from wtforms.widgets import TextArea
#import validators
#from wtforms.validators import DataRequired
#from toolbox.predict import *
#import pandas as pd
#import xgboost
#import warnings
#warnings.filterwarnings("ignore", category=UserWarning)
#import os
#import socketio



# App config.
DEBUG = True
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b7776a'

@app.route('/')
@app.route('/credit/', methods=['GET'])
def credit():
   
    #calcul prédiction défaut et probabilité de défaut
    #prediction, proba = predict_flask(form_id, dataframe)

    dict_final = {
        'prediction' : 1,
        'proba' : 0.2
        }

    print('Nouvelle Prédiction : \n', dict_final)

    return jsonify(dict_final)


#lancement de l'application
#if __name__ == "__main__":
#    port = os.environ.get("PORT",8080)
#    app.run(debug=False, host="0.0.0.1", port=port)
if __name__ == "__main__":
    app.run(debug=True,port=8080,use_reloader=False)
