from flask import Flask, render_template, request
import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
import numpy as np  
import pickle

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/sub', methods = ['POST'])

def submit():
    #HTML -> to python file
    if request.method == 'POST':
#         name = request.form['region_name']
        year = request.form['year']
#         longitude = request.form['region_longitude']
#         latitude = request.form['region_latitude']
#         cardinal_direction_labeling = request.form['cardinal_direction_labeling']
#         list = [[year, latitude, longitude,name,  cardinal_direction_labeling]]
#         print(list)
#         arr = np.array(list)
#         print(arr)

#         result = ValuePredictor(arr)
#         # prediction = str(result)
#  return render_template('submit.html',prediction=year)

    # Python -> to html file
    return render_template('submit.html', name_pyton = year)

# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,5)
#     loaded_model = pickle.load(open('random_forest.pkl','rb'))
#     result = loaded_model.predict(to_predict)
#     print((result[0]))

#     return result[0]

if __name__ == '__main__' :
    app.run(debug=True)
    # app.run()
