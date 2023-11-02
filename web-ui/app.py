from flask import Flask, request, jsonify,render_template
# from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
# import numpy as np
app = Flask(__name__)

def format_labels(labels):
    labels_list = []
    label = ''
    for i in labels:
        if i == ',':
            labels_list.append(label)
            label = ''
        elif i == ' ':
            continue
        else:
            label = str(label) + str(i)

    labels_list.append(label)
    return labels_list

@app.route('/')
def index():
    return render_template('index.html')

# to display the output in html do this => <p>{{output}}</p>
@app.route('/dataset1', methods=['GET', 'POST'])
def dataset1():
    if request.method=='POST':
        title=request.form['title']
        labels=request.form['label']
        print(title)
        input = []
        input.append(title)
        if labels == '':
            labels_list = None
        else:
            print(labels)
            labels_list = format_labels(labels)
        print(labels_list)
        input.append(labels_list)
        output = predict(input,dataset=1)
        return render_template('dataset1_output.html', output = output)
    return render_template('dataset1.html')

@app.route('/dataset2', methods=['GET', 'POST'])
def dataset2():
    if request.method=='POST':
        purpose=request.form['title']
        desc=request.form['label']
        print(purpose)
        print(desc)
        input = []
        input.append(purpose)
        input.append(desc)
        output = predict(input, dataset=2)
        return render_template('dataset2_output.html', output = output)
    return render_template('dataset2.html')

@app.route('/dataset3', methods=['GET', 'POST'])
def dataset3():
    if request.method=='POST':
        essay=request.form['title']
        print(essay)
        input = []
        input.append(essay)
        output = predict(input, dataset =3)
        return render_template('dataset3_output.html', output = output)
    return render_template('dataset3.html')

def predict(input,dataset):

    # inputs = loaded_tokenizer(input_text, return_tensors="tf", padding=True, truncation=True, max_length=128)
    # prediction = loaded_model.predict(inputs)
    prediction = 'output'
    return prediction

if __name__ == "__main__":
    app.run(debug=True)