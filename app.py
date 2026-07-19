from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open(r"C:\Users\dd961\Downloads\Titanic Prediction.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Model expects exactly 3 features, in this order: Pclass, Sex, Fam_type
    features = [
        float(request.form['Pclass']),
        float(request.form['Sex']),
        float(request.form['Fam_type'])
    ]

    prediction = model.predict([features])[0]
    result = 'Survived' if prediction == 1 else 'Did not survive'
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == "__main__":
    app.run(debug=True)