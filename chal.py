from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def convert(miles):
    return jsonify({
        'kilometers': miles / 0.62137
    })

if __name__ == '__main__':
   app.run()
