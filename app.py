from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    input_text = ''
    if request.method == "POST":
        input_text = request.form['text']
        output = predict_genres(input_text)[0]
        confidence_list = output['confidences']
        labels = [elem['label'] for elem in confidence_list if elem['confidence'] >= 0.23 ]
        label_text = ""
        for idx, label in enumerate(labels):
            label_text = label_text + label
            if idx != len(labels)-1: 
                label_text = label_text + ", "
        print(label_text)
        if label_text == "":
            label_text = "Please try Entering longer meaningful text input next time. Model is undergoing final update. Thank you for your patience"
            
        return render_template("index.html", input_text=input_text, output_text=label_text)
    else:
        return render_template("index.html", output_text='', input_text=input_text)

def predict_genres(input_text):
    response = requests.post("https://tanvir-ishraq-quote-text-style-classifier.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data

if __name__ == "__main__":
    app.run(debug=True)
