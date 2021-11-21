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

        region_name_drop_down = request.form['region_name_drop_down']
        year = request.form['year']
        [longitude, latitude, cardinal_region,state_label] = gettingValuesStates(region_name_drop_down)
#         list = [[year, latitude, longitude,state_label,  cardinal_region]]
#         print(list)
#         arr = np.array(list)

#         result = ValuePredictor(arr)
#         # prediction = str(result)
#  return render_template('submit.html',prediction=arr)

    # Python -> to html file
    return render_template('submit.html', name_pyton = cardinal_region)

#     return result[0]
# def ValuePredictor(to_predict_list):
#     to_predict = np.array(to_predict_list).reshape(1,5)
#     loaded_model = pickle.load(open('random_forest.pkl','rb'))
#     result = loaded_model.predict(to_predict)
#     severity = 'Unknown'

#     # Lowest to the highest ranking from the model [4, 1, 0, 3, 2]
#     match result:
#         case 2:
#             severity = "Highest"
#             return  severity
#         case 3:
#             severity = "second highest"
#             return  severity
#         case 0:
#             severity = 'medium'
#             return  severity
#         case 1:
#             severity = 'second lowest'
#             return  severity
#         case 4:
#             severity = 'Lowest'
#             return  severity
#     return result[0]

def gettingValuesStates(state_name):
    longitude = 0
    latitude = 0
    cardinal_region = 0
    state_label = 0

#     print(type(state_name))
    match state_name:
        case 'A & N ISLANDS':
            longitude = 92.735983
            latitude = 11.667026
            state_label = 0
            cardinal_region = 1

            return longitude, latitude, cardinal_region,state_label
#         case 'ANDHRA PRADESH':
#             longitude = 78.570026
#             latitude = 14.750429
#             state_label = 1
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'ARUNACHAL PRADESH':
#             longitude = 93.616601
#             latitude = 27.100399
#             state_label = 2
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'ASSAM':
#             longitude = 94.216667
#             latitude = 26.749981
#             state_label = 3
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'BIHAR':
#             longitude = 87.479973
#             latitude = 25.785414
#             state_label = 4
#             cardinal_region = 1

#             return longitude, latitude, cardinal_region,state_label
#         case 'CHANDIGARH':
#             longitude = 76.780006
#             latitude = 30.719997
#             state_label = 5
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'CHHATTISGARH':
#             longitude = 82.159987
#             latitude = 22.09042
#             state_label = 6
#             cardinal_region = 1

#             return longitude, latitude, cardinal_region,state_label
#         case 'D & N HAVELI':
#             longitude = 73.016618
#             latitude = 20.266578
#             state_label = 7
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'DAMAN & DIU':
#             longitude = 73.0169
#             latitude = 20.227
#             state_label = 8
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'GOA':
#             longitude = 73.818001
#             latitude = 15.491997
#             state_label = 9
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'GUJARAT':
#             longitude = 71.1924
#             latitude = 22.2587
#             state_label = 10
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'HARYANA':
#             longitude = 77.019991
#             latitude = 28.450006
#             state_label = 11
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'HIMACHAL PRADESH':
#             longitude = 77.166597
#             latitude = 31.100025
#             state_label = 12
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'JAMMU & KASHMIR':
#             longitude = 74.466658
#             latitude = 34.299959
#             state_label = 13
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'JHARKHAND':
#             longitude = 86.419986
#             latitude = 23.800393
#             state_label = 14
#             cardinal_region = 1

#             return longitude, latitude, cardinal_region,state_label
#         case 'KARNATAKA':
#             longitude = 76.919997
#             latitude = 12.570381
#             state_label = 15
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'KERALA':
#             longitude = 76.569993
#             latitude = 8.900373
#             state_label = 16
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'LAKSHADWEEP':
#             longitude = 72.6358
#             latitude = 10.5593
#             state_label = 17
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'MADHYA PRADESH':
#             longitude = 76.130019
#             latitude = 21.300391
#             state_label = 18
#             cardinal_region = 0

#             return longitude, latitude, cardinal_region,state_label
#         case 'MAHARASHTRA':
#             longitude = 73.160175
#             latitude = 19.250232
#             state_label = 19
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'MANIPUR':
#             longitude = 93.950017
#             latitude = 24.799971
#             state_label = 20
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'MEGHALAYA':
#             longitude = 91.880014
#             latitude = 25.570492
#             state_label = 21
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'MIZORAM':
#             longitude = 92.720015
#             latitude = 23.710399
#             state_label = 22
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'NAGALAND':
#             longitude = 94.11657
#             latitude = 25.666998
#             state_label = 23
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'ODISHA':
#             longitude = 85.900017
#             latitude = 19.82043
#             state_label = 24
#             cardinal_region = 1

#             return longitude, latitude, cardinal_region,state_label
#         case 'PUDUCHERRY':
#             longitude = 79.83
#             latitude = 11.934994
#             state_label = 25
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'PUNJAB':
#             longitude = 75.980003
#             latitude = 31.519974
#             state_label = 26
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'RAJASTHAN':
#             longitude = 74.2179
#             latitude = 27.0238
#             state_label = 27
#             cardinal_region = 5

#             return longitude, latitude, cardinal_region,state_label
#         case 'SIKKIM':
#             longitude = 88.616647
#             latitude = 27.33333
#             state_label = 28
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'TAMIL NADU':
#             longitude = 78.6569
#             latitude = 11.1271
#             state_label = 29
#             cardinal_region = 4

#             return longitude, latitude, cardinal_region,state_label
#         case 'TRIPURA':
#             longitude = 91.279999
#             latitude = 23.835404
#             state_label = 30
#             cardinal_region = 3

#             return longitude, latitude, cardinal_region,state_label
#         case 'UTTAR PRADESH':
#             longitude = 78.050006
#             latitude = 27.599981
#             state_label = 31
#             cardinal_region = 0

#             return longitude, latitude, cardinal_region,state_label
#         case 'UTTARAKHAND':
#             longitude = 78.050006
#             latitude = 30.320409
#             state_label = 32
#             cardinal_region = 2

#             return longitude, latitude, cardinal_region,state_label
#         case 'WEST BENGAL':
#             longitude = 88.329947
#             latitude = 22.58039
#             state_label = 33
#             cardinal_region = 1

#             return longitude, latitude, cardinal_region,state_label
    return longitude, latitude, cardinal_region,state_label
    

if __name__ == '__main__' :
#     app.run(debug=True)
    app.run()
