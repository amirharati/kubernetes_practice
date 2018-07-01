"""
    Simple front-end for online editor. 
"""
from flask import Flask, request
import requests
import json

# automaticlly generated dns for backend
pythonServiceHostName = "http://pyservice.default.svc.cluster.local:80/py/eval"

app = Flask(__name__, static_folder='site', static_url_path='')

@app.route("/", methods=['GET'])
def handle():
    return app.send_static_file("index.html")

@app.route("/python", methods=['GET', 'POST'])
def handlePython():
    if request.method == 'POST':
        if 'code' in request.form:
            code = request.form['code']
        elif 'code' in request.json['code']:
            code = request.json['code']
        else:
            return("error")
        r = requests.post(pythonServiceHostName , json = {'code': code})
      
      
        return json.dumps(r.json())
    else:
        return app.send_static_file("python.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
