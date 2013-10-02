import os, flask
app = flask.Flask(__name__)

import pymongo
db = pymongo.MongoClient(
    os.environ.get("MONGOLAB_URI", "mongodb://localhost/5mincloud")
).get_default_database()

@app.route("/", methods=["GET"])
def hello():
    messages = db.messages.find()
    return flask.render_template("hello.html", messages=messages)

@app.route("/", methods=["POST"])
def post():
    db.messages.insert({
        "message": flask.request.form["message"]
    })
    return flask.redirect("/")

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5050)))
