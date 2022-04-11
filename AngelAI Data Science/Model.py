from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder=r"E:\Angel Al\templates")
clf = pickle.load(open('Model.pkl', "rb"))
cv = pickle.load(open("cv.pkl", "rb"))


@app.route('/')
def Model():
    return render_template('Model.html')


@app.route('/Label', methods=['POST', 'GET'])
def Label():
    if request.method == 'POST':
        #HTML ->.py
        result = request.form['Data']
        result_pred = clf.predict(cv.transform([result]))
    #.py -> HTML
    return render_template("Label.html", result=result_pred)


if __name__ == '__main__':
    app.run(debug=True)