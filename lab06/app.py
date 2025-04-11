# Using flask to make an api
# import necessary libraries and functions
from logging import exception
from flask import Flask, jsonify, request, abort
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns API when we use GET.
@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
  
        data = "API Example: /weight?height=130.3"
        return data
  

import pickle
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Use the model to predict the weight for the input height.
# the input height is a query parameter of the URL with GET
# on the terminal type: curl http://127.0.0.1:5000/weight?height=33.3
# this returns {"height": 33.3, "weight": -25.860609898265146}
@app.route('/weight', methods = ['GET'])
def disp():
    # get the query parameter as string and fail if not there
    height = request.args.get("height")
    if height is None:
        abort(400, 'Missing height query parameter')
    try:
        height = float(height)
    except ValueError:
        abort(400, 'Height query parameter not float')

    # we get back an array holding the predicted value/s
    try:
        weight = loaded_model.predict([[height]])[0]
    except Exception:
        abort(400, 'Model prediction failed')

    # put response in a dictionary
    response = {}
    response["height"] = height
    response["weight"] = weight
    return jsonify(response)

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)