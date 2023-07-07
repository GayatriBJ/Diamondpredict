from flask import Flask, jsonify, request, render_template
from utils import Diamondprice
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Result" : "Successfull"})

@app.route('/Diamond_Price', methods = ["POST"])
def get_diamond_price():
    data = request.form
    print("Data :", data)

    carat   = data["carat"]
    cut     = data["cut"]
    color   = data["color"]
    clarity = data["clarity"]
    depth   = data["depth"]
    table   = data["table"]
    x       = data["x"]
    y       = data["y"]
    z       = data["z"]
   
    obj1 = Diamondprice()
    predicted_price = obj1.get_predicted_price(carat, cut, color, clarity, depth, table, x, y, z)
    return jsonify({"Result"  : f'Predicted Diamond price is {predicted_price} $ '})



if __name__ == "__main__":
    app.run()


