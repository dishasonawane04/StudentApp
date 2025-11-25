
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "data":{
            "regno":123232,
            "name": "Disha",
            "email": "disha.sonawne18@gmail.com"

        }
    }
if __name__ == "__main__":
    app.run(debug=True)