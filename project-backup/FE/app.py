from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BACKEND_API_URL = os.getenv("BACKEND_API_URL")


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        payload = {
            "firstName": request.form["firstName"],
            "lastName": request.form["lastName"],
            "mobileNumber": request.form["mobileNumber"],
            "address": request.form["address"]
        }

        try:
            response = requests.post(
                f"{BACKEND_API_URL}/api/customers",
                json=payload
            )

            data = response.json()

            message = data.get("message")

        except Exception as e:
            print(e)
            message = "Error connecting to backend"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=3000)