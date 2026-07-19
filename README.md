# Titanic Survival Prediction

A simple Flask web app that predicts whether a Titanic passenger would have survived, based on a trained Random Forest model.

## Features

The model takes 3 inputs:

| Feature | Description | Values |
|---|---|---|
| `Pclass` | Passenger class | 1, 2, or 3 |
| `Sex` | Passenger sex | 0 = Female, 1 = Male |
| `Fam_type` | Family group size | 0 = Alone, 1 = Small family, 2 = Large family |

## Project Structure

```
PythonProject1/
├── app.py                 # Flask application
├── templates/
│   └── index.html         # Web form + result display
├── model.pkl               # Trained RandomForestClassifier (not tracked in git)
└── README.md
```

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask scikit-learn
   ```

4. **Add the model file**
   Place `Titanic Prediction.pkl` (renamed to `model.pkl`) in the project root, or update the path in `app.py` to match its location.

## Running the app

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## How it works

1. The user submits passenger class, sex, and family type through the web form.
2. `app.py` builds a feature vector `[Pclass, Sex, Fam_type]` from the form input.
3. The trained model predicts survival (1 = survived, 0 = did not survive).
4. The result is rendered back on the same page.

## Notes

- The model was trained using scikit-learn 1.6.1. If you see an `InconsistentVersionWarning`, consider installing that exact version (`pip install scikit-learn==1.6.1`) to avoid unexpected prediction differences.
- This is a development server (`app.run(debug=True)`) — not suitable for production deployment as-is.

## License

MIT (or update to whatever license fits your project)




<img width="1392" height="531" alt="image" src="https://github.com/user-attachments/assets/aafb9ea8-1be3-4bd9-b621-352d03f37b85" />
<img width="1375" height="497" alt="image" src="https://github.com/user-attachments/assets/8900595e-9c28-4c5f-b2bc-b8a2eca82c88" />
<img width="1363" height="616" alt="image" src="https://github.com/user-attachments/assets/72c24e1d-f4f0-4902-9599-2ad4524b143b" />
<img width="1376" height="628" alt="image" src="https://github.com/user-attachments/assets/e90c4422-e54d-47ce-b150-da5343a1adda" />
<img width="1416" height="600" alt="image" src="https://github.com/user-attachments/assets/0375d5d8-1d53-48b6-b008-90a31233de87" />
<img width="846" height="601" alt="image" src="https://github.com/user-attachments/assets/450626f6-63fe-4e61-8ba0-520707c67abe" />
<img width="1235" height="687" alt="image" src="https://github.com/user-attachments/assets/076aa810-28d3-4bee-a1d7-904d7e683703" />
<img width="1226" height="606" alt="image" src="https://github.com/user-attachments/assets/2c3e97e8-ad13-4fe1-9f23-0bedbce041c6" />
<img width="936" height="342" alt="image" src="https://github.com/user-attachments/assets/c434ca3b-61a0-49e8-a2b1-4e50bd84c0b2" />
<img width="712" height="836" alt="image" src="https://github.com/user-attachments/assets/a6a3d931-c6e6-49ca-99b3-f0cebe76a64e" />
<img width="722" height="848" alt="image" src="https://github.com/user-attachments/assets/be263576-a754-47aa-999e-b7088d946e65" />
<img width="815" height="863" alt="image" src="https://github.com/user-attachments/assets/f59c7473-8b14-41a9-b762-c105e211c0f2" />











