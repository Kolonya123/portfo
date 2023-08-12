from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/components.html")
def components():
    return render_template("components.html")

def write_to_file(data):
    with open("database.txt", mode = "a") as database:
        email = data["email"]
        password = data["password"]
        message = data["message"]
        file = database.write(f"\n{email}, \t{password}, \t{message}")

def write_to_csv(data):
    with open("database.csv", mode = "a", newline="") as database2:
        email = data["email"]
        password = data["password"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,password,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return "Thank you, I will get in touch with you, asap!"
        except:
            return "Did not save to database"
    else: 
        return "Something went wrong. Try again!"
    