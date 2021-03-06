from flask import Flask, render_template, request
import requests
import simplejson as json
import os
app = Flask(__name__)

# render to index.html
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

# fetch books from google API
@app.route("/Book", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        bname = request.form['bname']
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + bname)
        json_data = json.loads(response.text)
        print(json_data['items'][0]['id'])
        return render_template("index.html", book=json_data['items'], available=json_data['totalItems'])

# route to delete book by id
@app.route("/book/delete/<string:id>")
def delte(id):
    return render_template("index.html")

# route to update books by id
@app.route("//posts/edit/<string:id>")
def update(id):
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
