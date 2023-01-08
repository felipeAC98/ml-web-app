from flask import Flask, render_template, request
import pickle
import socket

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
my_name = socket.gethostname()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'From host {my_name}: A house with {rooms} rooms per dwelling and located {distance} km to employment centers has a value of ${output}K')

@app.route("/predict_id", methods=['POST'])
def predict_id():
    id_request = int(request.form['id_request'])
    rooms = int(request.form['rooms'])
    distance = int(request.form['distance'])
    prediction = model.predict([[rooms, distance]])
    output = round(prediction[0], 2)
    return f'{my_name};{id_request};{output}'


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
